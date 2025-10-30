/**
 * Data for Clase 02: Vibe Coding - Desarrollo Asistido por IA
 * Source: GUIA_COMPLETA_VIBE_CODING.md
 */

// Hero images
import vinyl02 from "../../assets/vinyls/clase-02/vinilo.webp";
import halo02 from "../../assets/halos/clase-02.webp";

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

export interface TimelineEvent {
  era: string;
  period: string;
  title: string;
  description: string;
  keyEvents: string[];
  accent: "red" | "cyan";
}

export interface Tool {
  name: string;
  category: "no-code" | "low-code" | "ide" | "conversational";
  url: string;
  logo: string; // Path to logo image
  description: string;
  pricing: string;
  stack: string[];
  idealFor: string[];
  limitations: string[];
  promptExample?: string;
}

export interface ComparisonDimension {
  name: string;
  description: string;
  tools: {
    name: string;
    score: number;
    label?: string;
  }[];
}

export interface UseCase {
  label: string;
  icon: string;
  title: string;
  description: string;
  example: {
    company: string;
    problem: string;
    solution: string;
    tool: string;
    result: string;
  };
}

export interface PromptPattern {
  name: string;
  category: string;
  badExample: string;
  goodExample: string;
  explanation: string;
}

export interface GlossaryEntry {
  name: string;
  category: string;
  description: string;
  url: string;
  pricing: string;
  logo: string;
}

// ============================================
// HERO DATA
// ============================================

export const heroData = {
  classNumber: "02",
  title: "Vibe Coding",
  subtitle:
    "Desarrollo asistido por IA donde transmites tu visión mediante lenguaje natural y la inteligencia artificial genera código funcional en tiempo real. De la idea al prototipo en minutos.",
  date: "23 Oct 2025",
  duration: "2h",
  modality: "Presencial / Demo Lab",
  vinylImage: vinyl02,
  haloImage: halo02,
  metrics: [
    {
      value: "15+",
      label: "Herramientas",
      accent: "red" as const,
    },
    {
      value: "10x",
      label: "Más Rápido",
      accent: "cyan" as const,
    },
    {
      value: "55%",
      label: "↑ Productividad",
      accent: "red" as const,
    },
    {
      value: "MVP 90min",
      label: "Promedio Clase",
      accent: "cyan" as const,
    },
  ],
  stack: [
    "Lovable",
    "Replit Agent",
    "v0.dev",
    "Claude Artifacts",
    "Cursor",
    "ChatGPT Canvas",
    "Windsurf",
    "GitHub Copilot",
    "Bolt.new",
    "Supabase",
  ],
  ctas: [
    {
      label: "Ver Transcripción",
      href: "#transcripcion",
    },
    {
      label: "Descargar Recursos",
      href: "#recursos",
    },
    {
      label: "Ejercicio Final",
      href: "#ejercicio",
    },
  ],
};

// ============================================
// SECTION 1: FUNDAMENTOS
// ============================================

export const fundamentals: BentoItem[] = [
  {
    badge: "Definición",
    title: "¿Qué es Vibe Coding?",
    description:
      "Práctica emergente de desarrollo que utiliza IA generativa para crear código funcional a partir de instrucciones en lenguaje natural, permitiendo que personas sin conocimientos técnicos previos desarrollen aplicaciones completas.",
  },
  {
    badge: "Origen",
    title: "Acuñado por Andrew Ng",
    description:
      "Cofundador de OpenAI y ex-jefe de IA en Google Brain. Observó que el desarrollo estaba cambiando de 'escribir código' a 'dirigir la creación de código' mediante intención, emoción y contexto.",
  },
  {
    badge: "Filosofía",
    title: "Estado de Flujo Creativo",
    description:
      "El desarrollador visualiza la app completa, siente la UX, transmite su visión en lenguaje natural y itera colaborativamente con la IA como co-creador. Pensar en QUÉ construir, no CÓMO implementar.",
  },
  {
    badge: "Contexto",
    title: "41% del código en GitHub tiene IA",
    description:
      "En 2024, el 41% del código global en GitHub tiene trazas de IA. 25% de startups YC W2025 tienen código 95% generado por IA. 44% de developers profesionales usan herramientas IA diariamente.",
  },
  {
    badge: "Impacto",
    title: "55% ↑ Velocidad de Desarrollo",
    description:
      "Estudios de GitHub muestran 55% de aumento en velocidad, 40% de reducción en bugs, y 10x más rápido para prototipos vs desarrollo tradicional. Time-to-market de meses a días/horas.",
  },
  {
    badge: "Expansión",
    title: "Más Allá del Código",
    description:
      "El concepto 'Vibe' se expande: Vibe Designing (Figma AI), Vibe Writing (Claude), Vibe Music (Suno), Vibe Editing (Descript), Vibe Modeling 3D. Una nueva forma de co-crear con IA.",
  },
];

// ============================================
// SECTION 2: HISTORIA
// ============================================

