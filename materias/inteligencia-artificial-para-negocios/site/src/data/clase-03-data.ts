/**
 * Data for Clase 03: IA Generativa para Presentaciones e Infografías
 * Source: README.md de Clase 03 + Transcript de clase
 */

// Hero images
import vinyl03 from "../../assets/vinyls/clase-03/vinilo.webp";
import halo03 from "../../assets/halos/clase-03.webp";

// ============================================
// INTERFACES (Reutilizadas de Clase 02)
// ============================================

export interface Metric {
  value: string;
  label: string;
  accent: "red" | "cyan";
}

export interface CTA {
  label: string;
  href: string;
  icon?: string;
}

export interface BentoItem {
  badge: string;
  title: string;
  description: string;
  icon?: string;
}

export interface Tool {
  name: string;
  category: "no-code" | "low-code" | "ide" | "conversational";
  url: string;
  logo: string;
  description: string;
  pricing: string;
  stack: string[];
  idealFor: string[];
  limitations: string[];
  promptExample?: string;
}

export interface WorkflowStep {
  number: string;
  title: string;
  description: string;
  tips: string[];
}

export interface UseCase {
  title: string;
  context: string;
  tool: string;
  output: string;
}

export interface PromptExample {
  label: string;
  category: string;
  content: string;
}

export interface BestPractice {
  title: string;
  description: string;
  type: "do" | "dont";
}

// ============================================
// HERO DATA
// ============================================

export const heroData = {
  classNumber: "03",
  title: "IA Generativa Visual",
  subtitle:
    "Workflow completo para crear presentaciones ejecutivas e infografías con IA: Perplexity (investigación verificable) → ChatGPT Canvas (estructuración) → Gamma.app (generación visual). De 3 horas manuales a 10 minutos con IA.",
  date: "28 Oct 2025",
  duration: "2h",
  modality: "Práctica guiada 80/20",
  vinylImage: vinyl03,
  haloImage: halo03,
  metrics: [
    {
      value: "10min",
      label: "De Idea a Deck",
      accent: "red" as const,
    },
    {
      value: "200+",
      label: "Fuentes Citadas",
      accent: "cyan" as const,
    },
    {
      value: "6",
      label: "Herramientas IA",
      accent: "red" as const,
    },
    {
      value: "20x",
      label: "Más Rápido",
      accent: "cyan" as const,
    },
  ],
  stack: [
    "Perplexity.ai",
    "ChatGPT Canvas",
    "Gamma.app",
    "Canva Magic Studio",
    "Nano Banana",
    "Gemini",
  ],
  ctas: [
    {
      label: "Ver Workflow",
      href: "#workflow",
    },
    {
      label: "Herramientas",
      href: "#herramientas",
    },
    {
      label: "Ejercicio",
      href: "#ejercicio",
    },
  ],
};

// ============================================
// SECTION 1: FUNDAMENTOS
// ============================================

export const fundamentals: BentoItem[] = [
  {
    badge: "Investigación",
    title: "Información Fiable con Perplexity",
    description:
      "Deep Research verifica 200+ fuentes en 3 minutos vs alucinaciones de ChatGPT. Cada dato citado con papers y artículos académicos. Output en PDF de 16 páginas listo para estructurar.",
  },
  {
    badge: "Estructuración",
    title: "ChatGPT Canvas como Co-Editor",
    description:
      "Organiza 16 páginas de investigación en esquema de 7 slides con contenido agrupado lógicamente. Canvas permite editar y mantener versiones. De contenido bruto a estructura lista para Gamma.",
  },
  {
    badge: "Generación",
    title: "Gamma.app: Visual Profesional en Minutos",
    description:
      "De texto estructurado a presentación ejecutiva: imágenes IA automáticas, gráficos, paleta coherente. Sin marca de agua molesta. Exporta a PDF/PowerPoint. Templates múltiples (Bubble Gum, Minimal, Corporate).",
  },
];

// ============================================
// SECTION 2: HERRAMIENTAS
// ============================================

