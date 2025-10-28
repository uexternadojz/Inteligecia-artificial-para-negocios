# SVG Icon Generator Skill

**Status:** Production-ready ✅
**Version:** 1.0.0
**Last Updated:** October 27, 2025

---

## What This Skill Does

Automatically generates SVG icons with exact Orbital Lab brand colors through:
1. AI image generation (Replicate SDXL)
2. Color quantization to 4 brand colors
3. SVG vectorization with optimization

**Total time:** ~10 seconds | **Cost:** $0.002 per icon

---

## Quick Start

### 1. First-Time Setup (Already Done ✅)

The venv is already set up with all dependencies:
```bash
source .claude/skills/svg-icon-generator/venv/bin/activate
python -c "import PIL, numpy, svgwrite; print('✅ All dependencies ready')"
```

### 2. Generate an Icon

Just ask Claude in natural language:
```
"genera el ícono de Lighthouse Audience"
"create icon for Jaguar Orbital"
"vectorize this image with brand colors"
```

Claude will automatically:
- Detect the request
- Activate this skill
- Generate PNG with AI
- Quantize to brand colors
- Vectorize to SVG
- Report results

---

## Manual Usage

If you want to run scripts directly:

```bash
# Activate venv
source .claude/skills/svg-icon-generator/venv/bin/activate

# Quantize image
python scripts/quantize_colors.py \
  input.png \
  output-quantized.png \
  '#000000' '#ED2024' '#00D4FF' '#FFFFFF'

# Vectorize to SVG
python scripts/png_to_svg_optimized.py \
  output-quantized.png \
  output.svg

# Analyze quality
python scripts/analyze_png.py output-quantized.png
```

---

## File Structure

```
.claude/skills/svg-icon-generator/
├── README.md                    (this file)
├── SKILL.md                     (Claude's instructions)
├── venv/                        (Python virtual environment)
│   ├── bin/python
│   └── lib/
├── scripts/
│   ├── quantize_colors.py       (⭐ core transformation)
│   ├── png_to_svg_optimized.py  (vectorization)
│   ├── analyze_png.py           (quality validation)
│   └── setup_venv.sh            (venv setup)
└── resources/
    ├── methodology.md           (experiment findings)
    ├── brand-palette.json       (Orbital colors spec)
    └── vertical-prompts.md      (AI prompts for verticals)
```

---

## Orbital Verticals

1. **Strivio (Deportes)** ✅ - Soccer + neural networks
2. **Lighthouse (Negocio)** - Analytics + data nodes
3. **Jaguar (Biología)** - Jaguar + forest network
4. **AI Systems (Otros)** - Circuit board + data flow
5. **Academia (Academia)** - Graduation cap + learning tree

---

## Brand Colors

- **Black** `#000000` - Primary background (60-65%)
- **Red** `#ED2024` - Orbital brand accent (10-15%)
- **Cyan** `#00D4FF` - Tech/AI accent (10-15%)
- **White** `#FFFFFF` - Highlights (10-20%)

---

## Key Features

✅ **Automatic Activation** - Claude detects when you need icons
✅ **Brand Consistency** - Always uses exact color palette
✅ **Validated Methodology** - Based on Oct 27, 2025 experiment
✅ **Fast & Cheap** - 10 seconds, $0.002 per icon
✅ **Isolated Dependencies** - Own venv, no conflicts
✅ **Repo-Specific** - Only active in this project

---

## Success Criteria

After quantization, expect:
- ✅ 4 unique colors (from 50k+)
- ✅ High contrast (>100)
- ✅ All brand colors present
- ✅ Verdict: "EXCELLENT"

---

## Troubleshooting

### "ModuleNotFoundError"
**Solution:** Activate venv first
```bash
source .claude/skills/svg-icon-generator/venv/bin/activate
```

### SVG file is large (>500 KB)
**Expected:** Python vectorization produces ~490 KB files.

**For production (<50 KB):** Use Inkscape (optional)
```bash
inkscape quantized.png --export-type=svg --export-plain-svg --export-filename=final.svg
```

### Colors don't match after quantization
**Solution:** Verify hex codes include `#` prefix:
```bash
'#000000' '#ED2024' '#00D4FF' '#FFFFFF'  ✅ Correct
'000000' 'ED2024' '00D4FF' 'FFFFFF'      ❌ Wrong
```

---

## Documentation

- **SKILL.md** - Complete workflow and instructions
- **methodology.md** - Experiment findings and validation
- **vertical-prompts.md** - AI prompts for each vertical
- **brand-palette.json** - Color specifications

---

## Maintenance

**Update prompts:**
Edit `resources/vertical-prompts.md`

**Update colors:**
Edit hex codes in `brand-palette.json` and script calls

**Add dependencies:**
1. Add to `scripts/setup_venv.sh`
2. Run: `bash scripts/setup_venv.sh`

---

**Skill created:** October 27, 2025
**Based on:** Strivio icon validation (V2 methodology)
**Ready for:** All 5 Orbital verticals
