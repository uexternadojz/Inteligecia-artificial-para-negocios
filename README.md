# Docencia - Julián Zuluaga · Orbital Lab

Repositorio maestro para centralizar asignaturas, clases, tutoriales y recursos interactivos bajo el ecosistema **Orbital Nexus**.

---

## 🚀 Orbital Nexus

**Hub central de inteligencia artificial aplicada**: Sistema de sitios web federados que conecta docencia, proyectos y recursos de Orbital Lab, desplegable en GitHub Pages.

### Quick Links

- 📖 **[Requerimientos Completos](docs/ORBITAL_NEXUS_REQUIREMENTS.md)** - Especificación técnica
- 📊 **[Estado del Proyecto](docs/PROJECT_STATUS.md)** - Progreso actual
- 🤝 **[Guía de Contribución](docs/CONTRIBUTING.md)** - Cómo agregar contenido
- 🎨 **[Manifiesto de Marca](docs/brand/manifesto.md)** - Identidad visual
- 🔍 **[Análisis IT Empire](docs/research/itempire_inspiration.md)** - Inspiración de diseño

### Arquitectura en una Imagen

```
https://<user>.github.io/externado-docencia/
│
├── /                          ← Orbital Nexus (hub principal)
│   ├── Hero cinemático con video orbital
│   ├── Grid de 5 verticales (Deportes, Negocio, Biología, Otros, Academia)
│   ├── Catálogo de materias
│   └── Showcase de proyectos (Strivio, Lighthouse, Jaguar)
│
├── /materias/
│   ├── /mineria-de-datos/     ← Site de Minería de Datos
│   ├── /ia-negocios/          ← Site de IA para Negocios
│   └── ...                     (escalable: agregar materias sin reestructurar)
│
├── /clases/                   ← Guías HTML standalone
│   ├── /2025-10-23-crisp-dm/
│   └── /2025-10-28-prep-datos/
│
└── /recursos/                 ← Datasets, templates públicos
```

### Stack Tecnológico

- **Framework**: Astro 5.x (SSG, MPA)
- **Styling**: Tailwind CSS 4.x + tokens Orbital Lab
- **Animations**: Framer Motion (islands)
- **Monorepo**: npm workspaces
- **Deploy**: GitHub Pages + Actions (automático en push a main)

### Estado Actual

**Fase**: Pre-desarrollo (Arquitectura y Documentación)
**Assets**: ✅ 46 archivos listos (logos, videos, ilustraciones)
**Código**: ⏳ Monorepo pendiente de inicializar

Ver [PROJECT_STATUS.md](docs/PROJECT_STATUS.md) para detalles.

---

## 📁 Visión General del Repositorio

- **Materias**: Cada asignatura vive en `materias/<materia>/` con sus clases, handbooks y guías.
- **Recursos compartidos**: Componentes HTML/CSS/JS, datasets y plantillas reutilizables para acelerar nuevas clases.
- **Apps**: Sitios Astro deployables (`apps/nexus/`, `apps/materias/*`)
- **Packages**: Componentes y themes compartidos (`packages/ui-components/`, `packages/orbital-theme/`)
- **Herramientas**: Scripts y utilidades para generar contenidos (guías interactivas, scaffolds de clase).
- **Docs**: Documentación técnica y de marca.

```
.
├── materias/
│   └── mineria-de-datos/
│       ├── clases/
│       │   └── 2025-10-23-crisp-dm-fases-1-2/
│       ├── docs/
│       └── recursos/
├── recursos_compartidos/
│   ├── componentes/
│   ├── datasets/
│   ├── plantillas/
│   └── tutoriales/
├── herramientas/
│   └── scripts/
├── skills/
└── site/
```

## Primeros Pasos

1. Revisa `ARCHITECTURE.md` para entender la arquitectura y los flujos de trabajo sugeridos.
2. En `materias/` cada materia tiene un README con el mapa de clases y recursos activos.
3. Usa `herramientas/` para agregar o extender generadores (ej. crear guía HTML, scaffolds de clase, etc.).
4. Centraliza datasets y componentes que quieras reutilizar dentro de `recursos_compartidos/`.

## Próximos Movimientos

- Documentar la carpeta `skills/` con módulos temáticos reutilizables.
- Preparar el armazón de `site/` (framework, build y despliegue a GitHub Pages).
- Crear plantillas de clase para nuevas sesiones (README base, checklist, estructura de assets).
- Factorizar scripts monolíticos actuales para compartir componentes visuales y layouts entre clases.

---

**Autor**: Juan Zuluaga  
**Propósito**: Plataforma unificada de docencia con recursos interactivos reutilizables.

## Memoria para Agentes CLI

Consulta `docs/agent_memory.md` para tener un prompt base y las reglas de colaboración cuando un agente trabaje dentro del repositorio.

- Consulta `docs/perfil_profesional.md` para conocer la bio y ejes de trabajo de Julián Zuluaga.

- Identidad de marca de Orbital Lab: `docs/orbital_lab.md` y sub-marcas en `docs/submarcas_orbital.md`.

- Brandbook y manifiesto visual: manifiesto en `docs/brand/manifesto.md` y página interactiva en `docs/brand/manifesto.html` (incluye moodboard y sistema visual).
- Documentación de branding: `docs/brand/README.md` resume los archivos y cómo usarlos.

- Tokens y presets: consulta `recursos_compartidos/componentes/orbital_lab/` para colores, tipografías y componentes base.
