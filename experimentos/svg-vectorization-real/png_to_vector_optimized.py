#!/usr/bin/env python3
"""
PNG to Optimized Vector SVG Converter
Uses aggressive region merging to minimize shapes while maintaining visual fidelity.
"""

import numpy as np
from PIL import Image
import sys

def find_rectangular_regions(mask):
    """
    Find rectangular regions in a binary mask using a greedy algorithm.
    This is more efficient than tracing individual connected components.
    """
    regions = []
    mask = mask.copy()  # Don't modify original
    height, width = mask.shape

    while np.any(mask):
        # Find first white pixel
        coords = np.argwhere(mask)
        if len(coords) == 0:
            break

        y, x = coords[0]

        # Expand rectangle as much as possible
        # Find max width at this y position
        max_x = x
        while max_x < width and mask[y, max_x]:
            max_x += 1
        rect_width = max_x - x

        # Find max height with this width
        max_y = y
        while max_y < height:
            if not np.all(mask[max_y, x:x+rect_width]):
                break
            max_y += 1
        rect_height = max_y - y

        # Add rectangle
        regions.append({
            'x': int(x),
            'y': int(y),
            'width': int(rect_width),
            'height': int(rect_height)
        })

        # Mark this region as processed
        mask[y:y+rect_height, x:x+rect_width] = False

    return regions

def merge_adjacent_rects(regions, threshold=10):
    """
    Merge rectangles that are adjacent or nearly adjacent.
    """
    if len(regions) < 2:
        return regions

    merged = True
    while merged:
        merged = False
        new_regions = []
        used = set()

        for i, rect1 in enumerate(regions):
            if i in used:
                continue

            # Try to merge with subsequent rectangles
            merged_any = False
            for j in range(i + 1, len(regions)):
                if j in used:
                    continue

                rect2 = regions[j]

                # Check if they can be merged horizontally
                if (rect1['y'] == rect2['y'] and
                    rect1['height'] == rect2['height'] and
                    abs((rect1['x'] + rect1['width']) - rect2['x']) <= threshold):

                    # Merge horizontally
                    new_rect = {
                        'x': min(rect1['x'], rect2['x']),
                        'y': rect1['y'],
                        'width': (max(rect1['x'] + rect1['width'], rect2['x'] + rect2['width']) -
                                 min(rect1['x'], rect2['x'])),
                        'height': rect1['height']
                    }
                    new_regions.append(new_rect)
                    used.add(i)
                    used.add(j)
                    merged = True
                    merged_any = True
                    break

                # Check if they can be merged vertically
                elif (rect1['x'] == rect2['x'] and
                      rect1['width'] == rect2['width'] and
                      abs((rect1['y'] + rect1['height']) - rect2['y']) <= threshold):

                    # Merge vertically
                    new_rect = {
                        'x': rect1['x'],
                        'y': min(rect1['y'], rect2['y']),
                        'width': rect1['width'],
                        'height': (max(rect1['y'] + rect1['height'], rect2['y'] + rect2['height']) -
                                  min(rect1['y'], rect2['y']))
                    }
                    new_regions.append(new_rect)
                    used.add(i)
                    used.add(j)
                    merged = True
                    merged_any = True
                    break

            if not merged_any and i not in used:
                new_regions.append(rect1)

        regions = new_regions
        if not merged:
            break

    return regions

def process_color_layer(image_array, target_color):
    """
    Process a single color layer and return optimized rectangles.
    """
    # Create binary mask
    mask = np.all(image_array == target_color, axis=-1)

    if not np.any(mask):
        return []

    # Find rectangular regions
    regions = find_rectangular_regions(mask)

    # Merge adjacent rectangles
    regions = merge_adjacent_rects(regions, threshold=5)

    return regions

def rgb_to_hex(rgb):
    """Convert RGB tuple to hex string."""
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

def generate_optimized_svg(image_path, output_path, remove_background=True):
    """
    Generate highly optimized SVG with minimal shapes.
    """
    print(f"🎨 Loading image: {image_path}")
    img = Image.open(image_path).convert('RGB')
    width, height = img.size
    image_array = np.array(img)

    print(f"📐 Dimensions: {width}×{height}")

    # Get unique colors
    pixels = image_array.reshape(-1, 3)
    unique_colors = np.unique(pixels, axis=0)
    print(f"🎨 Found {len(unique_colors)} unique colors")

    # Process each color
    print("🔍 Processing color layers...")
    color_layers = {}

    for color_rgb in unique_colors:
        color_hex = rgb_to_hex(tuple(color_rgb))

        # Skip black background if requested
        if remove_background and color_hex == '#000000':
            continue

        regions = process_color_layer(image_array, color_rgb)
        if regions:
            color_layers[color_hex] = regions
            print(f"  {color_hex}: {len(regions)} shapes")

    # Generate SVG
    print("📝 Generating SVG...")
    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
    ]

    # Add background if not removed
    if not remove_background and '#000000' in [rgb_to_hex(tuple(c)) for c in unique_colors]:
        svg_lines.append(f'  <rect width="{width}" height="{height}" fill="#000000"/>')

    # Add color layers
    total_shapes = 0
    for color_hex, regions in sorted(color_layers.items()):
        for rect in regions:
            svg_lines.append(
                f'  <rect x="{rect["x"]}" y="{rect["y"]}" '
                f'width="{rect["width"]}" height="{rect["height"]}" '
                f'fill="{color_hex}"/>'
            )
            total_shapes += 1

    svg_lines.append('</svg>')

    # Write to file
    svg_content = '\n'.join(svg_lines)
    with open(output_path, 'w') as f:
        f.write(svg_content)

    file_size_kb = len(svg_content) / 1024

    print(f"✅ SVG generated!")
    print(f"📊 Total shapes: {total_shapes}")
    print(f"💾 File size: {file_size_kb:.1f} KB")
    print(f"📦 Saved: {output_path}")

    return total_shapes, file_size_kb

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python png_to_vector_optimized.py <input.png> <output.svg> [--keep-background]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    remove_bg = '--keep-background' not in sys.argv

    try:
        generate_optimized_svg(input_path, output_path, remove_background=remove_bg)
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
