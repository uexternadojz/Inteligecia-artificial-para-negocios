/**
 * Data for Clase 04: NotebookLM en Acción - IA para Investigación y Aprendizaje
 * Source: README.md de Clase 04 + Transcript de clase
 */

// Hero images
import vinyl04 from "../../assets/vinyls/clase-04/vinilo.webp";
import halo04 from "../../assets/halos/clase-04.webp";

// Tool logos
import geminiLogo from "../../assets/logos/gemini.png";

// ============================================
// INTERFACES (Reutilizadas de Clase 02/03)
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
  category: "research" | "learning" | "analysis" | "synthesis";
  url: string;
  logo?: string;
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
  number: "04",
  title: "NotebookLM en Acción",
  subtitle: "IA para Investigación y Aprendizaje",
  description:
    "Investigación y aprendizaje con IA: dos casos prácticos usando NotebookLM para analizar modelos de negocio (Tesla) y generar materiales de estudio sobre IA en Retail.",
  date: "30 Oct 2025",
  duration: "2h",
  modality: "Práctica guiada por casos 80/20",
  vinylImage: vinyl04,
  haloImage: halo04,
  metrics: [
    { value: "2", label: "Casos prácticos", accent: "red" },
    { value: "50", label: "Fuentes máximo", accent: "cyan" },
    { value: "6", label: "Herramientas NotebookLM", accent: "red" },
  ] as Metric[],
  ctas: [
    {
      label: "Abrir NotebookLM",
      href: "https://notebooklm.google.com",
      icon: "external-link",
    },
    {
      label: "Ver README pedagógico",
      href: "https://github.com/uexternadojz/Inteligecia-artificial-para-negocios/tree/main/materias/inteligencia-artificial-para-negocios/clases/2025-10-30-clase-04-notebook-llm",
      icon: "github",
    },
  ] as CTA[],
};

// ============================================
// FUNDAMENTALS (Bento Grid)
// ============================================

export const fundamentals: BentoItem[] = [
  {
    badge: "Diferenciador Clave",
    title: "Pensar vs Aprender",
    description:
      "NotebookLM no reemplaza el pensamiento humano; lo amplifica. Diferencia crítica: usar IA para PENSAR (analizar, cuestionar) vs APRENDER (sintetizar, estructurar).",
    icon: "🧠",
  },
  {
    badge: "Investigación Estratégica",
    title: "Caso Tesla: ¿Automotriz o Tech?",
    description:
      "Análisis de modelo de negocio híbrido. Explora innovación disruptiva, integración vertical, ecosistemas de IA (Dojo, Autopilot) y diversificación (Tesla Energy, Robotaxi).",
    icon: "🔍",
  },
  {
    badge: "Construcción de Conocimiento",
    title: "Caso IA en Retail",
    description:
      "Genera materiales de estudio completos: podcasts educativos, guías estructuradas, FAQs, mapas mentales y cronologías. Explora personalización, inventarios inteligentes y automatización.",
    icon: "📖",
  },
  {
    badge: "Herramientas Inteligentes",
    title: "Suite Completa de Estudio",
    description:
      "Audio Overview (podcasts 8-20 min), Study Guide (guías estructuradas), FAQ Generator, Timeline (cronologías), Briefing Doc (resúmenes ejecutivos), Table of Contents (índices navegables).",
    icon: "🛠️",
  },
  {
    badge: "Ventaja Competitiva",
    title: "Solo trabaja con TUS fuentes",
    description:
      "NotebookLM se diferencia de ChatGPT porque NO alucina datos. Trabaja exclusivamente con las fuentes que cargues (PDFs, URLs, docs, videos). Límite: 50 fuentes por notebook.",
    icon: "🛡️",
  },
  {
    badge: "Casos de Éxito",
    title: "Aplicaciones Reales",
    description:
      "Business Model Canvas automatizado, análisis comparativo de empresas, evaluación de tendencias de industria, generación de materiales educativos personalizados.",
    icon: "📈",
  },
];

// ============================================
// TOOLS
// ============================================

