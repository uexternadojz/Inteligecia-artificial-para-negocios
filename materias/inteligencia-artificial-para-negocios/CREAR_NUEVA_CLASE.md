# Guía: Crear Nueva Clase en IA para Negocios

> **Sistema Habilitador v1.0** - Automatización híbrida para crear clases del micrositio Astro con coherencia de brand Orbital Lab.

---

## 📋 Prerequisites (5 min)

Antes de comenzar, asegúrate de tener:

- [ ] **Tema definido** en syllabus del curso
- [ ] **Objetivos pedagógicos claros** (3-5 objetivos de aprendizaje)
- [ ] **Material pedagógico preparado:**
  - README en `clases/YYYY-MM-DD-clase-XX-tema/`
  - Transcript de la clase (`.vtt` o `.docx`)
  - Plan de clase (PDF o slides)
- [ ] **Video grabado** y subido a Google Drive con permisos de visualización
- [ ] **Stack de herramientas curado** (3-6 herramientas principales del tema)

---

## 🎯 Paso 1: Planificación (20 min)

### 1.1 Definir Concepto Visual

**Mood:** [Descripción visual del tema en 1-2 oraciones]

**Ejemplo:**
- Clase 02 (Vibe Coding): *"Desarrolladores creando código con IA, múltiples pantallas holográficas"*
- Clase 03 (IA Generativa Visual): *"Presentaciones generándose con IA, infografías y data viz flotando"*
- Clase 04 (NotebookLM): *"Notebooks inteligentes flotando, cerebro conectado a fuentes"*

