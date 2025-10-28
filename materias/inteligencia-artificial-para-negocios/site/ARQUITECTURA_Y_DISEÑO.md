# Arquitectura y Diseño: Orbital Vinyl Collection

**Documento de Referencia Técnica y Visual**
**Proyecto:** Micrositio Inteligencia Artificial para Negocios
**Universidad Externado de Colombia (Compensar)**
**Autor:** Julián Zuluaga - Orbital Lab
**Fecha:** 28 de octubre de 2025
**Versión:** 1.0

---

## 📖 Índice

1. [Visión General](#1-visión-general)
2. [Stack Técnico](#2-stack-técnico)
3. [Arquitectura de Información](#3-arquitectura-de-información)
4. [Sistema de Diseño Visual](#4-sistema-de-diseño-visual)
5. [Componentes Clave](#5-componentes-clave)
6. [Sistema de Assets](#6-sistema-de-assets)
7. [Interacciones y Animaciones](#7-interacciones-y-animaciones)
8. [Estructura de Datos](#8-estructura-de-datos)
9. [Flujo de Usuario](#9-flujo-de-usuario)
10. [Consideraciones de Accesibilidad](#10-consideraciones-de-accesibilidad)
11. [Deployment y Build](#11-deployment-y-build)
12. [Roadmap de Implementación](#12-roadmap-de-implementación)

---

## 1. Visión General

### 1.1 Concepto Central

**"Orbital Vinyl Collection"** - Micrositio cinematográfico que presenta cada clase como un vinilo holográfico en un laboratorio musical futurista.

### 1.2 Propósito

- **Presentar** la materia con estética Orbital (negro profundo + rojo orbital + halos cian)
- **Exhibir** cada clase como "vinilo holográfico" con portada ilustrada, spine lateral y contenido desplegable
- **Facilitar** acceso a materiales (README, slides, datasets, herramientas)
- **Preparar** estructura para despliegue en GitHub Pages

### 1.3 Filosofía de Diseño

**Mantra guía:** *"¿Ayuda a ver y entender mejor la IA corporativa?"*

- **Cinematográfico**: Hero inmersivo con video de fondo y halos orbitales
- **Translúcido**: Glassmorphism con blur y transparencias
- **Futurista**: Tipografías tech, métricas HUD, efectos glow
- **Accionable**: CTA claros, navegación intuitiva, recursos destacados

---

## 2. Stack Técnico

### 2.1 Framework Principal

```json
{
  "name": "orbital-vinyl-site",
  "version": "0.0.1",
  "type": "module"
}
```

**Tecnologías Core:**

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Astro** | 5.15.1 | SSG (Static Site Generation) framework |
| **TailwindCSS** | 4.1.16 | Sistema de estilos utility-first |
| **@tailwindcss/vite** | 4.1.16 | Plugin de Vite para Tailwind v4 |

### 2.2 Scripts Disponibles

```bash
npm run dev      # Servidor de desarrollo (port 4321)
npm run build    # Build estático para producción
npm run preview  # Preview del build localmente
npm run astro    # CLI de Astro
```

### 2.3 Configuración de Build

**astro.config.mjs:**

```javascript
export default defineConfig({
  site: process.env.SITE_URL || "https://example.com",
  base: process.env.BASE_PATH || "/",
  build: {
    assets: "relative"  // Paths relativos para GitHub Pages
  },
  vite: {
    plugins: [tailwindcss()]
  }
});
```

**Características clave:**
- ✅ **Assets relativos**: Compatible con subdirectorios de GitHub Pages
- ✅ **Variables de entorno**: `SITE_URL` y `BASE_PATH` configurables
- ✅ **Vite plugin**: Integración nativa de TailwindCSS v4

### 2.4 Dependencias Notables

**NO usa:**
- ❌ React/Vue/Svelte (solo Astro puro)
- ❌ Framer Motion (animaciones nativas CSS)
- ❌ GSAP (solo vanilla JS + CSS)
- ❌ Lenis smooth scroll (animaciones CSS scroll-timeline)

**Ventajas del enfoque minimalista:**
- ⚡ Build ultra-rápido (~2-3s)
- 📦 Bundle pequeño (~50KB JS)
- 🚀 Perfect Lighthouse score potencial
- 🔧 Mantenimiento simplificado

---

## 3. Arquitectura de Información

### 3.1 Estructura de Páginas

```
src/pages/
├── index.astro                     # Home principal
├── docs/
│   └── syllabus.astro             # Programa detallado
└── clases/
    └── 2025-10-23-clase-02-ia-corporativa.astro  # Detalle de clase
```

### 3.2 Home (index.astro)

**Secciones en orden:**

1. **HeroOrbit** - Hero fullscreen inmersivo
   - Título principal
   - Tagline: "Ver es entender la IA corporativa"
   - 2 CTAs: Ver syllabus | Colección completa

2. **HighlightsBento** - Tres highlights rápidos
   - Metodología Orbital
   - Stack Inteligente
   - Casos Orbital

3. **VinylGrid** - Colección de clases
   - Cards responsivas con vinilos
   - Hover interactivo con animación 3D
   - Modal con detalle completo

4. **ToolkitChips** - Herramientas destacadas
   - Chips con hover glow
   - Enlaces a plataformas externas

5. **FAQAccordion** - Preguntas frecuentes
   - Accordion expandible
   - 3 FAQs principales

6. **Footer** - Mantra y créditos
   - *"¿Ayuda a ver y entender mejor la IA corporativa?"*
   - Orbital Lab · Universidad Externado · 2025

### 3.3 Navegación

**Flow principal:**

```
Home
├── Ver Syllabus → /docs/syllabus
├── Colección completa → #coleccion (anchor)
├── Vinyl Card "Abrir pista" → Modal (dialog HTML)
└── Vinyl Card "Ver README" → /clases/{slug}/
```

**Navegación en modal:**
- ✅ Cierre con botón "Cerrar"
- ✅ Cierre con clic fuera (backdrop)
- ✅ Cierre con `Esc` (nativo HTML dialog)
- ⏸️ Navegación teclado `←` `→` (pendiente)

---

## 4. Sistema de Diseño Visual

### 4.1 Paleta de Colores

**Colores de marca Orbital:**

```css
/* Colores primarios */
--orbital-red: #ED2024;        /* rgb(237, 32, 36) */
--orbital-cyan: #00BCD4;       /* rgb(0, 188, 212) */
--orbital-black: #050509;      /* Fondo principal */

/* Grises tech */
--slate-100: #f1f5f9;          /* Texto principal */
--slate-300: rgba(226, 232, 240, 0.75);  /* Texto secundario */
--slate-400: rgba(148, 163, 184, 0.8);   /* Texto terciario */
--slate-500: rgba(148, 163, 184, 0.75);  /* Placeholders */

/* Transparencias */
--red-glow: rgba(237, 32, 36, 0.35);
--cyan-glow: rgba(0, 188, 212, 0.15);
--glass-bg: rgba(17, 17, 24, 0.92);
```

**Gradientes principales:**

```css
/* Fondo body con halos */
background-image:
  radial-gradient(circle at 20% 20%, rgba(237, 32, 36, 0.12), transparent 55%),
  radial-gradient(circle at 80% 10%, rgba(0, 188, 212, 0.1), transparent 45%),
  radial-gradient(circle at 50% 100%, rgba(237, 32, 36, 0.08), transparent 60%);

/* Hero overlay */
background: linear-gradient(
  180deg,
  rgba(5, 5, 9, 0.35) 0%,
  rgba(5, 5, 9, 0.75) 60%,
  rgba(5, 5, 9, 0.92) 100%
);
```

### 4.2 Tipografía

**Sistema de fuentes:**

```css
/* Títulos hero y secciones */
font-family: "Rajdhani", sans-serif;
font-weight: 500 | 600 | 700;
letter-spacing: 0.01em - 0.02em;

/* Cuerpo y descripciones */
font-family: "Inter", system-ui, -apple-system, sans-serif;
font-weight: 400 | 500 | 600;
letter-spacing: normal;

/* Código y métricas HUD */
font-family: "Fira Code", ui-monospace, "Courier New", monospace;
font-weight: 400 | 500;
```

**Escalas tipográficas:**

| Elemento | Tamaño | Peso | Familia |
|----------|--------|------|---------|
| Hero title | clamp(2.75rem, 5.5vw, 4.5rem) | 600-700 | Rajdhani |
| Section title | 1.75rem - 3rem | 600 | Rajdhani |
| Card title | 1.75rem | 600 | Rajdhani |
| Body text | 0.9rem - 1rem | 400-500 | Inter |
| Captions | 0.6rem - 0.75rem | 400-500 | Inter |
| Badges/Labels | 0.55rem - 0.7rem | 600 | Inter |
| HUD metrics | 0.7rem | 500 | Fira Code |

### 4.3 Espaciado y Layout

**Sistema de espaciado:**

```css
/* Contenedor principal */
width: min(1180px, 92vw);
padding: 0 clamp(1.5rem, 4vw, 2.5rem);

/* Hero vertical spacing */
padding: clamp(4rem, 8vw, 6rem) clamp(1.5rem, 4vw, 3rem);
gap: clamp(2rem, 6vw, 4rem);

/* Cards y componentes */
gap: 1.5rem - 2rem;
padding: 1.5rem - 2.5rem;
border-radius: 2rem (cards) | 1.5rem (imágenes) | 999px (botones);
```

**Grid responsive:**

```css
/* Vinyl rail - scroll horizontal en mobile */
.vinyl-rail {
  display: flex;
  gap: 1.75rem;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
}

/* Desktop - 3 columnas */
@media (min-width: 1024px) {
  .vinyl-rail {
    flex-wrap: wrap;
    overflow-x: visible;
  }
  .vinyl-card {
    flex: 1 1 calc(33.333% - 1.75rem);
  }
}
```

### 4.4 Efectos Visuales

**Glassmorphism (paneles translúcidos):**

```css
.panel-orbital {
  background: linear-gradient(
    135deg,
    rgba(17, 17, 24, 0.92),
    rgba(28, 28, 46, 0.68)
  );
  border: 1px solid rgba(237, 32, 36, 0.3);
  backdrop-filter: blur(18px);
}
```

**Glow orbital (efecto de halo):**

```css
.glow-orbital {
  box-shadow:
    0 0 45px rgba(237, 32, 36, 0.35),
    0 0 120px rgba(0, 188, 212, 0.15);
}
```

**Bordes gradiente (HUD):**

```css
.hud-outline {
  border-image: linear-gradient(
    120deg,
    rgba(237, 32, 36, 0.8),
    rgba(0, 188, 212, 0.7)
  ) 1;
  border-width: 1px;
  border-style: solid;
}
```

---

## 5. Componentes Clave

### 5.1 HeroOrbit (Hero Fullscreen)

**Archivo:** `src/components/HeroOrbit.astro`

**Estructura:**

```astro
<section class="hero-orbit">
  <video class="hero-orbit__video" autoplay loop muted>
    <!-- Video de fondo (hero-loop.webm) -->
  </video>
  <div class="hero-orbit__overlay" />
  <div class="hero-orbit__halo" />

  <div class="hero-orbit__content">
    <div>
      <h1 class="hero-orbit__title">Inteligencia Artificial para Negocios</h1>
      <p class="tagline">Ver es entender la IA corporativa.</p>
      <!-- CTAs -->
    </div>

    <aside class="hero-orbit__hud">
      <!-- HUD metrics: 3 clases, 6h, 80% práctica -->
    </aside>
  </div>
</section>
```

**Características:**
- ✅ Video de fondo fullscreen (con fallback a imagen estática)
- ✅ Overlay gradiente para legibilidad
- ✅ Halos rojo/cian con `mix-blend-mode: screen`
- ✅ Grid 2 columnas en desktop (1 columna mobile)
- ✅ HUD lateral con métricas animadas

### 5.2 VinylGrid (Colección de Clases)

**Archivo:** `src/components/VinylGrid.astro`

**Anatomía de VinylCard:**

```
┌─────────────────────────────────┐
│  ┌──────────┐    ╭──────╮       │  vinyl-card
│  │ Portada  │   ╱ Vinilo ╲      │
│  │ (sleeve) │  │  (record) │    │  ← vinyl-card__media
│  └──────────┘   ╲        ╱      │
│   "Mood text"    ╰───●───╯      │
│                                  │
│  Clase 02  [DISPONIBLE]         │  ← vinyl-card__meta
│                                  │
│  ▌Vibe Coding: IA que Programa  │  ← vinyl-card__title
│                                  │
│  La sesión estelar. Domina...   │  ← vinyl-card__synopsis
│                                  │
│  23 Oct 2025 · 2h · Práctica    │  ← vinyl-card__tags
│                                  │
│  [Abrir pista] [Ver README]     │  ← vinyl-card__actions
└─────────────────────────────────┘
```

**Interacciones:**

1. **Hover sobre card:**
   - Card eleva (`translateY(-10px)`)
   - Borde cambia a rojo (`rgba(237, 32, 36, 0.45)`)
   - Imagen de portada hace zoom (`scale(1.05)`)
   - Vinilo gira y se desliza (`rotate(12deg)`, `translateX(-20%)`)
   - Vinilo inicia rotación continua (`animation: spinRecord 9s linear infinite`)

2. **Click "Abrir pista":**
   - Abre modal con `<dialog>` HTML nativo
   - Backdrop con blur orbital
   - Panel con contenido completo de la clase

### 5.3 VinylModal (Dialog)

**Estructura:**

```html
<dialog id="vinyl-{slug}" class="vinyl-modal">
  <div class="vinyl-modal__backdrop" />  <!-- Glow rojo difuminado -->

  <article class="vinyl-modal__panel">
    <header>
      <span class="badge">Clase 02</span>
      <h3>Vibe Coding: IA que Programa</h3>
      <p>Synopsis...</p>
      <button data-vinyl-close>Cerrar</button>
    </header>

    <div class="vinyl-modal__content">
      <div class="vinyl-modal__hero">
        <img src="halo-02.webp" />  <!-- Imagen hero modal -->
      </div>

      <section>
        <h4>Stack</h4>
        <div class="chips">
          <span>Lovable</span>
          <span>Replit Agent</span>
          <!-- ... -->
        </div>
      </section>

      <section>
        <h4>Lo que lograrás</h4>
        <ul>
          <li>15+ herramientas</li>
          <li>MVP en 90 minutos</li>
          <!-- ... -->
        </ul>
      </section>

      <section>
        <h4>Recursos</h4>
        <div class="buttons">
          <a href="/clases/...">Guía completa</a>
          <a href="/transcripts/...">Transcripción .vtt</a>
        </div>
      </section>
    </div>
  </article>
</dialog>
```

**JavaScript del modal:**

```javascript
// Abrir modal con animación
button.addEventListener("click", () => {
  dialog.showModal();
  requestAnimationFrame(() =>
    dialog.classList.add("vinyl-modal--visible")
  );
});

// Cerrar con transición
const closeDialogs = (dialog) => {
  dialog.classList.remove("vinyl-modal--visible");
  dialog.addEventListener("transitionend", () => {
    dialog.close();
  }, { once: true });
};

// Listeners: botón cerrar, backdrop click, Esc key
closeBtn.addEventListener("click", () => closeDialogs(dialog));
dialog.addEventListener("click", (e) => {
  if (e.target === dialog) closeDialogs(dialog);
});
dialog.addEventListener("cancel", (e) => {
  e.preventDefault();
  closeDialogs(dialog);
});
```

### 5.4 HighlightsBento (Tarjetas de Destacados)

**Archivo:** `src/components/HighlightsBento.astro`

**Grid de 3 tarjetas:**

```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ CINEMÁTICA   │  │ TOOLSET      │  │ IMPACTO      │
│              │  │              │  │              │
│ Metodología  │  │ Stack        │  │ Casos        │
│ Orbital      │  │ Inteligente  │  │ Orbital      │
│              │  │              │  │              │
│ Laboratorios │  │ Lovable,     │  │ Strivio,     │
│ inmersivos,  │  │ Replit,      │  │ Lighthouse,  │
│ 80% práctica │  │ v0.dev...    │  │ Jaguar...    │
└──────────────┘  └──────────────┘  └──────────────┘
```

**Características:**
- Badge superior con label (CINEMÁTICA, TOOLSET, IMPACTO)
- Título de sección
- Descripción breve
- Glassmorphism con glow rojo

### 5.5 ToolkitChips (Herramientas)

**Archivo:** `src/components/ToolkitChips.astro`

**Chips horizontales con hover:**

```
[Lovable] [Replit Agent] [v0.dev] [Claude Artifacts] [Cursor IDE] [Gemini Flash]
```

**Interacción hover:**
- Glow rojo aumenta (`box-shadow: 0 18px 45px rgba(237, 32, 36, 0.38)`)
- Traslación vertical (`translateY(-2px)`)
- Enlaces externos abiertos en nueva pestaña

### 5.6 FAQAccordion (Preguntas Frecuentes)

**Archivo:** `src/components/FAQAccordion.astro`

**3 FAQs principales:**

1. ¿Necesito saber programar?
2. ¿Cómo se entregan los recursos?
3. ¿Qué necesito llevar?

**Interacción:**
- Click en pregunta expande respuesta
- Animación de altura (`max-height` transition)
- Solo un item abierto a la vez (accordion behavior)

---

## 6. Sistema de Assets

### 6.1 Estructura de Carpetas

```
assets/
├── hero/                    # Hero principal
│   ├── hero-lab.webp       # Imagen estática (2048×1280)
│   └── hero-loop.webm      # Video loop (8s, 4:5 crop)
│
├── vinyls/                  # Portadas de clases
│   ├── clase-01/
│   │   ├── vinilo.webp     # Portada vinilo
│   │   ├── vinilo-original.png
│   │   └── vinilo-loop.webm  (pendiente)
│   ├── clase-02/
│   │   ├── vinilo.webp     # Placeholder temporal
│   │   ├── vinilo-placeholder.png
│   │   └── notes.md
│   └── clase-03/
│       ├── vinilo.webp     # Placeholder temporal
│       ├── vinilo-placeholder.png
│       └── notes.md
│
├── halos/                   # Fondos para modales
│   ├── clase-01.webp       # Halo rojo gradiente
│   ├── clase-02.webp       # Halo rojo gradiente
│   ├── clase-03.webp       # Halo cian gradiente
│   └── notes.md
│
├── spines/                  # Lomos de vinilos
│   ├── clase-01.png        # Spine placeholder
│   ├── clase-02.png        # Spine placeholder
│   ├── clase-03.png        # Spine placeholder
│   └── notes.md
│
├── banners/                 (pendiente)
│   ├── metodologia.webp
│   ├── herramientas.webp
│   └── casos-orbital.webp
│
├── icons/                   (pendiente)
│   ├── lovable.svg
│   ├── replit.svg
│   └── claude.svg
│
└── GLOSARIO.md              # Control de assets
```

### 6.2 Especificaciones de Assets

**Hero:**
- **Formato:** WebP (estático) + WebM (loop)
- **Dimensiones:** 2400px+ ancho (hero-lab.webp: 2048×1280)
- **Peso:** ≤600KB (webp), ≤2MB (webm)
- **Características:** Loop ≤8s, recorte 16:9 a 4:5 para mobile

**Vinilos (portadas):**
- **Formato:** WebP con fallback PNG
- **Dimensiones:** 1:1 (square), mínimo 800×800px
- **Peso:** ≤300KB por imagen
- **Versiones:** `@1x` (800px), `@2x` (1600px) opcional

**Halos (fondos modal):**
- **Formato:** WebP
- **Dimensiones:** 1920×1080px (16:9)
- **Peso:** ≤400KB
- **Características:** Gradiente difuminado con glow rojo/cian

**Spines (lomos):**
- **Formato:** PNG transparente
- **Dimensiones:** 400×1400px (vertical)
- **Peso:** ≤100KB
- **Características:** Tipografía condensada con gradiente

### 6.3 Estado de Assets (2025-10-28)

**Completados (☑):**
- Hero lab (Gemini 2025-10-28) + loop (Hailuo → ffmpeg)
- Vinyl Clase 01 (Gemini actualizada 2025-10-26)
- Placeholders Clase 02 y 03 (Pillow script)
- Halos básicos con gradientes (script local)
- Spines placeholders (Pillow gradientes)

**Pendientes (☐):**
- Loops hover para vinilos (rotación/glow)
- Vinilos finales Clase 02 y 03 (sustituir placeholders)
- Banners secciones (Metodología, Herramientas, Casos)
- Iconos SVG lineales de herramientas
- Patrones de fondo (circuitos, mallas)

### 6.4 Prompts de Generación

**Hero Lab (Gemini 2025-10-28):**
```
Corporate AI control room futuristic design,
sleek data visualization dashboards,
holographic interfaces with red and cyan accents,
executive workspace with cityscape view,
cinematic lighting with Orbital Lab aesthetic,
deep blacks with red #ED2024 and cyan #00BCD4 highlights,
ultra detailed 8K, sci-fi professional
```

**Vinilo Clase 01 (Gemini 2025-10-26):**
```
Corporate ai control room, skyline at night,
red orbital glow, holographic dashboards,
cinematic lighting, ultra detailed,
orbital lab color palette
```

---

## 7. Interacciones y Animaciones

### 7.1 Animaciones CSS Nativas

**Rotación continua del vinilo (hover):**

```css
@keyframes spinRecord {
  from { rotate: 0deg; }
  to { rotate: 360deg; }
}

.vinyl-card:hover .vinyl-card__record {
  animation: spinRecord 9s linear infinite;
}
```

**Transiciones suaves:**

```css
/* Cards */
transition: transform 220ms ease,
            border-color 220ms ease,
            box-shadow 220ms ease;

/* Botones */
transition: transform 200ms ease,
            box-shadow 200ms ease,
            background-color 200ms ease;

/* Modal */
transition: opacity 220ms ease,
            transform 220ms ease;
```

### 7.2 Efectos de Hover

**Vinyl Card:**
```css
.vinyl-card:hover {
  transform: translateY(-10px);
  border-color: rgba(237, 32, 36, 0.45);
  box-shadow: 0 40px 110px rgba(237, 32, 36, 0.25);
}

.vinyl-card:hover .vinyl-card__sleeve img {
  transform: scale(1.05);
}

.vinyl-card:hover .vinyl-card__record {
  transform: translateX(-20%) rotate(12deg);
  animation: spinRecord 9s linear infinite;
}
```

**Botones CTA:**
```css
.hero-orbit__cta--primary:hover {
  transform: translateY(-2px) scale(1.01);
  box-shadow: 0 24px 55px rgba(237, 32, 36, 0.45);
}
```

### 7.3 Animaciones del Modal

**Entrada (showModal):**

1. `dialog.showModal()` - Abre dialog nativo
2. `requestAnimationFrame(() => addClass("vinyl-modal--visible"))` - Trigger animación CSS
3. Resultado:
   - Opacity: 0 → 1
   - Transform: `translateY(24px)` → `translateY(0)`
   - Duration: 220ms ease

**Salida (close):**

1. `removeClass("vinyl-modal--visible")` - Remueve clase
2. Escuchar `transitionend` event
3. `dialog.close()` cuando termina transición
4. Resultado:
   - Opacity: 1 → 0
   - Transform: `translateY(0)` → `translateY(24px)`

### 7.4 Scroll Behavior

**Smooth scrolling nativo:**

```css
html {
  scroll-behavior: smooth;
}
```

**Scroll snap en vinyl rail (mobile):**

```css
.vinyl-rail {
  scroll-snap-type: x mandatory;
}

.vinyl-card {
  scroll-snap-align: start;
}
```

**Scrollbar custom:**

```css
.vinyl-rail::-webkit-scrollbar {
  height: 8px;
}

.vinyl-rail::-webkit-scrollbar-thumb {
  background: rgba(237, 32, 36, 0.4);
  border-radius: 999px;
}
```

---

## 8. Estructura de Datos

### 8.1 TypeScript Interfaces

**course.ts:**

```typescript
export type ClassStatus = "draft" | "upcoming" | "published";

export interface ClassResource {
  label: string;
  href: string;
  type: "readme" | "slides" | "datasets" | "tools" | "otros";
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
}
```

### 8.2 Datos de Clases (classes)

**Clase 01 - Introducción IA Corporativa:**
```typescript
{
  slug: "clase-01-introduccion-ia-corporativa",
  number: "01",
  title: "Introducción IA Corporativa",
  mood: "Penthouse orbital, skyline con haces de datos",
  synopsis: "Encendemos la colección con un mapa estratégico...",
  status: "upcoming",
  date: "21 Oct 2025",
  duration: "2h",
  modality: "Presencial / Demo Lab",
  stack: ["Lentes Orbital", "Business Strategy", "Mapa de datos"],
  metrics: [
    "+12 casos IA Orbital",
    "Framework adopción 4D",
    "Checklist IA corporativa"
  ],
  resources: [
    { label: "Syllabus general", href: "/docs/syllabus", type: "readme" }
  ]
}
```

**Clase 02 - Vibe Coding:**
```typescript
{
  slug: "clase-02-vibe-coding",
  number: "02",
  title: "Vibe Coding: IA que Programa",
  mood: "DJ tech mezclando prompts, partículas rojo-cian",
  synopsis: "La sesión estelar. Domina Vibe Coding...",
  status: "published",
  date: "23 Oct 2025",
  duration: "2h",
  modality: "Práctica 80/20",
  stack: ["Lovable", "Replit Agent", "v0.dev"],
  metrics: [
    "15+ herramientas",
    "MVP en 90 minutos",
    "Casos reales Orbital"
  ],
  resources: [
    {
      label: "Guía completa Clase 02",
      href: "/clases/2025-10-23-clase-02-ia-corporativa/",
      type: "readme"
    },
    {
      label: "Transcripción .vtt",
      href: "/transcripts/clase-02.vtt",
      type: "otros"
    }
  ]
}
```

**Clase 03 - IA Generativa Visual:**
```typescript
{
  slug: "clase-03-ia-generativa-visual",
  number: "03",
  title: "IA Generativa Visual",
  mood: "Galería holográfica, mallas visuales flotando",
  synopsis: "Diseñamos experiencias visuales con IA...",
  status: "upcoming",
  date: "28 Oct 2025",
  duration: "2h",
  modality: "Demo / Hands-on",
  stack: ["Midjourney", "Imagen 3", "Nano Banana"],
  metrics: [
    "Guía prompts Orbital",
    "Workflow entrega creativa",
    "canvas multimodal"
  ],
  resources: [
    { label: "Brief creativo", href: "#brief-creativo", type: "otros" }
  ]
}
```

### 8.3 Highlights Data

```typescript
export const highlights = [
  {
    title: "Metodología Orbital",
    description: "Laboratorios inmersivos, 80% práctica, retos corporativos reales...",
    badge: "Cinemática"
  },
  {
    title: "Stack Inteligente",
    description: "Lovable, Replit, v0.dev, Claude Artifacts...",
    badge: "Toolset"
  },
  {
    title: "Casos Orbital",
    description: "Strivio, Lighthouse, Jaguar. Narrativas con impacto tangible...",
    badge: "Impacto"
  }
] as const;
```

### 8.4 Toolkit Data

```typescript
export const toolkit = [
  { label: "Lovable", href: "https://lovable.dev" },
  { label: "Replit Agent", href: "https://replit.com/ai" },
  { label: "v0.dev", href: "https://v0.dev" },
  { label: "Claude Artifacts", href: "https://claude.ai" },
  { label: "Cursor IDE", href: "https://cursor.sh" },
  { label: "Gemini Flash", href: "https://ai.google.dev/gemini-api" }
] as const;
```

### 8.5 FAQs Data

```typescript
export const faqs = [
  {
    question: "¿Necesito saber programar?",
    answer: "No. Arrancamos desde cero. La clave es aprender a orquestar prompts..."
  },
  {
    question: "¿Cómo se entregan los recursos?",
    answer: "Cada clase libera README interactivo, transcript y repositorio..."
  },
  {
    question: "¿Qué necesito llevar?",
    answer: "Laptop, cuenta en herramientas IA (puedes usar versiones free)..."
  }
] as const;
```

---

## 9. Flujo de Usuario

### 9.1 Journey Principal

```
1. Landing en Home
   ↓
2. Hero inmersivo captura atención
   - Video de fondo orbital
   - Título impactante: "Inteligencia Artificial para Negocios"
   - Tagline: "Ver es entender la IA corporativa"
   ↓
3. Highlights rápidos (3 tarjetas)
   - Metodología, Stack, Casos
   - Comprensión rápida del valor
   ↓
4. Colección de Vinilos
   - Scroll horizontal (mobile) o grid (desktop)
   - Hover sobre card → vinilo gira
   ↓
5. Click "Abrir pista"
   - Modal con detalle completo
   - Stack de herramientas
   - Métricas de aprendizaje
   - CTAs de recursos
   ↓
6. Click "Ver README" o "Guía completa"
   - Redirección a página de clase
   - Contenido markdown completo
   ↓
7. Toolkit y FAQs
   - Exploración de herramientas externas
   - Respuestas a dudas comunes
   ↓
8. Footer con mantra Orbital
```

### 9.2 Navegación Alternativa

**Desde Hero CTA "Ver syllabus":**
```
Home → /docs/syllabus → Programa detallado → Volver a Home
```

**Desde Hero CTA "Colección completa":**
```
Home → Scroll animado a #coleccion (anchor)
```

**Desde Vinyl Card "Ver README":**
```
Home → /clases/{slug}/ → Contenido markdown → Browser back
```

### 9.3 Interacciones Clave

**Card hover:**
- Movimiento: Card eleva 10px
- Vinilo: Gira y se desliza
- Feedback visual: Glow rojo aumenta

**Modal open:**
- Backdrop blur oscuro
- Panel anima desde abajo (translateY)
- Escape closes: Esc key, backdrop click, botón cerrar

**Scroll en colección:**
- Mobile: Horizontal scroll con snap
- Desktop: Grid estático 3 columnas

---

## 10. Consideraciones de Accesibilidad

### 10.1 Contraste de Colores

**Cumplimiento WCAG 2.1 AA:**

- ✅ Texto principal en `#f1f5f9` sobre `#050509` (ratio > 15:1)
- ✅ Texto secundario en `rgba(226, 232, 240, 0.75)` (ratio > 10:1)
- ⚠️ Badges/labels en 0.6rem - verificar ratio mínimo 4.5:1

**Recomendaciones:**
```css
/* Aumentar contraste en textos pequeños */
.vinyl-card__badge {
  color: rgba(255, 255, 255, 0.85);  /* Antes: 0.65 */
}
```

### 10.2 Semántica HTML

**Estructura jerárquica:**

```html
<main>
  <section aria-labelledby="hero-title">
    <h1 id="hero-title">Inteligencia Artificial para Negocios</h1>
  </section>

  <section aria-label="Highlights destacados">
    <h2>Metodología Orbital</h2>
  </section>

  <section id="coleccion" aria-label="Colección de clases">
    <h2>Colección de Vinilos</h2>
    <article aria-label="Clase 02: Vibe Coding">
      <h3>Vibe Coding: IA que Programa</h3>
    </article>
  </section>
</main>
```

### 10.3 Navegación por Teclado

**Elementos focuseables:**
- ✅ CTAs hero (Tab navegación)
- ✅ Cards en colección (Tab navegación)
- ✅ Botones "Abrir pista" y "Ver README"
- ✅ Modal "Cerrar" button
- ⏸️ Navegación entre cards con `←` `→` (pendiente)

**Focus indicators:**
```css
button:focus-visible,
a:focus-visible {
  outline: 2px solid rgba(237, 32, 36, 0.8);
  outline-offset: 3px;
}
```

### 10.4 Reduced Motion

**Respeto a preferencias de usuario:**

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }

  .vinyl-card:hover .vinyl-card__record {
    animation: none;  /* No rotación continua */
  }
}
```

### 10.5 ARIA Labels

**Dialog modal:**
```html
<dialog
  id="vinyl-clase-02"
  class="vinyl-modal"
  aria-labelledby="modal-title-02"
  aria-describedby="modal-synopsis-02"
>
  <h3 id="modal-title-02">Vibe Coding: IA que Programa</h3>
  <p id="modal-synopsis-02">La sesión estelar...</p>
</dialog>
```

**Botones de acción:**
```html
<button
  type="button"
  data-vinyl-open
  data-target="vinyl-clase-02"
  aria-label="Abrir detalle de Clase 02: Vibe Coding"
>
  Abrir pista
</button>
```

---

## 11. Deployment y Build

### 11.1 Build de Producción

```bash
# Instalar dependencias
npm install

# Build estático
npm run build

# Output generado en:
dist/
├── index.html
├── _astro/
│   ├── [hash].css
│   └── [hash].js
├── assets/
│   ├── hero/
│   ├── vinyls/
│   └── ...
└── clases/
    └── 2025-10-23-clase-02-ia-corporativa/
        └── index.html
```

### 11.2 GitHub Pages Deployment

**Workflow sugerido (.github/workflows/deploy.yml):**

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install dependencies
        run: npm ci

      - name: Build site
        run: npm run build
        env:
          SITE_URL: https://jzuluaga.github.io
          BASE_PATH: /docencia/materias/inteligencia-artificial-para-negocios/site

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./dist

  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to GitHub Pages
        uses: actions/deploy-pages@v4
```

### 11.3 Variables de Entorno

**Desarrollo local (.env):**
```bash
SITE_URL=http://localhost:4321
BASE_PATH=/
```

**Producción GitHub Pages:**
```bash
SITE_URL=https://jzuluaga.github.io
BASE_PATH=/docencia/materias/inteligencia-artificial-para-negocios/site
```

### 11.4 Configuración de Rutas

**astro.config.mjs ajustado:**

```javascript
export default defineConfig({
  site: "https://jzuluaga.github.io",
  base: "/docencia/materias/inteligencia-artificial-para-negocios/site",
  build: {
    assets: "relative"  // Crítico para subdirectorios
  }
});
```

### 11.5 Optimizaciones Pre-Build

**Compresión de imágenes:**
```bash
# WebP con calidad 85
cwebp -q 85 hero-lab-original.png -o hero-lab.webp

# Redimensionar para responsive
magick hero-lab.webp -resize 1920x hero-lab-desktop.webp
magick hero-lab.webp -resize 768x hero-lab-tablet.webp
```

**Compresión de videos:**
```bash
# WebM con VP9
ffmpeg -i hero-loop-original.mp4 \
  -c:v libvpx-vp9 -b:v 1M -crf 30 \
  -c:a libopus -b:a 128k \
  -vf scale=1280:720 \
  hero-loop.webm
```

---

## 12. Roadmap de Implementación

### 12.1 Estado Actual (2025-10-28)

✅ **Completado:**
- [x] Setup inicial Astro + TailwindCSS v4
- [x] Sistema de estilos globales (`global.css`)
- [x] Componente HeroOrbit con video de fondo
- [x] Componente VinylGrid con cards interactivas
- [x] Sistema de modal con dialog nativo
- [x] Data structure en TypeScript (`course.ts`)
- [x] Assets hero (imagen + video loop)
- [x] Placeholders de vinilos Clase 02 y 03
- [x] Componentes HighlightsBento, ToolkitChips, FAQAccordion
- [x] Página index completa con todas secciones

### 12.2 Fase 2 - Assets Finales (Próximos 7 días)

⏳ **En progreso:**
- [ ] Generar vinilos finales Clase 02 con IA (Midjourney/SDXL)
- [ ] Generar vinilos finales Clase 03
- [ ] Crear loops hover animados (rotación + glow)
- [ ] Spines finales con tipografía Rajdhani
- [ ] Banners de secciones (Metodología, Herramientas, Casos)
- [ ] Iconos SVG lineales de herramientas

### 12.3 Fase 3 - Contenido y Páginas (7-14 días)

⏳ **Pendiente:**
- [ ] Página `/docs/syllabus` completa
- [ ] Página detalle Clase 02 con markdown renderizado
- [ ] Integración de transcripción .vtt Clase 02
- [ ] Documentación Clase 01 (post-grabación)
- [ ] Brief creativo Clase 03

### 12.4 Fase 4 - Refinamiento UX (14-21 días)

⏳ **Pendiente:**
- [ ] Navegación teclado `←` `→` entre cards
- [ ] Smooth scroll con anchors animados
- [ ] Loading states para imágenes
- [ ] Error boundaries y fallbacks
- [ ] Búsqueda/filtrado de clases (futuro)

### 12.5 Fase 5 - Optimización y Launch (21-30 días)

⏳ **Pendiente:**
- [ ] Auditoría Lighthouse (target: 95+ en todas categorías)
- [ ] Lazy loading de imágenes y videos
- [ ] Service Worker para cache de assets
- [ ] Analytics integration (opcional)
- [ ] Workflow de GitHub Pages automatizado
- [ ] Testing cross-browser (Chrome, Safari, Firefox)
- [ ] Testing mobile (iOS Safari, Android Chrome)

---

## 📊 Métricas de Performance

### Objetivos Lighthouse

| Categoría | Target | Actual |
|-----------|--------|--------|
| Performance | 95+ | TBD |
| Accessibility | 100 | TBD |
| Best Practices | 100 | TBD |
| SEO | 100 | TBD |

### Bundle Size Targets

| Asset Type | Target | Actual |
|------------|--------|--------|
| HTML | <50KB | TBD |
| CSS | <100KB | TBD |
| JS | <50KB | TBD |
| Images | <3MB total | ~2MB |
| Video | <5MB | ~3MB |

---

## 🔧 Mantenimiento

### Agregar Nueva Clase

1. **Generar assets:**
   - Portada vinilo (1:1, webp)
   - Halo para modal (16:9, webp)
   - Spine (vertical, png)

2. **Actualizar `course.ts`:**
```typescript
export const classes: ClassEntry[] = [
  // ... clases existentes
  {
    slug: "clase-04-nuevo-tema",
    number: "04",
    title: "Título de la Nueva Clase",
    // ... resto de campos
  }
];
```

3. **Crear página de detalle (opcional):**
```
src/pages/clases/2025-11-XX-clase-04-nuevo-tema.astro
```

### Modificar Tema Visual

**Cambiar colores de marca:**
```css
/* global.css */
:root {
  --orbital-red: #ED2024;    /* Cambiar aquí */
  --orbital-cyan: #00BCD4;   /* Cambiar aquí */
}
```

**Ajustar tipografía:**
```css
/* global.css */
@import url("https://fonts.googleapis.com/css2?family=...");

.font-rajdhani {
  font-family: "NUEVA_FUENTE", sans-serif;
}
```

---

## 📚 Referencias

### Documentación Técnica

- [Astro Docs](https://docs.astro.build)
- [TailwindCSS v4 Beta](https://tailwindcss.com/docs)
- [MDN Web Docs - Dialog Element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog)
- [Web.dev - Glassmorphism](https://web.dev/glassmorphism)

### Inspiración Visual

- [Itempire Inspiration](../../docs/research/itempire_inspiration.md)
- [Orbital Brand Manifesto](../../docs/brand/manifesto.md)
- [Moodboard Orbital](../../docs/brand/assets/moodboard-orbital.png)

### Herramientas de Desarrollo

- [WebP Converter](https://developers.google.com/speed/webp)
- [FFmpeg Video Compression](https://ffmpeg.org)
- [SVGO Optimizer](https://github.com/svg/svgo)
- [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci)

---

## ✅ Checklist Final

**Pre-Launch:**

- [ ] Todos los assets finales generados y optimizados
- [ ] Lighthouse score 95+ en todas categorías
- [ ] Testing en Chrome, Safari, Firefox
- [ ] Testing mobile en iOS y Android
- [ ] GitHub Pages workflow funcionando
- [ ] README.md actualizado con instrucciones de build
- [ ] Documentación de componentes completa
- [ ] Contraste de colores verificado (WCAG AA)
- [ ] Navegación por teclado completa
- [ ] Error states manejados
- [ ] Loading states implementados
- [ ] Analytics configurado (opcional)

---

**Documento creado por:** Julián Zuluaga (Orbital Lab) + Claude (Anthropic)
**Última actualización:** 28 de octubre de 2025
**Versión:** 1.0 - Arquitectura Completa
**Contacto:** julian@orbitallab.co

---

> **Mantra Orbital:** *"¿Ayuda a ver y entender mejor la IA corporativa?"* Si la respuesta es sí, la experiencia está en órbita. ✨