export const tools: Tool[] = [
  {
    name: "Perplexity.ai",
    category: "conversational",
    url: "https://www.perplexity.ai",
    logo: "/assets/logos/perplexity.png",
    description:
      "Motor de investigación profunda con IA que cita 200+ fuentes automáticamente. Deep Research genera informes completos verificables en 3 minutos vs 10-15 min de ChatGPT.",
    pricing: "Free: 5 búsquedas/día | Pro: $20/mes (Deep Research ilimitado)",
    stack: ["GPT-4", "Claude 3", "Web scraping en tiempo real", "Academic papers"],
    idealFor: [
      "Investigación académica verificable",
      "Preparación de presentaciones con datos actualizados",
      "Due diligence corporativo",
      "Research de mercado con fuentes citadas",
    ],
    limitations: [
      "Límite de 5 búsquedas diarias en plan gratuito",
      "Deep Research solo disponible en Pro",
      "Velocidad variable según carga del servidor",
    ],
    promptExample:
      "Necesito investigación profunda sobre [TEMA]. Incluye mejores prácticas, tendencias más importantes, descripciones, ejemplos y todo lo que consideres para dominar el tema.",
  },
  {
    name: "ChatGPT Canvas",
    category: "conversational",
    url: "https://chat.openai.com",
    logo: "/assets/logos/chatgpt.png",
    description:
      "Modo de edición colaborativa para documentos y código. Ideal para iterar y estructurar contenido de presentaciones antes de diseñar. Mantiene versiones y permite edición directa.",
    pricing: "Free limitado | Plus: $20/mes (Canvas incluido)",
    stack: ["GPT-4o", "Markdown", "Collaborative editing", "Version control"],
    idealFor: [
      "Estructurar contenido de presentaciones",
      "Drafting de guiones y narrativas",
      "Edición colaborativa de documentos largos",
      "Preparación de prompts optimizados para Gamma",
    ],
    limitations: [
      "No genera visuales (solo texto)",
      "Límite de mensajes en versión gratuita",
      "Canvas solo disponible en Plus/Pro",
    ],
    promptExample:
      "Ayúdame a estructurar un esquema de diapositivas con esta información [PEGAR RESEARCH], donde me digas para cada diapositiva el contenido, referencias, detalles, etc. para un total de 7 diapositivas.",
  },
  {
    name: "Gamma.app",
    category: "conversational",
    url: "https://gamma.app",
    logo: "/assets/logos/gamma.png",
    description:
      "Convierte texto estructurado o documentos en presentaciones editables con narrativas sugeridas. Genera imágenes con IA automáticamente. Sin marca de agua molesta vs competidores.",
    pricing: "Free: 400 créditos | Pro: $10/mes (créditos ilimitados)",
    stack: ["IA generativa", "Templates múltiples", "Image AI", "Export PDF/PPT"],
    idealFor: [
      "Presentaciones ejecutivas con estructura lógica",
      "Decks de pitch para startups",
      "Reportes visuales con datos",
      "Propuestas comerciales profesionales",
    ],
    limitations: [
      "Personalización avanzada limitada en free",
      "Créditos de generación limitados (400 inicial)",
      "Templates predefinidos (no 100% custom desde cero)",
    ],
    promptExample:
      "[PEGAR ESQUEMA]\n\nConfig: Texto conciso, Audiencia: Profesionales, Tono: Profesional y persuasivo, Imágenes: Automático",
  },
  {
    name: "Canva Magic Studio",
    category: "low-code",
    url: "https://www.canva.com/magic/",
    logo: "/assets/logos/canva.png",
    description:
      "Suite visual con IA integrada: Magic Write (copywriting), Magic Media (imágenes IA), Magic Animate (animaciones). Para infografías y diseño con más control creativo que Gamma.",
    pricing: "Free: limitado | Pro: $12.99/mes | Teams: $14.99/usuario/mes",
    stack: ["Magic Write", "Magic Media", "Design AI", "Animation engine"],
    idealFor: [
      "Infografías verticales detalladas",
      "Posters y flyers de marketing",
      "Animaciones simples para slides",
      "Branding visual consistente",
    ],
    limitations: [
      "Exportación con marca de agua en free",
      "Límite de elementos premium",
      "Curva de aprendizaje mayor que Gamma",
    ],
    promptExample:
      "Genera una infografía vertical de 1 página con [CONTENIDO]. Estilo: minimalista, colores negro y rojo (#ED2024), íconos planos. Incluye call-to-action final.",
  },
  {
    name: "Nano Banana",
    category: "conversational",
    url: "https://nanobanana.ai",
    logo: "/assets/logos/nano-banana.png",
    description:
      "Generador de imágenes IA ultra-creativas con coherencia estilística superior. Ideal para fondos de diapositivas e ilustraciones conceptuales cuando las de Gamma no son suficientes.",
    pricing: "Credits-based: 100 gratis iniciales | ~$0.01 por imagen",
    stack: ["Stable Diffusion", "FLUX", "Custom fine-tuned models"],
    idealFor: [
      "Fondos de diapositivas personalizados",
      "Ilustraciones conceptuales únicas",
      "Hero images para presentaciones",
      "Assets visuales con estilo coherente a marca",
    ],
    limitations: [
      "Créditos limitados en free (100 iniciales)",
      "Queue system: velocidad variable según carga",
      "Requiere buenos prompts para mejores resultados",
    ],
    promptExample:
      "Ilustración vectorial futurista minimalista de [CONCEPTO], estilo geométrico, fondo negro (#000000) con acentos rojos (#ED2024) y cyan (#00BCD4), sin texto, composición horizontal 16:9.",
  },
  {
    name: "Gemini (Google)",
    category: "conversational",
    url: "https://gemini.google.com",
    logo: "/assets/logos/gemini.png",
    description:
      "IA integrada nativamente a Google Slides y Docs. Soporta co-creación y edición colaborativa en tiempo real. Ideal si ya trabajas en ecosistema Google Workspace.",
    pricing: "Free con cuenta Google | Workspace: incluido en plan corporativo",
    stack: ["Gemini Pro", "Google Workspace integration", "Colaboración real-time"],
    idealFor: [
      "Presentaciones colaborativas en equipo",
      "Integración directa con Google Slides existentes",
      "Resúmenes automáticos de documentos largos",
      "Workflows corporativos con Google Workspace",
    ],
    limitations: [
      "Atado al ecosistema Google (vendor lock-in)",
      "Menos visual y automatizado que Gamma",
      "Deep Research muy lento (10+ min vs 3 min Perplexity)",
    ],
    promptExample:
      "Analiza este documento y genera un esquema de 5 slides con los puntos más importantes. Audiencia: ejecutivos C-level.",
  },
];

