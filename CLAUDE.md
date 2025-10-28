# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is **Docencia**, a unified platform for interactive teaching materials developed by Juan Zuluaga (Julián Zuluaga) for Universidad Externado de Colombia. The repository centralizes course materials, reusable components, tools for content generation, and experimental workflows for AI-assisted teaching content creation.

## Project Context

**Owner:** Julián Zuluaga
- **Primary Role:** Professor at Universidad Externado (courses: Minería de Datos, IA Corporativa)
- **Secondary Role:** Founder of Orbital Lab (AI startup with 5 verticals: Strivio, Lighthouse, Jaguar, AI Systems, Academia)
- **Time Distribution:** Teaching 25%, Orbital Lab 60%, Personal/Legal 15%

**Key Personas & Projects:**
- Teaching materials for data mining and AI courses
- Orbital Lab brand system and visual identity (5 **verticales**: Deportes, Negocio, Biología, Otros, Academia)
- Experimental workflows for AI-generated educational content
- Integration with personal productivity systems (Notion, Google Calendar)

**IMPORTANT - Orbital Lab Verticales:**
- **Verticales** = Permanent categories (Deportes, Negocio, Biología, Otros, Academia)
- **Proyectos** = Specific implementations (e.g., Strivio, Lighthouse, Jaguar - these are examples, NOT the verticals)
- **Assets naming**: Always use vertical names (`deportes-icon.svg`), NEVER project names (`strivio-icon.svg`)
- See `docs/brand/VERTICALES_REFERENCE.md` for complete guide

## Directory Structure

```
docencia/
├── materias/                    # Active courses
│   ├── mineria-de-datos/        # Data Mining course (Externado)
│   └── inteligencia-artificial-para-negocios/  # Business AI course (Compensar @ Externado)
├── recursos_compartidos/        # Reusable assets across courses
│   ├── componentes/             # HTML/CSS/JS components
│   ├── datasets/                # Shared datasets (small examples only)
│   ├── plantillas/              # Templates for classes/materials
│   └── tutoriales/              # Cross-course tutorials
├── herramientas/                # Automation scripts and tools
│   └── scripts/                 # Python utilities for content generation
├── experimentos/                # AI experiments (image generation, vectorization)
├── docs/                        # Documentation and memory
│   ├── agent_memory.md          # Instructions for AI agents
│   ├── perfil_profesional.md   # Professional profile
│   ├── orbital_lab.md           # Orbital Lab identity
│   └── brand/                   # Brand manifesto and guidelines
├── skills/                      # Thematic modules (in development)
├── site/                        # Master web platform (planned)
└── .claude/                     # Claude Code local configuration
    ├── settings.local.json      # Auto-approved permissions
    └── skills/                  # Project-specific skills
        └── svg-icon-generator/  # SVG icon generation skill
```

## Common Development Tasks

### Working with Course Materials

**Create a new class:**
```bash
python herramientas/scripts/nueva_clase.py --materia mineria-de-datos --fecha 2025-11-05 --tema "Modelado Predictivo"
```

**Generate CRISP-DM interactive guide:**
```bash
python herramientas/scripts/generar_guia_crispdm.py -d recursos_compartidos/datasets/ejemplo.csv -o output/guia_interactiva.html
```

### Python Environment Setup

**All Python scripts use virtual environments:**
```bash
# Create venv (per experiment/class)
python -m venv venv

# Activate
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r herramientas/requirements.txt
```

**IMPORTANT:** Never commit `venv/` directories. They are gitignored globally.

### Working with Experiments

The `experimentos/` directory contains AI-powered workflows:

**Image generation experiments:**
- `replicate-sdxl-test/`: Replicate API + SDXL model testing
- `nano-banana-test/`: Google Vertex AI testing (requires billing)
- See `experimentos/RESUMEN_FINAL_OPCIONES.md` for comparison

