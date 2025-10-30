# Orbital Vinyl Collection — Micrositio IA para Negocios

Micrositio creado con **Astro 5 + Tailwind 4** para la materia Inteligencia Artificial para Negocios (Universidad Externado). Presenta las clases como una colección de vinilos holográficos, con hero cinematográfico, HUD de métricas y enlaces a recursos pedagógicos dentro del repositorio.

## 🚀 Stack

- [Astro 5](https://astro.build/) · SSG — output estático listo para GitHub Pages.
- Tailwind CSS 4 (via `@tailwindcss/vite`) para los estilos Orbital (glassmorphism + halos).
- Contenido en TypeScript (`src/data/course.ts`) que centraliza clases, highlights, toolkit, FAQs y detail views (overview, casos, prompts).
- Markdown importado directamente desde `clases/` para mostrar README pedagógicos dentro del sitio.

## 📁 Estructura clave

```text
site/
├── src/
│   ├── components/        # Hero, bento, grid de vinilos, toolkit, FAQ, profesor
│   ├── data/course.ts     # Metadata escalable de clases (stack, detail, prompts, etc.)
│   ├── layouts/BaseLayout # Layout global con backgrounds orbitales
│   ├── pages/             # Index + docs + clases renderizadas
│   └── styles/global.css  # Tokens (fuentes, fondos, utilidades)
├── assets/                # Arte fuente (vinilos, halos, spines, hero)
├── public/transcripts/    # Archivos .vtt servidos estáticamente
└── astro.config.mjs       # Config deploy con `SITE_URL` y `BASE_PATH`
```

### Estado actual

```
Hero fullscreen con video → usa /public/assets/hero/*
Clases:
  Clase 01 · Análisis de Datos con IA → status draft (placeholder negro)
  Clase 02 · Vibe Coding → status published (detalle completo, vinilo IA actualizado)
  Clase 03 · IA Generativa Visual → status upcoming (placeholder)
Syllabus → CTA deshabilitado (en construcción)
Profesor → sección con foto y enlaces (LinkedIn, Orbital Lab)
```

> Los assets en `assets/` se importan directamente desde los componentes para conservar control de versiones (Pillow placeholders marcados como tales en `assets/GLOSARIO.md`).

## 🧞 Comandos

Todos se ejecutan desde `materias/inteligencia-artificial-para-negocios/site`.

| Comando         | Acción                                         |
|-----------------|------------------------------------------------|
| `npm install`   | Instala dependencias                           |
| `npm run dev`   | Dev server (`http://localhost:4321`)           |
| `npm run build` | Build estático en `dist/`                      |
| `npm run preview` | Sirve la build localmente                    |

## 🔌 Variables para despliegue

Configura estas variables (por ejemplo en GitHub Actions o `.env`) antes de `npm run build`:

```bash
SITE_URL=https://<tu-usuario>.github.io
BASE_PATH=/inteligencia-artificial-para-negocios   # o "/" si usas dominio propio
```

`astro.config.mjs` usa `assets: "relative"` para facilitar despliegues en subrutas (GitHub Pages).

## ☁️ Despliegue en GitHub Pages

1. Crea un workflow (se incluye boceto en `.github/workflows/deploy.yml` dentro de `site/`).
2. Configura la acción para ejecutar `npm ci`, `npm run build` y publicar `dist/`.
3. Define `SITE_URL` y `BASE_PATH` en los *repository secrets* según la URL final.

## ➕ Extender la colección

- Añade nuevos vinilos en `src/data/course.ts` (status `published`, `upcoming` o `draft`).
- Genera assets definitivos siguiendo `site/assets/GLOSARIO.md` y reemplaza los placeholders.
- Crea páginas dedicadas en `src/pages/clases/<slug>.astro` importando los README correspondientes.
- Ajusta toolkits/FAQs desde los arrays exportados para mantener coherencia narrativa.

## 🧭 Roadmap inmediato

- Completar syllabus navegable y reactivar el CTA principal.
- Sustituir placeholders restantes (Clase 01 y Clase 03) por artes definitivos.
- Evaluar una isla interactiva (React/Framer) para tilt 3D y navegación de modales.
- Migrar metadata de clases a `astro:content` o CMS ligero si crece el número de cursos.

---

**Mantra Orbital:** “¿Ayuda a ver y entender mejor la IA corporativa?” Si la respuesta es sí, la experiencia está en órbita.
