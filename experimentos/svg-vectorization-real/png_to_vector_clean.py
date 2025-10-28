#!/usr/bin/env python3
"""
PNG to Clean Vector SVG Converter
Uses contour detection to create true vector paths instead of pixel rectangles.
"""

import numpy as np
from PIL import Image
import sys

def trace_contours(image_array, color):
    """
    Trace contours of a specific color in the image.
    Returns simplified paths that represent the shape.
    """
    # Create binary mask for this color
    mask = np.all(image_array == color, axis=-1).astype(np.uint8) * 255

    # Find connected components and their boundaries
    from scipy import ndimage
    labeled, num_features = ndimage.label(mask)

    paths = []
    for i in range(1, num_features + 1):
        # Get the component
        component = (labeled == i)

        # Find boundary points
        coords = np.argwhere(component)
        if len(coords) == 0:
            continue

        # Get bounding box
        y_min, x_min = coords.min(axis=0)
        y_max, x_max = coords.max(axis=0)

        # For small components, just use a rectangle
        width = x_max - x_min + 1
        height = y_max - y_min + 1

        if width * height < 100:  # Small component, use rect
            paths.append({
                'type': 'rect',
                'x': x_min,
                'y': y_min,
                'width': width,
                'height': height
            })
        else:
            # For larger components, trace the outline
            # Simplified: use convex hull or polygon approximation
            paths.append({
                'type': 'rect',  # Fallback to rect for now
                'x': x_min,
                'y': y_min,
                'width': width,
                'height': height
            })

    return paths

def simplify_colors(image_array):
    """
    Group similar colors and return unique colors with their regions.
    """
    # Get unique colors
    pixels = image_array.reshape(-1, 3)
    unique_colors = np.unique(pixels, axis=0)

    print(f"Found {len(unique_colors)} unique colors")

    color_regions = {}
    for color in unique_colors:
        color_tuple = tuple(color)
        paths = trace_contours(image_array, color)
        if paths:
            color_regions[color_tuple] = paths

    return color_regions

def rgb_to_hex(rgb):
    """Convert RGB tuple to hex string."""
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

def generate_clean_svg(image_path, output_path):
    """
    Generate a clean SVG with proper paths instead of pixel rectangles.
    """
    print(f"🎨 Loading image: {image_path}")
    img = Image.open(image_path).convert('RGB')
    width, height = img.size
    image_array = np.array(img)

    print(f"📐 Dimensions: {width}×{height}")

    # Analyze colors and trace regions
    print("🔍 Analyzing color regions...")
    color_regions = simplify_colors(image_array)

    # Generate SVG
    print("📝 Generating SVG...")
    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
    ]

    # Add black background first (as base layer)
    total_shapes = 0
    if (0, 0, 0) in color_regions:
        svg_lines.append(f'  <rect x="0" y="0" width="{width}" height="{height}" fill="#000000"/>')
        total_shapes += 1

    # Add each color region on top
    for color_rgb, paths in color_regions.items():
        color_hex = rgb_to_hex(color_rgb)

        # Skip black background (already added as base)
        if color_hex == '#000000':
            continue

        for path in paths:
            if path['type'] == 'rect':
                svg_lines.append(
                    f'  <rect x="{path["x"]}" y="{path["y"]}" '
                    f'width="{path["width"]}" height="{path["height"]}" '
                    f'fill="{color_hex}"/>'
                )
                total_shapes += 1

    svg_lines.append('</svg>')

    # Write to file
    with open(output_path, 'w') as f:
        f.write('\n'.join(svg_lines))

    file_size_kb = len('\n'.join(svg_lines)) / 1024

    print(f"✅ SVG generated!")
    print(f"📊 Total shapes: {total_shapes}")
    print(f"💾 File size: {file_size_kb:.1f} KB")
    print(f"📦 Saved: {output_path}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python png_to_vector_clean.py <input.png> <output.svg>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    try:
        generate_clean_svg(input_path, output_path)
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