export const timeline: TimelineEvent[] = [
  {
    era: "Era 1",
    period: "1950s-2000s",
    title: "Programación Manual",
    description: "Código escrito línea por línea en IDEs básicos",
    keyEvents: [
      "Vim, Emacs, Eclipse",
      "Foco en sintaxis y algoritmos",
      "Debugging manual intensivo",
    ],
    accent: "red",
  },
  {
    era: "Era 2",
    period: "2000s-2020",
    title: "Frameworks y Abstracción",
    description: "Frameworks abstraen complejidad técnica",
    keyEvents: [
      "Rails, Django, React",
      "Stack Overflow como 'IA' rudimentaria",
      "Copy-paste workflow común",
    ],
    accent: "cyan",
  },
  {
    era: "Era 3",
    period: "2020-2023",
    title: "AI-Assisted Coding",
    description: "Primeras herramientas con IA integrada",
    keyEvents: [
      "GitHub Copilot (Jun 2021)",
      "ChatGPT (Nov 2022)",
      "Replit Ghostwriter (2022)",
    ],
    accent: "red",
  },
  {
    era: "Era 4",
    period: "2023-Presente",
    title: "Vibe Coding",
    description: "Conversacional puro, sin código expuesto",
    keyEvents: [
      "Lovable, v0.dev (2023)",
      "Claude Artifacts (Mar 2024)",
      "ChatGPT Canvas, Cursor, Windsurf (2024)",
    ],
    accent: "cyan",
  },
];

// ============================================
// SECTION 3: HERRAMIENTAS
// ============================================

