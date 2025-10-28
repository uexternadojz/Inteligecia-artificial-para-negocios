#!/bin/bash
set -e

# Get skill directory (parent of scripts/)
SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="$SKILL_DIR/venv"

echo "🔧 Setting up svg-icon-generator skill environment..."
echo "📍 Skill location: $SKILL_DIR"

# Create venv if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
else
    echo "✅ Virtual environment already exists"
fi

# Activate and install dependencies
echo "📥 Installing dependencies..."
source "$VENV_DIR/bin/activate"
pip install --upgrade pip -q
pip install Pillow numpy svgwrite -q

echo ""
echo "✅ Skill environment ready!"
echo "📦 Installed packages:"
pip list | grep -E "(Pillow|numpy|svgwrite)"
echo ""
echo "To activate manually:"
echo "  source $VENV_DIR/bin/activate"
