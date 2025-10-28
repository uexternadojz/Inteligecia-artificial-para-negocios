#!/usr/bin/env python3
"""
Analyze PNG image quality for vectorization readiness
"""

import sys
from PIL import Image
import numpy as np
from pathlib import Path

def analyze_png(png_path):
    """Analyze PNG and return metrics"""

    if not Path(png_path).exists():
        print(f"❌ Error: File not found: {png_path}")
        sys.exit(1)

    # Load image
    img = Image.open(png_path)
    pixels = np.array(img)

    # Basic info
    print("=== 📊 PNG Analysis ===")
    print(f"File: {Path(png_path).name}")
    print(f"Dimensions: {img.size[0]}×{img.size[1]}")
    print(f"Mode: {img.mode}")

    # Color analysis
    if img.mode == 'RGBA':
        # Flatten RGB channels for color counting
        rgb_pixels = pixels[:,:,:3].reshape(-1, 3)
        unique_colors = np.unique(rgb_pixels, axis=0)
        print(f"Unique RGB colors: {len(unique_colors)}")

        # Check alpha channel
        alpha = pixels[:,:,3]
        has_transparency = np.any(alpha < 255)
        print(f"Has transparency: {has_transparency}")
    else:
        unique_colors = np.unique(pixels.reshape(-1, pixels.shape[2]), axis=0)
        print(f"Unique colors: {len(unique_colors)}")

    # Contrast analysis
    if img.mode in ['RGB', 'RGBA']:
        rgb = pixels[:,:,:3] if img.mode == 'RGBA' else pixels
        contrast = rgb.std()
        print(f"Contrast (std dev): {contrast:.2f}")

    # Detect primary colors
    print("\n=== 🎨 Color Detection ===")

    # Convert to RGB for analysis
    if img.mode == 'RGBA':
        rgb_img = img.convert('RGB')
    else:
        rgb_img = img

    rgb_array = np.array(rgb_img)

    # Check for expected colors
    colors_to_find = {
        'Black (#000000)': (0, 0, 0),
        'Red (#ED2024)': (237, 32, 36),
        'Cyan (#00D4FF)': (0, 212, 255)
    }

    for color_name, rgb_value in colors_to_find.items():
        # Allow some tolerance (±5)
        tolerance = 10
        mask = np.all(np.abs(rgb_array - rgb_value) < tolerance, axis=2)
        pixel_count = np.sum(mask)
        percentage = (pixel_count / (rgb_array.shape[0] * rgb_array.shape[1])) * 100

        if pixel_count > 0:
            print(f"✅ {color_name}: {pixel_count} pixels ({percentage:.2f}%)")
        else:
            print(f"❌ {color_name}: Not found")

    # Quality assessment
    print("\n=== ✅ Vectorization Readiness ===")

    checks = []

    # Check 1: Correct dimensions
    if img.size == (512, 512):
        print("✅ Dimensions: 512×512 (perfect)")
        checks.append(True)
    else:
        print(f"⚠️  Dimensions: {img.size} (expected 512×512)")
        checks.append(False)

    # Check 2: Limited colors
    if len(unique_colors) <= 15:
        print(f"✅ Color count: {len(unique_colors)} (good for vectorization)")
        checks.append(True)
    else:
        print(f"⚠️  Color count: {len(unique_colors)} (may have gradients)")
        checks.append(False)

    # Check 3: High contrast
    if img.mode in ['RGB', 'RGBA']:
        if contrast > 70:
            print(f"✅ Contrast: {contrast:.2f} (high)")
            checks.append(True)
        else:
            print(f"⚠️  Contrast: {contrast:.2f} (low)")
            checks.append(False)

    # Overall assessment
    print("\n" + "="*40)
    if all(checks):
        print("🎯 VERDICT: EXCELLENT - Ready for vectorization")
        return 0
    elif sum(checks) >= len(checks) * 0.6:
        print("⚠️  VERDICT: ACCEPTABLE - May need adjustments")
        return 0
    else:
        print("❌ VERDICT: POOR - Not optimal for vectorization")
        return 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_png.py <path_to_png>")
        sys.exit(1)

    png_path = sys.argv[1]
    sys.exit(analyze_png(png_path))
