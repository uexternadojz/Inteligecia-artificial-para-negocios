#!/usr/bin/env python3
"""
Color Quantization Script
Reduces PNG to specific brand colors for better vectorization
"""

import sys
from PIL import Image
import numpy as np

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    """Convert RGB tuple to hex color"""
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def quantize_to_palette(input_path, output_path, palette_hex):
    """
    Quantize image to specific color palette

    Args:
        input_path: Path to input PNG
        output_path: Path to output PNG
        palette_hex: List of hex colors (e.g., ['#000000', '#ED2024', '#00D4FF'])
    """
    print(f"🎨 Loading image: {input_path}")
    img = Image.open(input_path).convert('RGB')
    pixels = np.array(img)

    # Convert palette to RGB
    palette_rgb = [hex_to_rgb(c) for c in palette_hex]
    print(f"📋 Target palette: {palette_hex}")

    # Reshape for vectorized distance calculation
    h, w = pixels.shape[:2]
    pixels_flat = pixels.reshape(-1, 3).astype(float)

    # Calculate distance to each palette color
    print("🔄 Quantizing colors...")
    quantized = np.zeros_like(pixels_flat)

    for i, pixel in enumerate(pixels_flat):
        # Find nearest color in palette
        distances = [np.linalg.norm(pixel - np.array(color)) for color in palette_rgb]
        nearest_idx = np.argmin(distances)
        quantized[i] = palette_rgb[nearest_idx]

        # Progress indicator
        if i % 10000 == 0:
            progress = (i / len(pixels_flat)) * 100
            print(f"  Progress: {progress:.1f}%", end='\r')

    print(f"\n✅ Quantization complete!")

    # Reshape back to image
    quantized = quantized.reshape(h, w, 3).astype(np.uint8)
    quantized_img = Image.fromarray(quantized)

    # Save
    quantized_img.save(output_path)
    print(f"💾 Saved: {output_path}")

    # Count colors used
    unique_colors = np.unique(quantized.reshape(-1, 3), axis=0)
    print(f"\n📊 Colors used: {len(unique_colors)}")
    for color in unique_colors:
        hex_color = rgb_to_hex(tuple(color))
        pixel_count = np.sum(np.all(quantized == color, axis=2))
        percentage = (pixel_count / (h * w)) * 100
        print(f"  {hex_color}: {pixel_count:,} pixels ({percentage:.2f}%)")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python quantize_colors.py <input.png> <output.png> [color1] [color2] ...")
        print("Example: python quantize_colors.py input.png output.png '#000000' '#ED2024' '#00D4FF'")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Default Orbital brand palette
    if len(sys.argv) > 3:
        palette = sys.argv[3:]
    else:
        palette = ['#000000', '#ED2024', '#00D4FF', '#FFFFFF']  # Black, Red, Cyan, White

    quantize_to_palette(input_path, output_path, palette)