**SVG vectorization:**
```bash
cd experimentos/svg-vectorization-real
source venv/bin/activate
python png_to_vector_optimized.py input.png output.svg
```

### Managing Datasets

**Dataset policy:**
- Store **small example datasets** in `recursos_compartidos/datasets/`
- Large datasets (>10MB) are **gitignored** by default
- Reference datasets in class materials using relative paths
- Document dataset sources and licenses in README files

## Architecture Principles

### Course Structure (`materias/`)

Each course follows this pattern:
```
materias/<course-slug>/
├── README.md          # Course overview, schedule, class index
├── docs/              # Pedagogical documentation, bibliography
├── clases/            # Individual class sessions
│   └── YYYY-MM-DD-clase-XX-tema/
│       ├── README.md      # Objectives, materials, agenda
│       ├── datasets/      # Class-specific data
│       ├── notebooks/     # Jupyter notebooks
│       ├── scripts/       # Analysis scripts
│       └── output/        # Generated materials (gitignored)
└── recursos/          # Course-specific resources
```

**Naming convention:** `YYYY-MM-DD-clase-XX-tema` (e.g., `2025-10-23-clase-02-crisp-dm`)

### Reusable Components (`recursos_compartidos/`)

**When to move content here:**
- Visual components used in multiple classes (HTML/CSS/JS)
- Datasets referenced by multiple courses
- Templates for generating new materials
- Cross-course tutorials (Git, Python environments, etc.)

**When to keep content in course folders:**
- Class-specific analysis scripts
- Course-specific pedagogical docs
- One-off generated materials

### Tools and Automation (`herramientas/`)

**Current scripts:**
- `scripts/generar_guia_crispdm.py`: Generate CRISP-DM interactive guides (Plotly)
- `scripts/nueva_clase.py`: Scaffold new class structure

**Roadmap:**
- Template system using `cookiecutter` or `copier`
- Automated content indexing for `site/`
- CI/CD pipeline for deploying to GitHub Pages

### Experiments (`experimentos/`)

**Purpose:** Test AI workflows before integrating into production teaching materials.

**Key experiments:**
1. **Image generation** (Replicate SDXL, Hugging Face, local ComfyUI)
2. **SVG vectorization** (PNG → SVG with color quantization)
3. **Video generation** (attempted with Luma AI - ongoing)

**Workflow:**
- Each experiment has isolated `venv/`
- Results documented in experiment README
- Successful workflows graduate to `herramientas/` or `.claude/skills/`

## Brand System

