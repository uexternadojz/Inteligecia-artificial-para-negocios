# Guía de Contribución · Orbital Nexus

**Versión**: 1.0
**Fecha**: 2025-10-28

Bienvenido al repositorio de Orbital Nexus. Esta guía te ayudará a contribuir contenido académico, assets visuales o mejoras técnicas al proyecto.

---

## 📋 Tabla de Contenidos

1. [Primeros Pasos](#1-primeros-pasos)
2. [Cómo Agregar una Nueva Materia](#2-cómo-agregar-una-nueva-materia)
3. [Cómo Agregar una Nueva Clase](#3-cómo-agregar-una-nueva-clase)
4. [Cómo Agregar un Proyecto al Showcase](#4-cómo-agregar-un-proyecto-al-showcase)
5. [Guía de Estilo](#5-guía-de-estilo)
6. [Workflow de Git](#6-workflow-de-git)
7. [Testing y Validación](#7-testing-y-validación)
8. [FAQ](#8-faq)

---

## 1. Primeros Pasos

### 1.1 Requisitos Previos

**Software necesario**:
- Node.js ≥20.0.0
- npm ≥10.0.0
- Git ≥2.40.0
- VS Code (recomendado) con extensiones:
  - Astro
  - Tailwind CSS IntelliSense
  - Prettier - Code formatter

**Conocimientos recomendados**:
- Markdown / MDX básico
- Git básico (clone, commit, push, pull)
- Opcional: Astro, React (para componentes custom)

### 1.2 Clonar el Repositorio

```bash
# Clonar
git clone https://github.com/<user>/externado-docencia.git
cd externado-docencia

# Instalar dependencies (cuando el monorepo esté inicializado)
npm install

# Verificar estructura
ls -la
```

### 1.3 Leer Documentación Clave

**Antes de contribuir, lee**:
1. `docs/PROJECT_STATUS.md` - Entender estado actual
2. `docs/ORBITAL_NEXUS_REQUIREMENTS.md` - Comprender arquitectura
3. `docs/brand/manifesto.md` - Identidad visual
4. `docs/brand/VERTICALES_REFERENCE.md` - Nomenclatura crítica

**Tiempo de lectura**: ~20 minutos

---

## 2. Cómo Agregar una Nueva Materia

### 2.1 Crear Estructura Base

```bash
# Usar el template (cuando esté disponible)
npm run create:materia -- --name "nueva-materia"

# O manualmente:
mkdir -p apps/materias/nueva-materia
cp -r templates/materia/* apps/materias/nueva-materia/
```

### 2.2 Configurar Metadatos

**Archivo**: `apps/materias/nueva-materia/src/config.ts`

```typescript
export const materiaConfig = {
  slug: 'nueva-materia',
  title: 'Título del Curso',
  descripcion: 'Descripción breve (1-2 líneas)',
  profesor: 'Julián Zuluaga',
  vertical: 'academia', // deportes | negocio | biologia | otros | academia
  semestre: '2025-2',
  creditos: 3,
  modalidad: 'presencial', // presencial | virtual | hibrida
  horario: 'Lunes y Miércoles 8-10am',
  tags: ['Python', 'Data Science', 'ML'],
};
```

### 2.3 Configurar Astro

**Archivo**: `apps/materias/nueva-materia/astro.config.mjs`

```javascript
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

const site = process.env.SITE_URL || 'https://example.com';
const base = process.env.BASE_PATH || '/materias/nueva-materia';

export default defineConfig({
  site,
  base,
  build: {
    assets: 'relative',
  },
  vite: {
    plugins: [tailwindcss()],
  },
});
```

### 2.4 Crear Contenido Inicial

**Home de la materia**: `apps/materias/nueva-materia/src/pages/index.astro`

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
import { materiaConfig } from '../config';
---

<BaseLayout title={materiaConfig.title}>
  <section class="hero">
    <h1>{materiaConfig.title}</h1>
    <p>{materiaConfig.descripcion}</p>
  </section>

  <section class="info">
    <div class="metadata">
      <p>Semestre: {materiaConfig.semestre}</p>
      <p>Créditos: {materiaConfig.creditos}</p>
      <p>Horario: {materiaConfig.horario}</p>
    </div>
  </section>

  <section class="clases">
    <h2>Clases</h2>
    <!-- Auto-generado desde content collection -->
  </section>
</BaseLayout>
```

### 2.5 Registrar en Orbital Nexus

**Archivo**: `apps/nexus/src/content/materias/nueva-materia.json`

```json
{
  "title": "Título del Curso",
  "slug": "nueva-materia",
  "profesor": "Julián Zuluaga",
  "descripcion": "Descripción breve visible en catálogo",
  "vertical": "academia",
  "semestre": "2025-2",
  "creditos": 3,
  "modalidad": "presencial",
  "siteUrl": "https://<user>.github.io/externado-docencia/materias/nueva-materia/",
  "thumbnail": "/assets/materias/nueva-materia-thumb.png",
  "tags": ["Python", "Data Science", "ML"],
  "estado": "activo"
}
```

### 2.6 Deploy

```bash
# Commit cambios
git add .
git commit -m "feat(materia): add nueva-materia"
git push origin main

# GitHub Actions build automático
# Verificar en https://<user>.github.io/externado-docencia/materias/nueva-materia/
```

---

## 3. Cómo Agregar una Nueva Clase

### 3.1 Crear Archivo MDX

**Ubicación**: `apps/materias/<materia>/src/content/clases/YYYY-MM-DD-slug.mdx`

**Ejemplo**: `apps/materias/mineria-de-datos/src/content/clases/2025-11-15-regresion-lineal.mdx`

### 3.2 Agregar Frontmatter

```mdx
---
numero: 10
title: "Regresión Lineal Simple y Múltiple"
fecha: 2025-11-15
fase_crisp: "modelado"
objetivos:
  - Comprender los fundamentos de la regresión lineal
  - Implementar regresión simple en Python
  - Evaluar modelos con métricas apropiadas
recursos:
  guia_html: "https://.../clases/2025-11-15-regresion-lineal/"
  notebook: "/notebooks/clase-10-regresion.ipynb"
  datasets:
    - "/datasets/housing-prices.csv"
    - "/datasets/boston-housing.csv"
  slides: "https://docs.google.com/presentation/d/..."
tags:
  - Regresión
  - Supervised Learning
  - Python
  - Scikit-learn
estado: "proxima"
---

# Regresión Lineal Simple y Múltiple

## Introducción

La regresión lineal es uno de los algoritmos más fundamentales en machine learning...

## Contenido

### 1. Fundamentos Matemáticos

[Contenido aquí con sintaxis MDX]

### 2. Implementación en Python

```python
import numpy as np
from sklearn.linear_model import LinearRegression

# Código ejemplo
```

### 3. Ejercicios Prácticos

[Lista de ejercicios]

## Recursos Adicionales

- [Scikit-learn Docs](https://scikit-learn.org/...)
- [Estadística para Data Science](https://...)
```

### 3.3 Generar Guía HTML (Opcional)

Si la clase tiene guía interactiva generada con OpenSpecs:

```bash
cd materias/<materia>/clases/2025-11-15-regresion-lineal/
# Ejecutar generador
python ../../herramientas/generar_guia.py --config guia_config.yaml

# Se genera guia_interactiva_regresion.html
```

### 3.4 Validar Metadata

**Script de validación**:

```bash
npm run validate:clase -- --materia mineria-de-datos --clase 2025-11-15-regresion-lineal
```

**Verifica**:
- Frontmatter completo
- Fechas en formato correcto
- fase_crisp válida
- URLs de recursos accesibles
- Tags sin typos

### 3.5 Preview Local

```bash
# Desarrollo
npm run dev:mineria

# Navegar a http://localhost:4321/clases/regresion-lineal/
```

### 3.6 Deploy

```bash
git add apps/materias/mineria-de-datos/src/content/clases/2025-11-15-regresion-lineal.mdx
git commit -m "docs(mineria): add clase 10 regresión lineal"
git push origin main
```

---

## 4. Cómo Agregar un Proyecto al Showcase

### 4.1 Crear Archivo MDX

**Ubicación**: `apps/nexus/src/content/projects/<slug>.mdx`

**Ejemplo**: `apps/nexus/src/content/projects/strivio.mdx`

### 4.2 Agregar Frontmatter + Contenido

```mdx
---
title: "Strivio"
vertical: "deportes"
submarca: "strivio"
descripcion: "Plataforma de analítica deportiva con IA: métricas automáticas, clips de jugadas clave y análisis táctico para ligas semi-profesionales."
thumbnail: "/assets/projects/strivio-thumb.png"
featured: true
tecnologias:
  - Computer Vision
  - YOLOv8
  - PyTorch
  - React
  - FastAPI
link: "https://strivio.orbitallab.co"
github: "https://github.com/orbitallab/strivio"
fecha: 2024-06-15
---

# Strivio · Analítica Deportiva con IA

## El Problema

Las ligas semi-profesionales y amateur no tienen acceso a analítica deportiva avanzada...

## La Solución

Strivio automatiza el análisis de videos deportivos usando Computer Vision y genera:

- **Métricas en tiempo real**: Posesión, pases completados, tiros al arco
- **Clips automáticos**: Highlights de jugadas clave
- **Heatmaps**: Zonas de mayor actividad por jugador
- **Análisis táctico**: Formaciones, presión, transiciones

## Stack Técnico

[Detalles técnicos]

## Impacto

- 15 ligas usando la plataforma
- 500+ partidos analizados
- 2,000+ clips generados automáticamente

## Screenshots

![Dashboard Strivio](/assets/projects/strivio-dashboard.png)

## Demo

[Video o link a demo]
```

### 4.3 Agregar Assets

```bash
# Thumbnail (card en home)
# Dimensiones: 600x400px
# Formato: PNG o WebP
cp strivio-thumb.png recursos_compartidos/componentes/orbital_lab/assets/projects/

# Screenshots (dentro del MDX)
# Dimensiones: 1920x1080px o 16:9
cp strivio-dashboard.png recursos_compartidos/componentes/orbital_lab/assets/projects/
```

### 4.4 Deploy

```bash
git add .
git commit -m "feat(showcase): add strivio project"
git push origin main
```

---

## 5. Guía de Estilo

### 5.1 Nomenclatura de Archivos

**Materias**:
```
✅ mineria-de-datos/
✅ ia-negocios/
✅ deep-learning-aplicado/
❌ mineriadedatos/
❌ IA_Negocios/
❌ DL-Aplicado/
```

**Clases**:
```
✅ 2025-11-15-regresion-lineal.mdx
✅ 2025-10-23-crisp-dm-fases-1-2.mdx
❌ clase-10-regresion.mdx
❌ 2025-11-15-Regresión-Lineal.mdx
❌ regresion_lineal_2025.mdx
```

**Proyectos**:
```
✅ strivio.mdx
✅ lighthouse-audience.mdx
✅ jaguar-orbital.mdx
❌ Strivio.mdx
❌ lighthouse_audience.mdx
```

### 5.2 Formato de Commits

**Conventional Commits**:

```bash
# Nuevas features
feat(materia): add nueva-materia
feat(clase): add regresión lineal
feat(showcase): add strivio project

# Contenido/documentación
docs(mineria): update syllabus
docs(clase): add ejercicios regresión

# Fixes
fix(nav): correct breadcrumb links
fix(build): resolve GitHub Pages base path

# Mejoras UI/UX
style(hero): improve mobile responsive
style(cards): adjust hover animation

# Refactoring
refactor(components): extract GlobalNav to shared package

# Performance
perf(images): lazy load thumbnails
perf(video): compress hero video to 5 Mbps

# Tests
test(clase): validate frontmatter schema
```

### 5.3 Convenciones de Código

**Astro Components**:

```astro
---
// Props con interface
interface Props {
  title: string;
  description?: string;
}

const { title, description } = Astro.props;
---

<!-- Semantic HTML -->
<section class="hero">
  <h1>{title}</h1>
  {description && <p>{description}</p>}
</section>

<style>
  /* Scoped styles */
  .hero {
    @apply bg-black text-white;
  }
</style>
```

**Tailwind CSS**:

```astro
<!-- Usar clases de Tailwind en vez de CSS custom -->
✅ <div class="bg-black text-white p-6 rounded-lg">
❌ <div style="background: black; color: white; padding: 24px;">

<!-- Mobile-first -->
✅ <div class="text-sm md:text-base lg:text-lg">
❌ <div class="text-lg md:text-base sm:text-sm">

<!-- Usar tokens del theme -->
✅ <div class="bg-orbital-red text-orbital-white">
❌ <div class="bg-[#ED2024] text-[#FFFFFF]">
```

**MDX Content**:

```mdx
<!-- Headers con jerarquía correcta -->
# Título Principal (solo uno por archivo)
## Sección
### Subsección

<!-- Code blocks con lenguaje -->
```python
def funcion():
    return "valor"
```

<!-- Links con títulos descriptivos -->
✅ [Documentación de Scikit-learn](https://...)
❌ [Click aquí](https://...)

<!-- Imágenes con alt text -->
✅ ![Dashboard mostrando métricas de regresión](/assets/dashboard.png)
❌ ![imagen](/assets/dashboard.png)
```

### 5.4 Nomenclatura de Verticales

**CRÍTICO**: Usar nombres de **verticales**, NO de proyectos/submarcas.

```
✅ deportes (vertical)
❌ strivio (submarca)

✅ negocio (vertical)
❌ lighthouse (submarca)

✅ biologia (vertical)
❌ jaguar (submarca)

✅ otros (vertical)
❌ ai-systems (submarca)

✅ academia (vertical)
❌ academia-orbital (submarca)
```

**Referencia completa**: `docs/brand/VERTICALES_REFERENCE.md`

---

## 6. Workflow de Git

### 6.1 Branches

```
main                    (producción, protegido)
├── feat/nueva-materia  (nueva materia)
├── docs/clase-10       (nueva clase)
├── fix/nav-links       (bugfix)
└── refactor/components (refactoring)
```

**Convención**:
- `feat/` - Nuevas features
- `docs/` - Contenido educativo
- `fix/` - Bugfixes
- `style/` - UI/UX changes
- `refactor/` - Code refactoring
- `perf/` - Performance improvements

### 6.2 Flujo Típico

```bash
# 1. Sincronizar con main
git checkout main
git pull origin main

# 2. Crear branch
git checkout -b docs/clase-10-regresion

# 3. Hacer cambios
# [editar archivos]

# 4. Validar localmente
npm run validate:clase -- --clase 2025-11-15-regresion-lineal
npm run dev:mineria

# 5. Commit
git add .
git commit -m "docs(mineria): add clase 10 regresión lineal"

# 6. Push
git push origin docs/clase-10-regresion

# 7. Crear Pull Request en GitHub (opcional para revisión)
# O hacer merge directo si tienes permisos:
git checkout main
git merge docs/clase-10-regresion
git push origin main

# 8. Verificar deploy
# GitHub Actions construye automáticamente
# Verificar en https://<user>.github.io/externado-docencia/
```

### 6.3 Pull Requests (PRs)

**Template de PR**:

```markdown
## Descripción
Agrega clase 10 de Minería de Datos sobre regresión lineal.

## Tipo de cambio
- [ ] Nueva materia
- [x] Nueva clase
- [ ] Nuevo proyecto
- [ ] Bugfix
- [ ] Documentación

## Checklist
- [x] Frontmatter completo y validado
- [x] Preview local testeado
- [x] Assets agregados (si aplica)
- [x] Links verificados (no 404s)
- [x] Commits con mensajes descriptivos

## Screenshots (si aplica)
[Captura de la clase en preview local]
```

---

## 7. Testing y Validación

### 7.1 Validación de Contenido

**Antes de commit**:

```bash
# Validar frontmatter de clase
npm run validate:clase -- --materia mineria-de-datos --clase 2025-11-15-regresion-lineal

# Validar links (no 404s)
npm run check:links

# Validar imágenes existen
npm run check:images
```

### 7.2 Preview Local

```bash
# Nexus
npm run dev:nexus
# http://localhost:4321/

# Materia específica
npm run dev:mineria
# http://localhost:4321/

# Build local (simula producción)
npm run build:all
npm run preview
```

### 7.3 Testing Manual

**Checklist antes de deploy**:

- [ ] Navegación funciona (header, breadcrumbs, footer)
- [ ] Todas las imágenes cargan
- [ ] Videos reproducen correctamente
- [ ] Links externos abren en nueva pestaña
- [ ] Formularios funcionan (si aplica)
- [ ] Mobile responsive (testar en ≥1 dispositivo)
- [ ] No hay console errors en DevTools

### 7.4 Lighthouse Audit

```bash
# Después de deploy
npm run lighthouse -- --url="https://<user>.github.io/externado-docencia/"

# Target scores:
# Performance: ≥90
# Accessibility: ≥95
# Best Practices: ≥90
# SEO: ≥95
```

---

## 8. FAQ

### Q1: ¿Dónde encuentro los assets (logos, imágenes)?

**R**: `recursos_compartidos/componentes/orbital_lab/assets/`

Subdirectorios:
- `brand/` - Logos oficiales
- `hero/` - Videos y glows para hero section
- `lab/` - Iconos e ilustraciones de verticales
- `projects/` - Thumbnails de proyectos

Ver inventario completo: `docs/brand/assets-checklist.md`

### Q2: ¿Cómo genero una guía HTML interactiva?

**R**: Usar generador OpenSpecs:

```bash
cd materias/<materia>/clases/<fecha-slug>/
python ../../herramientas/generar_guia.py --config guia_config.yaml
```

La guía se integra automáticamente en el build.

Ver ejemplo: `materias/mineria-de-datos/clases/2025-10-23-crisp-dm-fases-1-2/`

### Q3: ¿Puedo agregar componentes React custom?

**R**: Sí, pero con precaución:

```astro
---
// Solo usar client: directives cuando sea necesario
import InteractiveChart from '../components/InteractiveChart.jsx';
---

<!-- Static by default -->
<InteractiveChart data={chartData} />

<!-- Hydrate solo si necesita interactividad -->
<InteractiveChart data={chartData} client:load />

<!-- Lazy load cuando entra al viewport -->
<InteractiveChart data={chartData} client:visible />
```

Preferir HTML/CSS estático siempre que sea posible (mejor performance).

### Q4: ¿Cómo actualizo el thumbnail de una materia?

**R**:

1. Crear imagen 600x400px en formato PNG o WebP
2. Guardar en `recursos_compartidos/componentes/orbital_lab/assets/materias/<slug>-thumb.png`
3. Actualizar JSON: `apps/nexus/src/content/materias/<slug>.json`
   ```json
   {
     "thumbnail": "/assets/materias/<slug>-thumb.png"
   }
   ```
4. Commit y push

### Q5: ¿Cómo sé qué vertical usar para mi materia?

**R**: Las 5 verticales son:

1. **Deportes**: Analítica deportiva, performance, tracking (ej. Strivio)
2. **Negocio**: Marketing, audiencias, publicidad OOH (ej. Lighthouse)
3. **Biología**: Conservación, fauna, ecosistemas (ej. Jaguar Orbital)
4. **Otros**: Automatización corporativa, ERP/CRM, RAG (ej. AI Systems)
5. **Academia**: Educación, formación, cursos (ej. Minería de Datos, IA para Negocios)

Si es contenido educativo → **Academia**

Ver detalles: `docs/brand/VERTICALES_REFERENCE.md`

### Q6: El deploy falló, ¿cómo debuggeo?

**R**:

1. Ir a GitHub → Actions tab
2. Click en el workflow fallido
3. Expandir el job con error
4. Leer logs (buscar líneas rojas)

**Errores comunes**:

- **Build timeout**: Reducir tamaño de videos/imágenes
- **404 assets**: Verificar paths relativos
- **Invalid frontmatter**: Validar schema Zod
- **Merge conflicts**: Sincronizar con main primero

Si no puedes resolverlo, crear issue en GitHub con logs.

### Q7: ¿Puedo usar Google Analytics u otro tracker?

**R**: Sí, agregar en `apps/nexus/src/layouts/BaseLayout.astro`:

```astro
---
const GA_MEASUREMENT_ID = import.meta.env.PUBLIC_GA_ID;
---

<head>
  <!-- ... -->
  {GA_MEASUREMENT_ID && (
    <script async src={`https://www.googletagmanager.com/gtag/js?id=${GA_MEASUREMENT_ID}`}></script>
    <script is:inline define:vars={{ GA_MEASUREMENT_ID }}>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', GA_MEASUREMENT_ID);
    </script>
  )}
</head>
```

Configurar `PUBLIC_GA_ID` en GitHub Secrets.

### Q8: ¿Cómo migro contenido existente de otra plataforma?

**R**: Depende de la fuente:

**Desde Google Docs**:
- Exportar como Markdown
- Limpiar formato con Pandoc
- Agregar frontmatter manualmente
- Ajustar paths de imágenes

**Desde Notion**:
- Exportar como Markdown & CSV
- Script de conversión: `herramientas/notion-to-mdx.js`

**Desde WordPress**:
- Plugin "Export to Markdown"
- Revisar frontmatter generado

**Desde PDFs**:
- No recomendado (mejor recrear en MDX)
- Si es necesario: Adobe Acrobat → Word → Markdown

---

## 📚 Recursos Adicionales

### Documentación Oficial
- [Astro Docs](https://docs.astro.build/)
- [MDX Docs](https://mdxjs.com/)
- [Tailwind CSS](https://tailwindcss.com/)

### Tutoriales Internos
- `docs/tutorials/crear-primera-clase.md` (pendiente)
- `docs/tutorials/generar-guia-html.md` (pendiente)

### Ejemplos de Referencia
- Materia completa: `apps/materias/ia-negocios/`
- Clase MDX: `apps/materias/mineria-de-datos/src/content/clases/2025-10-23-crisp-dm-fases-1-2.mdx`
- Proyecto showcase: `apps/nexus/src/content/projects/strivio.mdx`

---

## 🆘 Soporte

**¿Necesitas ayuda?**

1. Revisar `docs/PROJECT_STATUS.md` (puede estar documentado)
2. Buscar en issues cerrados de GitHub
3. Crear nuevo issue con label `question`
4. Contactar a Julián Zuluaga directamente

**Issues en GitHub**:
- Bug report: `bug` label
- Feature request: `enhancement` label
- Pregunta: `question` label
- Documentación: `documentation` label

---

**Gracias por contribuir a Orbital Nexus** 🚀

_Este documento se actualiza conforme evolucionan las prácticas del proyecto._
