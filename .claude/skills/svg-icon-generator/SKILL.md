---
name: "svg-icon-generator"
description: "Generate SVG icons with Orbital brand colors (black #000000, red #ED2024, cyan #00D4FF) from AI images. Automatically quantizes PNG to 4 exact brand colors and vectorizes to optimized SVG. Use when user needs icons, vertical illustrations, brand assets, or mentions 'generate icon', 'crear ícono', 'vectorize', 'quantize colors', 'colores de marca', 'Strivio', 'Lighthouse', 'Jaguar', 'AI Systems', 'Academia', or any of the 5 Orbital verticals."
version: "1.0.0"
dependencies: "python>=3.8, Pillow, numpy, svgwrite"
---

# SVG Icon Generator Skill

Automated pipeline for generating production-ready SVG icons with exact Orbital Lab brand colors.

**Validated Methodology:** Based on Oct 27, 2025 experiment with 2 SDXL iterations + quantization + vectorization testing.

---

## Quick Start

Generate an icon for any Orbital vertical in 3 steps:

```bash
# Step 1: Generate PNG with AI (use Replicate MCP)
# Step 2: Quantize to brand colors
# Step 3: Vectorize to SVG
```

**Total time:** ~10 seconds | **Cost:** $0.002 per icon

---

## Pipeline Steps

### Step 1: Generate PNG with AI

Use **Replicate MCP** with SDXL model:

**Parameters:**
- Model: `stability-ai/sdxl`
- Dimensions: 512×512
- Steps: 28
- Guidance: 7.5-8
- Scheduler: K_EULER

**Prompt template:**
```
flat vector icon, [SUBJECT] with neural network lines, geometric [PATTERN],
black background, red cyan accents, solid colors only, hard edges,
minimalist tech graphic, NO gradients NO shadows
```

**Negative prompt:**
```
gradients, shadows, textures, photorealistic, soft edges, blur, smooth, realistic, 3d, depth, shading, lighting
```

See `resources/vertical-prompts.md` for optimized prompts for each vertical.

**Output:** Raw PNG (~334 KB, 50k-70k colors)

---

### Step 2: Quantize to Brand Colors ⭐ (CRITICAL)

This is the **core transformation** that makes AI-generated images brand-consistent.

**Activate venv:**
```bash
source .claude/skills/svg-icon-generator/venv/bin/activate
```

**Run quantization:**
```bash
python .claude/skills/svg-icon-generator/scripts/quantize_colors.py \
  input.png \
  output-quantized.png \
  '#000000' '#ED2024' '#00D4FF' '#FFFFFF'
```

**What it does:**
- Reduces 50k+ colors → exactly 4 brand colors
- Increases contrast (typically 90-110 → 107-119)
- Distributes colors: Black ~60%, Red ~12%, Cyan ~12%, White ~14%
- File size: 334 KB → ~18 KB

**Expected results:**
```
📊 Colors used: 4
  #000000: ~160,000 pixels (60-65%)
  #ed2024: ~30,000 pixels (10-15%)  ← Orbital red
  #00d4ff: ~32,000 pixels (10-15%)  ← Tech cyan
  #ffffff: ~36,000 pixels (10-20%)
```

**Validate with analyzer:**
```bash
python .claude/skills/svg-icon-generator/scripts/analyze_png.py output-quantized.png
```

**Success criteria:**
- ✅ Verdict: "EXCELLENT - Ready for vectorization"
- ✅ 4 unique colors
- ✅ Contrast >70 (typically 107-119)
- ✅ All 3 brand colors detected

---

### Step 3: Vectorize to SVG

**Run vectorization:**
```bash
python .claude/skills/svg-icon-generator/scripts/png_to_svg_optimized.py \
  output-quantized.png \
  output.svg
```

**What it does:**
- Converts pixels to rectangles with horizontal merging
- Optimizes from naive 262k rects → ~11k rects (95% reduction)
- Generates web-ready SVG

**Output:**
- File size: ~440-490 KB
- Elements: 10k-12k rectangles
- Format: SVG with `<rect>` elements grouped by color

**Limitation:** This produces rect-based SVG. For production (<50 KB, path-based), use Inkscape:
```bash
# Optional production step (requires Inkscape installed):
inkscape output-quantized.png \
  --export-type=svg \
  --export-plain-svg \
  --export-filename=output-production.svg
```

