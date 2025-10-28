# Checklist de Assets · Orbital Nexus

Marca una casilla cuando el recurso esté listo y versionado en el repositorio. Cada ítem incluye una idea guía para tu prompt (Nano Banana / Veo / herramienta IA).

## 1. Hero / Portal de Entrada
- [x] Video loop principal (`hero/orbital-portal.mp4`, 1920×1080, loop 10-15s)  
  - Poster estático (`hero/orbital-portal-thumb.png`) generado desde el primer frame.
  _Idea_: “Portal energético rojo-negro, partículas orbitando, vista central cinemática estilo laboratorio futurista. Cámara dolly-in suave, luces volumétricas, tonos rojos y cian. Ambientación tecnólogica, textura metálica.”
- [x] Overlay de partículas (`hero/particles.mp4` – partículas rojas/cian sobre fondo negro; usar mix-blend-mode: screen)
  _Idea_: "Partículas luminosas rojas y cian flotando en cámara lenta, con transparencia alpha. Deben loopear y servir como capa overlay."
- [x] **Glows y flares** (`hero/glow-*.png`) ✅
  - [x] `glow-red-01.png` (622KB) - Flare circular rojo intenso, centro brillante
  - [x] `glow-red-02.png` (580KB) - Halo rojo difuso atmosférico
  - [x] `glow-cyan-01.png` (714KB) - Flare circular cyan complementario
  - [x] `glow-red-wide.png` (497KB) - Flare horizontal para hero widescreen
  - [x] `glow-composite.png` (820KB) - Fusión dual rojo+cyan
  - _Generados con Flux Dev ($0.015 total), 1024x1024px, blend mode: screen_
  - _Nota: Post-proceso alpha opcional documentado en `hero/notes/glows-postprocess.md`_
- [ ] Lockup tagline "Ver es entender" (SVG)
  _Generar manualmente en vector (Figma/Illustrator) con tipografía Overcame.

## 2. Constelación Orbital (Laboratorio)

### Las 5 Verticales (Categorías Permanentes)
1. **Deportes** - Analítica deportiva con IA (ej. Strivio)
2. **Negocio** - Analítica de audiencias y marketing (ej. Lighthouse Audience)
3. **Biología** - Conservación ambiental con CV (ej. Jaguar Orbital)
4. **Otros** - Automatización corporativa (ej. AI Systems/Superagents)
5. **Academia** - Formación aplicada en IA (ej. Academia Orbital)

⚠️ **IMPORTANTE:** Los nombres entre paréntesis son **proyectos ejemplo**, NO las verticales. Los assets se nombran por **vertical**, no por proyecto.

