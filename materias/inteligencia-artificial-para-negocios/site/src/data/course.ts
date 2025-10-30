import vinyl01 from "../../assets/vinyls/clase-01/vinilo.webp";
import vinyl02 from "../../assets/vinyls/clase-02/vinilo.webp";
import vinyl03 from "../../assets/vinyls/clase-03/vinilo.webp";

import halo01 from "../../assets/halos/clase-01.webp";
import halo02 from "../../assets/halos/clase-02.webp";
import halo03 from "../../assets/halos/clase-03.webp";

import spine01 from "../../assets/spines/clase-01.png";
import spine02 from "../../assets/spines/clase-02.png";
import spine03 from "../../assets/spines/clase-03.png";

export type ClassStatus = "draft" | "upcoming" | "published";

export interface ClassResource {
  label: string;
  href: string;
  type: "readme" | "slides" | "datasets" | "tools" | "otros";
}

export interface ClassDetailSection {
  title: string;
  items: string[];
}

export interface ClassDetailPrompt {
  label: string;
  content: string;
}

export interface ClassDetailCase {
  title: string;
  context: string;
  tool: string;
  output: string;
}

export interface ClassDetail {
  overview?: string;
  sections?: ClassDetailSection[];
  prompts?: ClassDetailPrompt[];
  cases?: ClassDetailCase[];
}

export interface ClassEntry {
  slug: string;
  number: string;
  title: string;
  mood: string;
  synopsis: string;
  status: ClassStatus;
  date: string;
  duration: string;
  modality: string;
  stack: string[];
  metrics: string[];
  resources: ClassResource[];
  vinylImage: ImageMetadata;
  haloImage: ImageMetadata;
  spineImage: ImageMetadata;
  detail?: ClassDetail;
}