export const tools: Tool[] = [
  {
    name: "Lovable",
    category: "no-code",
    url: "https://lovable.dev",
    logo: `${import.meta.env.BASE_URL}assets/logos/lovable.png`,
    description:
      "Chat conversacional puro para generar apps fullstack completas (frontend + backend + DB) sin código expuesto. Preview en tiempo real y deploy automático.",
    pricing: "Free: 100 tokens/mes | Pro: $20/mes",
    stack: ["React", "TailwindCSS", "Node.js", "PostgreSQL"],
    idealFor: [
      "MVPs de validación (1-4h)",
      "Prototipos para pitch",
      "Landing pages interactivas",
      "Herramientas internas",
    ],
    limitations: [
      "Tokens limitados en plan gratuito",
      "Código no exportable fácilmente",
      "Vendor lock-in",
      "No ideal para apps complejas (>20 vistas)",
    ],
  },
  {
    name: "Replit Agent",
    category: "no-code",
    url: "https://replit.com/ai",
    logo: `${import.meta.env.BASE_URL}assets/logos/replit.png`,
    description:
      "IDE completo en la nube con Agent mode conversacional y Ghostwriter para autocompletado. Soporta 50+ lenguajes con deploy con un click.",
    pricing: "Free limitado | Hacker: $7/mes | Pro: $20/mes",
    stack: ["Python", "Node.js", "Go", "React", "Flask", "MongoDB"],
    idealFor: [
      "Apps fullstack con backend complejo",
      "APIs REST/GraphQL",
      "Bots Discord/Telegram",
      "Herramientas de scraping",
    ],
    limitations: [
      "Performance limitada en free",
      "Cold starts si inactivo >1h",
      "Límites RAM/CPU en free tier",
    ],
  },
  {
    name: "v0.dev",
    category: "low-code",
    url: "https://v0.dev",
    logo: `${import.meta.env.BASE_URL}assets/logos/v0.png`,
    description:
      "Genera componentes React individuales con Next.js + TailwindCSS + shadcn/ui. Código visible, editable y exportable desde el inicio.",
    pricing: "Free: 200 créditos/mes | Pro: $20/mes (Vercel)",
    stack: ["Next.js 14", "TailwindCSS", "shadcn/ui", "TypeScript"],
    idealFor: [
      "Componentes UI individuales",
      "Dashboards con gráficos",
      "Landing pages modernas",
      "Sections de marketing",
    ],
    limitations: [
      "No genera backend",
      "Requiere conocimiento de React",
      "Tokens limitados rápidamente",
    ],
  },
  {
    name: "Claude Artifacts",
    category: "conversational",
    url: "https://claude.ai",
    logo: `${import.meta.env.BASE_URL}assets/logos/claude.png`,
    description:
      "Genera HTML/React/SVG/Mermaid en 'artifacts' con preview inmediato. Edición iterativa conversacional y share vía URL pública.",
    pricing: "Free limitado | Pro: $20/mes",
    stack: ["HTML", "JavaScript", "React", "SVG", "Mermaid"],
    idealFor: [
      "Prototipos visuales rápidos",
      "Visualizaciones de datos",
      "Infografías interactivas",
      "Diagramas explicativos",
    ],
    limitations: [
      "No genera backend",
      "No persiste datos",
      "Limitado a single-page apps",
    ],
  },
  {
    name: "Cursor",
    category: "ide",
    url: "https://cursor.sh",
    logo: `${import.meta.env.BASE_URL}assets/logos/cursor.png`,
    description:
      "IDE completo (fork de VS Code) con Cmd+K para edición inline, chat contextual con codebase y Composer para arquitectura de código.",
    pricing: "$20/mes",
    stack: ["Cualquier lenguaje", "GPT-4", "Claude 3.5", "Gemini"],
    idealFor: [
      "Desarrollo profesional fullstack",
      "Refactoring código legacy",
      "Migración entre frameworks",
      "Generación de tests automáticos",
    ],
    limitations: [
      "Requiere expertise en programación",
      "Costo mensual significativo",
      "Curva de aprendizaje",
    ],
  },
  {
    name: "ChatGPT Canvas",
    category: "conversational",
    url: "https://chat.openai.com",
    logo: `${import.meta.env.BASE_URL}assets/logos/chatgpt.png`,
    description:
      "Edición colaborativa de código y documentos con preview lateral. Iteración conversacional para refinar código Python, JavaScript, HTML, CSS.",
    pricing: "Free limitado | Plus: $20/mes",
    stack: ["Python", "JavaScript", "HTML", "CSS", "Markdown"],
    idealFor: [
      "Scripts rápidos",
      "Edición colaborativa de código",
      "Documentación técnica",
      "Tutoriales interactivos",
    ],
    limitations: [
      "No genera apps completas",
      "No deploy integrado",
      "Contexto limitado vs Claude",
    ],
  },
  {
    name: "Windsurf",
    category: "ide",
    url: "https://codeium.com/windsurf",
    logo: `${import.meta.env.BASE_URL}assets/logos/windsurf.png`,
    description:
      "IDE AI-first con Flow mode para edición multi-archivo y Cascade para chat contextual. Alternative open-source a Cursor con modelos propios.",
    pricing: "Free (ilimitado) | Pro: $15/mes",
    stack: ["Cualquier lenguaje", "Modelos propios de Codeium"],
    idealFor: [
      "Desarrollo profesional",
      "Equipos pequeños",
      "Refactoring multi-archivo",
      "Alternative económica a Cursor",
    ],
    limitations: [
      "Más nuevo (menos maduro que Cursor)",
      "Comunidad más pequeña",
      "Menos integraciones",
    ],
  },
  {
    name: "GitHub Copilot",
    category: "ide",
    url: "https://github.com/features/copilot",
    logo: `${import.meta.env.BASE_URL}assets/logos/copilot.png`,
    description:
      "Autocompletado inteligente en VS Code, JetBrains, Neovim. Sugiere líneas completas o funciones basadas en contexto y comentarios.",
    pricing: "Free (estudiantes) | $10/mes | $19/mes (Business)",
    stack: ["Cualquier lenguaje en VS Code", "OpenAI Codex"],
    idealFor: [
      "Autocompletado inteligente",
      "Boilerplate rápido",
      "Developers en VS Code",
      "Integración con GitHub",
    ],
    limitations: [
      "No genera apps completas",
      "Funciona mejor con código existente",
      "Requiere suscripción",
    ],
  },
  {
    name: "Bolt.new",
    category: "low-code",
    url: "https://bolt.new",
    logo: `${import.meta.env.BASE_URL}assets/logos/bolt.png`,
    description:
      "Apps fullstack editables con preview en tiempo real. Código visible y modificable con deploy integrado a Netlify/Vercel.",
    pricing: "Free limitado | Pro: información no pública",
    stack: ["React", "Node.js", "TailwindCSS", "TypeScript"],
    idealFor: [
      "Apps fullstack editables",
      "Prototipado rápido con backend",
      "Aprendizaje de código generado",
    ],
    limitations: [
      "Relativamente nuevo",
      "Documentación limitada",
      "Comunidad pequeña",
    ],
  },
  {
    name: "Supabase",
    category: "low-code",
    url: "https://supabase.com",
    logo: `${import.meta.env.BASE_URL}assets/logos/supabase.png`,
    description:
      "Backend as a Service (BaaS) con PostgreSQL, autenticación, storage y APIs en tiempo real. Alternative open-source a Firebase.",
    pricing: "Free: 500MB DB | Pro: $25/mes",
    stack: ["PostgreSQL", "REST API", "GraphQL", "Realtime"],
    idealFor: [
      "Backend rápido para MVPs",
      "Autenticación lista",
      "Storage de archivos",
      "Realtime features",
    ],
    limitations: [
      "Curva de aprendizaje inicial",
      "Free tier limitado para producción",
      "Vendor lock-in parcial",
    ],
  },
];

// ============================================
// SECTION 4: COMPARACIÓN
// ============================================