export const tools: Tool[] = [
  {
    name: "NotebookLM",
    category: "research",
    url: "https://notebooklm.google.com",
    description:
      "Asistente de investigación con IA de Google (basado en Gemini 2.0). Crea notebooks inteligentes que analizan tus fuentes y generan podcasts, guías, FAQs, mapas mentales y cronologías automáticamente.",
    pricing: "Gratis (cuenta Google)",
    stack: ["Gemini 2.0", "Google AI", "Source Grounding"],
    idealFor: [
      "Investigación de modelos de negocio",
      "Análisis de fuentes múltiples (PDFs, URLs, videos)",
      "Generación de materiales de estudio",
      "Podcasts educativos automáticos",
      "Síntesis de información compleja",
    ],
    limitations: [
      "Límite de 50 fuentes por notebook",
      "Solo trabaja con fuentes cargadas (no búsqueda web)",
      "Podcasts en inglés primariamente (transcripción en español disponible)",
      "Requiere fuentes de calidad (OCR malo = resultados pobres)",
    ],
    promptExample: `Crea un Business Model Canvas completo para Tesla. Incluye:
1. Propuesta de valor (diferenciación clave)
2. Segmentos de clientes (targets principales)
3. Canales (cómo llega al cliente)
4. Relaciones con clientes (engagement)
5. Flujos de ingresos (desglose por línea de negocio)
6. Recursos clave (tecnológicos, humanos, financieros)
7. Actividades clave (desarrollo, producción, marketing)
8. Socios clave (proveedores, alianzas estratégicas)
9. Estructura de costos (principales drivers)`,
  },
  {
    name: "Gemini 2.0",
    category: "synthesis",
    url: "https://ai.google.dev/gemini-api",
    logo: geminiLogo.src,
    description:
      "Modelo multimodal de Google que potencia NotebookLM. Capacidad nativa de procesar texto, imágenes, audio y video en un solo modelo.",
    pricing: "API con tier gratuito generoso",
    stack: ["Multimodal", "Context caching", "Grounding con Google Search"],
    idealFor: [
      "Análisis multimodal (texto + imágenes + video)",
      "Contexto largo (1M+ tokens)",
      "Grounding con búsqueda en tiempo real",
      "Generación de código y razonamiento",
    ],
    limitations: [
      "No tan fuerte en razonamiento complejo vs GPT-4 o Claude",
      "Límites de API gratuita (requests por minuto)",
    ],
  },
];

// ============================================
// WORKFLOW STEPS
// ============================================

export const workflow: WorkflowStep[] = [
  {
    number: "01",
    title: "Cargar Fuentes de Calidad",
    description:
      "Subir entre 5-8 fuentes confiables (artículos, PDFs, reportes, videos). Evitar PDFs escaneados de baja calidad (OCR malo). Máximo 50 fuentes por notebook.",
    tips: [
      "Fuentes actualizadas (2024-2025) para datos relevantes",
      "Combinar tipos: artículos académicos + noticias + reportes de industria",
      "URLs de sitios autorizados (Forbes, McKinsey, HBR, Bloomberg)",
      "Videos de YouTube con transcripciones automáticas funcionan bien",
    ],
  },
  {
    number: "02",
    title: "Formular Prompts Estratégicos",
    description:
      "Hacer preguntas específicas con contexto. No genérico tipo 'resume todo'. Iterar y refinar basándote en las respuestas.",
    tips: [
      "Estructura: Contexto + Pregunta + Formato esperado",
      "Ejemplo: 'Genera un Business Model Canvas para Tesla incluyendo...'",
      "Usar prompts diferentes para explorar múltiples ángulos",
      "Combinar análisis + visualización (mapa mental, cronología)",
    ],
  },
  {
    number: "03",
    title: "Explorar Todas las Herramientas",
    description:
      "No usar solo una herramienta. Combinar podcast + guía + mapa mental + FAQ para aprendizaje completo.",
    tips: [
      "Audio Overview: Conversación de 8-20 min entre dos hosts IA",
      "Study Guide: Guía estructurada con secciones y subtemas",
      "FAQ Generator: Extrae preguntas frecuentes automáticamente",
      "Timeline: Cronología visual de eventos clave",
      "Briefing Doc: Resumen ejecutivo de 1-2 páginas",
    ],
  },
  {
    number: "04",
    title: "Verificar y Contrastar",
    description:
      "No confiar ciegamente. Verificar información crítica con fuentes originales. NotebookLM cita fuentes - revisar contexto.",
    tips: [
      "Revisar las citas que NotebookLM incluye en las respuestas",
      "Contrastar datos cuantitativos con fuentes originales",
      "Validar conclusiones con expertos o fuentes adicionales",
      "Usar notebooks temáticos separados (1 tema = 1 notebook)",
    ],
  },
];

