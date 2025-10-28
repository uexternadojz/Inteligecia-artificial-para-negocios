# Orbital Vinyl Collection — Concepto de Sitio

Documento guía para el diseño y desarrollo del micrositio de la materia **Inteligencia Artificial para Negocios**. Reúne la visión estética, la arquitectura de información y los requerimientos técnicos previos a construir el front-end.

---

## 1. Propósito del Micrositio
- Presentar la materia desde un **home cinematográfico** que transmita la estética Orbital (negro profundo + rojo orbital + halos cian).
- Exhibir cada clase como un **“vinilo holográfico”**: portada ilustrada, spine lateral con número y contenido desplegable.
- Facilitar el acceso a materiales (README, slides, datasets, herramientas) y contar la narrativa de impacto de la materia.
- Preparar estructura para despliegue independiente en GitHub Pages desde este sub-repo.

---

## 2. Narrativa y Mood Visual
- **Concepto central:** *Orbital Vinyl Collection*. Los conceptos de clase son pistas dentro de un laboratorio musical futurista.
- **Referencias clave:** `docs/brand/manifesto.md`, `docs/research/itempire_inspiration.md`, `docs/brand/assets/moodboard-orbital.png`.
- **Elementos distintivos:**
  - Portadas generadas con IA (Nano Banana) con halos rojos, circuitos y personajes tech.
  - Cards translúcidas (`glassmorphism`) con glow rojo `rgba(237,32,36,0.35)`.
  - Tipografía: Rajdhani/Overcame para títulos, Inter/Audiowide para cuerpo, Fira Code para datos.
  - Animaciones de entrada tipo `framer-motion`: tilt 3D, parallax suave, contadores HUD.

---

## 3. Arquitectura de Información

### 3.1 Home
- **Hero Orbital**: título, tagline “Ver es entender la IA corporativa”, CTA a syllabus, halo animado.
- **Highlights bento**: tres tarjetas rápidas (Metodología, Herramientas, Casos Orbital).
- **Colección de Vinilos**: grid responsiva con cards que adelantan cada clase.
- **Sección Herramientas**: chips con iconos lineales (Lovable, Replit, v0.dev, Claude).
- **Bloque Roadmap / Preguntas frecuentes**: mini-accordion.
- **Footer**: mantra Orbital + enlaces a recursos compartidos y README general.

### 3.2 Vista de Clase (modal/panel)
- **Portada ampliada** con efecto glow y metadata (fecha, duración, modalidad).
- **Objetivos + agenda** en lista animada.
- **CTA primarios**: `Ver README`, `Descargar recursos`, `Abrir ejercicios`.
- **Stack usado**: badges (No-code, IA conversacional, datasets).
- **Sección “Lo que lograrás”** con micro bullets y métricas.
- **Navegación**: flechas `Anterior / Siguiente` + teclado (`←` `→`).

### 3.3 Detalle ampliado (scroll anclado opcional)
- Permitir saltar a subpáginas o anchors para documentación extensa (p.ej. `/clase/02-vibe-coding` generada dinámicamente) cuando sea necesario.

---

## 4. Componentes Clave

| Componente | Descripción | Interacción |
|------------|-------------|-------------|
| `HeroOrbit` | Hero fullscreen con partícula/halo dinámico y CTA principal | Animación de partículas `canvas` opcional, fallback CSS |
| `VinylGrid` | Grid responsiva (3 columnas desktop, 2 tablet, 1 mobile) | Tilt 3D al hover, glow pulsante, reorder con filtros |
| `VinylCard` | Card principal de clase (portada, spine, metadata) | `framer-motion` para tilt, `aria-expanded` |
| `ClassModal` | Panel lateral/overlay con detalle completo | Scroll interno, atajos teclado, blur del fondo |
| `ToolkitChips` | Chips con iconos lineales de herramientas | Animación hover (glow + desplazamiento) |
| `HUDMetrics` | Contadores (clases activas, horas, % práctica) | Conteo animado al entrar en viewport |

---

## 5. Generación de Assets

- **Vinilos de clase**: imagen principal 4:5 (o 8:5 si se prioriza apaisado) con glow orbital. Generar versión estática (`.webp`) y loop animado corto (`.webm`/`.mp4` ≤6s) para hover.
- **Spine & labels**: textura vertical con tipografía condensada (`Clase 01`, etc.) para simular lomo de vinilo.
- **Ilustraciones conceptuales**: piezas panorámicas para hero y secciones (Metodología, Herramientas, Casos Orbital). Seguir prompts de `docs/brand/ilustraciones-verticales.md`.
- **Fondos y halos**: texturas abstractas (mallas de datos, circuitos). Optimizar tamaño (≤400KB) con `imagemagick`.
- **Iconografía lineal**: estilo monocromo rojo/cian, siguiendo `docs/brand/iconos-verticales.md`.

### 5.1 Tabla de referencia para clases activas