### Assets
- [x] Iconos SVG verticales (Deportes, Negocio, Biología, Otros, Academia) ✅  
  _Archivo base_: `icon-<vertical>.svg` con stroke rojo (#ED2024) y grosor 1.8  
  - **Deportes** (`icon-deportes.svg`): Icono “dumbbell” adaptado  
  - **Negocio** (`icon-negocio.svg`): Icono “handshake”  
  - **Biología** (`icon-biologia.svg`): Icono “shell”  
  - **Otros** (`icon-otros.svg`): Icono “orbit”  
  - **Academia** (`icon-academia.svg`): Icono “book-open”

- [x] **Ilustraciones hero por vertical** (PNG 1920x1080, ubicadas en `lab/`) ✅
  - [x] **Deportes** (`deportes-hero.png`) - Balón holográfico con métricas orbitando
  - [x] **Negocio** (`negocio-hero.png`) - Skyline urbano con rayos de tracking de audiencias
  - [x] **Biología** (`biologia-hero.png`) - Selva con sensores ambientales y fauna
  - [x] **Otros** (`otros-hero.png`) - Centro de comando de automatización IA
  - [x] **Academia** (`academia-hero.png`) - Constelación de conocimiento con rutas neuronales

- [ ] Mini loop/render por vertical (`lab/deportes-loop.mp4`, `lab/negocio-loop.mp4`, etc.)
  _Ideas por vertical_:
  - **Deportes**: Balón holográfico con métricas y heatmaps orbitando, trazos de movimiento
  - **Negocio**: Skyline nocturno con rayos de luz rastreando audiencias, datos flotantes
  - **Biología**: Selva oscura con silueta de fauna, sensores ambientales, alertas visuales
  - **Otros**: Terminales de datos con flujos de automatización, integración de sistemas
  - **Academia**: Libro o aula holográfica con conocimiento fluyendo, símbolos educativos

- [ ] Mapa radial del núcleo orbital (SVG)
  _Generar manualmente: diagrama circular con nodo central 'Orbital Lab' y 5 satélites (Deportes, Negocio, Biología, Otros, Academia) conectados con líneas orbitales.

## 3. Experiencias & Demos
- [ ] Capturas de demos/notebooks (`demos/demo-*.png`)  
  _Tomar del contenido real (Plotly, guías, etc.).
- [ ] Clips cortos por demo (`demos/demo-*.mp4`)  
  _Idea_: “Grabación de pantalla o animación IA que muestre dashboards y visualizaciones flotando.”
- [ ] Logotipos de tecnologías (SVG)  
  _Descargar vectores oficiales (PyTorch, RAG, Tableau, etc.).

## 4. Docencia CRISP-DM
- [ ] Timeline CRISP-DM (SVG)  
  _Generar manual: línea orbital con 6 fases, iconografía mínima.
- [ ] Thumbnails de clases (`docencia/clase-*.png`)  
  _Idea_: “Imagen de fondo abstracta roja/cian con el título de la clase y fase CRISP-DM sobrepuesta.”
- [ ] Slides o keyframes destacados (`docencia/slide-*.png`)  
  _Exportar desde material existente o generar collage con IA (representación de datos, diagramas).

## 5. Ecosistema / Comunidad
- [ ] Mapa estilizado (SVG)  
  _Idea_: “Mapa mundial oscuro con puntos luminosos en Bogotá, LatAm, aliados. Líneas suavemente curvadas conectando nodos.”
- [ ] Retratos / testimonios (`ecosistema/profile-*.png`)  
  _Idea_: “Retratos semi-fotorrealistas de socios/estudiantes con iluminación rojiza, fondo tecnológico.”
- [ ] Iconos de partners (SVG)  
  _Manual: vectorizar logos reales.

## 6. Personal / Bio
- [x] **Retrato principal** (`bio/portrait.jpg`) ✅
  - Foto profesional corporativa con fondo rojo/negro degradado
  - 97KB, resolución alta, lista para web
  - _Fuente_: Foto corporativa existente (2025-10-28)
- [x] **Background futurista** (`bio/background.jpg`) ✅
  - Skyline futurista nocturno con neón rojo/cyan desde altura
  - 1920x1080px, 170KB
  - _Generado con Flux Dev ($0.003), soft focus para overlay de texto_
- [ ] Badges de arquetipos/skills (SVG)
  _Manual: diseño vectorial con iconos (Creador, Sabio, Mentor, Científico).

## 7. Hangar de Contacto
- [x] **Mapa caliente** (`contact/heatmap.png`) ✅
  - Heatmap rojo sobre mapa mundial oscuro, concentrado en Bogotá/LatAm
  - 1920x1080px, 725KB, estilo radar
  - _Generado con Flux Dev ($0.003)_
- [ ] Iconos sociales (SVG)
  _Manual: vectores oficiales (LinkedIn, GitHub, X, etc.).
- [x] **Ilustración sala de control** (`contact/hangar.png`) ✅
  - Interior de control room orbital con displays holográficos
  - 1920x1080px, 1.3MB, vista panorámica exterior
  - _Generado con Flux Dev ($0.003)_

## 8. HUD y UI
- [ ] Set HUD (barras, retículas, etc.) (`hud/*.svg`)  
  _Idea_: “Retículas circulares, grids hexagonales, líneas de lectura, indicadores minimalistas en rojo/cian.”
- [ ] Indicadores de scroll/dots (SVG)  
  _Manual: diseño vectorial simple acorde al HUD.
- [ ] Texturas/patterns (PNG 2048²)  
  _Idea_: “Superficie metálica oscura con líneas de circuito en rojo/cian.”

## 9. Tipografías
- [ ] Overcame Bold (WOFF2/WOFF)
- [ ] Audiowide Regular (WOFF2/WOFF)
- [ ] Alternativas web (Rajdhani, Inter) — confirmar licencias.  
  _Descargar desde Google Fonts / fuentes propias.

## 10. Modelos 3D / GLB
- [ ] Portal hero (`3d/portal.glb`)  
  _Idea_: “Anillo 3D con energías rojas, textura metálica, interior lumínico.”
- [ ] Pods/drones demos (`3d/pod-*.glb`)  
  _Idea_: “Drones esféricos con paneles HUD, uno por vertical.”
- [ ] Iconos 3D verticales (`3d/icon-*.glb`)  
  _Idea_: “Representación tridimensional de cada vertical (balón holográfico, torre, jaguar, cerebro, libro).”
- [ ] Texturas comprimidas (KTX2/WebP)

## 11. Copy y Metadatos
- [ ] JSON contenido por sección (`content/sections.json`)  
  _Incluir textos definitivos, CTA, métricas.
- [ ] Tabla clases/proyectos (`content/classes.json`, `content/projects.json`)  
  _Estructura: título, fecha, fase, tags, enlaces.
- [ ] Audio opcional (loop `.mp3`)  
  _Idea_: “Ambiente suave futurista con pulsos electrónicos.”
