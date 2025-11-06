#!/usr/bin/env python3
"""
Generate placeholder assets for Clase 04 - NotebookLM
Following the same style as other class placeholders
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Colors - Orbital brand
BLACK = (0, 0, 0)
RED = (237, 32, 36)  # #ED2024
CYAN = (0, 212, 255)  # #00D4FF
WHITE = (255, 255, 255)

# Directories
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VINYLS_DIR = os.path.join(SCRIPT_DIR, "vinyls/clase-04")
HALOS_DIR = os.path.join(SCRIPT_DIR, "halos")
SPINES_DIR = os.path.join(SCRIPT_DIR, "spines")

os.makedirs(VINYLS_DIR, exist_ok=True)
os.makedirs(HALOS_DIR, exist_ok=True)
os.makedirs(SPINES_DIR, exist_ok=True)


def create_vinyl_placeholder(output_path: str):
    """
    Create vinyl placeholder: 1024x1024px circular gradient
    Theme: NotebookLM / Research / Connected brain
    """
    size = 1024
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Create radial gradient effect (black to cyan/red)
    center = size // 2
    for i in range(center, 0, -3):
        # Mix cyan and red based on radius
        factor = i / center
        r = int(RED[0] * (1 - factor) + CYAN[0] * factor * 0.3)
        g = int(RED[1] * (1 - factor) + CYAN[1] * factor * 0.3)
        b = int(RED[2] * (1 - factor) + CYAN[2] * factor * 0.7)
        alpha = int(255 * factor)

        draw.ellipse(
            [center - i, center - i, center + i, center + i],
            fill=(r, g, b, alpha),
            outline=None
        )

    # Inner circle (darker)
    inner_radius = center // 3
    draw.ellipse(
        [center - inner_radius, center - inner_radius,
         center + inner_radius, center + inner_radius],
        fill=(20, 20, 40, 255),
        outline=None
    )

    # Save as PNG first, then convert to WebP
    png_path = output_path.replace('.webp', '.png')
    img.save(png_path, "PNG")
    img.save(output_path, "WEBP", quality=85)
    print(f"✓ Created vinyl: {output_path}")


def create_halo_placeholder(output_path: str):
    """
    Create halo background: 2400x1400px gradient
    Theme: Cyan/Purple for research/learning vibe
    """
    width, height = 2400, 1400
    img = Image.new("RGB", (width, height), BLACK)
    draw = ImageDraw.Draw(img)

    # Create horizontal gradient with glow spots
    for y in range(height):
        factor = y / height
        # Cyan to purple gradient
        r = int(CYAN[0] * (1 - factor) + 150 * factor)
        g = int(CYAN[1] * (1 - factor) + 50 * factor)
        b = int(CYAN[2] * (1 - factor) + 200 * factor)

        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Add glow circles (simulating notebook pages)
    glow_positions = [(600, 400), (1200, 800), (1800, 500)]
    for x, y in glow_positions:
        for radius in range(200, 0, -10):
            alpha = int(30 * (radius / 200))
            color = (CYAN[0] + 30, CYAN[1] + 30, CYAN[2], alpha)
            draw.ellipse(
                [x - radius, y - radius, x + radius, y + radius],
                fill=None,
                outline=color,
                width=2
            )

    # Save
    png_path = output_path.replace('.webp', '.png')
    img.save(png_path, "PNG")
    img.save(output_path, "WEBP", quality=85)
    print(f"✓ Created halo: {output_path}")


def create_spine_placeholder(output_path: str):
    """
    Create spine decoration: 400x1400px vertical gradient
    Theme: Cyan accent for NotebookLM
    """
    width, height = 400, 1400
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Vertical gradient (cyan to transparent)
    for x in range(width):
        factor = x / width
        alpha = int(200 * (1 - factor))
        draw.line([(x, 0), (x, height)], fill=(*CYAN, alpha))

    # Try to add text (may fail if font not available)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
        text = "CLASE 04"

        # Rotate text
        txt_img = Image.new("RGBA", (height, width), (0, 0, 0, 0))
        txt_draw = ImageDraw.Draw(txt_img)
        txt_draw.text((height // 2, width // 2), text, font=font, fill=(*WHITE, 200), anchor="mm")
        txt_img = txt_img.rotate(90, expand=True)

        # Paste rotated text
        img.alpha_composite(txt_img, (0, 0))
    except Exception as e:
        print(f"  ⚠ Could not add text to spine: {e}")
        print("  Spine will be generated without text")

    # Save
    img.save(output_path, "PNG")
    print(f"✓ Created spine: {output_path}")


def main():
    print("Generating Clase 04 placeholder assets...")
    print()

    # Generate all three assets
    create_vinyl_placeholder(os.path.join(VINYLS_DIR, "vinilo.webp"))
    create_halo_placeholder(os.path.join(HALOS_DIR, "clase-04.webp"))
    create_spine_placeholder(os.path.join(SPINES_DIR, "clase-04.png"))

    print()
    print("✓ All assets generated successfully!")
    print()
    print("Asset locations:")
    print(f"  - Vinyl: {VINYLS_DIR}/vinilo.webp")
    print(f"  - Halo: {HALOS_DIR}/clase-04.webp")
    print(f"  - Spine: {SPINES_DIR}/clase-04.png")


if __name__ == "__main__":
    main()