// ============================================
// SECTION 3: WORKFLOW PASO A PASO
// ============================================

export const workflow: WorkflowStep[] = [
  {
    number: "1",
    title: "INVESTIGACIÓN PROFUNDA",
    description:
      "Usa Perplexity Deep Research para obtener información fiable con 200+ fuentes citadas. Output: PDF de 16 páginas con referencias completas.",
    tips: [
      "Define scope claro del tema (ej: 'Tendencias digitales 2025')",
      "Solicita ejemplos concretos y casos de uso específicos",
      "Exporta resultado en PDF para preservar referencias citadas",
      "Tiempo estimado: 3-5 minutos vs 10-15 min ChatGPT",
      "⚠️ IMPORTANTE: Perplexity cita fuentes, ChatGPT puede inventar datos",
    ],
  },
  {
    number: "2",
    title: "ESTRUCTURACIÓN DE CONTENIDO",
    description:
      "Organiza la investigación en esquema de diapositivas con ChatGPT Canvas. Output: Estructura de 7 slides con contenido agrupado lógicamente.",
    tips: [
      "Pega el research completo de Perplexity en ChatGPT",
      "Define número de slides objetivo (5-7 slides óptimo para presentaciones)",
      "Pide agrupación lógica de contenido por temas relacionados",
      "Usa Canvas para mantener versiones editables",
      "Solicita referencias por slide para verificar datos después",
    ],
  },
  {
    number: "3",
    title: "GENERACIÓN VISUAL",
    description:
      "Convierte el esquema estructurado en presentación profesional con Gamma.app. Output: Deck con imágenes IA, gráficos y paleta coherente.",
    tips: [
      "⚠️ NO pegues research bruto, usa esquema estructurado de Canvas",
      "Configura audiencia y tono ANTES de generar (afecta narrativa)",
      "Elige template que alinee con tu marca (ej: Bubble Gum, Minimal)",
      "Texto: Conciso (no mínimo ni detallado) → Regla 6×6",
      "Imágenes: Automático (mezcla IA + fotos libres de repositorios)",
    ],
  },
  {
    number: "4",
    title: "PERSONALIZACIÓN VISUAL",
    description:
      "Genera imágenes custom con Nano Banana o DALL·E si las de Gamma no convencen o necesitas alineación exacta a branding corporativo.",
    tips: [
      "Usa prompts con estilo específico (ej: 'vectorial minimalista', 'foto realista')",
      "Define colores exactos con hex codes (#ED2024, #00BCD4)",
      "Solicita composición horizontal 16:9 para slides (no cuadrado)",
      "Itera 2-3 veces si resultado no es satisfactorio",
      "Descarga en alta resolución (Gamma acepta imágenes externas)",
    ],
  },
  {
    number: "5",
    title: "REVISIÓN Y REFINAMIENTO",
    description:
      "Verifica datos contra fuentes, ajusta diseño y asegura coherencia visual y narrativa. IA genera base, humano perfecciona.",
    tips: [
      "Chequea cifras y estadísticas contra fuentes de Perplexity",
      "Aplica regla 6×6: Máximo 6 líneas por slide, 6 palabras por línea",
      "Revisa paleta de colores (3 colores máximo: primario + acento + neutro)",
      "Asegura legibilidad en proyección (fuente ≥18pt, contraste alto)",
      "Pide feedback a colega: ¿Se entiende sin tu narración?",
    ],
  },
  {
    number: "6",
    title: "EXPORTACIÓN",
    description:
      "Exporta a PDF o PowerPoint y genera link público para compartir. Gamma permite ambos formatos sin pérdida de calidad.",
    tips: [
      "Gamma: Botón 'Export' → PDF (presentar) o PowerPoint (editar)",
      "Genera link público si necesitas compartir online sin descargar",
      "Descarga también versión editable por si necesitas ajustes futuros",
      "Nomenclatura clara: [Tema]_[Fecha]_[Versión].pdf",
      "Guarda en Drive/Dropbox: presentaciones se reutilizan frecuentemente",
    ],
  },
];

