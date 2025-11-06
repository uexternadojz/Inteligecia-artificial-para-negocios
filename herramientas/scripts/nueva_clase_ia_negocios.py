#!/usr/bin/env python3
"""
Script de Automatización: Crear Nueva Clase IA para Negocios

Genera estructura de archivos, templates y actualiza course.ts
para crear una nueva clase del micrositio Astro.

Uso:
    python nueva_clase_ia_negocios.py \
        --numero 05 \
        --fecha 2025-11-06 \
        --tema "Agentes IA Autónomos" \
        --mood "Autonomous agents orchestrating tasks" \
        --stack "LangChain,CrewAI,AutoGPT" \
        --metrics "3:Arquitecturas:red,10x:Rápido:cyan"

Versión: 1.0
Autor: Julián Zuluaga (Orbital Lab)
"""

import argparse
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Tuple

# Pillow para generar placeholders
try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("⚠️ Pillow no instalado. Instalando...")
    os.system("pip install Pillow")
    from PIL import Image, ImageDraw, ImageFont


# ============================================
# CONFIGURACIÓN
# ============================================

# Rutas relativas al repo
REPO_ROOT = Path(__file__).parent.parent.parent
SITE_ROOT = REPO_ROOT / "materias/inteligencia-artificial-para-negocios/site"
ASSETS_ROOT = SITE_ROOT / "assets"
DATA_DIR = SITE_ROOT / "src/data"
PAGES_DIR = SITE_ROOT / "src/pages/clases"

# Brand colors Orbital Lab
BRAND_COLORS = {
    "black": "#000000",
    "black_soft": "#0b0b0f",
    "red": "#ED2024",
    "red_warm": "#FF3B30",
    "cyan": "#00D4FF",
    "gray": "#1F1F28",
    "gray_light": "#A2A5B3",
}


# ============================================
# FUNCIONES AUXILIARES
# ============================================

def parse_metrics(metrics_str: str) -> List[Tuple[str, str, str]]:
    """Parse string de métricas en formato 'valor:label:accent,valor:label:accent'"""
    if not metrics_str:
        return []

    metrics = []
    for metric in metrics_str.split(","):
        parts = metric.strip().split(":")
        if len(parts) == 3:
            metrics.append((parts[0], parts[1], parts[2]))

    return metrics


def slugify(text: str) -> str:
    """Convierte texto a slug (lowercase, hyphen-separated)"""
    text = text.lower()
    text = re.sub(r'[áàäâã]', 'a', text)
    text = re.sub(r'[éèëê]', 'e', text)
    text = re.sub(r'[íìïî]', 'i', text)
    text = re.sub(r'[óòöôõ]', 'o', text)
    text = re.sub(r'[úùüû]', 'u', text)
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def format_date(date_str: str) -> str:
    """Convierte YYYY-MM-DD a formato display (DD Mes YYYY)"""
    date = datetime.strptime(date_str, "%Y-%m-%d")
    months_es = [
        "", "Ene", "Feb", "Mar", "Abr", "May", "Jun",
        "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"
    ]
    return f"{date.day:02d} {months_es[date.month]} {date.year}"


def create_directories(numero: int):
    """Crea estructura de directorios para la clase"""
    dirs = [
        ASSETS_ROOT / f"vinyls/clase-{numero:02d}/original",
        ASSETS_ROOT / "halos",
        ASSETS_ROOT / "spines",
    ]

    for dir_path in dirs:
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"✅ Directorio creado: {dir_path.relative_to(REPO_ROOT)}")