| Clase | Mood / escenas sugeridas | Prompt base (resumen) | Assets a generar |
|-------|---------------------------|------------------------|------------------|
| Clase 01 · Introducción IA Corporativa | Penthouse corporativo futurista, skyline con haces de datos, ejecutivos frente a tableros holográficos | “corporate ai control room, skyline at night, red orbital glow, holographic dashboards, cinematic lighting, ultra detailed, orbital lab color palette” | 1) Portada vinilo estática<br>2) Loop hover (rotación leve)<br>3) Spine etiquetada<br>4) Fondo modal con patrones de datos |
| Clase 02 · Vibe Coding | Estudio creativo con turntable de código, DJ tech mezclando prompts, partículas rojas/cian | “ai coding dj booth, vinyl records emitting code, neon red cyan lighting, futuristic studio, energetic vibe, detailed, orbital lab branding” | 1) Portada vinilo<br>2) Loop animado (pulsos de luz)<br>3) Spine `Clase 02`<br>4) Texture glow para modal |
| Clase 03 · IA Generativa Visual | Galería de arte holográfico, pantallas gigantes, artistas con IA, mallas visuales flotando | “ai generative art gallery, holographic canvases, red and cyan beams, futuristic museum, cinematic sci-fi, vibrant, orbital aesthetic” | 1) Portada vinilo<br>2) Loop animado con destellos<br>3) Spine `Clase 03`<br>4) Background con patrones pixel/arte |

> Nota: la tabla se actualizará a medida que se agreguen nuevas clases para mantener consistencia y planificar assets incrementalmente.

### 5.2 Animaciones e interacciones previstas
- Hover de vinilo: leve rotación, glow intensificado, muestra snippet (texto o mini waveform).
- Idle motion: flotación vertical ±4px desfasada entre cards para sensación viva.
- Modal reveal: panel deslizable con blur orbital, incluye `prefers-reduced-motion` para desactivar animaciones.
- Hero: partículas orbitando (canvas o vídeo) sincronizadas con scroll.

### 5.3 Organización de assets
- Todos los recursos se almacenarán en `assets/` siguiendo la estructura descrita en `assets/GLOSARIO.md`.
- Cada carpeta incluye un `notes.md` opcional para registrar prompts y ajustes de post-proceso cuando aplique.
- Mantener formatos finales optimizados (WebP, WebM, SVG) dentro de este repositorio; fuentes originales de alta resolución pueden residir fuera para preservar tamaño ligero.

---

## 6. Stack Técnico Propuesto

- **Framework**: Astro 4.x (SSG) con TailwindCSS + `astro:content`.
- **Islas interactivas**: componentes React (`VinylCard`, `ClassModal`) con `framer-motion`.
- **Animaciones de scroll**: `@studio-freight/lenis` (smooth scroll) + `framer-motion` intersection observers. GSAP opcional.
- **Gestión de contenido**: archivos MD/MDX en `src/content/classes/` con frontmatter.
- **Deployment**: Astro → build estático → GitHub Pages usando workflow `deploy.yml` (pendiente de crear).

---

## 7. Roadmap de Implementación

1. **Setup**: inicializar proyecto Astro dentro de `site/`, importar tokens (`base.css`) y configurar Tailwind.
2. **Data**: definir schema `ClassEntry` (`slug`, `fecha`, `titulo`, `descripcion`, `portada`, `recursos`).
3. **Hero & HUD**: maquetar hero con animaciones básicas y métricas.
4. **VinylGrid**: construir cards con efecto tilt y modal funcional.
5. **Secciones complementarias**: herramientas, casos Orbital, FAQ.
6. **Optimización y accesibilidad**: contraste AA, `prefers-reduced-motion`, atributos `aria`.
7. **Preparación Github Pages**: workflow, `astro.config` con `base`/`site`, README con instrucciones.

---

## 8. Consideraciones de Marca y UX
- Mantener contraste mínimo 4.5:1 en texto; usar cian para resaltar datos sin saturar.
- Incluir versiones sin animaciones pesadas (`prefers-reduced-motion`).
- Documentar prompts y presets para reproducir estilo visual.
- El sitio debe sentirse vivo pero claro: prioridad a la exploración de clases y acceso rápido a recursos.

---

## 9. Próximos Pasos Inmediatos
1. Validar naming final del proyecto (p.ej. `orbital-vinyl-classroom`).
2. Definir lista inicial de clases con metadata y assets requeridos.
3. Preparar prompts para generar portadas IA y probar 2-3 variantes.
4. Iniciar setup técnico cuando se apruebe este concepto.

---

> **Mantra guía:** *“¿Ayuda a ver y entender mejor la IA corporativa?”* Si la respuesta es sí, la experiencia está en órbita.

---

## 10. Checklist de Producción Visual (Wave 1 — Clases 01-03)

- [ ] Portada vinilo Clase 01 (`webp` + loop `webm`)
- [ ] Spine Clase 01 (textura vertical 400×1400px aprox.)
- [ ] Fondo/halo Clase 01 para modal
- [ ] Portada vinilo Clase 02 (`webp` + loop `webm`)
- [ ] Spine Clase 02
- [ ] Fondo/halo Clase 02
- [ ] Portada vinilo Clase 03 (`webp` + loop `webm`)
- [ ] Spine Clase 03
- [ ] Fondo/halo Clase 03
- [ ] Ilustración hero laboratorio orbital (estática + loop opcional)
- [ ] Banners conceptuales secciones (Metodología, Herramientas, Casos Orbital)
- [ ] Iconos lineales herramientas principales (Lovable, Replit, v0.dev, Claude, etc.)
- [ ] Texturas genéricas de patrón orbital (para hover y secciones intermedias)

> Marcar cada ítem al generar y optimizar los assets correspondientes. Añadir nuevos bloques al checklist conforme se agreguen clases o secciones.