export const comparisonDimensions: ComparisonDimension[] = [
  {
    name: "Facilidad de Uso",
    description: "Escala: 1 (difícil) → 10 (muy fácil)",
    tools: [
      { name: "Lovable", score: 10 },
      { name: "Claude Artifacts", score: 9 },
      { name: "ChatGPT Canvas", score: 9 },
      { name: "Replit Agent", score: 8 },
      { name: "v0.dev", score: 7 },
      { name: "Bolt.new", score: 7 },
      { name: "Windsurf", score: 6 },
      { name: "Cursor", score: 5 },
      { name: "GitHub Copilot", score: 4 },
    ],
  },
  {
    name: "Control sobre Código",
    description: "Escala: 1 (sin control) → 10 (total)",
    tools: [
      { name: "Cursor", score: 10 },
      { name: "GitHub Copilot", score: 10 },
      { name: "Windsurf", score: 9 },
      { name: "Replit Agent", score: 8 },
      { name: "Bolt.new", score: 7 },
      { name: "v0.dev", score: 7 },
      { name: "ChatGPT Canvas", score: 6 },
      { name: "Claude Artifacts", score: 5 },
      { name: "Lovable", score: 2 },
    ],
  },
  {
    name: "Velocidad de Prototipado",
    description: "Tiempo para MVP funcional",
    tools: [
      { name: "Lovable", score: 1, label: "0.5-2h" },
      { name: "Claude Artifacts", score: 1, label: "0.5-1h" },
      { name: "v0.dev", score: 2, label: "1-3h" },
      { name: "Replit Agent", score: 3, label: "2-4h" },
      { name: "ChatGPT Canvas", score: 2, label: "1-3h" },
      { name: "Bolt.new", score: 3, label: "2-5h" },
      { name: "Windsurf", score: 6, label: "4-8h" },
      { name: "Cursor", score: 9, label: "6-12h" },
      { name: "Código manual", score: 30, label: "20-40h" },
    ],
  },
];

// ============================================
// SECTION 5: METODOLOGÍA
// ============================================

export const methodology = {
  workflow: [
    {
      number: "01",
      title: "Visualizar Completo",
      description:
        "Cierra los ojos y visualiza la app terminada: colores, estructura, interacciones, flujo del usuario. Siente la experiencia.",
      tips: [
        "Usa referencias visuales (apps similares, mockups)",
        "Define 3-5 vistas principales primero",
        "Piensa en el usuario final, no en el código",
      ],
    },
    {
      number: "02",
      title: "Describir con Claridad",
      description:
        "Transmite tu visión en lenguaje natural: funcionalidades específicas, diseño detallado, datos de ejemplo, comportamientos esperados.",
      tips: [
        "Estructura: Funcionalidades → Diseño → Datos",
        "Usa ejemplos concretos, no abstracciones",
        "Incluye edge cases si son críticos",
      ],
    },
    {
      number: "03",
      title: "Iterar Rápido",
      description:
        "Revisa el resultado, identifica qué mejorar y refina con prompts específicos. La IA es tu co-creador, no un oráculo perfecto.",
      tips: [
        "Cambios incrementales (1-2 ajustes por iteración)",
        "Sé específico: 'el botón rojo del modal'",
        "Prueba en diferentes dispositivos",
      ],
    },
    {
      number: "04",
      title: "Validar Temprano",
      description:
        "Comparte con usuarios reales lo antes posible. El feedback es más valioso que el código perfecto.",
      tips: [
        "Deploy inmediato, aunque sea básico",
        "5-10 usuarios son suficientes para validar",
        "Prioriza feedback de comportamiento sobre opiniones",
      ],
    },
  ],
  principles: [
    {
      icon: "🎯",
      title: "Especificidad sobre Generalidad",
      description:
        "En lugar de 'una tabla bonita', di 'tabla con 5 columnas, bordes redondeados, hover azul claro, filtros superiores'.",
    },
    {
      icon: "📦",
      title: "Datos de Ejemplo Realistas",
      description:
        "Proporciona datos mock realistas. 'Crear 20 productos con nombres, precios, categorías y stock' genera mejor resultado que datos genéricos.",
    },
    {
      icon: "🎨",
      title: "Referencias Visuales Explícitas",
      description:
        "Menciona apps o componentes conocidos: 'Como Notion', 'Estilo Stripe', 'Similar a Linear'. La IA tiene contexto de diseños populares.",
    },
    {
      icon: "🔄",
      title: "Iteración Incremental",
      description:
        "Cambios pequeños y frecuentes superan a cambios grandes. Ajusta colores, luego espaciado, luego interacciones.",
    },
  ],
  antiPatterns: [
    {
      icon: "❌",
      title: "Prompts Vagos",
      bad: "Crea una app de tareas",
      good: "Crea app de tareas con tabla (5 columnas: nombre, prioridad, estado, asignado, fecha), filtros superiores, modal para nueva tarea, contador de completadas",
    },
    {
      icon: "❌",
      title: "Sin Datos de Ejemplo",
      bad: "Agrega una lista de productos",
      good: "Agrega 15 productos con: nombre (ej: iPhone 14), precio ($999), categoría (Electrónica), stock (0-50), imagen placeholder",
    },
    {
      icon: "❌",
      title: "Asumir Conocimiento Previo",
      bad: "Conecta con la API que te mostré antes",
      good: "Conecta con la API de OpenAI: endpoint https://api.openai.com/v1/chat/completions, header Authorization: Bearer $API_KEY, body con model y messages",
    },
    {
      icon: "❌",
      title: "Cambios Múltiples Simultáneos",
      bad: "Cambia colores, reorganiza layout y agrega autenticación",
      good: "[3 prompts separados] 1) Cambia primario a azul #3B82F6, 2) Layout: sidebar izquierdo fijo, 3) Agrega login con email/password",
    },
  ],
};

