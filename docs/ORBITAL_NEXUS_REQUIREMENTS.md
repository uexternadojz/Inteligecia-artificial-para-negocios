# Orbital Nexus · Especificación de Requerimientos

**Versión**: 1.0
**Fecha**: 2025-10-28
**Autor**: Julián Zuluaga
**Estado**: Aprobado

---

## 1. Visión General

Orbital Nexus es el hub central que conecta toda la ecosistema de docencia, proyectos y recursos de Orbital Lab. Es un sistema de sitios web federados que permite gestionar múltiples cursos, clases y contenido educativo de forma escalable, desplegable completamente en GitHub Pages.

### 1.1 Objetivos Estratégicos

- **Centralización**: Un punto de entrada único para estudiantes, colaboradores y empleadores
- **Escalabilidad**: Agregar materias y clases sin reestructurar el sistema
- **Autonomía**: Cada materia puede evolucionar independientemente
- **Profesionalismo**: Experiencia visual premium inspirada en IT Empire
- **Accesibilidad**: Compatible con GitHub Pages gratuito

### 1.2 Inspiración Visual

Basado en análisis exhaustivo de [IT Empire](https://itempire.com/):
- Hero cinemático con video de fondo y parallax multi-capa
- Arquitectura de información por secciones fullscreen
- Microinteracciones sutiles (hover effects, scroll-triggered animations)
- Paleta negro profundo + rojo orbital (#ED2024)
- HUD elements y navegación contextual

---

## 2. Actores del Sistema

### 2.1 Estudiantes (Primario)
**Objetivos**:
- Explorar cursos disponibles por vertical (Deportes, Negocio, Biología, etc.)
- Acceder a clases individuales con guías interactivas
- Descargar recursos (datasets, notebooks, slides)
- Conocer proyectos reales de Orbital Lab

**Flujo típico**:
1. Llegar a Orbital Nexus (búsqueda/link directo)
2. Navegar por verticales o catálogo de materias
3. Entrar a materia específica (ej. Minería de Datos)
4. Acceder a clase específica
5. Descargar/ejecutar recursos

### 2.2 Julián Zuluaga (Profesor/Administrador)
**Objetivos**:
- Publicar nuevas materias rápidamente
- Actualizar contenido de clases existentes
- Mostrar proyectos profesionales (portfolio)
- Mantener identidad de marca Orbital Lab

**Flujo típico**:
1. Crear carpeta de materia en `materias/`
2. Escribir contenido en MDX
3. Commit + push → GitHub Actions deploy automático
4. Verificar en producción

### 2.3 Agentes CLI (Automatización)
**Objetivos**:
- Generar guías HTML desde templates
- Actualizar content collections
- Optimizar assets (imágenes, videos)
- Mantener documentación sincronizada

**Capacidades requeridas**:
- Leer `PROJECT_STATUS.md` para entender estado
- Escribir en `content/` folders
- Ejecutar scripts de build
- Actualizar metadatos

---

## 3. Requerimientos Funcionales

### RF-001: Hub Principal (Orbital Nexus)

#### RF-001.1 Hero Section
**Prioridad**: CRÍTICA
**Descripción**: Sección de entrada cinemática con identidad Orbital Lab

**Elementos obligatorios**:
- Video de fondo en loop (orbital-portal.mp4, 10-15s)
- Overlay de partículas (particles.mp4) con blend mode screen
- Glows rojos/cyan estratégicamente posicionados
- Logo Orbital Lab (SVG, responsive)
- Tagline "Ver es entender"
- CTA principal "Explorar Laboratorio"
- Indicador de scroll (animated)

**Comportamiento**:
- Parallax en video (speed: 0.5x scroll)
- Fade-in de elementos con stagger delay
- CTA hover: lift + glow effect
- Mobile: video reemplazado por poster estático

**Assets requeridos**:
- `assets/hero/orbital-portal.mp4` ✅
- `assets/hero/particles.mp4` ✅
- `assets/hero/glow-*.png` (5 variaciones) ✅
- `assets/brand/orbital-lab-logo.svg` ✅

#### RF-001.2 Lab Grid (5 Verticales)
**Prioridad**: CRÍTICA
**Descripción**: Grid de verticales de Orbital Lab con hover reveal

**Verticales permanentes**:
1. **Deportes**: Analítica deportiva con IA (ej. Strivio)
2. **Negocio**: Analítica de audiencias y marketing (ej. Lighthouse Audience)
3. **Biología**: Conservación ambiental con CV (ej. Jaguar Orbital)
4. **Otros**: Automatización corporativa (ej. AI Systems/Superagents)
5. **Academia**: Formación aplicada en IA (ej. Academia Orbital)

**Componentes por card**:
- Icono SVG vectorial con stroke rojo (#ED2024)
- Título de la vertical
- Descripción corta (1-2 líneas)
- Ejemplo de proyecto entre paréntesis
- Background illustration (1920x1080) que aparece en hover

**Comportamiento**:
- Hover: scale(1.02) + translateY(-8px)
- Background fade-in desde opacity:0
- Border glow animation
- Click: navegar a sección de proyectos filtrada

**Assets requeridos**:
- `assets/lab/icon-*.svg` (5 iconos) ✅
- `assets/lab/*-hero.png` (5 ilustraciones) ✅

#### RF-001.3 Catálogo de Materias
**Prioridad**: ALTA
**Descripción**: Listado de cursos activos con filtros

**Información por materia**:
- Título del curso
- Descripción corta
- Vertical asociada (badge con color)
- Semestre y créditos
- Estado (Activo, Próximo, Archivo)
- Thumbnail (imagen de portada)
- Link al sitio de la materia

**Filtros**:
- Por vertical (Deportes, Negocio, etc.)
- Por estado (Activo, Próximo, Archivo)
- Por semestre

**Source de datos**:
- Content collection `content/materias/*.json`
- Schema Zod con validación

#### RF-001.4 Showcase de Proyectos
**Prioridad**: MEDIA
**Descripción**: Gallery de proyectos profesionales (Strivio, Lighthouse, Jaguar)

**Información por proyecto**:
- Nombre y submarca
- Vertical asociada
- Descripción ejecutiva
- Tecnologías utilizadas (badges)
- Thumbnail/screenshot
- Link externo (opcional)
- Estado: Featured / Regular

**Layout**:
- Featured projects: cards grandes (1/2 ancho)
- Regular projects: cards pequeñas (1/3 ancho)
- Masonry grid responsive

**Source de datos**:
- Content collection `content/projects/*.mdx`
- Puede incluir contenido largo en MDX

#### RF-001.5 Bio Section
**Prioridad**: MEDIA
**Descripción**: Sección personal de Julián Zuluaga

**Elementos**:
- Portrait profesional (foto corporativa)
- Background futurista (cityscape nocturno)
- Texto bio (2-3 párrafos)
- Arquetipos: Creador + Sabio
- Links a redes (LinkedIn, GitHub, Email)
- CTA "Descargar CV" (opcional)

**Assets requeridos**:
- `assets/bio/portrait.jpg` ✅
- `assets/bio/background.jpg` ✅

#### RF-001.6 Contact Section
**Prioridad**: BAJA
**Descripción**: Footer con mapa de impacto y formulario

**Elementos**:
- Heatmap mundial con concentración en Bogotá/LatAm
- Ilustración de hangar/control room
- Email de contacto visible
- Formulario simple (Nombre, Email, Mensaje)
- Links a redes sociales
- Copyright y logo vertical

**Assets requeridos**:
- `assets/contact/heatmap.png` ✅
- `assets/contact/hangar.png` ✅

---

### RF-002: Sitio por Materia

#### RF-002.1 Home de Materia
**Prioridad**: CRÍTICA
**Descripción**: Landing page del curso específico

**Elementos obligatorios**:
- Header con logo Orbital Lab + breadcrumbs a Nexus
- Hero con título del curso + descripción
- Sección "¿Qué aprenderás?" (objetivos de aprendizaje)
- Timeline de clases con estado (completada, activa, próxima)
- Recursos descargables (datasets, templates, bibliografía)
- Información del profesor
- Footer con navegación a Nexus

**Metadatos**:
- Título
- Descripción
- Semestre/año
- Créditos
- Horario
- Modalidad (presencial/virtual/híbrida)
- Vertical asociada

#### RF-002.2 Listado de Clases
**Prioridad**: CRÍTICA
**Descripción**: Índice de todas las sesiones del curso

**Vista por clase**:
- Número de clase
- Título
- Fecha de realización
- Fase CRISP-DM asociada (si aplica)
- Estado visual (dot verde/amarillo/gris)
- Recursos disponibles (iconos: HTML, Notebook, Dataset, Slides)
- Link a página de clase

**Filtros**:
- Por fase CRISP-DM
- Por estado
- Por tags

**Ordenamiento**:
- Cronológico (default)
- Alfabético
- Por fase CRISP-DM

#### RF-002.3 Página de Clase Individual
**Prioridad**: ALTA
**Descripción**: Contenido de una sesión específica

**Secciones**:
- Header con breadcrumbs (Nexus > Materia > Clase)
- Metadata (fecha, fase, tags)
- Objetivos de aprendizaje
- Contenido principal (MDX renderizado)
- Recursos embebidos:
  - Iframe de guía HTML interactiva
  - Link a notebook en nbviewer/Colab
  - Botón de descarga de datasets
- Navegación anterior/siguiente clase
- Footer con link a Nexus

**Content collection schema**:
```typescript
{
  numero: number,
  title: string,
  fecha: Date,
  fase_crisp: enum,
  objetivos: string[],
  recursos: {
    guia_html: string (URL),
    notebook: string (path),
    datasets: string[] (paths),
    slides: string (URL)
  },
  tags: string[]
}
```

---

### RF-003: Guías HTML Standalone

#### RF-003.1 Integración en Build
**Prioridad**: ALTA
**Descripción**: Guías HTML generadas con OpenSpecs accesibles desde sitios

**Estrategia**:
1. Guías viven en `materias/<materia>/clases/<fecha-slug>/guia.html`
2. Script de build las copia a `dist/clases/<fecha-slug>/`
3. Son servidas como páginas estáticas autónomas
4. Embedibles vía iframe en páginas de clase

**URLs esperadas**:
- Standalone: `https://.../clases/2025-10-23-crisp-dm/index.html`
- Desde materia: `https://.../materias/mineria-de-datos/clases/crisp-dm/` (embebido)

#### RF-003.2 Componente Iframe Embedder
**Prioridad**: MEDIA
**Descripción**: Componente Astro para embeber guías HTML con UX mejorada

**Features**:
- Detección de altura automática del iframe
- Loading skeleton mientras carga
- Link "Abrir en pestaña nueva"
- Manejo de errores (404, timeout)

**Uso**:
```astro
<GuiaEmbed
  src="/clases/2025-10-23-crisp-dm/"
  title="Guía Interactiva CRISP-DM"
  fallbackUrl="https://..."
/>
```

---

### RF-004: Sistema de Build y Deploy

#### RF-004.1 Monorepo con Workspaces
**Prioridad**: CRÍTICA
**Descripción**: Estructura de carpetas escalable con dependencies compartidas

**Workspaces**:
```
├── apps/
│   ├── nexus/              (Orbital Nexus)
│   └── materias/
│       ├── mineria-de-datos/
│       └── ia-negocios/
├── packages/
│   ├── ui-components/      (Componentes Astro reutilizables)
│   └── orbital-theme/      (Tailwind config + tokens)
```

**Comandos npm**:
- `npm run dev:nexus` - Desarrollar Orbital Nexus
- `npm run dev:mineria` - Desarrollar materia específica
- `npm run build:all` - Compilar todo
- `npm run preview` - Preview producción local

#### RF-004.2 GitHub Actions Workflow
**Prioridad**: CRÍTICA
**Descripción**: Deploy automático a GitHub Pages en push a main

**Jobs**:
1. **Checkout** código
2. **Setup** Node.js 20
3. **Install** dependencies (npm install)
4. **Build Nexus** (apps/nexus → dist/)
5. **Build Materias** (loop sobre apps/materias/*/)
6. **Copy Static HTML** (guías standalone)
7. **Merge Builds** (estructura final en dist/)
8. **Deploy** a gh-pages branch

**Triggers**:
- Push a branch `main`
- Manual workflow dispatch
- Preview en PRs (opcional, fase 2)

#### RF-004.3 Merge de Builds
**Prioridad**: CRÍTICA
**Descripción**: Script que une todos los sites en estructura GitHub Pages

**Estructura final en `dist/`**:
```
dist/
├── index.html              (Nexus home)
├── materias/
│   ├── index.html          (catálogo)
│   ├── mineria-de-datos/
│   │   ├── index.html
│   │   └── clases/
│   └── ia-negocios/
│       ├── index.html
│       └── clases/
├── clases/                 (HTML standalone)
│   └── 2025-10-23-crisp-dm/
├── assets/                 (symlinked desde recursos_compartidos)
└── _astro/                 (chunks JS/CSS)
```

**Script bash**:
```bash
#!/bin/bash
# herramientas/build-all.sh

# Build Nexus
cd apps/nexus
npm run build
cd ../..

# Build each materia
for materia in apps/materias/*; do
  cd $materia
  SITE_URL="https://<user>.github.io/externado-docencia" \
  BASE_PATH="/materias/$(basename $materia)" \
  npm run build
  cd ../../..
done

# Merge builds
mkdir -p dist
cp -r apps/nexus/dist/* dist/
mkdir -p dist/materias
for materia in apps/materias/*/dist; do
  name=$(basename $(dirname $materia))
  cp -r $materia dist/materias/$name
done

# Copy standalone HTML classes
mkdir -p dist/clases
find materias/*/clases -name "*.html" -exec cp {} dist/clases/ \;
```

---

## 4. Requerimientos No Funcionales

### RNF-001: Performance

**Objetivo**: Experiencia rápida incluso con videos y animaciones

**Métricas Core Web Vitals**:
- **LCP** (Largest Contentful Paint): ≤ 2.5s
  - Hero video optimizado (H.264, 5-8 Mbps, 1920x1080)
  - Poster estático como fallback en mobile
  - Preload critical assets

- **FID/INP** (First Input Delay / Interaction to Next Paint): ≤ 200ms
  - JavaScript total bundle ≤ 150KB (inicial)
  - Code splitting por ruta
  - Lazy load Framer Motion islands

- **CLS** (Cumulative Layout Shift): ≤ 0.1
  - Aspect ratio boxes en imágenes/videos
  - Reservar espacio para web fonts
  - No ads ni contenido dinámico en ATF

**Optimizaciones de assets**:
- Imágenes: WebP/AVIF con fallback PNG/JPG
- Videos: MP4 con múltiples resoluciones (1080p desktop, 720p mobile)
- Fonts: WOFF2 con preload, font-display: swap
- SVGs: Inline críticos, lazy-load decorativos

**Estrategia de carga**:
```html
<!-- Critical CSS inline -->
<style>/* Tailwind base + hero styles */</style>

<!-- Preload hero video -->
<link rel="preload" as="video" href="/assets/hero/orbital-portal.mp4">

<!-- Async non-critical -->
<script type="module" src="/client.js" defer></script>
```

### RNF-002: Accesibilidad (WCAG 2.1 AA)

**Contraste**:
- Texto sobre negro: blanco puro (#FFFFFF)
- Texto sobre rojo: blanco (ratio 4.5:1 mínimo)
- Links: subrayado en hover + cambio de color
- Estados focus: outline visible (no outline:none sin alternativa)

**Navegación por teclado**:
- Tab order lógico (hero CTA → nav → content)
- Skip links ("Saltar a contenido principal")
- Modals/overlays: trap focus + ESC para cerrar
- No hover-only interactions (siempre alternativa en click/focus)

**Screen readers**:
- Landmarks semánticos (`<header>`, `<nav>`, `<main>`, `<footer>`)
- Alt text descriptivo en imágenes (no "imagen" o "foto")
- ARIA labels en iconos interactivos
- Video: subtítulos/transcripciones (opcional fase 2)

**Reduced motion**:
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

### RNF-003: SEO

**Meta tags por página**:
```html
<title>Orbital Nexus · Inteligencia Artificial Aplicada</title>
<meta name="description" content="Hub de IA aplicada: docencia, proyectos y recursos. Deportes, negocio, biología y automatización corporativa.">
<meta name="keywords" content="IA, Machine Learning, Docencia, CRISP-DM, Computer Vision">
```

**OpenGraph para redes sociales**:
```html
<meta property="og:title" content="Orbital Nexus">
<meta property="og:description" content="Ver es entender">
<meta property="og:image" content="https://.../og-image.png">
<meta property="og:type" content="website">
```

**Sitemap automático**:
- Astro genera `sitemap.xml` con todas las rutas
- Incluir prioridad (Nexus: 1.0, Materias: 0.8, Clases: 0.6)
- Actualización automática en cada build

**URLs semánticas**:
- ✅ `/materias/mineria-de-datos/`
- ✅ `/materias/mineria-de-datos/clases/crisp-dm-fases-1-2/`
- ❌ `/mat/md/c/1/` (no usar slugs cortos crípticos)

**Structured data (JSON-LD)**:
```json
{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "Minería de Datos",
  "description": "...",
  "provider": {
    "@type": "Person",
    "name": "Julián Zuluaga"
  }
}
```

### RNF-004: Escalabilidad

**Sin límite de materias/clases**:
- Basado en filesystem (no DB)
- Content collections escalan a 1000s de archivos
- Build incremental (solo cambios reconstruyen)

**Agregar materia nueva**:
```bash
# 1. Crear carpeta
mkdir -p apps/materias/nueva-materia

# 2. Copiar template
cp -r templates/materia/* apps/materias/nueva-materia/

# 3. Editar config
vim apps/materias/nueva-materia/src/config.ts

# 4. Crear content
mkdir -p apps/materias/nueva-materia/src/content/clases

# 5. Deploy
git add . && git commit -m "feat: add nueva-materia" && git push
```

**Agregar clase nueva**:
```bash
# 1. Crear MDX
touch apps/materias/mineria-de-datos/src/content/clases/2025-11-15-regresion-lineal.mdx

# 2. Agregar frontmatter
---
numero: 10
title: "Regresión Lineal Simple"
fecha: 2025-11-15
fase_crisp: "modelado"
---

# 3. Deploy automático
git add . && git commit -m "docs: add clase 10 regresion" && git push
```

**Performance con escala**:
- Build time: ~3-5 min para 10 materias con 50 clases cada una
- Puede paralelizar builds con GitHub Actions matrix
- Cache de node_modules y .astro para acelerar

### RNF-005: Mantenibilidad

**Código compartido**:
- Componentes en `packages/ui-components/`
- Estilos en `packages/orbital-theme/`
- No duplicar código entre sites

**Documentación técnica**:
- JSDoc en componentes complejos
- README en cada workspace
- ADRs (Architecture Decision Records) en `docs/decisions/`

**Testing (fase 2)**:
- Unit tests: Vitest para utils
- Component tests: Playwright para flujos críticos
- Visual regression: Percy o Chromatic (opcional)

**Versionamiento**:
- Semantic versioning en package.json
- Changelog automático con conventional commits
- Tags de release en GitHub

---

## 5. Arquitectura Técnica

### 5.1 Stack Tecnológico

**Framework**: Astro 5.x
- SSG (Static Site Generation)
- MPA (Multi-Page Application) nativo
- Island architecture (React solo en componentes interactivos)
- Content Collections API
- Zero JS by default

**Styling**: Tailwind CSS 4.x
- Shared config en `packages/orbital-theme/`
- Tokens de diseño desde Design Book
- Custom plugins para animaciones

**Animaciones**: Framer Motion
- Solo en islands (componentes con `client:load`)
- Scroll-triggered animations
- Parallax effects
- Hover states complejos

**Monorepo**: npm workspaces
- Nativo en Node.js 16+
- Sin overhead de Turborepo (puede migrar después)
- Shared dependencies automáticas

**Deploy**: GitHub Pages
- Gratuito para repos públicos
- HTTPS automático
- CDN global de GitHub
- Custom domain soportado

### 5.2 Estructura de Directorios

```
externado/docencia/
├── .github/
│   └── workflows/
│       └── deploy.yml          (GitHub Actions)
│
├── apps/
│   ├── nexus/                  (Orbital Nexus - Hub principal)
│   │   ├── src/
│   │   │   ├── pages/
│   │   │   │   ├── index.astro         (home con hero)
│   │   │   │   ├── materias/
│   │   │   │   │   └── index.astro     (catálogo)
│   │   │   │   ├── about.astro         (bio section como página)
│   │   │   │   └── contact.astro       (contacto standalone)
│   │   │   ├── components/
│   │   │   │   ├── HeroSection.astro
│   │   │   │   ├── LabGrid.astro
│   │   │   │   ├── VerticalCard.astro
│   │   │   │   ├── ProjectShowcase.astro
│   │   │   │   └── GlobalNav.astro
│   │   │   ├── content/
│   │   │   │   ├── config.ts           (Zod schemas)
│   │   │   │   ├── materias/
│   │   │   │   │   ├── mineria-de-datos.json
│   │   │   │   │   └── ia-negocios.json
│   │   │   │   └── projects/
│   │   │   │       ├── strivio.mdx
│   │   │   │       ├── lighthouse.mdx
│   │   │   │       └── jaguar.mdx
│   │   │   ├── layouts/
│   │   │   │   └── BaseLayout.astro
│   │   │   └── styles/
│   │   │       └── global.css
│   │   ├── public/
│   │   │   └── assets/         (symlink a recursos_compartidos)
│   │   ├── astro.config.mjs
│   │   ├── tailwind.config.js
│   │   └── package.json
│   │
│   └── materias/
│       ├── mineria-de-datos/
│       │   ├── src/
│       │   │   ├── pages/
│       │   │   │   ├── index.astro
│       │   │   │   ├── syllabus.astro
│       │   │   │   └── clases/
│       │   │   │       └── [slug].astro
│       │   │   ├── content/
│       │   │   │   ├── config.ts
│       │   │   │   └── clases/
│       │   │   │       ├── 2025-10-23-crisp-dm-fases-1-2.mdx
│       │   │   │       └── 2025-10-28-preparacion-datos.mdx
│       │   │   └── components/
│       │   │       └── ClaseCard.astro
│       │   ├── astro.config.mjs
│       │   └── package.json
│       │
│       └── ia-negocios/         (ya existe, migrar)
│
├── packages/
│   ├── ui-components/           (Componentes reutilizables)
│   │   ├── src/
│   │   │   ├── GlobalNav.astro
│   │   │   ├── Footer.astro
│   │   │   ├── GuiaEmbed.astro
│   │   │   └── Breadcrumbs.astro
│   │   └── package.json
│   │
│   └── orbital-theme/           (Tailwind + tokens)
│       ├── index.js             (export tailwind config)
│       ├── tokens.json          (colores, fonts, spacing)
│       └── package.json
│
├── materias/                    (contenido legacy, mantener)
│   ├── mineria-de-datos/
│   │   └── clases/
│   │       └── */guia.html      (HTML standalone)
│   └── inteligencia-artificial-para-negocios/
│
├── recursos_compartidos/        (mantener estructura actual)
│   └── componentes/orbital_lab/assets/
│
├── herramientas/
│   ├── build-all.sh             (script de build monorepo)
│   └── merge-builds.sh          (unir dist/ folders)
│
├── docs/
│   ├── ORBITAL_NEXUS_REQUIREMENTS.md  (este documento)
│   ├── PROJECT_STATUS.md
│   └── CONTRIBUTING.md
│
├── package.json                 (root, workspaces config)
├── README.md
└── ARCHITECTURE.md
```

### 5.3 Content Collections Schemas

#### Nexus: Materias
```typescript
// apps/nexus/src/content/config.ts
import { defineCollection, z } from 'astro:content';

const materiasCollection = defineCollection({
  type: 'data',
  schema: z.object({
    title: z.string(),
    slug: z.string(),
    profesor: z.string(),
    descripcion: z.string(),
    vertical: z.enum(['deportes', 'negocio', 'biologia', 'otros', 'academia']),
    semestre: z.string(),             // "2025-1"
    creditos: z.number(),
    modalidad: z.enum(['presencial', 'virtual', 'hibrida']),
    siteUrl: z.string().url().optional(),
    thumbnail: z.string(),            // path relativo a /assets/
    tags: z.array(z.string()),
    estado: z.enum(['activo', 'proximo', 'archivo']),
    horario: z.string().optional(),   // "Martes 8-10am"
  }),
});

const projectsCollection = defineCollection({
  type: 'content',                     // permite MDX
  schema: z.object({
    title: z.string(),
    vertical: z.enum(['deportes', 'negocio', 'biologia', 'otros', 'academia']),
    submarca: z.enum(['strivio', 'lighthouse', 'jaguar', 'ai-systems', 'academia-orbital']),
    descripcion: z.string(),
    thumbnail: z.string(),
    featured: z.boolean().default(false),
    tecnologias: z.array(z.string()),
    link: z.string().url().optional(),
    github: z.string().url().optional(),
    fecha: z.date().optional(),
  }),
});

export const collections = {
  'materias': materiasCollection,
  'projects': projectsCollection,
};
```

#### Materia Individual: Clases
```typescript
// apps/materias/mineria-de-datos/src/content/config.ts
import { defineCollection, z } from 'astro:content';

const clasesCollection = defineCollection({
  type: 'content',                     // MDX
  schema: z.object({
    numero: z.number(),
    title: z.string(),
    fecha: z.date(),
    fase_crisp: z.enum([
      'entendimiento-negocio',
      'entendimiento-datos',
      'preparacion',
      'modelado',
      'evaluacion',
      'despliegue'
    ]).optional(),
    objetivos: z.array(z.string()),
    recursos: z.object({
      guia_html: z.string().url().optional(),
      notebook: z.string().optional(),
      datasets: z.array(z.string()).optional(),
      slides: z.string().url().optional(),
    }),
    tags: z.array(z.string()),
    estado: z.enum(['completada', 'activa', 'proxima']).default('proxima'),
  }),
});

export const collections = {
  'clases': clasesCollection,
};
```

### 5.4 Sistema de Navegación Global

**Componente shared**: `packages/ui-components/src/GlobalNav.astro`

```astro
---
interface Props {
  currentSite: 'nexus' | 'materia';
  materiaSlug?: string;
  materiaTitle?: string;
}

const { currentSite, materiaSlug, materiaTitle } = Astro.props;

// Detectar BASE_URL del entorno
const isProduction = import.meta.env.PROD;
const nexusUrl = isProduction
  ? 'https://<user>.github.io/externado-docencia/'
  : '/';

const materiaUrl = materiaSlug
  ? `${nexusUrl}materias/${materiaSlug}/`
  : null;
---

<nav class="fixed top-0 w-full bg-black/90 backdrop-blur-sm z-50 border-b border-white/10">
  <div class="container mx-auto px-6 py-4 flex items-center justify-between">
    <!-- Logo (always links to Nexus) -->
    <a href={nexusUrl} class="flex items-center gap-3">
      <img src="/assets/brand/logo-orbital.svg" alt="Orbital Lab" class="h-10" />
      {currentSite === 'materia' && (
        <span class="text-white/60 text-sm">/ {materiaTitle}</span>
      )}
    </a>

    <!-- Main Nav -->
    <div class="flex items-center gap-6">
      <a href={`${nexusUrl}materias/`} class="text-white/80 hover:text-white">
        Cursos
      </a>
      <a href={`${nexusUrl}about/`} class="text-white/80 hover:text-white">
        Acerca
      </a>

      {currentSite === 'materia' && materiaUrl && (
        <a href={materiaUrl} class="px-4 py-2 border border-red-600 text-red-600 hover:bg-red-600 hover:text-white rounded">
          Inicio del Curso
        </a>
      )}
    </div>
  </div>
</nav>
```

**Uso**:
```astro
<!-- En Orbital Nexus -->
<GlobalNav currentSite="nexus" />

<!-- En Materia -->
<GlobalNav
  currentSite="materia"
  materiaSlug="mineria-de-datos"
  materiaTitle="Minería de Datos"
/>
```

---

## 6. Fases de Implementación

### Fase 1: Fundamentos (Semana 1)
**Objetivo**: Infraestructura base funcional

**Tareas**:
1. ✅ Crear documentación (REQUIREMENTS, STATUS, CONTRIBUTING)
2. ✅ Actualizar READMEs globales
3. [ ] Inicializar monorepo:
   - `package.json` root con workspaces
   - Crear `apps/nexus/` con Astro
   - Crear `packages/ui-components/`
   - Crear `packages/orbital-theme/`
4. [ ] Setup Tailwind theme:
   - Tokens de diseño desde Design Book
   - Configuración compartida
5. [ ] Implementar componentes base:
   - GlobalNav
   - Footer
   - BaseLayout
6. [ ] Setup GitHub Actions:
   - Workflow básico de build + deploy

**Entregable**: Orbital Nexus con hero estático y navegación

---

### Fase 2: Orbital Nexus MVP (Semana 2)
**Objetivo**: Hub principal con estética IT Empire

**Tareas**:
1. [ ] HeroSection component:
   - Video background con parallax
   - Particles overlay
   - Glows estratégicos
   - CTA animado
2. [ ] LabGrid component:
   - 5 cards de verticales
   - Hover reveal de backgrounds
   - Animaciones Framer Motion
3. [ ] Content collections:
   - Materias (JSON data)
   - Projects (MDX)
4. [ ] Página Materias:
   - Catálogo con filtros
   - Cards responsive
5. [ ] Bio section:
   - Portrait + background
   - Texto bio + links
6. [ ] Contact section:
   - Heatmap + hangar
   - Formulario simple

**Entregable**: Orbital Nexus completo y deployado

---

### Fase 3: Integración de Materias (Semana 3)
**Objetivo**: Sitios de materias funcionales

**Tareas**:
1. [ ] Template de materia:
   - Estructura de carpetas
   - astro.config.mjs con base path
   - Content collections setup
2. [ ] Migrar IA-Negocios:
   - Mover de `materias/ia-negocios/site/` a `apps/materias/ia-negocios/`
   - Adaptar config para GitHub Pages
   - Integrar GlobalNav compartido
3. [ ] Crear Minería de Datos site:
   - Aplicar template
   - Importar clases existentes como MDX
   - Linkear guías HTML standalone
4. [ ] Componente GuiaEmbed:
   - Iframe con auto-height
   - Loading state
   - Error handling
5. [ ] Sistema de build unificado:
   - Script `build-all.sh`
   - Merge de dist/ folders

**Entregable**: 2 materias deployadas con ≥5 clases cada una

---

### Fase 4: Polish y Optimización (Semana 4)
**Objetivo**: Experiencia premium

**Tareas**:
1. [ ] Animaciones avanzadas:
   - Scroll-triggered fade-ins
   - Parallax multi-capa en hero
   - Smooth scroll navigation
2. [ ] Mobile responsive:
   - Hero con poster en mobile
   - LabGrid en 1 columna
   - Navigation drawer
3. [ ] Performance optimization:
   - Lazy-load images
   - Code splitting
   - Preload critical assets
4. [ ] SEO:
   - Meta tags dinámicos
   - Sitemap.xml
   - OpenGraph images
5. [ ] Accessibility:
   - Keyboard navigation
   - Screen reader testing
   - Color contrast validation
6. [ ] Testing:
   - Manual QA en Chrome, Firefox, Safari
   - Mobile testing (iOS, Android)
   - Lighthouse audit (score ≥90)

**Entregable**: Sitio production-ready con calidad profesional

---

## 7. Criterios de Éxito

### Métricas Técnicas
- [ ] Orbital Nexus accesible en `https://<user>.github.io/externado-docencia/`
- [ ] Materias accesibles en `/materias/<slug>/`
- [ ] Guías HTML standalone en `/clases/<slug>/`
- [ ] Build time total ≤ 5 minutos
- [ ] Lighthouse Performance score ≥ 90
- [ ] Lighthouse Accessibility score ≥ 95
- [ ] Lighthouse SEO score ≥ 95
- [ ] Zero console errors en producción

### Métricas de Contenido
- [ ] ≥2 materias desplegadas
- [ ] ≥10 clases con contenido MDX
- [ ] ≥5 proyectos en showcase
- [ ] Bio completa con links a redes
- [ ] Formulario de contacto funcional

### Métricas de UX
- [ ] Navegación intuitiva (testeada con 3+ usuarios)
- [ ] Tiempo de carga percibido ≤ 3s
- [ ] Mobile responsive validado en ≥3 dispositivos
- [ ] Hover effects funcionan en todos los browsers
- [ ] No hay layouts rotos en viewport 320px-2560px

---

## 8. Riesgos y Mitigaciones

### Riesgo 1: GitHub Pages no sirve correctamente los sub-paths
**Probabilidad**: BAJA
**Impacto**: ALTO
**Mitigación**:
- Probar deploy en repo de prueba antes de producción
- Usar `base` config en Astro (ya probado en IA-Negocios)
- Alternativa: Vercel/Netlify (gratis para proyectos personales)

### Riesgo 2: Build time excede 10 minutos (límite GitHub Actions)
**Probabilidad**: MEDIA (con 10+ materias)
**Impacto**: MEDIO
**Mitigación**:
- Cache de node_modules y .astro builds
- Build incremental (detectar cambios por materia)
- Split workflow: Nexus + Materias en jobs paralelos

### Riesgo 3: Videos de hero causan LCP alto (>4s)
**Probabilidad**: MEDIA
**Impacto**: ALTO
**Mitigación**:
- Comprimir video a 5 Mbps (actualmente 8 Mbps)
- Preload del video
- Usar poster estático en mobile
- Lazy-load particles.mp4 (no crítico)

### Riesgo 4: Complejidad de mantener múltiples sites
**Probabilidad**: BAJA
**Impacto**: MEDIO
**Mitigación**:
- Componentes compartidos en packages/
- Template claro para nuevas materias
- Scripts automatizados de build
- Documentación exhaustiva (CONTRIBUTING.md)

---

## 9. Decisiones Técnicas Clave

### Decisión 1: Astro vs Next.js
**Elegido**: Astro
**Razones**:
- SSG nativo (Next.js requiere `output: 'export'`)
- Zero JS by default (mejor performance)
- MPA más simple para contenido educativo
- Content Collections API superior para markdown
- Mejor para GitHub Pages (sin config adicional)

### Decisión 2: npm workspaces vs Turborepo
**Elegido**: npm workspaces
**Razones**:
- Sin overhead adicional (nativo Node.js)
- Suficiente para 2-5 sites
- Puede migrar a Turborepo después si escala
- Menos curva de aprendizaje

### Decisión 3: Monorepo vs Multi-repo
**Elegido**: Monorepo
**Razones**:
- Compartir componentes fácilmente
- Deploy atómico (todo o nada)
- Versionamiento sincronizado
- Single source of truth para assets

### Decisión 4: MDX vs JSON para contenido de clases
**Elegido**: MDX
**Razones**:
- Permite embeber componentes React/Astro
- Mejor DX para contenido largo
- Syntax highlighting nativo
- Frontmatter para metadata estructurada

---

## 10. Referencias

### Documentos Relacionados
- `PROJECT_STATUS.md` - Estado actual del proyecto
- `CONTRIBUTING.md` - Guía para agregar contenido
- `docs/brand/manifesto.md` - Identidad de marca Orbital Lab
- `docs/research/itempire_inspiration.md` - Análisis de IT Empire
- `docs/brand/assets-checklist.md` - Inventario de assets

### Recursos Técnicos
- [Astro Docs](https://docs.astro.build/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Framer Motion](https://www.framer.com/motion/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [GitHub Pages](https://docs.github.com/en/pages)

### Inspiración Visual
- [IT Empire](https://itempire.com/) - Análisis completo en `docs/research/`
- Orbital Lab Design Book (PDF)

---

**Fin del documento**