export const classes: ClassEntry[] = [
  {
    slug: "clase-01-analisis-datos-ia",
    number: "01",
    title: "Análisis de Datos con IA",
    mood: "Placeholder en negro, tablero de datos difuso",
    synopsis:
      "Contenido en construcción. Esta pista cubrirá frameworks de analítica, data storytelling y casos de inteligencia de negocios potenciados con IA.",
    status: "draft",
    date: "21 Oct 2025",
    duration: "2h",
    modality: "Presencial / Demo Lab",
    stack: [],
    metrics: ["Contenido en progreso"],
    resources: [],
    vinylImage: vinyl01,
    haloImage: halo01,
    spineImage: spine01,
  },
  {
    slug: "clase-02-vibe-coding",
    number: "02",
    title: "Vibe Coding: IA que Programa",
    mood: "DJ tech mezclando prompts, partículas rojo-cian",
    synopsis:
      "La sesión estelar. Entramos en flujo creativo para dirigir a la IA y levantar MVPs, herramientas internas y dashboards sin escribir código manual.",
    status: "published",
    date: "23 Oct 2025",
    duration: "2h",
    modality: "Práctica 80/20",
    stack: ["Lovable", "Replit Agent", "v0.dev", "Bolt.new", "Claude Artifacts", "Cursor"],
    metrics: [
      "41% del código global ya es generado por IA",
      "15+ plataformas exploradas en vivo",
      "Hands-on: MVP funcional en 90 minutos",
    ],
    resources: [
      {
        label: "Guía completa Clase 02",
        href: `${import.meta.env.BASE_URL}/clases/clase-02-vibe-coding`,
        type: "readme",
      },
      {
        label: "Playbook Vibe Coding (PDF)",
        href: "https://github.com/jzuluaga/education-research/blob/main/externado/docencia/materias/inteligencia-artificial-para-negocios/clases/2025-10-23-clase-02-ia-corporativa/GUIA_COMPLETA_VIBE_CODING.md",
        type: "otros",
      },
      {
        label: "Transcripción .vtt",
        href: `${import.meta.env.BASE_URL}/transcripts/clase-02.vtt`,
        type: "otros",
      },
    ],
    vinylImage: vinyl02,
    haloImage: halo02,
    spineImage: spine02,
    detail: {
      overview:
        "Exploramos la mentalidad de Vibe Coding, diferenciando no-code, low-code y asistentes developer para dirigir a la IA como directores creativos.",
      sections: [
        {
          title: "Perfiles que impacta",
          items: [
            "Usuarios no técnicos: founders, marketers y educadores que levantan MVPs sin código",
            "Perfiles semi-técnicos: designers y PMs que orquestan componentes con ligera edición",
            "Developers profesionales que aceleran pipelines con Cursor, Windsurf y Copilot",
          ],
        },
        {
          title: "Estructura de la sesión",
          items: [
            "20 min · Marco conceptual y datos de adopción",
            "30 min · Demo en vivo creando una app end-to-end",
            "60 min · Taller hands-on por equipos con feedback",
            "10 min · Showcase, retro y documentación de aprendizajes",
          ],
        },
        {
          title: "Aprendizajes clave",
          items: [
            "La barrera del software desaparece: la skill crítica es comunicar a la IA",
            "El rol del programador evoluciona a director creativo que diseña intención",
            "Vibe Coding democratiza la validación de ideas con ciclos 10x más rápidos",
          ],
        },
      ],
      cases: [
        {
          title: "Prototipado rápido",
          context: "Pitch de nuevo producto o servicio",
          tool: "Lovable · Bolt.new",
          output: "MVP navegable listo para demo en 1-4h",
        },
        {
          title: "Herramientas internas",
          context: "Automatizar procesos del equipo",
          tool: "Replit Agent · Claude Artifacts",
          output: "App personalizada operativa en 2-8h",
        },
        {
          title: "Dashboards personalizados",
          context: "Visualizar métricas del negocio",
          tool: "Bolt.new + Supabase",
          output: "Dashboard interactivo con datos reales en 4-12h",
        },
      ],
      prompts: [
        {
          label: "Prompt básico",
          content: `Crea una landing page para mi startup de delivery de comida saludable.
Debe incluir:
- Hero con CTA
- Sección de beneficios (3 cards)
- Galería de platos (6 imágenes)
- Formulario de contacto
- Footer con redes sociales

Estilo: minimalista, verdes y blancos, tipografía moderna.`,
        },
        {
          label: "Prompt intermedio",
          content: `Necesito un dashboard para visualizar métricas de ventas.
- Conectar a API REST (mock data por ahora)
- Gráficos: línea ventas mensuales, barras top productos, pie categorías
- Filtros: rango de fechas y región
- Tabla con paginación

Stack: React + Recharts. Estilo dark inspirado en Stripe Dashboard.`,
        },
        {
          label: "Prompt avanzado",
          content: `Construye una app fullstack de gestión de tareas con autenticación.
Backend: Node + Express, PostgreSQL (Supabase), JWT.
Frontend: Next.js 14, Tailwind, shadcn/ui, Zustand, React Hook Form + Zod.
Features: login/signup, CRUD de tareas, categorías/tags, filtros avanzados y dark mode toggle.`,
        },
      ],
    },
  },
  {
    slug: "clase-03-ia-generativa-visual",
    number: "03",
    title: "IA Generativa Visual",
    mood: "Galería holográfica con diapositivas IA, destellos rojo/cian",
    synopsis:
      "Workflow completo de presentaciones profesionales con IA: investigación profunda con Perplexity, estructuración con ChatGPT Canvas y diseño visual con Gamma.app. De idea a deck ejecutivo en 10 minutos.",
    status: "published",
    date: "28 Oct 2025",
    duration: "2h",
    modality: "Práctica guiada 80/20",
    stack: ["Perplexity.ai", "ChatGPT Canvas", "Gamma.app", "Canva Magic Studio", "Nano Banana", "Gemini"],
    metrics: [
      "10min de idea a deck profesional vs 3h manual",
      "200+ fuentes citadas automáticamente con Perplexity",
      "6 herramientas IA probadas en vivo",
      "Velocidad 20x más rápida que proceso tradicional",
    ],
    resources: [
      {
        label: "Página interactiva Clase 03",
        href: `${import.meta.env.BASE_URL}/clases/clase-03-ia-generativa-visual`,
        type: "readme",
      },
      {
        label: "README pedagógico",
        href: "https://github.com/jzuluaga/education-research/tree/main/externado/docencia/materias/inteligencia-artificial-para-negocios/clases/2025-10-28-clase-03-ia-generativa-visual",
        type: "readme",
      },
      {
        label: "Transcript completo",
        href: "https://github.com/jzuluaga/education-research/blob/main/materias/inteligencia-artificial-para-negocios/clases/2025-10-28-clase-03-ia-generativa-visual/transcripc%20clase3.docx",
        type: "otros",
      },
    ],
    vinylImage: vinyl03,
    haloImage: halo03,
    spineImage: spine03,
    detail: {
      overview:
        "Workflow profesional de 3 pasos demostrado en vivo: investigación profunda con Perplexity Deep Research (200+ fuentes citadas), estructuración de narrativa con ChatGPT Canvas y generación visual con Gamma.app. Caso de estudio: Tendencias Digitales 2025.",
      sections: [
        {
          title: "Workflow de 3 Pasos",
          items: [
            "Paso 1: Investigación con Perplexity Deep Research (3-5 min) - Verificación de fuentes automática",
            "Paso 2: Estructuración con ChatGPT Canvas (2-3 min) - Narrativa y storytelling coherente",
            "Paso 3: Diseño Visual con Gamma.app (3-5 min) - Generación automática de slides profesionales",
            "Resultado: Deck ejecutivo completo en 10 minutos vs 3 horas manual",
          ],
        },
        {
          title: "Herramientas Complementarias",
          items: [
            "Canva Magic Studio: Infografías y gráficos personalizados con IA",
            "Nano Banana: Imágenes custom para branding específico",
            "Gemini 2.0 Flash: Multimodalidad avanzada (voz, visión, tiempo real)",
            "Todas con planes gratuitos disponibles para comenzar",
          ],
        },
        {
          title: "Lecciones Críticas",
          items: [
            "⚠️ CRÍTICO: Perplexity cita fuentes reales, ChatGPT puede inventar datos",
            "Verificar siempre información sensible antes de presentar",
            "La IA acelera 20x pero el criterio humano es insustituible",
            "Regla 6×6: Máximo 6 líneas por slide, 6 palabras por línea",
          ],
        },
      ],
      cases: [
        {
          title: "Presentación Ejecutiva de Tendencias Digitales 2025",
          context: "Pitch de tendencias digitales 2025 para directivos C-level (caso real demostrado en clase)",
          tool: "Perplexity → ChatGPT Canvas → Gamma.app",
          output: "Deck profesional de 7 slides en 10 minutos vs 3 horas manual. Incluye datos verificados, narrativa coherente y diseño ejecutivo.",
        },
        {
          title: "Infografía de Proceso Corporativo",
          context: "Comunicación interna de nuevo flujo de trabajo para equipos no técnicos",
          tool: "ChatGPT Canvas + Canva Magic Studio",
          output: "Infografía vertical con 5 pasos, iconografía consistente y branding corporativo alineado.",
        },
        {
          title: "Hero Visual Personalizado",
          context: "Imagen destacada para landing page de producto fintech, colores de marca específicos",
          tool: "Nano Banana (Replicate + SDXL)",
          output: "Ilustración vectorial minimalista en azul y dorado, resolución 1024x1024px, lista para web.",
        },
      ],
      prompts: [
        {
          label: "Investigación profunda (Perplexity)",
          content: `Necesito investigación profunda sobre [TEMA ESPECÍFICO] con estas características:

1. Fuentes académicas y de industria verificadas
2. Datos estadísticos recientes (2024-2025)
3. Ejemplos concretos de empresas o casos de éxito
4. Tendencias emergentes y proyecciones futuras
5. Cita todas las fuentes con enlaces directos

Audiencia: [PERFIL DE AUDIENCIA]
Propósito: Crear presentación ejecutiva de 7 slides

⚠️ IMPORTANTE: Solo datos verificables con fuentes citadas, NO inventes información.`,
        },
        {
          label: "Estructuración (ChatGPT Canvas)",
          content: `Tengo esta investigación sobre [TEMA] [PEGAR OUTPUT DE PERPLEXITY].

Crea la estructura de una presentación de 7 slides para [AUDIENCIA] con este formato:

**Slide 1 - Título**
- Título impactante
- Subtítulo contextualizador

**Slides 2-6 - Contenido**
Para cada slide:
- Título descriptivo (máx 6 palabras)
- 3 bullets clave (máx 6 palabras cada uno)
- Datos/estadísticas con fuente
- Sugerencia de gráfico/visual

**Slide 7 - Llamado a la Acción**
- Resumen ejecutivo
- Próximos pasos concretos

Tono: [PROFESIONAL/INSPIRADOR/TÉCNICO]`,
        },
        {
          label: "Generación visual (Gamma.app)",
          content: `[PEGAR ESTRUCTURA DE CHATGPT]

Genera esta presentación con estas características de diseño:

- Paleta: [COLORES DE MARCA o Negro + acentos profesionales]
- Estilo: Ejecutivo minimalista
- Fuente: San-serif moderna
- Imágenes: Stock profesional relacionado con [TEMA]
- Gráficos: Sugeridos en estructura (barras, línea, pie según corresponda)

Exportar en formato PowerPoint para edición posterior.`,
        },
        {
          label: "Infografía (Canva Magic Studio)",
          content: `Crea una infografía vertical sobre [TEMA] con:

**Estructura:**
1. Encabezado impactante con estadística clave
2. 5 secciones con ícono + título + descripción (máx 15 palabras)
3. Llamado a la acción al final

**Diseño:**
- Colores: [HEX CODES DE MARCA]
- Estilo: [Minimalista/Corporativo/Creativo]
- Iconografía: [Plana/Línea/3D]
- Dimensiones: 1080x1920px (vertical para redes)`,
        },
        {
          label: "Imagen personalizada (Nano Banana)",
          content: `A [TIPO DE COMPOSICIÓN] featuring [SUJETO PRINCIPAL] with [ELEMENTOS SECUNDARIOS], [ESTILO VISUAL], [ILUMINACIÓN], using [PALETA DE COLORES], [DETALLES TÉCNICOS]

Ejemplo:
A minimalist flat illustration featuring a fintech startup logo with golden coins floating around it, modern tech aesthetic, soft lighting, using blue (#0066CC) and gold (#FFD700) color palette, vector style, clean lines, 1024x1024px`,
        },
      ],
    },
  },
];