// ============================================
// SECTION 6: CASOS DE USO
// ============================================

export const useCases: Record<string, UseCase> = {
  healthcare: {
    label: "Healthcare",
    icon: "🏥",
    title: "Telemedicina y Gestión de Pacientes",
    description:
      "Portales de pacientes, scheduling de citas, historias clínicas digitales y dashboards médicos.",
    example: {
      company: "Clínica Regional (Ejemplo)",
      problem:
        "Gestión manual de citas médicas genera errores, doble-booking y frustración de pacientes. 40% de llamadas son para agendar/reagendar.",
      solution:
        "Portal de pacientes con Lovable: calendario interactivo, selección de especialista, confirmación automática, recordatorios SMS.",
      tool: "Lovable (MVP) + Supabase (Backend) + Twilio (SMS)",
      result:
        "Reducción 70% llamadas administrativas, 90% pacientes prefieren portal online, ROI 3 meses.",
    },
  },
  ecommerce: {
    label: "E-Commerce",
    icon: "🛒",
    title: "Tiendas Online y Marketplace",
    description:
      "Catálogos de productos, carritos de compra, checkout, dashboards de ventas y herramientas de inventario.",
    example: {
      company: "Boutique Local (Ejemplo)",
      problem:
        "Dependencia de marketplace (Mercado Libre) con comisiones 12%. Imposible construir marca propia. Sin datos de clientes.",
      solution:
        "Tienda online con v0.dev (frontend) + Stripe (pagos) + Supabase (productos/órdenes). Catálogo, carrito, checkout en 8 horas.",
      tool: "v0.dev (UI) + Stripe + Supabase",
      result:
        "Comisiones reducidas a 2.9%, base de datos de 500 clientes, email marketing propio, margen bruto +15%.",
    },
  },
  education: {
    label: "Educación",
    icon: "📚",
    title: "Plataformas de Aprendizaje",
    description:
      "LMS, quizzes interactivos, tracking de progreso, contenido adaptativo y herramientas de evaluación.",
    example: {
      company: "Universidad Externado (Real - Clase)",
      problem:
        "Materiales de clase dispersos (Drive, email, Moodle). Estudiantes pierden recursos. Sin tracking de progreso individual.",
      solution:
        "Portal de clase con Claude Artifacts: guías interactivas, ejercicios con feedback inmediato, progreso visual por estudiante.",
      tool: "Claude Artifacts (Prototipos) + Notion API (Contenido)",
      result:
        "Engagement +40%, tiempo de búsqueda de materiales -60%, satisfacción estudiantil 4.8/5.",
    },
  },
  finance: {
    label: "Finanzas",
    icon: "💰",
    title: "Fintech y Gestión Financiera",
    description:
      "Dashboards financieros, herramientas de presupuesto, tracking de gastos y reportes automatizados.",
    example: {
      company: "Kathleen - Tesorería (Real - Clase)",
      problem:
        "Gestión manual de flujos de caja en Excel. Errores frecuentes, reportes tardíos, sin visibilidad en tiempo real para CFO.",
      solution:
        "Dashboard de tesorería con Lovable: entrada/salida de efectivo, proyecciones automáticas, alertas de liquidez, exportar PDF.",
      tool: "Lovable (30 min en clase)",
      result:
        "Prototipo funcional en clase, validado con CFO, en desarrollo para producción. Estimado: ahorro 10h/semana.",
    },
  },
  hr: {
    label: "Recursos Humanos",
    icon: "👥",
    title: "HR Tech y Gestión de Talento",
    description:
      "Portales de empleados, onboarding digital, tracking de vacaciones, evaluaciones de desempeño.",
    example: {
      company: "Startup Tech (Ejemplo)",
      problem:
        "Onboarding manual de nuevos empleados: 20+ emails, documentos dispersos, 2 semanas hasta productividad plena.",
      solution:
        "Portal de onboarding con Replit Agent: checklist interactivo, firma digital de documentos, videos de bienvenida, asignación automática de accesos.",
      tool: "Replit Agent + DocuSign API + Slack API",
      result:
        "Onboarding reducido a 3 días, satisfacción nuevos empleados 9/10, HR ahorra 15h por contratación.",
    },
  },
};