// ============================================
// SECTION 4: CASOS DE USO REALES
// ============================================

export const useCases: UseCase[] = [
  {
    title: "Presentación Ejecutiva de Tendencias Digitales 2025",
    context:
      "Pitch de tendencias digitales 2025 para directivos C-level. Necesidad: información verificable, actualizada, con fuentes académicas. Timeline: 1 día de preparación.",
    tool: "Perplexity (investigación 200+ fuentes) → ChatGPT Canvas (estructura 7 slides) → Gamma.app (generación visual con template Bubble Gum)",
    output:
      "Deck profesional de 7 slides en 10 minutos vs 3 horas manual. Incluye: gráficos automáticos, imágenes IA alineadas a contenido, referencias citadas en notas de presentador, paleta corporativa coherente. Formato final: PDF presentable + PowerPoint editable.",
  },
  {
    title: "Infografía Educativa: 5 Pasos del Pensamiento Crítico",
    context:
      "Visual de 5 pasos del pensamiento crítico para estudiantes universitarios. Necesidad: diseño minimalista, iconografía clara, formato vertical para imprimir A4.",
    tool: "ChatGPT (estructura de contenido) → Canva Magic Studio (diseño con Magic Write + Magic Media)",
    output:
      "Infografía vertical con iconografía consistente, colores negro (#000000) y rojo (#ED2024), tipografía Inter legible, call-to-action final. Lista para imprimir en alta resolución (300dpi). Tiempo: 15 minutos vs 2 horas en Illustrator manual.",
  },
  {
    title: "Hero Image Alineada a Branding Corporativo",
    context:
      "Ilustración futurista minimalista para slide de portada de presentación corporativa. Necesidad: alineación exacta a paleta de marca (negro #000000, rojo #ED2024, cyan #00BCD4), estilo geométrico, sin texto.",
    tool: "Nano Banana con prompt optimizado: 'Ilustración vectorial futurista minimalista de presentaciones con IA, estilo geométrico, fondo negro con acentos rojos y cyan, sin texto, composición 16:9'",
    output:
      "Imagen vectorial 16:9 en alta resolución, coherente con identidad de marca, estilo geométrico limpio. 3 iteraciones de refinamiento (ajuste de colores, composición, densidad visual). Tiempo: 5 minutos + 2 iteraciones. Costo: ~$0.03 total.",
  },
];

// ============================================
// SECTION 5: PROMPTS OPTIMIZADOS
// ============================================

