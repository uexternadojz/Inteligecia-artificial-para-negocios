# Optimized AI Prompts for Orbital Verticals

**Methodology:** Based on validated V2 approach (Oct 27, 2025)
**Model:** SDXL (stability-ai/sdxl)
**Validation:** Strivio icon successfully generated and quantized

---

## Template Structure

All prompts follow this proven structure:

```
flat vector icon, [SUBJECT] with neural network lines, geometric [PATTERN],
black background, red cyan accents, solid colors only, hard edges,
minimalist tech graphic, NO gradients NO shadows
```

**Key constraints:**
- Keep under 77 tokens (CLIP limit)
- Always include: "flat vector icon", "black background", "red cyan accents"
- Always exclude: "NO gradients NO shadows"
- Subject + Pattern = unique per vertical

---

## Universal Parameters

**SDXL Configuration:**
```json
{
  "model": "stability-ai/sdxl",
  "version": "39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
  "width": 512,
  "height": 512,
  "num_inference_steps": 28,
  "guidance_scale": 8,
  "scheduler": "K_EULER"
}
```

**Negative Prompt (Universal):**
```
gradients, shadows, textures, photorealistic, soft edges, blur, smooth, realistic, 3d, depth, shading, lighting
```

---

## Vertical 1: Strivio (Deportes) ✅ VALIDATED

**Subject:** Soccer ball
**Pattern:** Heatmap
**Status:** Production-ready

### Prompt
```
flat vector icon, soccer ball with neural network lines, geometric heatmap,
black background, red cyan accents, solid colors only, hard edges,
minimalist tech graphic, NO gradients NO shadows
```

### Expected Results
After quantization:
- Black: 62.05%
- Red: 11.56%
- Cyan: 12.63%
- White: 13.76%
- Contrast: 106.81
- Verdict: EXCELLENT

### Validation Data
- Generated: Oct 27, 2025
- Method: V2 (optimized 77-token prompt)
- Output: `output/strivio-icon-v2-quantized.png` (18 KB, 4 colors)
- SVG: `output/strivio-icon-v2-final.svg` (492 KB, 11k rects)

---

## Vertical 2: Lighthouse Audience (Negocio)

**Subject:** Urban skyline with lighthouse antenna rays
**Pattern:** Geometric audience analysis pattern
**Status:** Ready to generate
**Checklist Prompt:** Skyline urbano con faro/antena emitiendo rayos de análisis de audiencias, estilo arquitectónico minimal tech

### Prompt
```
flat vector icon, urban skyline with lighthouse antenna rays, geometric audience analysis pattern,
black background, red cyan accents, solid colors only, hard edges,
minimalist tech graphic, NO gradients NO shadows
```

### Keywords
- Analytics, OOH, audience measurement
- Lighthouse, urban, advertising tech
- Business intelligence, data visualization

---

## Vertical 3: Jaguar Orbital (Biología)

**Subject:** Jaguar silhouette with DNA pattern
**Pattern:** Geometric orbital sensor lines
**Status:** Ready to generate
**Checklist Prompt:** Silueta de jaguar con patrón de ADN y sensores orbitales, fusión naturaleza-tecnología, líneas orgánicas tech

### Prompt
```
flat vector icon, jaguar silhouette with DNA pattern, geometric orbital sensor lines,
black background, red cyan accents, solid colors only, hard edges,
minimalist tech graphic, NO gradients NO shadows
```

### Keywords
- Conservation, environmental monitoring
- Wildlife, jaguar, CV detection
- Biodiversity, nature-tech fusion

---

## Vertical 4: Academia Orbital (Academia)

**Subject:** Orbital book with data circuit lines
**Pattern:** Geometric knowledge flow pattern
**Status:** Ready to generate
**Checklist Prompt:** Libro orbital con circuitos de datos emanando, conocimiento tecnológico, educativo-futurista

### Prompt
```
flat vector icon, orbital book with data circuit lines, geometric knowledge flow pattern,
black background, red cyan accents, solid colors only, hard edges,
minimalist tech graphic, NO gradients NO shadows
```

### Keywords
- Education, training, courses
- AI literacy, knowledge flow
- Digital ethics, applied learning

---

## Vertical 5: AI Systems/Superagents (Otros)

**Subject:** Brain gear with connected nodes
**Pattern:** Geometric automation pattern
**Status:** Ready to generate
**Checklist Prompt:** Engranaje cerebral con nodos conectados representando automatización inteligente, mecánico-neuronal

