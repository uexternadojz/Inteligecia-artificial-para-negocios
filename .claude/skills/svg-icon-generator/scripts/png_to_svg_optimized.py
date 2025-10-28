#!/usr/bin/env python3
"""
Optimized PNG to SVG converter with horizontal rect merging
Reduces SVG file size by combining adjacent pixels of same color
"""

import sys
from PIL import Image
import svgwrite
import numpy as np

def rgb_to_hex(rgb):
    """Convert RGB tuple to hex color"""
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def find_horizontal_runs(row):
    """Find continuous horizontal runs of same color in a row"""
    runs = []
    if len(row) == 0:
        return runs

    start_x = 0
    current_color = row[0]

    for x in range(1, len(row)):
        if not np.array_equal(row[x], current_color):
            # Run ended, save it
            runs.append((start_x, x - 1, tuple(current_color)))
            start_x = x
            current_color = row[x]

    # Add final run
    runs.append((start_x, len(row) - 1, tuple(current_color)))
    return runs

def png_to_svg_optimized(input_path, output_path):
    """
    Convert PNG to SVG with optimized rect merging

    Args:
        input_path: Path to input PNG (should be quantized)
        output_path: Path to output SVG
    """
    print(f"🎨 Loading image: {input_path}")
    img = Image.open(input_path).convert('RGB')
    pixels = np.array(img)
    height, width = pixels.shape[:2]

    print(f"📐 Dimensions: {width}×{height}")
    print(f"🔄 Optimizing horizontal runs...")

    # Create SVG
    dwg = svgwrite.Drawing(output_path, size=(width, height), profile='tiny')

    # Background (most common color)
    unique, counts = np.unique(pixels.reshape(-1, 3), axis=0, return_counts=True)
    bg_color = tuple(unique[np.argmax(counts)])
    bg_hex = rgb_to_hex(bg_color)
    dwg.add(dwg.rect(insert=(0, 0), size=(width, height), fill=bg_hex))
    print(f"🎨 Background: {bg_hex}")

    # Process each row for horizontal runs
    rects_by_color = {}
    total_rects = 1  # background rect

    for y in range(height):
        runs = find_horizontal_runs(pixels[y])

        for start_x, end_x, color in runs:
            # Skip background color
            if color == bg_color:
                continue

            hex_color = rgb_to_hex(color)
            if hex_color not in rects_by_color:
                rects_by_color[hex_color] = []

            # Add rect for this horizontal run
            rect_width = end_x - start_x + 1
            rects_by_color[hex_color].append((start_x, y, rect_width, 1))
            total_rects += 1

        # Progress indicator
        if y % 50 == 0:
            progress = (y / height) * 100
            print(f"  Progress: {progress:.1f}%", end='\r')

    print(f"\n✅ Optimization complete!")
    print(f"📊 Colors: {len(rects_by_color) + 1} (including background)")

    # Add rects to SVG grouped by color
    for color, rects in rects_by_color.items():
        print(f"  {color}: {len(rects):,} rects")
        group = dwg.g(fill=color, stroke='none')
        for x, y, w, h in rects:
            group.add(dwg.rect(insert=(x, y), size=(w, h)))
        dwg.add(group)

    # Save
    dwg.save()
    print(f"\n💾 Saved: {output_path}")
    print(f"📊 Total SVG elements: {total_rects:,}")

    # Check file size
    import os
    file_size_kb = os.path.getsize(output_path) / 1024
    print(f"📦 File size: {file_size_kb:.1f} KB")

    if file_size_kb > 100:
        print(f"⚠️  Large file (>{100}KB)")
    elif file_size_kb > 50:
        print(f"⚠️  Acceptable but could be optimized further")
    else:
        print(f"✅ Excellent file size (<50KB)")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python png_to_svg_optimized.py <input.png> <output.svg>")
        sys.exit(1)

    png_to_svg_optimized(sys.argv[1], sys.argv[2])