export const highlights = [
  {
    title: "Metodología Orbital",
    description: "Laboratorios inmersivos, 80% práctica, retos corporativos reales y feedback en vivo.",
    badge: "Cinemática",
  },
  {
    title: "Stack Inteligente",
    description: "Lovable, Replit, v0.dev, Claude Artifacts y un toolkit curado para prototipar al ritmo del mercado.",
    badge: "Toolset",
  },
  {
    title: "Casos Orbital",
    description: "Strivio, Lighthouse, Jaguar. Narrativas que muestran impacto tangible con dashboards y métricas.",
    badge: "Impacto",
  },
] as const;

export const toolkit = [
  { label: "Lovable", href: "https://lovable.dev" },
  { label: "Replit Agent", href: "https://replit.com/ai" },
  { label: "v0.dev", href: "https://v0.dev" },
  { label: "Claude Artifacts", href: "https://claude.ai" },
  { label: "Cursor IDE", href: "https://cursor.sh" },
  { label: "Gemini Flash", href: "https://ai.google.dev/gemini-api" },
] as const;

export const faqs = [
  {
    question: "¿Necesito saber programar?",
    answer:
      "No. Arrancamos desde cero. La clave es aprender a orquestar prompts, interfaces y decisiones estratégicas para que la IA construya contigo.",
  },
  {
    question: "¿Cómo se entregan los recursos?",
    answer:
      "Cada clase libera README interactivo, transcript y repositorio de assets. Podrás revisarlos desde el micrositio o GitHub.",
  },
  {
    question: "¿Qué necesito llevar?",
    answer:
      "Laptop, cuenta en herramientas IA (puedes usar las versiones free) y mentalidad experimental. Nosotros proveemos datasets y guías.",
  },
] as const;

export const hudMetrics = [
  { label: "Clases activas", value: "03", accent: "red" },
  { label: "Horas en vivo", value: "06h", accent: "cyan" },
  { label: "% práctica", value: "80%", accent: "red" },
  { label: "Herramientas", value: "15+", accent: "cyan" },
] as const;