**Colores dominantes:** [Seleccionar uno]
- `red` - Rojo orbital (#ED2024) para acción, urgencia, herramientas
- `cyan` - Cyan data (#00D4FF) para datos, análisis, tech
- `balanced` - Mix balanceado de ambos

**Estilo visual:** [Seleccionar uno]
- `futuristic` - Sci-fi, holográfico, neon
- `corporate` - Profesional, limpio, minimalista
- `academic` - Formal, estructurado, diagramático
- `tech` - Código, terminales, interfaces

---

### 1.2 Curar Stack de Herramientas

Lista de 3-6 herramientas principales que se usarán en la clase:

- [ ] **Herramienta 1:** [Nombre] - [Breve descripción]
  - Logo disponible: ✅ / ❌ (verificar en `site/assets/logos/`)
- [ ] **Herramienta 2:** [Nombre]
- [ ] **Herramienta 3:** [Nombre]
- [ ] ...

**Verificar logos:**
```bash
ls site/assets/logos/ | grep -i [herramienta]
```

Si falta un logo:
1. Descargar PNG/SVG oficial del sitio de la herramienta
2. O usar Playwright para screenshot: `/browser captura logo de [herramienta]`
3. Optimizar y guardar en `site/assets/logos/[herramienta].png`

---

### 1.3 Definir Métricas Clave (4 métricas)

Las métricas deben:
- Ser **cuantificables** (números, tiempos, porcentajes)
- **Balancear** red/cyan para visual harmony (2 red + 2 cyan ideal)
- **Resumir** el impacto o alcance de la clase

**Template:**
```typescript
metrics: [
  { value: "[NÚMERO]", label: "[LABEL CORTO]", accent: "red" },
  { value: "[NÚMERO]", label: "[LABEL CORTO]", accent: "cyan" },
  { value: "[NÚMERO]", label: "[LABEL CORTO]", accent: "red" },
  { value: "[NÚMERO]", label: "[LABEL CORTO]", accent: "cyan" }
]
```

**Ejemplos por clase:**
- Clase 02: `"15+"` herramientas, `"10x"` más rápido, `"55%"` ↑ productividad, `"MVP 90min"`
- Clase 03: `"10min"` de idea a deck, `"200+"` fuentes citadas, `"6"` herramientas IA, `"20x"` más rápido
- Clase 04: `"2"` casos prácticos, `"50"` fuentes máximo, `"6"` herramientas NotebookLM, `"2h"` duración

---

### 1.4 Esbozar Casos de Uso (2-3)

Casos reales o hipotéticos que demuestren aplicación práctica:

**Caso 1:**
- **Título:** [Nombre descriptivo]
- **Contexto:** [Problema o necesidad del negocio]
- **Herramienta:** [Qué herramienta/IA se usa]
- **Output esperado:** [Resultado tangible]

**Caso 2:** ...

**Ejemplo (Clase 04):**
- Título: *"Tesla: ¿Empresa Automotriz o Tecnológica?"*
- Contexto: *Investigar modelo de negocio híbrido...*
- Herramienta: *NotebookLM + fuentes Forbes/Bloomberg*
- Output: *Business Model Canvas completo, 5 preguntas críticas*

---

## 🤖 Paso 2: Ejecutar Script Automatizado (2 min)

### 2.1 Comando

```bash
cd herramientas/scripts/
python nueva_clase_ia_negocios.py \
  --numero 05 \
  --fecha 2025-11-06 \
  --tema "Agentes IA Autónomos" \
  --mood "Autonomous agents orchestrating tasks, multiple AI brains connected" \
  --stack "LangChain,CrewAI,AutoGPT,LangGraph" \
  --metrics "3:Arquitecturas:red,10x:Más Rápido:cyan,85%:Automatizado:red,5:Herramientas:cyan"
```

### 2.2 Parámetros

| Parámetro | Descripción | Ejemplo |
|-----------|-------------|---------|
| `--numero` | Número de clase (entero) | `05` |
| `--fecha` | Fecha de la clase (YYYY-MM-DD) | `2025-11-06` |
| `--tema` | Título corto de la clase | `"Agentes IA Autónomos"` |
| `--mood` | Descripción visual para prompts (1-2 oraciones) | `"Autonomous agents..."` |
| `--stack` | Herramientas separadas por coma | `"LangChain,CrewAI"` |
| `--metrics` | Métricas en formato `valor:label:accent` separadas por coma | `"3:Arquitecturas:red,10x:Rápido:cyan"` |

### 2.3 Outputs Esperados

El script generará automáticamente:

✅ **Estructura de carpetas:**
```
site/assets/
├── vinyls/clase-05/
│   └── original/ (vacío, para guardar versiones)
├── halos/ (ya existe)
└── spines/ (ya existe)
```

✅ **Placeholders generados:**
- `site/assets/spines/clase-05.png` (lomo vertical con Pillow)
- `site/assets/halos/clase-05.png` (halo temporal con gradiente)

✅ **Template de data:**
- `site/src/data/clase-05-data.ts` con estructura completa y TODOs

✅ **Scaffold de página:**
- `site/src/pages/clases/clase-05-agentes-ia.astro` con imports y secciones base

✅ **Actualización de course.ts:**
- Imports de vinyl, halo, spine
- Nueva entrada en `classes[]`
- Counter incrementado en `hudMetrics`

### 2.4 Verificar

```bash
# Verificar estructura
ls -la site/assets/vinyls/clase-05/
ls site/assets/spines/clase-05.png
ls site/assets/halos/clase-05.png

# Verificar templates
cat site/src/data/clase-05-data.ts | head -20
cat site/src/pages/clases/clase-05-agentes-ia.astro | head -15

# Verificar course.ts actualizado
grep "clase-05" site/src/data/course.ts
```

---

## 🎨 Paso 3: Generar Assets Visuales (15 min)

### 3.1 Generar Vinyl Hero (Imagen Principal)

**Usar Claude Code con Skill: `image-generation-expert`**

**Prompt recomendado:**
```
Genera vinyl hero para clase "[TEMA]" con mood:
"[COPIAR MOOD DEL PASO 1.1]"

Requerimientos técnicos:
- Estilo: minimalista futurista, 1024x1024px, clean geometric style
- Background: negro (#000000) o very dark (#0b0b0f)
- Acentos: rojo orbital (#ED2024) y cyan data (#00D4FF)
- High contrast, professional quality

Concepto visual específico:
[EXPANDIR BASADO EN MOOD - ejemplos:]
- Agentes IA: múltiples cerebros/nodes conectados, orquestación de tareas
- Análisis de Datos: dashboards holográficos, data viz flotando
- Computer Vision: cámaras + neural networks, detección de objetos
```

**Modelo recomendado:** Flux Dev ($0.0035/img, 6-8s, balance calidad/costo)

**Output esperado:**
- Archivo guardado en: `site/assets/vinyls/clase-05/vinilo.png`

---

### 3.2 Generar Halo Background (Fondo Difuso)

**Prompt recomendado:**
```
Genera halo blur background complementario para tema "[TEMA]":

Características:
- Gradientes suaves de cyan (#00D4FF) y red (#ED2024)
- Base negra (#000000), very blurred atmospheric
- Orbital halos effect, soft glow
- 1920x1080px
- Debe complementar vinyl sin competir visualmente
```

**Modelo recomendado:** Flux Dev (mismo modelo para coherencia)

**Output esperado:**
- Archivo guardado en: `site/assets/halos/clase-05.png`

---

### 3.3 Optimizar Imágenes (PNG → WebP)

```bash
cd site/assets/

# Optimizar vinyl
cd vinyls/clase-05/
cwebp -q 85 vinilo.png -o vinilo.webp
ls -lh vinilo.*  # Verificar tamaño (debe reducir ~40-60%)

# Optimizar halo
cd ../../halos/
cwebp -q 80 clase-05.png -o clase-05.webp
ls -lh clase-05.*

# Opcional: eliminar PNGs originales si WebP es correcto
# rm vinilo.png clase-05.png
```

---

### 3.4 Seleccionar Icono Principal

Emoji relevante para la clase (usado en hero y metadata):

**Opciones por tema:**
- Agentes IA: 🤖 (robot), 🧠 (cerebro), 🔗 (cadena/orquestación)
- Computer Vision: 👁️ (ojo), 📸 (cámara), 🎯 (detección)
- NLP: 💬 (chat), 📝 (texto), 🗣️ (speech)
- Data Science: 📊 (gráficos), 🔬 (análisis), 📈 (tendencias)
- MLOps: ⚙️ (engranajes), 🚀 (deploy), 🔄 (pipeline)

**Actualizar en template:**
```typescript
// site/src/data/clase-05-data.ts
export const heroData = {
  // ...
  icon: "🤖", // <- Seleccionar emoji
}
```

---

## ✍️ Paso 4: Completar Contenido (60-90 min)

Editar: `site/src/data/clase-05-data.ts`

### 4.1 Hero Data

```typescript
export const heroData = {
  number: "05", // ✅ Auto-generado
  title: "Agentes IA Autónomos", // ✅ Auto-generado
  subtitle: "[COMPLETAR: 1-2 líneas descriptivas del tema]",
  description: "[COMPLETAR: Párrafo extendido de 3-4 líneas]",
  date: "06 Nov 2025", // ✅ Auto-generado
  duration: "2h", // [AJUSTAR si es diferente]
  modality: "Práctica guiada 80/20", // [AJUSTAR si es diferente]
  vinylImage: vinyl05, // ✅ Auto-generado
  haloImage: halo05, // ✅ Auto-generado
  metrics: [ // ✅ Auto-generado (validar y ajustar)
    { value: "3", label: "Arquitecturas", accent: "red" },
    { value: "10x", label: "Más Rápido", accent: "cyan" },
    { value: "85%", label: "Automatizado", accent: "red" },
    { value: "5", label: "Herramientas", accent: "cyan" }
  ] as Metric[],
  ctas: [ // [COMPLETAR CTAs relevantes]
    { label: "Ver Workflow", href: "#workflow", icon: "arrow-right" },
    { label: "Herramientas", href: "#tools", icon: "tool" },
    { label: "GitHub README", href: "https://github.com/...", icon: "github" }
  ] as CTA[],
};
```

**Tips:**
- **Subtitle:** Debe enganchar en 1-2 líneas (no más de 120 caracteres)
- **Description:** Expandir tema con keywords relevantes para SEO
- **Metrics:** Verificar que valores sean impactantes y balanceados (2 red + 2 cyan)
- **CTAs:** Máximo 3, priorizar acciones internas (#sections) antes que externas

---

### 4.2 Fundamentals (Bento Grid)

Crear **4-6 items** que capturen conceptos clave del tema:

```typescript
export const fundamentals: BentoItem[] = [
  {
    badge: "[CATEGORÍA]", // Ej: "Concepto Clave", "Diferenciador", "Arquitectura"
    title: "[TÍTULO CORTO]", // Máx 4-5 palabras
    description: "[DESCRIPCIÓN DETALLADA]", // 2-3 líneas, específica y práctica
    icon: "🤖" // Emoji relevante
  },
  // ... 3-5 items más
];
```

**Guías:**
- **Variar longitud** de descriptions para ritmo visual (alternar cortas/largas)
- **Iconos emoji** deben ser distintos y representativos
- **Badges** deben categorizar claramente (evitar repetir)
- **Titles** deben ser concisos pero descriptivos

**Ejemplo (Clase 04 - NotebookLM):**
```typescript
{
  badge: "Diferenciador Clave",
  title: "Pensar vs Aprender",
  description: "NotebookLM no reemplaza el pensamiento humano; lo amplifica...",
  icon: "🧠"
},
{
  badge: "Investigación Estratégica",
  title: "Caso Tesla: ¿Automotriz o Tech?",
  description: "Análisis de modelo de negocio híbrido...",
  icon: "🔍"
}
```

---

### 4.3 Workflow (Opcional - si aplica)

Si la clase tiene un **proceso paso a paso** claro, crear 4-6 pasos:

```typescript
export const workflow: WorkflowStep[] = [
  {
    number: "01",
    title: "[TÍTULO DEL PASO]",
    description: "[DESCRIPCIÓN DEL PASO - 2-3 líneas]",
    tips: [
      "Tip práctico 1",
      "Tip práctico 2",
      "Tip práctico 3"
    ]
  },
  // ... pasos 02, 03, 04, etc.
];
```

**Cuándo NO usar workflow:**
- Clases conceptuales sin proceso lineal
- Clases de herramientas múltiples sin orden específico

**Ejemplo (Clase 04 - NotebookLM):**
```typescript
{
  number: "01",
  title: "Cargar Fuentes de Calidad",
  description: "Subir entre 5-8 fuentes confiables (artículos, PDFs, reportes, videos)...",
  tips: [
    "Fuentes actualizadas (2024-2025) para datos relevantes",
    "Combinar tipos: artículos académicos + noticias + reportes",
    "URLs de sitios autorizados (Forbes, McKinsey, HBR)",
    "Videos de YouTube con transcripciones funcionan bien"
  ]
}
```

---

### 4.4 Tools (Herramientas)

Documentar **2-4 herramientas principales** del stack:

```typescript
export const tools: Tool[] = [
  {
    name: "[NOMBRE HERRAMIENTA]",
    category: "research" | "learning" | "analysis" | "synthesis" | "development" | "design",
    url: "https://...",
    logo: "[nombre].png" | undefined, // Si existe en assets/logos/
    description: "[DESCRIPCIÓN TÉCNICA - 2-3 líneas con contexto]",
    pricing: "Gratis" | "Freemium" | "$XX/mes" | "API con tier gratuito",
    stack: ["Tecnología 1", "Tecnología 2", "Tecnología 3"], // Base técnica
    idealFor: [
      "Caso de uso 1",
      "Caso de uso 2",
      "Caso de uso 3"
    ],
    limitations: [
      "Limitación 1",
      "Limitación 2"
    ],
    promptExample: `[PROMPT EJEMPLO CONCRETO Y ÚTIL]`
  },
  // ... 1-3 herramientas más
];
```

**Tips:**
- **Category:** Categorizar correctamente para filtros futuros
- **Description:** Debe explicar qué hace y por qué es relevante
- **Pricing:** Ser específico con tiers gratuitos/pagos
- **Stack:** Tecnologías subyacentes (para contexto técnico)
- **idealFor:** Casos de uso concretos y medibles
- **Limitations:** Ser honesto con restricciones (builds trust)
- **promptExample:** Debe ser copy-pasteable y útil

---

### 4.5 Use Cases (Casos de Uso)

Crear **2-3 casos reales o hipotéticos** que demuestren aplicación:

```typescript
export const useCases: UseCase[] = [
  {
    title: "[TÍTULO DESCRIPTIVO DEL CASO]",
    context: "[CONTEXTO: Problema, necesidad, objetivo del negocio - 3-4 líneas]",
    tool: "[HERRAMIENTA(S) USADA(S) + fuentes/datos si aplica]",
    output: "[OUTPUT TANGIBLE: Qué se generó, formato, métricas - 2-3 líneas]"
  },
  // ... 1-2 casos más
];
```

**Ejemplo (Clase 04):**
```typescript
{
  title: "Tesla: ¿Empresa Automotriz o Tecnológica?",
  context: "Investigar modelo de negocio híbrido de Tesla. Analizar innovación disruptiva (vehículos eléctricos + software OTA), integración vertical (baterías hasta seguros), ecosistemas de IA (Dojo, Autopilot, FSD), diversificación (Tesla Energy, Robotaxi, Optimus).",
  tool: "NotebookLM + Fuentes: Artículos Forbes/Bloomberg, reportes financieros 10-K, análisis S&P/McKinsey",
  output: "Business Model Canvas completo, 5 preguntas críticas de inversionista, mapa mental de líneas de negocio, podcast de conclusiones, análisis argumentado: ¿automotriz o tech?"
}
```

---

### 4.6 Prompt Library (Biblioteca de Prompts)

Crear **5-7 prompts categorizados** y reutilizables:

```typescript
export const promptExamples: PromptExample[] = [
  {
    label: "[NOMBRE DEL PROMPT]",
    category: "[CATEGORÍA TEMÁTICA]", // Ej: "Análisis Estratégico", "Benchmarking", "Due Diligence"
    content: `[PROMPT MULTILINEA COPY-PASTEABLE]

Incluye:
- Contexto claro
- Estructura esperada
- Formato de salida

Ejemplo: "Genera un análisis SWOT para [EMPRESA]..."
`
  },
  // ... 4-6 prompts más
];
```

**Categorías sugeridas:**
- Análisis Estratégico (SWOT, Business Model Canvas, Porter's 5 Forces)
- Benchmarking (Comparaciones competitivas)
- Due Diligence (Preguntas de inversionista, risk assessment)
- Herramientas de Estudio (Podcasts, guías, FAQs, flashcards)
- Visualización (Mapas mentales, diagramas, cronologías)
- Ética y Compliance (Riesgos, regulaciones, sesgos)

---

### 4.7 Best Practices (Mejores Prácticas)

Documentar **5-6 DOs y 5-6 DON'Ts** basados en experiencia real:

```typescript
export const bestPractices: BestPractice[] = [
  // ✅ DOs
  {
    title: "[PRÁCTICA RECOMENDADA]",
    description: "[EXPLICACIÓN DE POR QUÉ ES IMPORTANTE - 1-2 líneas]",
    type: "do"
  },
  // ... 4-5 DOs más

  // ❌ DON'Ts
  {
    title: "[PRÁCTICA A EVITAR]",
    description: "[EXPLICACIÓN DE POR QUÉ ES PROBLEMÁTICA - 1-2 líneas]",
    type: "dont"
  },
  // ... 4-5 DON'Ts más
];
```

**Ejemplo (Clase 04):**
```typescript
// DO
{
  title: "Cargar fuentes de calidad y actualizadas (2024-2025)",
  description: "Fuentes recientes de sitios confiables (Forbes, McKinsey, HBR, Bloomberg). Evitar contenido desactualizado que puede llevar a conclusiones erróneas.",
  type: "do"
},

// DON'T
{
  title: "Subir PDFs escaneados de baja calidad (OCR malo)",
  description: "OCR defectuoso = texto ilegible = respuestas inútiles. Preferir PDFs nativos digitales o re-escanear con OCR de calidad.",
  type: "dont"
}
```

---

### 4.8 Video Data (Opcional - si hay grabación)

Si hay video de la clase en Google Drive:

```typescript
export const videoData = {
  title: "Grabación Completa de la Clase",
  description: "[DESCRIPCIÓN: Qué se cubre en el video - 1-2 líneas]",
  embedUrl: "https://drive.google.com/file/d/[FILE_ID]/preview",
  duration: "2h", // [AJUSTAR]
  date: "06 Nov 2025",
  available: true,
  chapters: [
    { time: "00:00", title: "[CAPÍTULO 1]" },
    { time: "15:00", title: "[CAPÍTULO 2]" },
    { time: "65:00", title: "[CAPÍTULO 3]" },
    { time: "115:00", title: "[CAPÍTULO 4 - Cierre]" }
  ],
};
```

**Obtener File ID de Google Drive:**
1. Abrir video en Drive
2. Click derecho → "Get link" o "Share"
3. URL será: `https://drive.google.com/file/d/[FILE_ID]/view?usp=sharing`
4. Copiar `[FILE_ID]` y cambiar `/view` por `/preview`

**Si no hay video:**
```typescript
export const videoData = {
  title: "Grabación de Clase",
  description: "Video no disponible aún. Consultar materiales en GitHub.",
  embedUrl: "",
  available: false,
  chapters: [],
};
```

---

### 4.9 Resources (Links Externos)

Añadir **3-5 recursos adicionales**:

```typescript
export const resources = [
  {
    title: "[NOMBRE DEL RECURSO]",
    url: "https://...",
    type: "tool" | "documentation" | "transcript" | "slides" | "external"
  },
  // ... 2-4 recursos más
];
```

**Tipos sugeridos:**
- `tool` - Link a la herramienta en sí
- `documentation` - README pedagógico en GitHub
- `transcript` - Transcripción de la clase
- `slides` - Presentación o plan de clase
- `external` - Artículos, papers, tutoriales externos

---

## 🧪 Paso 5: Testing Local (10 min)

### 5.1 Levantar Dev Server

```bash
cd site/
npm run dev
```

Abrir: http://localhost:4321

---

### 5.2 Checklist de Validación

**Hero Section:**
- [ ] Vinyl hero se ve correctamente (no distorsionado)
- [ ] Halo background visible pero no invasivo
- [ ] Título y subtitle legibles
- [ ] 4 métricas visibles y balanceadas (2 red + 2 cyan)
- [ ] CTAs funcionales (internal links + externos)

**Bento Grid (Fundamentals):**
- [ ] Grid responsive: 1 columna móvil → 2 tablet → 3 desktop
- [ ] Iconos emoji visibles (NO texto)
- [ ] Descriptions con longitud variada para ritmo visual
- [ ] Badges distintivos y categorizados

**Workflow (si aplica):**
- [ ] Pasos numerados correctamente (01, 02, 03...)
- [ ] Tips legibles y útiles
- [ ] Layout responsive

**Tools Grid:**
- [ ] Cards con logos visibles (o placeholder si falta)
- [ ] Pricing claro
- [ ] Categorías correctas
- [ ] Links funcionales

**Use Cases:**
- [ ] Estructura clara: Context → Tool → Output
- [ ] Casos relevantes y concretos

**Prompt Library:**
- [ ] Prompts copy-pasteables (con botón copiar funcional)
- [ ] Categorías visibles
- [ ] Formato code block preservado

**Best Practices:**
- [ ] 2 columnas: DOs (izquierda) | DON'Ts (derecha)
- [ ] Iconos ✅ ❌ visibles
- [ ] Balance de items (similar cantidad en ambas columnas)

**Video Section (si aplica):**
- [ ] Embed de Google Drive funcional
- [ ] Fallback a GitHub si no hay embed
- [ ] Chapters listados con timestamps

**Resources:**
- [ ] Links válidos y funcionales
- [ ] Iconos de tipo correctos

**Navegación:**
- [ ] Link "← Volver a todas las clases" funcional
- [ ] Home → Clase → Home navegación OK
- [ ] Clase visible en home vinyl grid

---

### 5.3 Testing Responsive

**Probar en diferentes viewports:**
```bash
# Desktop (1920x1080)
# Tablet (768x1024)
# Mobile (375x667)
```

- [ ] Hero no se corta en móvil
- [ ] Bento grid colapsa correctamente
- [ ] Tool cards stack en móvil
- [ ] Video embed responsive (no overflow)

---

### 5.4 Performance

**Verificar tiempos de carga:**
```bash
# Lighthouse en DevTools
# Objetivo: Performance > 85, Accessibility > 95
```

- [ ] Imágenes optimizadas (WebP, < 100KB)
- [ ] No console errors
- [ ] Fonts cargan correctamente

---

## 🚀 Paso 6: Commit y Deploy (5 min)

### 6.1 Verificar Cambios

```bash
git status
```

Deberías ver:
- `site/assets/vinyls/clase-05/vinilo.webp` (nuevo)
- `site/assets/halos/clase-05.webp` (nuevo)
- `site/assets/spines/clase-05.png` (nuevo)
- `site/src/data/clase-05-data.ts` (nuevo)
- `site/src/pages/clases/clase-05-agentes-ia.astro` (nuevo)
- `site/src/data/course.ts` (modificado)

### 6.2 Añadir Archivos

```bash
git add site/assets/vinyls/clase-05/
git add site/assets/halos/clase-05.webp
git add site/assets/spines/clase-05.png
git add site/src/data/clase-05-data.ts
git add site/src/pages/clases/clase-05-agentes-ia.astro
git add site/src/data/course.ts
```

### 6.3 Commit con Mensaje Descriptivo

```bash
git commit -m "$(cat <<'EOF'
feat: Add Clase 05 - Agentes IA Autónomos

- Generate hero images with Flux Dev (vinyl + halo)
- Complete data file with fundamentals, tools, workflow
- Add 3 use cases and 7 prompt examples
- Document 6 DOs and 6 DON'Ts
- Update course.ts with new class entry

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

### 6.4 Push a GitHub

```bash
git push origin main
```

**GitHub Actions desplegará automáticamente a GitHub Pages** (si configurado).

Verificar deploy: https://github.com/[usuario]/[repo]/actions

---

## 🔧 Troubleshooting

### Problema: Imagen generada no cumple expectativas

**Solución:**
1. Iterar prompt 2-3 veces ajustando keywords
2. Cambiar modelo (SDXL → Flux Dev → Flux Pro)
3. Especificar más detalles técnicos (lighting, composition, style)

**Ejemplo de iteración:**
```
v1: "Agentes IA orquestando tareas" (muy genérico)
v2: "Multiple AI agent nodes connected in network, orchestrating..."
v3: "Futuristic AI agent architecture, autonomous nodes with glowing..."
```

---

### Problema: Logo de herramienta no existe

**Solución:**

**Opción 1: Descargar oficial**
1. Ir al sitio de la herramienta
2. Buscar "Press Kit" o "Brand Assets"
3. Descargar PNG/SVG en alta resolución
4. Guardar en `site/assets/logos/[herramienta].png`

**Opción 2: Screenshot con Playwright**
```bash
# Usar comando /browser de Claude Code
/browser captura logo de [herramienta] desde [URL]
```

**Opción 3: Placeholder temporal**
```typescript
// En clase-XX-data.ts
logo: undefined, // Sin logo por ahora
```

---

### Problema: Video no embebe en Google Drive

**Causas:**
- Permisos incorrectos (debe ser "Anyone with the link")
- URL mal formateada (debe usar `/preview` no `/view`)

**Solución:**
1. Abrir video en Drive
2. Click derecho → Share → Change to "Anyone with the link"
3. Obtener URL: `https://drive.google.com/file/d/[FILE_ID]/view`
4. Cambiar a: `https://drive.google.com/file/d/[FILE_ID]/preview`

**Fallback:**
```typescript
embedUrl: "", // Dejar vacío
available: false, // Marcar como no disponible
// Añadir link directo en resources[]
```

---

### Problema: course.ts no se actualiza correctamente

**Causas:**
- Sintaxis incorrecta en array `classes[]`
- Imports mal formateados
- Counter en `hudMetrics` no incrementado

**Solución:**
```bash
# Verificar sintaxis
npm run build  # Debe pasar sin errores

# Buscar errores de TypeScript
npx tsc --noEmit

# Verificar imports
grep "clase-05" site/src/data/course.ts
```

---

### Problema: Build falla en GitHub Actions

**Causas comunes:**
- Imagen faltante (import apunta a archivo inexistente)
- TypeScript error (tipo incorrecto en data file)
- Dependencia faltante

**Solución:**
```bash
# Probar build local
cd site/
npm run build

# Ver logs de error
cat dist/index.html  # Verificar que se generó

# Verificar imports
ls -la assets/vinyls/clase-05/vinilo.webp
ls -la assets/halos/clase-05.webp
```

---

## ⏱️ Tiempos Estimados

| Fase | Tiempo | Acumulado |
|------|--------|-----------|
| **1. Planificación** | 20 min | 20 min |
| **2. Script automatizado** | 2 min | 22 min |
| **3. Generación de assets** | 15 min | 37 min |
| **4. Contenido** | 60-90 min | 97-127 min |
| **5. Testing** | 10 min | 107-137 min |
| **6. Commit/Deploy** | 5 min | **112-142 min** |

**Total: ~2h (112-142 min)**

vs **Manual completo: ~3h (180 min)**

**Ahorro: 38-68 min (21-38%)**

---

## 📚 Referencias

- **Documentación de Brand:** `docs/brand/manifesto.md`
- **Verticales Reference:** `docs/brand/VERTICALES_REFERENCE.md`
- **Concepto de Diseño:** `site/CONCEPTO.md`
- **Clases Existentes (referencias):**
  - Clase 02: `site/src/data/clase-02-data.ts`
  - Clase 03: `site/src/data/clase-03-data.ts`
  - Clase 04: `site/src/data/clase-04-data.ts`

---

## 🆘 Soporte

**¿Dudas o problemas?**
1. Revisar clases anteriores para ver ejemplos
2. Consultar documentación en `docs/`
3. Revisar logs de build: `npm run build --verbose`

**Mejoras a este documento:**
- PRs bienvenidos en: `materias/inteligencia-artificial-para-negocios/CREAR_NUEVA_CLASE.md`
- Sugerencias vía Issues en GitHub

---

**Última actualización:** 2025-11-06
**Versión:** 1.0
**Autor:** Julián Zuluaga (Orbital Lab / Universidad Externado)