export const promptExamples: PromptExample[] = [
  {
    label: "Investigación Profunda",
    category: "Perplexity Deep Research",
    content: `Necesito investigación profunda sobre [TEMA ESPECÍFICO].

Incluye:
- Mejores prácticas actuales (2024-2025)
- Tendencias más importantes con datos cuantitativos
- Descripciones detalladas de conceptos clave
- Ejemplos concretos de casos de uso
- Todo lo que consideres relevante para dominar el tema

Enfoque: [Técnico / Ejecutivo / Educativo]
Audiencia objetivo: [Perfil específico]`,
  },
  {
    label: "Estructuración de Contenido",
    category: "ChatGPT Canvas",
    content: `Ayúdame a estructurar un esquema de diapositivas con esta información:

[PEGAR INVESTIGACIÓN COMPLETA DE PERPLEXITY]

Requerimientos:
- Total de slides: 7 (incluye intro y conclusión)
- Para cada diapositiva indica:
  * Título claro y conciso
  * Contenido clave (bullets, máx 6 líneas)
  * Referencias específicas del research
  * Sugerencia de visual (gráfico, imagen, diagrama)

Para algunas diapositivas tendremos que agrupar contenido relacionado.
Ayúdame a estructurar el contenido completo por cada diapositiva.`,
  },
  {
    label: "Generación de Presentación",
    category: "Gamma.app",
    content: `[PEGAR ESQUEMA ESTRUCTURADO DE CHATGPT]

Configuración de generación:
- Cantidad de texto: Conciso (no mínimo ni detallado)
- Audiencia: Profesionales y directivos
- Tono: Profesional, claro y persuasivo
- Idioma: Español (Latinoamérica)
- Imágenes: Automático (mezcla IA + fotos libres)
- Template: [Bubble Gum / Minimal / Corporate según marca]

IMPORTANTE: No incluir títulos técnicos como "Estructura de diapositivas" en contenido.`,
  },
  {
    label: "Infografía Educativa",
    category: "Canva Magic Studio",
    content: `Genera una infografía vertical de una página con los 5 pasos del [PROCESO/CONCEPTO].

Estilo visual:
- Minimalista, profesional
- Colores: negro (#000000) y rojo (#ED2024)
- Íconos: planos, estilo lineal
- Tipografía: Inter o similar (legible)

Estructura:
- Header: Título principal + tagline
- 5 secciones: número grande + ícono + título + descripción breve (2-3 líneas)
- Footer: Call-to-action + logo/contacto

Formato: Vertical A4 (210×297mm), alta resolución (300dpi) para imprimir.`,
  },
  {
    label: "Imagen IA Personalizada",
    category: "Nano Banana / DALL·E",
    content: `Crea una ilustración para slide de presentación corporativa:

Concepto: [DESCRIBIR IDEA CENTRAL, ej: "persona creando presentaciones con IA"]

Estilo:
- Vectorial futurista minimalista
- Estilo geométrico, formas limpias
- Sin texto ni tipografía

Colores (hex codes exactos):
- Fondo: negro #000000
- Acentos principales: rojo #ED2024 y cyan #00BCD4
- Detalles: gris claro #F5F5F5

Composición:
- Formato: horizontal 16:9 (1920×1080px mínimo)
- Protagonista: [ELEMENTO CENTRAL]
- Balance visual: [DESCRIPCIÓN DE LAYOUT]

Referencia de estilo: [Opcional: "Similar a ilustraciones de Stripe/Linear"]`,
  },
];

// ============================================
// SECTION 6: BUENAS PRÁCTICAS
// ============================================