// ============================================
// SECTION 7: PATRONES DE PROMPTING
// ============================================

export const promptPatterns: PromptPattern[] = [
  {
    name: "Patrón 1: Estructura Clara",
    category: "Organización",
    badExample: "Crea una app de gestión de inventario con productos y categorías",
    goodExample: `Crea una app de gestión de inventario.

FUNCIONALIDADES:
- Dashboard: cards con total productos, bajo stock, valor inventario
- Tabla productos: 6 columnas (SKU, nombre, categoría, stock, precio, acciones)
- Filtros: categoría (dropdown), búsqueda (input), orden (stock asc/desc)
- Modal nueva producto: formulario con validación
- Modal editar: pre-fill con datos existentes
- Botón eliminar con confirmación

DISEÑO:
- Paleta: verde #10B981 primario, gris neutro fondo
- Tipografía: Inter, limpia
- Iconos: Lucide
- Layout: header fijo, contenido centrado max-width 1200px

DATOS:
- 25 productos mock variados (electrónica, ropa, alimentos)
- 5 categorías con colores únicos`,
    explanation:
      "Estructura clara con secciones separadas (Funcionalidades, Diseño, Datos) permite a la IA entender prioridades y relaciones. Sin ambigüedad.",
  },
  {
    name: "Patrón 2: Datos Realistas",
    category: "Contenido",
    badExample: "Agrega una lista de empleados",
    goodExample: `Agrega tabla de empleados con 20 registros mock:

COLUMNAS:
- ID (auto-incremento)
- Nombre completo (variado: Juan Pérez, María García, etc.)
- Email (formato: nombre.apellido@company.com)
- Departamento (Engineering, Sales, HR, Marketing, Finance)
- Posición (Junior, Mid, Senior, Lead, Manager)
- Fecha ingreso (últimos 5 años, variado)
- Salario ($30k-$150k según posición)
- Estado (Activo: 90%, Inactivo: 10%)

DISTRIBUCIÓN:
- 40% Engineering, 25% Sales, 20% Marketing, 15% otros
- 60% Mid/Senior, 30% Junior, 10% Lead/Manager`,
    explanation:
      "Datos realistas con distribución lógica generan mejor UI y permiten probar filtros/ordenamiento con casos de uso reales.",
  },
  {
    name: "Patrón 3: Referencias Visuales",
    category: "Diseño",
    badExample: "Diseño moderno y minimalista",
    goodExample: `Diseño inspirado en Linear (linear.app):

CARACTERÍSTICAS:
- Paleta: gris casi negro (#0D1117), acentos violeta (#8B5CF6)
- Tipografía: Inter 400/500/600, line-height ajustado
- Espaciado: generoso, 24px entre secciones, 16px entre items
- Bordes: sutiles (1px), redondeados (8px cards, 6px buttons)
- Hover: transición 200ms, lift shadow sutil
- Iconos: outline style, 20px, stroke-width 1.5
- Animaciones: micro-interactions suaves, no invasivas`,
    explanation:
      "Referenciar apps conocidas (Linear, Notion, Stripe) da contexto visual inmediato. La IA ha visto miles de ejemplos de estos diseños.",
  },
  {
    name: "Patrón 4: Comportamientos Específicos",
    category: "Interacciones",
    badExample: "Agrega modal para crear nueva tarea",
    goodExample: `Modal para crear nueva tarea:

TRIGGER:
- Botón "Nueva Tarea" (primario, esquina superior derecha)
- Atajo teclado: Cmd+N / Ctrl+N

MODAL:
- Overlay oscuro backdrop-blur
- Card centrado, max-width 500px
- Header: "Nueva Tarea" + botón cerrar (X esquina)
- Form:
  * Título (input, autofocus, placeholder "Ej: Diseñar landing page")
  * Descripción (textarea, 3 líneas, opcional)
  * Prioridad (select: Baja/Media/Alta/Crítica, default Media)
  * Asignado (select con avatares, default usuario actual)
  * Fecha límite (date picker, default +7 días)
- Footer: "Cancelar" (secundario, ESC) + "Crear" (primario, Enter)

VALIDACIÓN:
- Título requerido (min 3 caracteres)
- Error en rojo bajo input
- Deshabilitar "Crear" si inválido

COMPORTAMIENTO:
- Crear: cerrar modal, agregar a tabla, toast confirmación "✓ Tarea creada"
- Cancelar: cerrar sin guardar, confirmar si hay cambios
- Click fuera: mismo que Cancelar`,
    explanation:
      "Especificar triggers, validaciones, estados y comportamientos edge-case evita iteraciones. La IA genera UX completa en un solo prompt.",
  },
  {
    name: "Patrón 5: Iteración Incremental",
    category: "Refinamiento",
    badExample:
      "Cambia los colores a azul, reorganiza el layout en grid, agrega autenticación y conecta con API",
    goodExample: `[Iteración 1]
Cambia color primario a azul #3B82F6 (botones, links, acentos). Mantén todo lo demás igual.

[Esperar resultado]

[Iteración 2]
Reorganiza sección de productos: de lista vertical a grid 3 columnas (desktop), 2 (tablet), 1 (mobile).

[Esperar resultado]

[Iteración 3]
Agrega modal de login: email + password, botón "Iniciar Sesión", link "¿Olvidaste contraseña?". Mock por ahora, sin backend real.

[Esperar resultado]

[Iteración 4]
Conecta login con API: POST a https://api.example.com/auth/login, body {email, password}, response {token, user}. Guardar token en localStorage, redirect a /dashboard.`,
    explanation:
      "Cambios incrementales (1-2 ajustes por prompt) permiten validar cada paso, identificar errores temprano y mantener control. Más lento pero más efectivo.",
  },
];