**Orbital Lab Identity:**
- Primary brand: Orbital Lab (parent company)
- **5 Verticales (categories):** Deportes, Negocio, Biología, Otros, Academia
- **Current projects (examples):** Strivio (Deportes), Lighthouse (Negocio), Jaguar (Biología), AI Systems (Otros), Academia Orbital (Academia)
- Visual system: Black (#000000), Red (#ED2024), Cyan (#00D4FF)
- Assets: `docs/brand/`, `recursos_compartidos/componentes/orbital_lab/`
- **Critical:** Assets are ALWAYS named by vertical (`deportes-*`, `negocio-*`), NEVER by project name

**Usage in teaching:**
- Course materials use Orbital branding for consistency
- Generated assets follow brand color palette
- Icon system represents each vertical

## AI Integration Notes

### Claude Code Skills

**Project-local skill:**
- `svg-icon-generator`: Converts PNG images to brand-colored SVG icons
  - Automatically quantizes to Orbital brand colors
  - Optimized SVG output with SVGO
  - Used for vertical iconography

**Global skills (from `~/.claude/`):**
- `image-generation-expert`: Professional image generation with SDXL/Flux models
  - Activates on keywords: "genera imagen", "create image", "logo"
  - Prompt engineering optimization
  - Cost tracking and model selection

### MCP Servers Available

**User-level (global) MCP servers:**
- **Context7**: Up-to-date library documentation
- **Perplexity**: Deep research (credit-limited, fallback to WebSearch)
- **Figma**: Design-to-code workflows
- **Replicate**: AI image generation API
- **Playwright**: Headless browser automation
- **Browser MCP**: Real Chrome automation (authenticated sessions)
- **Notion**: Workspace integration (for Orbital Assistant)
- **Google Calendar**: Calendar management and sync
- **Google Docs & Drive**: Document and file management

### Image Generation Workflows

**Recommended approach (as of 2025):**
1. **Hugging Face** (free, no credit card): 1,000 images/month
2. **Replicate + SDXL** ($5 credit, requires card): $0.002/image
3. **Local ComfyUI** (free, requires GPU): Unlimited

See `experimentos/RESUMEN_FINAL_OPCIONES.md` for detailed comparison.

## Documentation Strategy

**Memory for AI agents:**
- `docs/agent_memory.md`: Instructions for CLI agents working in this repo
- `docs/perfil_profesional.md`: Julián's professional context
- `docs/orbital_lab.md`: Company identity and mission
- `docs/brand/`: Visual identity system and manifesto

**For new contributors:**
- `README.md`: Repository overview and getting started
- `ARCHITECTURE.md`: Architectural principles and workflows
- Course-level: `materias/<course>/README.md`
- Class-level: `materias/<course>/clases/<session>/README.md`

## Development Best Practices

### Code Organization

- Keep Python dependencies in course/experiment-level `requirements.txt`
- Never version `venv/`, `__pycache__/`, or `.ipynb_checkpoints/`
- Large datasets (>10MB) are gitignored - document source URLs instead
- Reuse HTML/CSS/JS components from `recursos_compartidos/componentes/`

### Naming Conventions

- **Classes:** `YYYY-MM-DD-clase-XX-tema` (hyphen-separated, lowercase)
- **Courses:** `slug-de-materia` (e.g., `mineria-de-datos`)
- **Scripts:** `verb_noun.py` (e.g., `generar_guia_crispdm.py`)
- **Datasets:** `descriptive_name.csv` (e.g., `supermarket_analysis.csv`)

### Git Workflow

- Centralize datasets in `recursos_compartidos/datasets/` when shared
- Document script dependencies and usage in README files
- Update course README tables when adding new classes
- Move successful experiment code to `herramientas/` when production-ready

### Testing and Validation

- Add usage examples to script docstrings
- Test generation scripts with sample datasets before deploying
- Validate HTML outputs in multiple browsers
- Document any manual steps required after generation

## Integration with External Systems

**Notion (Orbital Assistant):**
- Project management in Notion workspace
- Sync between teaching schedule and personal productivity system
- See `productividadPersonal/personalAgent/` (external repo)

**Google Calendar:**
- Class schedules synced with personal calendar
- Time blocking for course preparation
- Conflict detection with Orbital Lab projects

**VSCode Integration:**
- Claude Code runs as native extension
- File references use clickable markdown links
- Auto-approved permissions in `.claude/settings.local.json`

## Troubleshooting

**Perplexity MCP 401 errors:**
- Monthly credit limits exceeded
- Automatically fallback to native `WebSearch` tool
- See global `CLAUDE.md` instructions for handling

**Missing datasets:**
- Large files are gitignored - check course README for download URLs
- Example datasets should be in `recursos_compartidos/datasets/`

**Import errors:**
- Ensure virtual environment is activated
- Check `requirements.txt` in relevant directory
- Install with `pip install -r requirements.txt`

## Roadmap

**Short-term:**
- Complete `site/` master platform (framework, build, deployment)
- Standardize class templates with `cookiecutter`
- Extract reusable HTML components from existing classes
- Automate course index generation

**Long-term:**
- Publish `skills/` as documented thematic modules
- CI/CD pipeline for GitHub Pages deployment
- Automated grading scripts integration
- Student submission portal

---

**Last updated:** 2025-10-28
**Maintained by:** Julián Zuluaga (Orbital Lab / Universidad Externado)
