# Orbital Nexus - Hub Principal

Este directorio albergará el sitio web principal del ecosistema **Orbital Nexus**, un hub cinemático que conecta docencia, proyectos y recursos bajo la identidad visual de Orbital Lab.

---

## 🎯 Visión

**Orbital Nexus** es el punto de entrada a todo el ecosistema de docencia e investigación aplicada:

- **Hub central**: Página principal con hero cinemático, navegación a materias, proyectos destacados y perfil profesional
- **Sistema federado**: Conecta múltiples sites de materias independientes
- **Estética cinematic-tech**: Inspirado en IT Empire (video backgrounds, parallax, HUD elements, animaciones fluidas)
- **Deployable**: GitHub Pages con CI/CD automático

---

## 🏗️ Arquitectura Actual

```
site/                          # ← ESTÁS AQUÍ (pendiente de migración)
└── README.md

apps/nexus/                    # ← NUEVA UBICACIÓN (por crear)
├── src/
│   ├── pages/
│   │   └── index.astro       # Hero + LabGrid + Catálogo + Showcase + Bio + Contact
│   ├── layouts/
│   │   └── MainLayout.astro
│   ├── components/
│   │   ├── Hero.astro        # Video orbital + particles.js
│   │   ├── LabGrid.astro     # Grid 5 verticales con hover effects
│   │   ├── MateriaCatalog.astro
│   │   ├── ProjectShowcase.astro
│   │   ├── BioSection.astro
│   │   └── ContactSection.astro
│   └── content/
│       ├── materias/         # Data: catálogo de materias
│       ├── proyectos/        # Data: showcase proyectos
│       └── config.ts         # Schemas Zod
├── public/
│   └── assets/               # Symlink a recursos_compartidos/componentes/orbital_lab/assets
└── astro.config.ts           # BASE_PATH: '/' (root de GitHub Pages)
```

**Estado**: 🚧 Pendiente de inicialización del monorepo

---

## 📐 Stack Tecnológico

### Core
- **Astro 5.x**: SSG (Static Site Generation), Island Architecture
- **Tailwind CSS 4.x**: Utility-first con tokens de Orbital Lab
- **TypeScript**: Type-safe content y componentes

### Animaciones & Interactividad
- **Framer Motion**: Parallax scrolling, scroll-triggered animations
- **particles.js**: Efecto de partículas en Hero
- **Video backgrounds**: MP4 optimizados con lazy loading

### Content Management
- **Astro Content Collections**: Filesystem-based con Zod schemas
- **MDX**: Para páginas con contenido interactivo embebido

### Deploy
- **GitHub Actions**: Build automático en push a `main`
- **GitHub Pages**: Hosting estático gratuito

---

## 🎨 Secciones Principales

### 1. Hero Cinemático
**Inspiración**: IT Empire hero section
**Elementos**:
- Video de fondo: `orbital-motion-bg.mp4` (10s loop)
- Overlay con partículas orbitales (particles.js)
- Logo + tagline: "Ver es Entender"
- CTA: "Explorar Lab"

**Assets**:
- Video: `recursos_compartidos/componentes/orbital_lab/assets/hero/orbital-motion-bg.mp4`
- Partículas: `orbital-particles-overlay.mp4`
- Glows: `red-glow.png`, `cyan-glow.png`

---

### 2. Lab Grid (5 Verticales)
**Concepto**: Grid interactivo con las 5 áreas de trabajo

**Verticales**:
1. **Deportes (Strivio)** - Sports analytics
2. **Negocio (Lighthouse)** - Marketing OOH
3. **Biología (Jaguar)** - Conservación ambiental
4. **Otros (AI Systems)** - Automatización corporativa
5. **Academia (Orbital Academia)** - Educación aplicada

**Interacción**:
- Hover: Overlay con descripción + CTA
- Click: Navega a página de vertical con proyectos relacionados

**Assets por vertical**: Icon, ilustración hero, 2 proyectos ilustrados

---

### 3. Catálogo de Materias
**Data source**: `apps/nexus/src/content/materias/*.json`

