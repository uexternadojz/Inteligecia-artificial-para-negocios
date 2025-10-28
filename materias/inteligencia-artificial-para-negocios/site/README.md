# Orbital Vinyl Collection — Micrositio IA para Negocios

Micrositio creado con **Astro 5 + Tailwind 4** para la materia Inteligencia Artificial para Negocios (Universidad Externado). Presenta las clases como una colección de vinilos holográficos, con hero cinematográfico, HUD de métricas y enlaces a recursos pedagógicos dentro del repositorio.

## 🚀 Stack

- [Astro 5](https://astro.build/) · SSG — output estático listo para GitHub Pages.
- Tailwind CSS 4 (via `@tailwindcss/vite`) para los estilos Orbital (glassmorphism + halos).
- Contenido en TypeScript (`src/data/course.ts`) que centraliza clases, highlights, toolkit y FAQs.
- Markdown importado directamente desde `clases/` para mostrar README pedagógicos dentro del sitio.

## 📁 Estructura clave

```text
site/
├── src/
│   ├── components/        # Hero, bento, grid de vinilos, toolkit y FAQ
│   ├── data/course.ts     # Metadata escalable de clases y secciones
│   ├── layouts/BaseLayout # Layout global con backgrounds orbitales
│   ├── pages/             # Index + docs + clases renderizadas
│   └── styles/global.css  # Tokens (fuentes, fondos, utilidades)
├── assets/                # Arte fuente (vinilos, halos, spines, hero)
├── public/transcripts/    # Archivos .vtt servidos estáticamente
└── astro.config.mjs       # Config deploy con `SITE_URL` y `BASE_PATH`
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

1. Crea un workflow (ver ejemplo en `.github/workflows/deploy.yml` cuando se agregue).
2. Configura la acción para ejecutar `npm ci`, `npm run build` y publicar `dist/`.
3. Define `SITE_URL` y `BASE_PATH` en los *repository secrets* según la URL final.

## ➕ Extender la colección

- Añade nuevos vinilos en `src/data/course.ts` (status `published`, `upcoming` o `draft`).
- Genera assets definitivos siguiendo `site/assets/GLOSARIO.md` y reemplaza los placeholders.
- Crea páginas dedicadas en `src/pages/clases/<slug>.astro` importando los README correspondientes.
- Ajusta toolkits/FAQs desde los arrays exportados para mantener coherencia narrativa.

## 🧭 Roadmap inmediato

- Sustituir placeholders generados con Pillow por artes definitivos.
- Implementar interacciones `framer-motion` via islas React para el tilt 3D y modales.
- Agregar workflow de despliegue (`deploy.yml`) y documentación pública del syllabus.
- Integrar `astro:content` para manejar metadata de clases vía Markdown/MDX.

---

**Mantra Orbital:** “¿Ayuda a ver y entender mejor la IA corporativa?” Si la respuesta es sí, la experiencia está en órbita.