def generate_placeholder_spine(numero: int):
    """Genera spine placeholder con Pillow"""
    # Dimensiones: 100x600px (lomo vertical)
    width, height = 100, 600
    img = Image.new('RGB', (width, height), BRAND_COLORS["black_soft"])
    draw = ImageDraw.Draw(img)

    # Gradiente simple rojo → cyan
    for y in range(height):
        ratio = y / height
        r = int(237 + (0 - 237) * ratio)  # #ED2024 → #00D4FF
        g = int(32 + (212 - 32) * ratio)
        b = int(36 + (255 - 36) * ratio)
        draw.rectangle([(0, y), (width, y + 1)], fill=(r, g, b))

    # Texto vertical (número de clase)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
    except:
        font = ImageFont.load_default()

    # Rotar texto
    txt_img = Image.new('RGBA', (200, 100), (0, 0, 0, 0))
    txt_draw = ImageDraw.Draw(txt_img)
    txt_draw.text((10, 10), f"{numero:02d}", fill="white", font=font)
    txt_img = txt_img.rotate(90, expand=True)

    # Pegar en centro
    img.paste(txt_img, ((width - txt_img.width) // 2, (height - txt_img.height) // 2), txt_img)

    # Guardar
    output_path = ASSETS_ROOT / f"spines/clase-{numero:02d}.png"
    img.save(output_path, "PNG")
    print(f"✅ Spine placeholder generado: {output_path.relative_to(REPO_ROOT)}")


def generate_placeholder_halo(numero: int):
    """Genera halo placeholder con Pillow"""
    # Dimensiones: 1920x1080px
    width, height = 1920, 1080
    img = Image.new('RGB', (width, height), BRAND_COLORS["black"])
    draw = ImageDraw.Draw(img)

    # Gradiente radial simple (centro rojo, bordes cyan)
    center_x, center_y = width // 2, height // 2
    max_radius = ((width // 2) ** 2 + (height // 2) ** 2) ** 0.5

    for y in range(height):
        for x in range(width):
            distance = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
            ratio = min(distance / max_radius, 1.0)

            # Rojo (#ED2024) en centro → Cyan (#00D4FF) en bordes
            r = int(237 + (0 - 237) * ratio)
            g = int(32 + (212 - 32) * ratio)
            b = int(36 + (255 - 36) * ratio)

            # Aplicar transparencia (muy suave)
            alpha = int(80 * (1 - ratio))
            draw.point((x, y), fill=(r, g, b))

    # Aplicar blur (simulado con resize)
    img = img.resize((width // 4, height // 4), Image.LANCZOS)
    img = img.resize((width, height), Image.LANCZOS)

    output_path = ASSETS_ROOT / f"halos/clase-{numero:02d}.png"
    img.save(output_path, "PNG")
    print(f"✅ Halo placeholder generado: {output_path.relative_to(REPO_ROOT)}")


def generate_data_template(numero: int, fecha: str, tema: str, mood: str,
                          stack: List[str], metrics: List[Tuple[str, str, str]]) -> str:
    """Genera template de clase-XX-data.ts"""

    # Formato de fecha
    date_formatted = format_date(fecha)

    # Generar imports de logos
    logo_imports = []
    for tool in stack:
        logo_name = slugify(tool.lower())
        logo_imports.append(f'import {logo_name}Logo from "../../assets/logos/{logo_name}.png";')

    logo_imports_str = "\n".join(logo_imports) if logo_imports else "// Logos de herramientas (añadir según necesidad)"

    # Generar métricas
    metrics_str = ""
    if metrics:
        metrics_lines = []
        for value, label, accent in metrics:
            metrics_lines.append(f'    {{ value: "{value}", label: "{label}", accent: "{accent}" }},')
        metrics_str = "\n".join(metrics_lines)
    else:
        metrics_str = """    { value: "[COMPLETAR]", label: "[LABEL]", accent: "red" },
    { value: "[COMPLETAR]", label: "[LABEL]", accent: "cyan" },
    { value: "[COMPLETAR]", label: "[LABEL]", accent: "red" },
    { value: "[COMPLETAR]", label: "[LABEL]", accent: "cyan" }"""

    # Template completo
    template = f"""/**
 * Data for Clase {numero:02d}: {tema}
 * Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
 */

// Hero images
import vinyl{numero:02d} from "../../assets/vinyls/clase-{numero:02d}/vinilo.webp";
import halo{numero:02d} from "../../assets/halos/clase-{numero:02d}.webp";

// Tool logos
{logo_imports_str}

// ============================================
// INTERFACES (Reutilizadas de clases anteriores)
// ============================================

export interface Metric {{
  value: string;
  label: string;
  accent: "red" | "cyan";
}}

export interface CTA {{
  label: string;
  href: string;
  icon?: string;
}}

export interface BentoItem {{
  badge: string;
  title: string;
  description: string;
  icon?: string;
}}

export interface Tool {{
  name: string;
  category: "research" | "learning" | "analysis" | "synthesis" | "development" | "design";
  url: string;
  logo?: string;
  description: string;
  pricing: string;
  stack: string[];
  idealFor: string[];
  limitations: string[];
  promptExample?: string;
}}

export interface WorkflowStep {{
  number: string;
  title: string;
  description: string;
  tips: string[];
}}

export interface UseCase {{
  title: string;
  context: string;
  tool: string;
  output: string;
}}

export interface PromptExample {{
  label: string;
  category: string;
  content: string;
}}

export interface BestPractice {{
  title: string;
  description: string;
  type: "do" | "dont";
}}

// ============================================
// HERO DATA
// ============================================

export const heroData = {{
  number: "{numero:02d}",
  title: "{tema}",
  subtitle: "[COMPLETAR: 1-2 líneas descriptivas del tema]",
  description:
    "[COMPLETAR: Párrafo extendido de 3-4 líneas explicando qué se cubrirá en la clase]",
  date: "{date_formatted}",
  duration: "2h",
  modality: "Práctica guiada 80/20",
  vinylImage: vinyl{numero:02d},
  haloImage: halo{numero:02d},
  metrics: [
{metrics_str}
  ] as Metric[],
  ctas: [
    {{
      label: "Ver Workflow",
      href: "#workflow",
      icon: "arrow-right",
    }},
    {{
      label: "Herramientas",
      href: "#tools",
      icon: "tool",
    }},
    {{
      label: "GitHub README",
      href: "https://github.com/uexternadojz/Inteligecia-artificial-para-negocios",
      icon: "github",
    }},
  ] as CTA[],
}};

// ============================================
// FUNDAMENTALS (Bento Grid)
// ============================================

export const fundamentals: BentoItem[] = [
  {{
    badge: "[CATEGORÍA]",
    title: "[TÍTULO CORTO]",
    description:
      "[DESCRIPCIÓN DETALLADA - 2-3 líneas explicando este concepto fundamental]",
    icon: "🤖", // Emoji relevante al tema
  }},
  // TODO: Añadir 3-5 items más
  // Variar longitud de descriptions para ritmo visual
  // Usar badges distintivos: "Concepto Clave", "Diferenciador", "Arquitectura", etc.
];

// ============================================
// TOOLS (Herramientas)
// ============================================

export const tools: Tool[] = [
  {{
    name: "[HERRAMIENTA 1]",
    category: "development", // research | learning | analysis | synthesis | development | design
    url: "https://...",
    logo: undefined, // Añadir si existe: {stack[0].lower()}Logo.src
    description:
      "[DESCRIPCIÓN TÉCNICA - 2-3 líneas explicando qué hace la herramienta y por qué es relevante]",
    pricing: "Gratis" | "Freemium" | "$XX/mes",
    stack: ["Tecnología 1", "Tecnología 2", "Tecnología 3"],
    idealFor: [
      "Caso de uso 1",
      "Caso de uso 2",
      "Caso de uso 3",
    ],
    limitations: [
      "Limitación 1",
      "Limitación 2",
    ],
    promptExample: `[PROMPT EJEMPLO CONCRETO Y COPY-PASTEABLE]

Estructura:
- Contexto claro
- Formato esperado
- Ejemplo específico
`,
  }},
  // TODO: Añadir 1-3 herramientas más del stack
];

// ============================================
// WORKFLOW STEPS (Opcional - si la clase tiene proceso paso a paso)
// ============================================

export const workflow: WorkflowStep[] = [
  {{
    number: "01",
    title: "[TÍTULO DEL PASO]",
    description:
      "[DESCRIPCIÓN DEL PASO - 2-3 líneas explicando qué se hace en este paso]",
    tips: [
      "Tip práctico 1",
      "Tip práctico 2",
      "Tip práctico 3",
    ],
  }},
  // TODO: Añadir pasos 02, 03, 04, etc.
  // Si la clase NO tiene workflow claro, comentar o eliminar esta sección
];

// ============================================
// USE CASES (Casos de Uso)
// ============================================

export const useCases: UseCase[] = [
  {{
    title: "[TÍTULO DESCRIPTIVO DEL CASO]",
    context:
      "[CONTEXTO: Problema, necesidad, objetivo del negocio - 3-4 líneas]",
    tool: "[HERRAMIENTA(S) USADA(S) + fuentes/datos si aplica]",
    output:
      "[OUTPUT TANGIBLE: Qué se generó, formato, métricas - 2-3 líneas]",
  }},
  // TODO: Añadir 1-2 casos más
  // Preferir casos reales o hipotéticos muy concretos
];

// ============================================
// PROMPT EXAMPLES (Biblioteca de Prompts)
// ============================================

export const promptExamples: PromptExample[] = [
  {{
    label: "[NOMBRE DEL PROMPT]",
    category: "[CATEGORÍA TEMÁTICA]", // Ej: "Análisis Estratégico", "Benchmarking"
    content: `[PROMPT MULTILINEA COPY-PASTEABLE]

Incluye:
- Contexto claro
- Estructura esperada
- Formato de salida

Ejemplo: "Genera un análisis SWOT para [EMPRESA]..."
`,
  }},
  // TODO: Añadir 4-6 prompts más
  // Categorías sugeridas: Análisis Estratégico, Benchmarking, Due Diligence,
  // Herramientas de Estudio, Visualización, Ética y Compliance
];

// ============================================
// BEST PRACTICES (Mejores Prácticas)
// ============================================

export const bestPractices: BestPractice[] = [
  // ✅ DOs
  {{
    title: "[PRÁCTICA RECOMENDADA]",
    description:
      "[EXPLICACIÓN DE POR QUÉ ES IMPORTANTE - 1-2 líneas]",
    type: "do",
  }},
  // TODO: Añadir 4-5 DOs más

  // ❌ DON'Ts
  {{
    title: "[PRÁCTICA A EVITAR]",
    description:
      "[EXPLICACIÓN DE POR QUÉ ES PROBLEMÁTICA - 1-2 líneas]",
    type: "dont",
  }},
  // TODO: Añadir 4-5 DON'Ts más
];

// ============================================
// VIDEO DATA (Para sección de video en la página)
// ============================================

export const videoData = {{
  title: "Grabación Completa de la Clase",
  description:
    "[DESCRIPCIÓN: Qué se cubre en el video - 1-2 líneas]",
  embedUrl: "", // TODO: Añadir URL de Google Drive preview
  duration: "2h",
  date: "{date_formatted}",
  available: false, // TODO: Cambiar a true cuando video esté disponible
  chapters: [
    {{ time: "00:00", title: "Introducción a {tema}" }},
    {{ time: "15:00", title: "[CAPÍTULO 2]" }},
    {{ time: "65:00", title: "[CAPÍTULO 3]" }},
    {{ time: "115:00", title: "Cierre y Reflexión" }},
  ],
}};

// ============================================
// ADDITIONAL RESOURCES
// ============================================

export const resources = [
  {{
    title: "README pedagógico completo",
    url: "https://github.com/uexternadojz/Inteligecia-artificial-para-negocios/tree/main/materias/inteligencia-artificial-para-negocios/clases/{fecha}-clase-{numero:02d}-{slugify(tema)}",
    type: "documentation",
  }},
  // TODO: Añadir 2-4 recursos más (herramientas, transcripts, slides, externos)
];
"""

    return template


def generate_page_template(numero: int, tema: str, slug: str) -> str:
    """Genera template de clase-XX-tema.astro"""

    template = f"""---
/**
 * Página: Clase {numero:02d} - {tema}
 * Generated: {datetime.now().strftime('%Y-%m-%d')}
 */

import BaseLayout from "../../../layouts/BaseLayout.astro";
import ClassHero from "../../../components/ClassHero.astro";
import BentoGrid from "../../../components/BentoGrid.astro";
import WorkflowStepper from "../../../components/WorkflowStepper.astro";
import ToolCard from "../../../components/ToolCard.astro";

// Data imports
import {{
  heroData,
  fundamentals,
  tools,
  workflow,
  useCases,
  promptExamples,
  bestPractices,
  videoData,
  resources,
}} from "../../../data/clase-{numero:02d}-data";
---

<BaseLayout title="Clase {numero:02d} · {tema}">
  <!-- Hero Section -->
  <ClassHero {{...heroData}} />

  <!-- Fundamentals (Bento Grid) -->
  <section class="section-orbital">
    <div class="container-orbital">
      <h2 class="section-title">Fundamentos</h2>
      <BentoGrid items={{fundamentals}} />
    </div>
  </section>

  <!-- Workflow (si aplica - descomentar si workflow está definido) -->
  <!--
  <section class="section-orbital bg-dark">
    <div class="container-orbital">
      <h2 class="section-title">Workflow</h2>
      <WorkflowStepper steps={{workflow}} />
    </div>
  </section>
  -->

  <!-- Tools Section -->
  <section class="section-orbital">
    <div class="container-orbital">
      <h2 class="section-title">Herramientas</h2>
      <div class="grid gap-6 sm:grid-cols-1 lg:grid-cols-2">
        {{tools.map((tool) => <ToolCard tool={{tool}} />)}}
      </div>
    </div>
  </section>

  <!-- Use Cases -->
  <section class="section-orbital bg-dark">
    <div class="container-orbital">
      <h2 class="section-title">Casos de Uso</h2>
      <div class="space-y-6">
        {{
          useCases.map((useCase, i) => (
            <div class="panel-orbital">
              <h3 class="text-2xl font-bold mb-4">
                Caso {{i + 1}}: {{useCase.title}}
              </h3>
              <div class="space-y-3">
                <div>
                  <span class="text-cyan-orbital font-semibold">Contexto:</span>
                  <p class="text-gray-300 mt-1">{{useCase.context}}</p>
                </div>
                <div>
                  <span class="text-red-orbital font-semibold">Herramienta:</span>
                  <p class="text-gray-300 mt-1">{{useCase.tool}}</p>
                </div>
                <div>
                  <span class="text-cyan-orbital font-semibold">Output:</span>
                  <p class="text-gray-300 mt-1">{{useCase.output}}</p>
                </div>
              </div>
            </div>
          ))
        }}
      </div>
    </div>
  </section>

  <!-- Prompt Library -->
  <section class="section-orbital">
    <div class="container-orbital">
      <h2 class="section-title">Biblioteca de Prompts</h2>
      <div class="space-y-6">
        {{
          promptExamples.map((prompt) => (
            <div class="panel-orbital">
              <div class="flex items-start justify-between mb-3">
                <div>
                  <h3 class="text-xl font-bold">{{prompt.label}}</h3>
                  <span class="text-sm text-cyan-orbital">{{prompt.category}}</span>
                </div>
                <button
                  onclick="navigator.clipboard.writeText(this.dataset.content)"
                  data-content={{prompt.content}}
                  class="btn-secondary"
                >
                  📋 Copiar prompt
                </button>
              </div>
              <pre class="bg-black/50 p-4 rounded-lg overflow-x-auto"><code>{{prompt.content}}</code></pre>
            </div>
          ))
        }}
      </div>
    </div>
  </section>

  <!-- Best Practices (2 columnas: DOs | DON'Ts) -->
  <section class="section-orbital bg-dark">
    <div class="container-orbital">
      <h2 class="section-title">Mejores Prácticas</h2>
      <div class="grid gap-6 md:grid-cols-2">
        <!-- DOs Column -->
        <div>
          <h3 class="text-2xl font-bold mb-4 text-cyan-orbital">✅ Hacer</h3>
          <div class="space-y-4">
            {{
              bestPractices
                .filter((bp) => bp.type === "do")
                .map((bp) => (
                  <div class="panel-orbital border-l-4 border-cyan-orbital">
                    <h4 class="font-semibold mb-2">{{bp.title}}</h4>
                    <p class="text-gray-300 text-sm">{{bp.description}}</p>
                  </div>
                ))
            }}
          </div>
        </div>

        <!-- DON'Ts Column -->
        <div>
          <h3 class="text-2xl font-bold mb-4 text-red-orbital">❌ No Hacer</h3>
          <div class="space-y-4">
            {{
              bestPractices
                .filter((bp) => bp.type === "dont")
                .map((bp) => (
                  <div class="panel-orbital border-l-4 border-red-orbital">
                    <h4 class="font-semibold mb-2">{{bp.title}}</h4>
                    <p class="text-gray-300 text-sm">{{bp.description}}</p>
                  </div>
                ))
            }}
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Video Section (si aplica) -->
  {{
    videoData.available && videoData.embedUrl && (
      <section class="section-orbital">
        <div class="container-orbital">
          <h2 class="section-title">Grabación de la Clase</h2>
          <div class="mx-auto max-w-4xl">
            <div class="panel-orbital">
              <h3 class="text-xl font-bold mb-2">{{videoData.title}}</h3>
              <p class="text-gray-300 mb-4">{{videoData.description}}</p>
              <div class="aspect-video mb-4">
                <iframe
                  src={{videoData.embedUrl}}
                  class="w-full h-full rounded-lg"
                  allow="autoplay; encrypted-media"
                  allowfullscreen
                />
              </div>
              <div class="space-y-2">
                <h4 class="font-semibold text-cyan-orbital">Capítulos:</h4>
                <ul class="space-y-1">
                  {{videoData.chapters.map((chapter) => (
                    <li class="text-sm text-gray-300">
                      <span class="text-red-orbital font-mono">{{chapter.time}}</span> - {{chapter.title}}
                    </li>
                  ))}}
                </ul>
              </div>
            </div>
          </div>
        </div>
      </section>
    )
  }}

  <!-- Resources -->
  <section class="section-orbital bg-dark">
    <div class="container-orbital">
      <h2 class="section-title">Recursos Adicionales</h2>
      <div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {{
          resources.map((resource) => (
            <a
              href={{resource.url}}
              target="_blank"
              rel="noopener noreferrer"
              class="panel-orbital hover:border-cyan-orbital transition-all"
            >
              <h4 class="font-semibold mb-2">{{resource.title}}</h4>
              <span class="text-sm text-gray-400">{{resource.type}}</span>
            </a>
          ))
        }}
      </div>
    </div>
  </section>

  <!-- CTA Final -->
  <section class="section-orbital">
    <div class="container-orbital text-center">
      <a href="/Inteligecia-artificial-para-negocios/" class="btn-primary">
        ← Volver a todas las clases
      </a>
    </div>
  </section>
</BaseLayout>
"""

    return template


def update_course_ts(numero: int, fecha: str, tema: str, slug: str, mood: str):
    """Actualiza course.ts con la nueva clase"""
    course_ts_path = DATA_DIR / "course.ts"

    if not course_ts_path.exists():
        print(f"❌ Error: {course_ts_path} no existe")
        return

    with open(course_ts_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Añadir imports (después de los imports existentes)
    import_section = f"""import vinyl{numero:02d} from "../../assets/vinyls/clase-{numero:02d}/vinilo.webp";
import halo{numero:02d} from "../../assets/halos/clase-{numero:02d}.webp";
import spine{numero:02d} from "../../assets/spines/clase-{numero:02d}.png";"""

    # Buscar última línea de imports (antes de interfaces)
    import_pattern = r"(import spine\d+ from.*?;)"
    match = re.findall(import_pattern, content)
    if match:
        last_import = match[-1]
        content = content.replace(last_import, f"{last_import}\n{import_section}")

    # 2. Añadir entry en classes[] (antes del cierre del array)
    date_formatted = format_date(fecha)
    new_class_entry = f"""  {{
    slug: "clase-{numero:02d}-{slug}",
    number: "{numero:02d}",
    title: "{tema}",
    mood: "{mood}",
    synopsis:
      "[COMPLETAR: 2-3 líneas describiendo la clase]",
    status: "published",
    date: "{date_formatted}",
    duration: "2h",
    modality: "Práctica 80/20",
    prerequisites: [],
    stack: [], // TODO: Añadir stack de herramientas
    outcomes: [], // TODO: Añadir outcomes esperados
    vinylImage: vinyl{numero:02d},
    haloImage: halo{numero:02d},
    spineImage: spine{numero:02d},
    detail: {{
      overview: "[COMPLETAR]",
      sections: [],
      prompts: [],
      cases: [],
    }},
  }},"""

    # Buscar el array classes[] y añadir antes del cierre
    classes_pattern = r"(export const classes = \[.*?)\];"
    if re.search(classes_pattern, content, re.DOTALL):
        content = re.sub(
            classes_pattern,
            f"\\1{new_class_entry}\n];",
            content,
            flags=re.DOTALL
        )

    # 3. Incrementar counter en hudMetrics (buscar "Clases activas")
    counter_pattern = r'({{ label: "Clases activas", value: ")(\d+)(")'
    current_count = int(re.search(counter_pattern, content).group(2))
    new_count = current_count + 1
    content = re.sub(counter_pattern, f'\\1{new_count:02d}\\3', content)

    # Guardar
    with open(course_ts_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ course.ts actualizado con Clase {numero:02d}")


# ============================================
# FUNCIÓN PRINCIPAL
# ============================================

def main():
    parser = argparse.ArgumentParser(
        description="Genera estructura y templates para nueva clase IA para Negocios",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplo:
    python nueva_clase_ia_negocios.py \\
        --numero 05 \\
        --fecha 2025-11-06 \\
        --tema "Agentes IA Autónomos" \\
        --mood "Autonomous agents orchestrating tasks" \\
        --stack "LangChain,CrewAI,AutoGPT" \\
        --metrics "3:Arquitecturas:red,10x:Rápido:cyan"
        """
    )

    parser.add_argument("--numero", type=int, required=True, help="Número de clase (ej: 05)")
    parser.add_argument("--fecha", type=str, required=True, help="Fecha en formato YYYY-MM-DD")
    parser.add_argument("--tema", type=str, required=True, help="Título de la clase")
    parser.add_argument("--mood", type=str, required=True, help="Descripción visual para prompts")
    parser.add_argument("--stack", type=str, default="", help="Herramientas separadas por coma")
    parser.add_argument("--metrics", type=str, default="", help="Métricas en formato 'valor:label:accent,...'")

    args = parser.parse_args()

    # Validaciones
    try:
        datetime.strptime(args.fecha, "%Y-%m-%d")
    except ValueError:
        print("❌ Error: fecha debe estar en formato YYYY-MM-DD")
        sys.exit(1)

    if args.numero < 1 or args.numero > 99:
        print("❌ Error: número debe estar entre 1 y 99")
        sys.exit(1)

    # Parse inputs
    stack_list = [s.strip() for s in args.stack.split(",") if s.strip()]
    metrics_list = parse_metrics(args.metrics)
    slug = slugify(args.tema)

    print("\n" + "=" * 60)
    print(f"🚀 Creando Clase {args.numero:02d}: {args.tema}")
    print("=" * 60 + "\n")

    # 1. Crear directorios
    print("📁 Creando estructura de directorios...")
    create_directories(args.numero)

    # 2. Generar placeholders
    print("\n🎨 Generando placeholders...")
    generate_placeholder_spine(args.numero)
    generate_placeholder_halo(args.numero)

    # 3. Generar data template
    print("\n📝 Generando template de data...")
    data_template = generate_data_template(
        args.numero, args.fecha, args.tema, args.mood, stack_list, metrics_list
    )
    data_file_path = DATA_DIR / f"clase-{args.numero:02d}-data.ts"
    with open(data_file_path, 'w', encoding='utf-8') as f:
        f.write(data_template)
    print(f"✅ Data template creado: {data_file_path.relative_to(REPO_ROOT)}")

    # 4. Generar page template
    print("\n📄 Generando template de página...")
    page_template = generate_page_template(args.numero, args.tema, slug)
    page_file_path = PAGES_DIR / f"clase-{args.numero:02d}-{slug}.astro"
    with open(page_file_path, 'w', encoding='utf-8') as f:
        f.write(page_template)
    print(f"✅ Página template creada: {page_file_path.relative_to(REPO_ROOT)}")

    # 5. Actualizar course.ts
    print("\n🔄 Actualizando course.ts...")
    update_course_ts(args.numero, args.fecha, args.tema, slug, args.mood)

    # Resumen final
    print("\n" + "=" * 60)
    print("✅ Estructura generada exitosamente!")
    print("=" * 60)
    print("\n📋 Próximos pasos:")
    print(f"1. Generar hero images (vinyl + halo) con Claude Code skill")
    print(f"2. Completar contenido en: {data_file_path.relative_to(REPO_ROOT)}")
    print(f"3. Ajustar página en: {page_file_path.relative_to(REPO_ROOT)}")
    print(f"4. Testing: cd site/ && npm run dev")
    print(f"5. Commit y push a GitHub")
    print("\n📖 Ver guía completa: materias/inteligencia-artificial-para-negocios/CREAR_NUEVA_CLASE.md")
    print()


if __name__ == "__main__":
    main()