// ============================================
// USE CASES
// ============================================

export const useCases: UseCase[] = [
  {
    title: "Tesla: ¿Empresa Automotriz o Tecnológica?",
    context:
      "Investigar modelo de negocio híbrido de Tesla. Analizar innovación disruptiva (vehículos eléctricos + software OTA), integración vertical (baterías hasta seguros), ecosistemas de IA (Dojo, Autopilot, FSD), diversificación (Tesla Energy, Robotaxi, Optimus).",
    tool: "NotebookLM + Fuentes: Artículos Forbes/Bloomberg, reportes financieros 10-K, análisis S&P/McKinsey",
    output:
      "Business Model Canvas completo, 5 preguntas críticas de inversionista, mapa mental de líneas de negocio, podcast de conclusiones, análisis argumentado: ¿automotriz o tech?",
  },
  {
    title: "IA en Retail: Generación de Materiales Educativos",
    context:
      "Comprender transformación del retail con IA: personalización predictiva (recomendaciones), optimización de inventarios (demand forecasting), automatización (chatbots, checkouts sin cajeros), integración físico-digital (tiendas inteligentes, AR). Casos: Amazon Go, Zara RFID, Walmart AI Labs, Shopify Magic.",
    tool: "NotebookLM + Fuentes: McKinsey/Gartner retail reports, casos Amazon/Zara/Walmart, white papers Google Cloud Retail/AWS Personalize",
    output:
      "Podcast educativo 8-10 min, guía de estudio completa (5 casos de uso + beneficios + desafíos), 10 FAQs + 10 flashcards, mapa mental por área funcional (logística, marketing, ventas, operaciones).",
  },
];

// ============================================
// PROMPT EXAMPLES
// ============================================