---

## Vertical-Specific Configuration

### The 5 Orbital Verticals

1. **Strivio (Deportes)** - Soccer ball + neural network tracking
2. **Lighthouse Audience (Negocio)** - Analytics graph + data nodes
3. **Jaguar Orbital (Biología)** - Jaguar + forest network
4. **AI Systems (Otros)** - Circuit board + data flow
5. **Academia Orbital (Academia)** - Graduation cap + learning paths

**See `resources/vertical-prompts.md` for complete optimized prompts.**

---

## Virtual Environment Setup

**IMPORTANT:** This skill has its own isolated venv to avoid dependency conflicts.

### First-Time Setup

If venv doesn't exist, run:
```bash
bash .claude/skills/svg-icon-generator/scripts/setup_venv.sh
```

This installs:
- Pillow (image processing)
- numpy (color analysis)
- svgwrite (SVG generation)

### Activate Before Running Scripts

```bash
source .claude/skills/svg-icon-generator/venv/bin/activate
```

**Note:** Always activate venv before executing Python scripts to ensure correct dependencies.

---

## File Organization

**Input:** Save AI-generated PNGs to `output/` in project root

**Output structure:**
```
output/
├── {vertical}-icon-raw.png          (Original AI generation)
├── {vertical}-icon-quantized.png    (⭐ Brand colors applied)
└── {vertical}-icon.svg              (Vectorized output)
```

**Example:**
```
output/
├── strivio-icon-raw.png
├── strivio-icon-quantized.png       ← Use this for professional vectorization
└── strivio-icon.svg
```

---

## Cost & Performance

| Metric | Value |
|--------|-------|
| AI Generation (SDXL) | $0.002 per image |
| Quantization | Free (local compute) |
| Vectorization | Free (local compute) |
| **Total per icon** | **$0.002** |
| Generation time | 1-2 seconds |
| Quantization time | 3 seconds |
| Vectorization time | 5 seconds |
| **Total time** | **~10 seconds** |

**For all 5 verticals:** $0.01 total, ~50 seconds

---

## Methodology & Key Findings

Based on validated experiment (see `resources/methodology.md`):

### ✅ What Works Extremely Well

