#!/bin/bash
# Batch vectorize all 5 vertical icons with V1 method

set -e

# Activate venv
source venv/bin/activate

# Define source and output directories
SOURCE_DIR="../../recursos_compartidos/componentes/orbital_lab/assets/lab"
OUTPUT_DIR="./output"

# Create output directory
mkdir -p "$OUTPUT_DIR"

echo "╔══════════════════════════════════════════════════════════════════════════════╗"
echo "║       🎨 BATCH VECTORIZATION - V1 METHOD (Optimized Contour Tracing)        ║"
echo "╚══════════════════════════════════════════════════════════════════════════════╝"
echo ""

# Array of icon names
ICONS=("deportes" "negocio" "biologia" "academia" "otros")

# Process each icon
for icon in "${ICONS[@]}"; do
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "🔄 Processing: $icon"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    INPUT_PNG="$SOURCE_DIR/${icon}-icon.png"
    OUTPUT_SVG="$OUTPUT_DIR/${icon}-icon-optimized.svg"

    # Check if PNG exists
    if [ ! -f "$INPUT_PNG" ]; then
        echo "❌ Error: $INPUT_PNG not found"
        continue
    fi

    # Vectorize
    python png_to_vector_clean.py "$INPUT_PNG" "$OUTPUT_SVG"

    echo ""
done

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ BATCH VECTORIZATION COMPLETE"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📊 Summary:"
echo ""
ls -lh "$OUTPUT_DIR"/*.svg | awk '{print "  " $9 " - " $5}'
echo ""
echo "🔍 Total disk usage:"
du -sh "$OUTPUT_DIR"
echo ""
echo "💡 Next steps:"
echo "  1. Review SVG files in: $OUTPUT_DIR"
echo "  2. Compare with originals"
echo "  3. Replace originals if approved"