export const promptExamples: PromptExample[] = [
  {
    label: "Business Model Canvas",
    category: "Análisis Estratégico",
    content: `Crea un Business Model Canvas completo para [EMPRESA]. Incluye:
1. Propuesta de valor (diferenciación clave)
2. Segmentos de clientes (targets principales)
3. Canales (cómo llega al cliente)
4. Relaciones con clientes (engagement)
5. Flujos de ingresos (desglose por línea de negocio)
6. Recursos clave (tecnológicos, humanos, financieros)
7. Actividades clave (desarrollo, producción, marketing)
8. Socios clave (proveedores, alianzas estratégicas)
9. Estructura de costos (principales drivers)

Formato: Tabla con 9 bloques claramente definidos.`,
  },
  {
    label: "Análisis Comparativo de Empresas",
    category: "Benchmarking",
    content: `¿Qué diferencia a [EMPRESA A] de [EMPRESA B]?

Compara en estas dimensiones:
- Márgenes operativos y estructura de costos
- Modelo de distribución y venta
- Estrategia de innovación (R&D spend, patentes)
- Dependencia de software vs hardware
- Posicionamiento de marca y segmento de mercado
- Ecosistema de partners y alianzas

Genera tabla comparativa con datos cuantitativos cuando sea posible.`,
  },
  {
    label: "Preguntas de Inversionista Institucional",
    category: "Due Diligence",
    content: `Genera 5 preguntas críticas que un inversionista institucional debería hacerse antes de invertir $10M en [EMPRESA].

Incluye:
- Riesgos tecnológicos (dependencia de tech propietaria, obsolescencia)
- Riesgos regulatorios (compliance, cambios en normativas)
- Riesgos competitivos (nuevos entrantes, guerra de precios)
- Riesgos de ejecución (capacidad del management, supply chain)
- Riesgos financieros (flujo de caja, estructura de deuda)

Para cada pregunta, sugiere fuentes de información para validar.`,
  },
  {
    label: "Podcast Educativo",
    category: "Herramientas de Estudio",
    content: `Crea un podcast educativo de 10 minutos sobre [TEMA].

Características:
- Estilo: Conversación entre dos expertos (uno explica, otro pregunta)
- Audiencia: [PERFIL DE AUDIENCIA - ej: gerentes sin background técnico]
- Incluye ejemplos concretos de [EMPRESAS RELEVANTES]
- Estructura: Intro (contexto), 3 casos de uso principales, beneficios cuantificables, desafíos, tendencias futuras
- Tono: Profesional pero accesible, evitar jerga técnica excesiva

Duración objetivo: 8-12 minutos`,
  },
  {
    label: "Guía de Estudio Completa",
    category: "Herramientas de Estudio",
    content: `Genera una guía de estudio completa sobre [TEMA].

Estructura:
1. Introducción (contexto y relevancia)
2. 5 casos de uso principales (con ejemplos de empresas reales)
3. Beneficios cuantificables (ROI, eficiencia, revenue impact)
4. Desafíos de implementación (técnicos, organizacionales, presupuestarios)
5. Tendencias futuras (próximos 2-3 años)
6. Glosario de términos clave
7. Recursos adicionales (papers, casos de estudio, herramientas)

Formato: Markdown con secciones claramente delimitadas.`,
  },
  {
    label: "Mapa Mental por Área Funcional",
    category: "Visualización",
    content: `Elabora un mapa mental con los casos de uso de [TECNOLOGÍA] por área funcional:

Áreas a cubrir:
- Logística y supply chain (forecasting, routing, warehouse automation)
- Marketing y personalización (segmentación, targeting, content generation)
- Ventas y experiencia del cliente (chatbots, recomendaciones, self-service)
- Operaciones y eficiencia (process automation, quality control, predictive maintenance)

Para cada área:
- Tecnologías específicas (ej: computer vision, NLP, reinforcement learning)
- Herramientas comerciales disponibles (ej: Google Cloud AI, AWS SageMaker)
- Casos de éxito documentados (empresa + resultado cuantificable)

Formato: Estructura jerárquica con nodos principales y subnodos.`,
  },
  {
    label: "Ética y Regulación",
    category: "Riesgos y Compliance",
    content: `Resume los desafíos éticos y regulatorios asociados al uso de [TECNOLOGÍA] en [INDUSTRIA]:

Dimensiones a analizar:
- Privacidad de datos (GDPR, CCPA, protección de PII)
- Sesgo algorítmico (fairness, discriminación en decisiones automatizadas)
- Transparencia (explicabilidad de modelos, derecho a saber)
- Precios dinámicos (fairness, manipulación de consumidores vulnerables)
- Desplazamiento laboral (impacto social, reentrenamiento)
- Regulaciones emergentes (AI Act Europa, Executive Orders USA, normativas locales)

Para cada desafío:
- Descripción del riesgo
- Regulaciones aplicables (con referencias específicas)
- Mejores prácticas de la industria
- Casos de multas o sanciones documentadas`,
  },
];

// ============================================
// BEST PRACTICES
// ============================================