1. **Color Quantization** - 99.99% color reduction with quality improvement
2. **Brand Color Enforcement** - Forces exact hex values (#000000, #ED2024, #00D4FF)
3. **Contrast Enhancement** - Typically increases from ~95 to ~115
4. **Automated Pipeline** - Fully scriptable, repeatable results
5. **Cost Efficiency** - $0.002 per icon, ~10 seconds

### ❌ What Doesn't Work

1. **SDXL Direct Generation** - Cannot generate flat vector style (always photorealistic)
2. **Prompt Engineering Alone** - V2 optimized prompt was WORSE than V1 (more colors)
3. **Python-Only Path Vectorization** - Produces large files (need Inkscape for production)

### 🎯 Critical Insight

**Post-processing > Prompt engineering** for exact brand color control.

Trying to make SDXL generate flat graphics is futile. Instead:
- Accept photorealistic output
- Transform it with quantization
- Get perfect brand colors every time

### 📊 V2 Methodology (Preferred)

The experiment validated two approaches. **V2 is superior:**

**Why V2 wins:**
- 113% more cyan (12.63% vs 5.92%)
- 35% more red (11.56% vs 8.59%)
- Better visual balance (less white, more color)
- User aesthetic preference

**V2 Prompt:**
```
flat vector icon, soccer ball with neural network lines, geometric heatmap,
black background, red cyan accents, solid colors only, hard edges,
minimalist tech graphic, NO gradients NO shadows
```

**V2 Results:**
- Unique colors: 4 ✅
- Contrast: 106.81 ✅
- Black: 62.05%, Red: 11.56%, Cyan: 12.63%, White: 13.76%
- Distribution: Nearly uniform red/cyan (~12% each) = strong brand identity

---

## Examples & Common Patterns

### Example 1: Generate Lighthouse Icon

```bash
# User request: "genera el ícono de Lighthouse Audience"

# Step 1: Claude activates skill, generates PNG with Replicate MCP
# Prompt: "flat vector icon, analytics graph with data nodes..."

# Step 2: Quantize
source .claude/skills/svg-icon-generator/venv/bin/activate
python .claude/skills/svg-icon-generator/scripts/quantize_colors.py \
  output/lighthouse-raw.png \
  output/lighthouse-quantized.png \
  '#000000' '#ED2024' '#00D4FF' '#FFFFFF'

# Step 3: Vectorize
python .claude/skills/svg-icon-generator/scripts/png_to_svg_optimized.py \
  output/lighthouse-quantized.png \
  output/lighthouse.svg

# Report results
python .claude/skills/svg-icon-generator/scripts/analyze_png.py \
  output/lighthouse-quantized.png
```

### Example 2: Batch Generate All 5 Verticals

```bash
# Generate all 5 icons sequentially
for vertical in strivio lighthouse jaguar ai-systems academia; do
  echo "🎨 Generating $vertical icon..."

  # Step 1: AI generation (Replicate MCP)
  # ... (Claude generates with appropriate prompt)

  # Step 2-3: Process with scripts
  source .claude/skills/svg-icon-generator/venv/bin/activate
  python .claude/skills/svg-icon-generator/scripts/quantize_colors.py \
    "output/${vertical}-raw.png" \
    "output/${vertical}-quantized.png" \
    '#000000' '#ED2024' '#00D4FF' '#FFFFFF'

  python .claude/skills/svg-icon-generator/scripts/png_to_svg_optimized.py \
    "output/${vertical}-quantized.png" \
    "output/${vertical}.svg"
done
```

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'PIL'"

**Solution:** Venv not activated
```bash
source .claude/skills/svg-icon-generator/venv/bin/activate
```

### Issue: "Command 'python' not found"

**Solution:** Use python3
```bash
python3 .claude/skills/svg-icon-generator/scripts/quantize_colors.py ...
```

Or activate venv (which provides `python` symlink):
```bash
source .claude/skills/svg-icon-generator/venv/bin/activate
python .claude/skills/svg-icon-generator/scripts/quantize_colors.py ...
```

### Issue: Quantized image has wrong colors

**Solution:** Verify hex codes match exactly
```bash
# Correct (with # prefix):
'#000000' '#ED2024' '#00D4FF' '#FFFFFF'

# Wrong (no # prefix):
'000000' 'ED2024' '00D4FF' 'FFFFFF'
```

### Issue: SVG file is huge (>1 MB)

**Expected:** Python vectorization produces 400-500 KB files with 10k-12k rects.

**For production (<50 KB):**
```bash
# Option 1: Use Inkscape (path-based vectorization)
inkscape quantized.png --export-type=svg --export-plain-svg --export-filename=final.svg

# Option 2: Manual vectorization in Figma/Illustrator
# Open quantized.png → Image Trace → Export SVG
```

---

## Advanced Usage

### Custom Color Palettes

Use different brand colors:
```bash
python .claude/skills/svg-icon-generator/scripts/quantize_colors.py \
  input.png \
  output.png \
  '#1a1a1a' '#ff6b35' '#00bfff' '#f0f0f0'
```

### Analyze Before Quantization

Check original image metrics:
```bash
python .claude/skills/svg-icon-generator/scripts/analyze_png.py raw-input.png
```

Expected issues:
- 50k-70k unique colors
- Low brand color presence (<1%)

---

## When to Use This Skill

### ✅ Automatic Activation Triggers

- "generate icon for [vertical]"
- "crear ícono de Strivio/Lighthouse/Jaguar/etc"
- "vectorize this image with brand colors"
- "quantize to Orbital palette"
- "apply brand colors to this PNG"
- Any mention of the 5 verticals

### ✅ Best For

- Orbital Lab vertical icons
- Brand-consistent illustrations
- Automated asset generation
- Rapid prototyping with exact colors

### ❌ Not Suitable For

- Photos (use original)
- Complex gradients (quantization removes them)
- Multi-brand projects (single palette hardcoded)

---

## Resources

- `resources/methodology.md` - Complete experiment analysis
- `resources/brand-palette.json` - Color specs and vertical definitions
- `resources/vertical-prompts.md` - Optimized prompts for each vertical

---

## Maintenance

**Update prompts:** Edit `resources/vertical-prompts.md`
**Update colors:** Edit hex codes in scripts or `resources/brand-palette.json`
**Add dependencies:** Add to `scripts/setup_venv.sh` and re-run

---

**Skill Status:** Production-ready ✅
**Last Updated:** October 27, 2025
**Validated With:** Strivio icon (V2 methodology)