// ============================================
// SECTION 8: VIDEO DE CLASE
// ============================================

export const videoData = {
  title: "Grabación Completa de la Clase",
  description:
    "Sesión de 2 horas donde construimos MVPs en vivo con Lovable, Replit Agent y v0.dev. Incluye demostraciones prácticas, troubleshooting en tiempo real y casos de éxito de estudiantes.",
  duration: "2h 15min",
  date: "23 Oct 2025",
  thumbnail: `${import.meta.env.BASE_URL}assets/clase-02/video-thumbnail.jpg`,
  driveUrl: "https://drive.google.com/file/d/EXAMPLE_ID/view", // Replace with actual URL
  chapters: [
    { time: "00:00", title: "Introducción: ¿Qué es Vibe Coding?" },
    { time: "15:30", title: "Demo 1: Lovable - App de Tareas en 30 min" },
    { time: "45:00", title: "Demo 2: Replit Agent - Bot de Discord" },
    { time: "1:15:00", title: "Demo 3: v0.dev - Dashboard Financiero" },
    { time: "1:45:00", title: "Caso Real: Kathleen - App de Tesorería" },
    { time: "2:00:00", title: "Q&A y Mejores Prácticas" },
  ],
};

// ============================================
// SECTION 9: GLOSARIO
// ============================================

export const glossary: GlossaryEntry[] = [
  {
    name: "Bolt.new",
    category: "Low-Code",
    description:
      "Apps fullstack editables con preview en tiempo real. Código visible y modificable con deploy integrado.",
    url: "https://bolt.new",
    pricing: "Free limitado | Pro: TBD",
    logo: `${import.meta.env.BASE_URL}assets/logos/bolt.png`,
  },
  {
    name: "ChatGPT Canvas",
    category: "Conversational",
    description:
      "Edición colaborativa de código y documentos con preview lateral. Iteración conversacional para Python, JS, HTML, CSS.",
    url: "https://chat.openai.com",
    pricing: "Free limitado | Plus: $20/mes",
    logo: `${import.meta.env.BASE_URL}assets/logos/chatgpt.png`,
  },
  {
    name: "Claude Artifacts",
    category: "Conversational",
    description:
      "Genera HTML/React/SVG/Mermaid con preview inmediato. Share vía URL pública.",
    url: "https://claude.ai",
    pricing: "Free limitado | Pro: $20/mes",
    logo: `${import.meta.env.BASE_URL}assets/logos/claude.png`,
  },
  {
    name: "Codeium",
    category: "IDE",
    description:
      "Alternative open-source a GitHub Copilot. Autocompletado inteligente gratis e ilimitado.",
    url: "https://codeium.com",
    pricing: "Free (ilimitado) | Teams: $12/usuario/mes",
    logo: `${import.meta.env.BASE_URL}assets/logos/codeium.png`,
  },
  {
    name: "Cursor",
    category: "IDE",
    description:
      "IDE AI-first (fork de VS Code) con Cmd+K, chat contextual y Composer para arquitectura.",
    url: "https://cursor.sh",
    pricing: "$20/mes",
    logo: `${import.meta.env.BASE_URL}assets/logos/cursor.png`,
  },
  {
    name: "Firebase",
    category: "Backend",
    description:
      "Backend as a Service de Google: Firestore, Auth, Storage, Hosting, Functions.",
    url: "https://firebase.google.com",
    pricing: "Free tier generoso | Blaze: pay-as-you-go",
    logo: `${import.meta.env.BASE_URL}assets/logos/firebase.png`,
  },
  {
    name: "GitHub Copilot",
    category: "IDE",
    description:
      "Autocompletado inteligente en VS Code, JetBrains, Neovim. Powered by OpenAI Codex.",
    url: "https://github.com/features/copilot",
    pricing: "Free (estudiantes) | $10/mes | $19/mes (Business)",
    logo: `${import.meta.env.BASE_URL}assets/logos/copilot.png`,
  },
  {
    name: "Lovable",
    category: "No-Code",
    description:
      "Chat conversacional puro para apps fullstack. Preview en tiempo real y deploy automático.",
    url: "https://lovable.dev",
    pricing: "Free: 100 tokens/mes | Pro: $20/mes",
    logo: `${import.meta.env.BASE_URL}assets/logos/lovable.png`,
  },
  {
    name: "Replit Agent",
    category: "No-Code",
    description:
      "IDE en la nube con Agent mode conversacional. Soporta 50+ lenguajes con deploy 1-click.",
    url: "https://replit.com/ai",
    pricing: "Free limitado | Hacker: $7/mes | Pro: $20/mes",
    logo: `${import.meta.env.BASE_URL}assets/logos/replit.png`,
  },
  {
    name: "Supabase",
    category: "Backend",
    description:
      "Backend as a Service open-source: PostgreSQL, Auth, Storage, Realtime. Alternative a Firebase.",
    url: "https://supabase.com",
    pricing: "Free: 500MB DB | Pro: $25/mes",
    logo: `${import.meta.env.BASE_URL}assets/logos/supabase.png`,
  },
  {
    name: "v0.dev",
    category: "Low-Code",
    description:
      "Genera componentes React con Next.js + TailwindCSS + shadcn/ui. Código exportable.",
    url: "https://v0.dev",
    pricing: "Free: 200 créditos/mes | Pro: $20/mes",
    logo: `${import.meta.env.BASE_URL}assets/logos/v0.png`,
  },
  {
    name: "Vercel AI SDK",
    category: "Framework",
    description:
      "SDK para building AI apps con streaming, tool calling y multi-provider support.",
    url: "https://sdk.vercel.ai",
    pricing: "Open-source (free)",
    logo: `${import.meta.env.BASE_URL}assets/logos/vercel.png`,
  },
  {
    name: "Windsurf",
    category: "IDE",
    description:
      "IDE AI-first de Codeium con Flow mode y Cascade. Alternative open-source a Cursor.",
    url: "https://codeium.com/windsurf",
    pricing: "Free (ilimitado) | Pro: $15/mes",
    logo: `${import.meta.env.BASE_URL}assets/logos/windsurf.png`,
  },
];