export const bestPractices: BestPractice[] = [
  {
    title: "Cargar fuentes de calidad y actualizadas (2024-2025)",
    description:
      "Fuentes recientes de sitios confiables (Forbes, McKinsey, HBR, Bloomberg). Evitar contenido desactualizado que puede llevar a conclusiones erróneas.",
    type: "do",
  },
  {
    title: "Formular prompts específicos con contexto",
    description:
      "Estructura clara: Contexto + Pregunta + Formato esperado. Ejemplo: 'Genera un Business Model Canvas para Tesla incluyendo...' vs 'resume todo'.",
    type: "do",
  },
  {
    title: "Iterar y refinar preguntas basadas en respuestas",
    description:
      "Primera respuesta es punto de partida. Profundizar con follow-ups: '¿Qué datos respaldan esto?', '¿Cómo se compara con X?'",
    type: "do",
  },
  {
    title: "Combinar múltiples herramientas (podcast + guía + mapa)",
    description:
      "No limitarse a una sola herramienta. Audio Overview para síntesis, Study Guide para estructura, FAQ para dudas comunes, Timeline para contexto histórico.",
    type: "do",
  },
  {
    title: "Verificar información crítica con fuentes originales",
    description:
      "NotebookLM cita fuentes - revisarlas. Contrastar datos cuantitativos (ingresos, márgenes, market share) con reportes financieros oficiales.",
    type: "do",
  },
  {
    title: "Usar notebooks temáticos separados (1 tema = 1 notebook)",
    description:
      "Mantener foco. Notebook para Tesla, otro para Retail AI, otro para análisis competitivo. Evita confusión entre contextos no relacionados.",
    type: "do",
  },
  {
    title: "Subir PDFs escaneados de baja calidad (OCR malo)",
    description:
      "OCR defectuoso = texto ilegible = respuestas inútiles. Preferir PDFs nativos digitales o re-escanear con OCR de calidad.",
    type: "dont",
  },
  {
    title: "Preguntas genéricas tipo 'resume todo'",
    description:
      "Resulta en resúmenes superficiales. Mejor: '¿Cuáles son los 3 drivers clave de ingresos de Tesla y cómo han evolucionado 2020-2024?'",
    type: "dont",
  },
  {
    title: "Aceptar la primera respuesta sin validar",
    description:
      "IA puede interpretar mal fuentes o hacer generalizaciones. Siempre contrastar con fuentes originales, especialmente para datos críticos de negocio.",
    type: "dont",
  },
  {
    title: "Usar solo una herramienta y no explorar el resto",
    description:
      "NotebookLM tiene 6+ herramientas. Solo usar Study Guide = perder Audio Overview (podcasts), FAQ, Timeline, Briefing Doc.",
    type: "dont",
  },
  {
    title: "Confiar ciegamente sin contrastar datos",
    description:
      "NotebookLM trabaja con tus fuentes pero puede malinterpretar. Para decisiones importantes, validar con expertos o fuentes adicionales.",
    type: "dont",
  },
  {
    title: "Mezclar temas no relacionados en un solo notebook",
    description:
      "Tesla + Retail AI + análisis competitivo en 1 notebook = confusión. IA mezcla contextos. Mejor: 1 notebook por tema específico.",
    type: "dont",
  },
];

// ============================================
// ADDITIONAL RESOURCES
// ============================================

export const resources = [
  {
    title: "NotebookLM (herramienta)",
    url: "https://notebooklm.google.com",
    type: "tool",
  },
  {
    title: "README pedagógico completo",
    url: "https://github.com/uexternadojz/Inteligecia-artificial-para-negocios/tree/main/materias/inteligencia-artificial-para-negocios/clases/2025-10-30-clase-04-notebook-llm",
    type: "documentation",
  },
  {
    title: "Transcripción completa de clase",
    url: "https://github.com/uexternadojz/Inteligecia-artificial-para-negocios/blob/main/materias/inteligencia-artificial-para-negocios/clases/2025-10-30-clase-04-notebook-llm/transcript%20(2)%20(1).docx",
    type: "transcript",
  },
  {
    title: "Plan de clase (PDF)",
    url: "https://github.com/uexternadojz/Inteligecia-artificial-para-negocios/blob/main/materias/inteligencia-artificial-para-negocios/clases/2025-10-30-clase-04-notebook-llm/Clase%20Notebooklm%20Negocios.pdf",
    type: "slides",
  },
  {
    title: "Gemini API Documentation",
    url: "https://ai.google.dev/gemini-api",
    type: "external",
  },
];

// ============================================
// VIDEO DATA (Para sección de video en la página)
// ============================================

export const videoData = {
  title: "Grabación Completa de la Clase",
  description:
    "Sesión práctica de 2 horas explorando NotebookLM con dos casos reales: análisis de Tesla y generación de materiales sobre IA en Retail.",
  embedUrl: "https://drive.google.com/file/d/1GBgwpPGxwnKfdRp7aR2Yhbr9AU6AB4qQ/preview",
  duration: "2h",
  date: "30 Oct 2025",
  available: true,
  chapters: [
    { time: "00:00", title: "Introducción a NotebookLM" },
    { time: "15:00", title: "Caso 1: Tesla - Investigación Estratégica" },
    { time: "65:00", title: "Caso 2: IA en Retail - Herramientas de Estudio" },
    { time: "115:00", title: "Cierre y Reflexión" },
  ],
};