**Card de Materia**:
```typescript
{
  title: "Minería de Datos",
  slug: "mineria-de-datos",
  vertical: "academia",
  descripcion: "...",
  semestre: "2025-1",
  creditos: 3,
  thumbnail: "/assets/materias/mineria-de-datos.jpg",
  siteUrl: "/materias/mineria-de-datos",
  estado: "activo" | "proximo" | "archivo"
}
```

**Layout**: Grid responsive con filtros por vertical y estado

---

### 4. Project Showcase
**Destacados**: Strivio, Lighthouse Audience, Jaguar Orbital

**Card de Proyecto**:
- Thumbnail/video
- Título + descripción corta
- Tags (tecnologías)
- CTA: "Ver Demo" / "Leer Caso"

---

### 5. Bio Section
**Contenido**:
- Foto profesional
- Bio corta (150 palabras)
- Keywords: IA, Computer Vision, Sports Analytics
- Links: LinkedIn, GitHub, Orbital Lab

**Asset**: `recursos_compartidos/componentes/orbital_lab/assets/bio/profile-photo.jpg`

---

### 6. Contact Section
**Elementos**:
- Email: julian@orbitallab.co
- Formulario de contacto (Formspree o similar)
- Social links

**Asset**: `contact-background-abstract.mp4`

---

## 🚀 Próximos Pasos

### Fase 1: Setup (PRÓXIMO)
1. Inicializar monorepo con npm workspaces
2. Crear `apps/nexus/` con Astro CLI
3. Setup `packages/orbital-theme/` con tokens
4. Setup `packages/ui-components/` con componentes base
5. Configurar Tailwind con tema de Orbital Lab

### Fase 2: Implementación Hero + Lab Grid
1. Hero con video background + parallax
2. LabGrid con 5 verticales (hover states)
3. Global navigation (sticky header)
4. Footer con links

### Fase 3: Catálogo + Showcase
1. Content Collections para materias y proyectos
2. Cards con thumbnails e información
3. Filtros y búsqueda básica
4. Animaciones de entrada (scroll-triggered)

### Fase 4: Bio + Contact
1. Bio section con foto y links
2. Contact form funcional
3. Social links (LinkedIn, GitHub)

### Fase 5: Deploy
1. GitHub Actions workflow
2. Build script para merge de dist/
3. Deploy a GitHub Pages
4. Testing E2E (Playwright)

---

## 📖 Documentación de Referencia

- **Requerimientos completos**: [ORBITAL_NEXUS_REQUIREMENTS.md](../docs/ORBITAL_NEXUS_REQUIREMENTS.md)
- **Estado del proyecto**: [PROJECT_STATUS.md](../docs/PROJECT_STATUS.md)
- **Arquitectura técnica**: [ARCHITECTURE.md](../ARCHITECTURE.md)
- **Guía de contribución**: [CONTRIBUTING.md](../docs/CONTRIBUTING.md)
- **Manifiesto de marca**: [manifesto.md](../docs/brand/manifesto.md)
- **Inspiración de diseño**: [itempire_inspiration.md](../docs/research/itempire_inspiration.md)

---

## 💡 Notas de Implementación

### Assets
- Todos los assets visuales (46 archivos) ya están generados en `recursos_compartidos/componentes/orbital_lab/assets/`
- Usar symlinks desde `apps/nexus/public/assets/` para evitar duplicación

### Performance
- Videos optimizados (< 2MB, 10s loops)
- Lazy loading para videos below-the-fold
- Preload para Hero video
- Image optimization vía Astro Image

### Accesibilidad
- Alt text descriptivo para todas las imágenes
- Contraste WCAG AA mínimo
- Keyboard navigation funcional
- Skip links para navegación rápida

### SEO
- Meta tags completos (title, description, OG)
- Sitemap.xml generado automáticamente
- robots.txt configurado
- Structured data (JSON-LD) para perfil profesional

---

**Última actualización**: 2025-10-28
**Responsable**: Julián Zuluaga
**Estado**: 📋 Documentación completa - Listo para inicializar monorepo