### Prompt
```
flat vector icon, brain gear with connected nodes, geometric automation pattern,
black background, red cyan accents, solid colors only, hard edges,
minimalist tech graphic, NO gradients NO shadows
```

### Keywords
- Automation, RAG, agents
- Corporate systems, integrations
- Brain-mechanical, neural automation

---

## Prompt Engineering Notes

### ✅ What Works

1. **Concise structure** - Keep under 77 tokens
2. **Explicit negatives** - "NO gradients NO shadows" critical
3. **Style keywords** - "flat vector", "solid colors", "hard edges"
4. **Subject + Pattern** - Makes each vertical unique
5. **Brand colors mentioned** - "red cyan accents"

### ❌ What Doesn't Work

1. **Long detailed prompts** - Gets truncated by CLIP
2. **Relying on positive only** - Must use negative prompts
3. **Asking for specific colors** - SDXL ignores hex codes
4. **Expecting flat output** - SDXL is photorealistic (fix with quantization)

### 🎯 Critical Insight

**Don't fight SDXL's photorealistic nature.** Instead:
1. Generate with style hints
2. Accept photorealistic output
3. Transform with quantization
4. Get perfect brand colors

---

## Iteration Guidelines

If first generation doesn't meet expectations:

### Issue: Too much white background
**Solution:** Regenerate with same prompt (seed variation)

### Issue: Subject not clear
**Solution:** Emphasize subject in prompt:
```
flat vector icon, LARGE soccer ball [rest of prompt]
```

### Issue: Colors off after quantization
**Solution:** This is normal - quantization fixes it
- Original: 50k-70k colors
- Quantized: 4 colors (always works)

### Issue: Pattern not prominent
**Solution:** Adjust pattern description:
```
geometric heatmap → dense geometric heatmap pattern
```

---

## Batch Generation Script

Generate all 5 verticals sequentially:

```bash
#!/bin/bash
verticals=("strivio" "lighthouse" "jaguar" "ai-systems" "academia")

for vertical in "${verticals[@]}"; do
  echo "🎨 Generating $vertical icon..."

  # Step 1: Generate PNG with Replicate MCP
  # (Use appropriate prompt from this file)

  # Step 2: Quantize
  source .claude/skills/svg-icon-generator/venv/bin/activate
  python .claude/skills/svg-icon-generator/scripts/quantize_colors.py \
    "output/${vertical}-raw.png" \
    "output/${vertical}-quantized.png" \
    '#000000' '#ED2024' '#00D4FF' '#FFFFFF'

  # Step 3: Vectorize
  python .claude/skills/svg-icon-generator/scripts/png_to_svg_optimized.py \
    "output/${vertical}-quantized.png" \
    "output/${vertical}.svg"

  # Step 4: Validate
  python .claude/skills/svg-icon-generator/scripts/analyze_png.py \
    "output/${vertical}-quantized.png"

  echo "✅ $vertical complete"
  echo "---"
done

echo "🎉 All 5 verticals generated!"
echo "Total cost: $0.01"
```

---

## Examples of Good vs Bad Prompts

### ❌ Bad: Too Long
```
Create a highly detailed flat vector style illustration of a soccer ball
with neural network tracking visualization overlays showing player movement
patterns and heatmap data with geometric patterns in the background using
only solid colors with hard edges and no gradients or shadows on a pure
black background with red and cyan accent colors for a modern tech aesthetic
suitable for a sports analytics platform icon at 512x512 resolution
```
**Problem:** 95 tokens, will be truncated at 77

### ✅ Good: Concise
```
flat vector icon, soccer ball with neural network lines, geometric heatmap,
black background, red cyan accents, solid colors only, hard edges,
minimalist tech graphic, NO gradients NO shadows
```
**Success:** 27 words, ~35 tokens, under limit

---

## Quality Checklist

Before considering a generation successful:

- [ ] PNG generated (512×512)
- [ ] Quantization applied (4 colors)
- [ ] Analysis shows "EXCELLENT" verdict
- [ ] Black 55-65%
- [ ] Red 10-15%
- [ ] Cyan 10-15%
- [ ] White 10-20%
- [ ] Contrast >70 (ideally >100)
- [ ] SVG generated (<500 KB)
- [ ] Visually matches vertical theme

---

**Last Updated:** October 27, 2025
**Validated Verticals:** 1/5 (Strivio)
**Next to Generate:** Lighthouse Audience