export const bestPractices: BestPractice[] = [
  {
    title: "Verificar Datos con Fuentes",
    description:
      "Perplexity cita fuentes automáticamente, ChatGPT puede inventar. SIEMPRE verifica cifras y estadísticas contra research original.",
    type: "do",
  },
  {
    title: "Estructurar Antes de Generar",
    description:
      "NO pegues investigación bruta a Gamma. Usa ChatGPT Canvas primero para organizar contenido lógicamente en esquema de slides.",
    type: "do",
  },
  {
    title: "Usar Canvas para Versiones",
    description:
      "ChatGPT Canvas mantiene historial editable. Usa para iterar esquema antes de enviar a Gamma (evita desperdiciar créditos).",
    type: "do",
  },
  {
    title: "Regla 6×6 en Slides",
    description:
      "Máximo 6 líneas por slide, 6 palabras por línea. Gamma tiende a generar texto denso: especifica 'Conciso' en configuración.",
    type: "do",
  },
  {
    title: "Paleta de 3 Colores Máximo",
    description:
      "Primario + acento + neutro. Más colores = diseño caótico. Define hex codes en prompt si tienes branding corporativo.",
    type: "do",
  },
  {
    title: "Confiar Ciegamente en IA",
    description:
      "ChatGPT puede alucinar datos. Gemini Deep Research es muy lento. SIEMPRE usa Perplexity para investigación verificable.",
    type: "dont",
  },
  {
    title: "Pegar Research Bruto a Gamma",
    description:
      "Gamma con 16 páginas de texto genera slides sobrecargados. Estructura primero en ChatGPT Canvas → Gamma solo recibe esquema.",
    type: "dont",
  },
  {
    title: "No Definir Audiencia ni Tono",
    description:
      "Gamma sin contexto genera presentación genérica. Define audiencia (ejecutivos/técnicos/estudiantes) y tono (formal/casual) antes de generar.",
    type: "dont",
  },
  {
    title: "Ignorar Coherencia Visual",
    description:
      "Cambiar template mid-deck o usar imágenes de estilos distintos rompe narrativa visual. Mantén consistencia de inicio a fin.",
    type: "dont",
  },
  {
    title: "Omitir Notas de Presentador",
    description:
      "Gamma genera contenido conciso para slides. Agrega notas con detalles, referencias y guión de narración para ti (invisible para audiencia).",
    type: "dont",
  },
];

// ============================================
// SECTION 7: VIDEO DE CLASE
// ============================================

export const videoData = {
  title: "Grabación Completa de la Clase",
  description:
    "Demostración en vivo del workflow completo: Perplexity Deep Research (Tendencias Digitales 2025) → ChatGPT Canvas (estructura 7 slides) → Gamma.app (generación con template Bubble Gum). Incluye troubleshooting y buenas prácticas.",
  duration: "2h",
  date: "28 Oct 2025",
  thumbnail: "/assets/clase-03/video-thumbnail.jpg",
  driveUrl: "https://drive.google.com/file/d/1k-eIwhFWTwoX2L9Y4nSB7trj8jQr_Glc/preview",
  available: true,
  chapters: [
    { time: "00:00", title: "Introducción: Cambio de Paradigma en Presentaciones" },
    { time: "10:00", title: "Demo 1: Perplexity Deep Research (200+ fuentes)" },
    { time: "25:00", title: "Demo 2: ChatGPT Canvas - Estructuración" },
    { time: "45:00", title: "Demo 3: Gamma.app - Generación Visual" },
    { time: "1:10:00", title: "Personalización: Nano Banana + Imágenes Custom" },
    { time: "1:30:00", title: "Ejercicio Práctico Individual (20 min)" },
    { time: "1:50:00", title: "Q&A y Buenas Prácticas" },
  ],
};

// ============================================
// SECTION 8: EJERCICIO FINAL
// ============================================

export const finalChallenge = {
  title: "Ejercicio Individual: Genera tu Primera Presentación con IA",
  description:
    "Replica el workflow completo con un tema personal o profesional relevante para ti. Tiempo límite: 20 minutos.",
  timeLimit: 20, // minutes
  requirements: [
    "Usar workflow de 3 pasos: Perplexity → ChatGPT Canvas → Gamma.app",
    "Tema específico (no abstracto): negocio, académico o personal",
    "Presentación de 5-7 slides mínimo",
    "Al menos 1 imagen generada con IA (Gamma automático cuenta)",
    "Exportar en PDF o generar link público",
  ],
  deliverables: [
    "Link público de Gamma o PDF descargado",
    "Screenshot de presentación final",
    "Documento con: a) Prompt Perplexity usado, b) Esquema ChatGPT, c) Configuración Gamma",
  ],
  evaluation: [
    {
      criteria: "Claridad Visual y Narrativa",
      weight: "40%",
      description:
        "¿Jerarquía clara? ¿Orden lógico? ¿Storytelling coherente? ¿Regla 6×6 aplicada?",
    },
    {
      criteria: "Creatividad y Coherencia",
      weight: "30%",
      description:
        "¿Uso inteligente de IA para reforzar mensaje? ¿Consistencia estilística? ¿Paleta coherente?",
    },
    {
      criteria: "Buenas Prácticas IA",
      weight: "20%",
      description:
        "¿Workflow correcto? ¿Prompts estructurados? ¿Datos verificados? ¿Fuentes citadas?",
    },
    {
      criteria: "Presentación Final",
      weight: "10%",
      description: "¿Exportación correcta? ¿Formato profesional? ¿Listo para compartir?",
    },
  ],
};