// ============================================
// SECTION 10: EJERCICIO FINAL
// ============================================

export const finalChallenge = {
  title: "Ejercicio Individual: Construye tu Primer MVP",
  description:
    "Elige un problema real de tu trabajo o vida personal y construye un MVP funcional usando las herramientas de la clase. Tiempo límite: 90 minutos.",
  timeLimit: 90, // minutes
  requirements: [
    "Elegir UNA herramienta (Lovable, Replit, v0.dev o Claude Artifacts)",
    "Definir problema específico (no abstracto)",
    "Crear MVP funcional con mínimo 3 funcionalidades core",
    "Deploy y obtener URL pública para compartir",
    "Documentar: prompt inicial + 2-3 iteraciones clave",
  ],
  examples: [
    {
      profile: "No técnico",
      idea: "App de seguimiento de gastos mensuales",
      tool: "Lovable",
      features: [
        "Formulario agregar gasto (monto, categoría, fecha)",
        "Tabla de gastos con filtros por categoría",
        "Dashboard con total gastado y breakdown por categoría (gráfico)",
      ],
    },
    {
      profile: "HTML básico",
      idea: "Landing page para freelancer",
      tool: "v0.dev",
      features: [
        "Hero con foto, nombre, tagline, CTA contacto",
        "Sección servicios (3 cards)",
        "Portfolio con 6 proyectos (grid responsive)",
        "Formulario contacto con validación",
      ],
    },
    {
      profile: "Estudiante",
      idea: "Tracker de hábitos diarios",
      tool: "Claude Artifacts",
      features: [
        "Lista de hábitos (nombre, meta diaria, icono)",
        "Marcar como completado cada día (calendario visual)",
        "Racha actual y mejor racha por hábito",
      ],
    },
  ],
  evaluation: [
    {
      criteria: "Funcionalidad",
      weight: "40%",
      description: "¿El MVP resuelve el problema planteado? ¿Funciona sin errores?",
    },
    {
      criteria: "Claridad de Prompts",
      weight: "30%",
      description:
        "¿Los prompts son específicos y estructurados? ¿Siguen mejores prácticas?",
    },
    {
      criteria: "Diseño/UX",
      weight: "20%",
      description: "¿Es visualmente coherente? ¿Responsive? ¿Intuitivo de usar?",
    },
    {
      criteria: "Iteración",
      weight: "10%",
      description:
        "¿Documentaste al menos 2 iteraciones de mejora? ¿Aprendiste del proceso?",
    },
  ],
  submission: {
    format: "Link a app deployed + documento con prompts usados",
    deadline: "Fin de clase (23 Oct 2025, 10:00 PM)",
    deliverables: [
      "URL pública del MVP funcionando",
      "Screenshot de la app",
      "Documento (.md o .txt) con: a) Problema, b) Herramienta elegida, c) Prompt inicial, d) 2-3 iteraciones clave, e) Aprendizajes",
    ],
  },
};
