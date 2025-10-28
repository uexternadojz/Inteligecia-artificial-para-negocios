# Manifiesto de Marca — Julián Zuluaga · Orbital Lab

## 0. Prólogo

Soy Julián Zuluaga. Orbital Lab es la extensión viva de mi marca personal. Somos ciencia, diseño y negocio orbitando con propósito. Creemos que **ver es entender** y que la inteligencia artificial solo cobra sentido cuando transforma historias humanas.

Este manifiesto fija el ADN para cada pieza que construyamos: web docente, guías HTML, presentaciones, productos, clases, superagentes y colaboraciones.

---

## 1. Visión y Razón de Ser

- **Visión**: convertir ideas en inteligencia e impacto real. 
- **Misión**: diseñar tecnología que interprete, prediga y decida, conectando datos con decisiones humanas.
- **Ambición**: liderar desde Latinoamérica un hub global de innovación aplicada donde talento, estética y datos convergen.

### Mantra
> "Desarrollar inteligencia que vea, piense y transforme." 

---

## 2. Arquetipos y Personalidad

| Arquetipo | Manifestación |
|-----------|---------------|
| **El Creador** | Experimenta, prototipa, compone futuros posibles. Cada clase, demo o producto es una pieza artesanal. |
| **El Sabio** | Traduce complejidad técnica en conocimiento claro, accionable y ético. |

**Tono:** visionario, técnico, empático, inspirador.<br>
**Actitud:** rebelde elegante; rigurosidad + sensibilidad estética.<br>
**Valores:** precisión, ética, pedagogía, innovación responsable.

---

## 3. Pilares de Marca

1. **Tecnología visible** — Interfaces orbitales, mallas de datos, HUDs que revelan procesos internos.
2. **Minimalismo de poder** — Negro profundo como lienzo, rojo orbital como energía. Espacios negativos que permiten respirar.
3. **Narrativa humana** — Deporte, empresa, aula y conservación como escenarios donde la IA genera impacto tangible.
4. **Aprendizaje aplicado** — Clases, workshops y documentación que enseñan haciendo.
5. **Interoperabilidad** — Repositorios, agentes, datasets y scripts conectados para reutilizar conocimiento.

---

## 4. Voz y Storytelling

### Principios narrativos
- Contextualiza con preguntas (“¿Qué sucede si…?”).
- Visualiza antes de explicar (“Esto es lo que vimos”).
- Conecta con acción (“Así lo aplicamos con Strivio / Superagent / Clase”).
- Cierra con invitación (“Explora el laboratorio”, “Replica el pipeline”).

### Guía de lenguaje
- Evita jerga innecesaria. Usa analogías visuales.
- Balancea español + términos técnicos habituales en IA.
- Incluye referencias y código fuente siempre que sea posible.

---

## 5. Sistema Visual

### Paleta Base
| Uso | Color | Código |
|-----|-------|--------|
| Fondo principal | Negro profundo | `#000000` / `#0b0b0f` |
| Acento orbital | Rojo vivo | `#ED2024` |
| Resaltado cálido | Rojo claro | `#FF3B30` |
| Acento frío (datos) | Cian lumínico | `#00D4FF` |
| Neutros | Gris grafito / plata | `#1F1F28`, `#A2A5B3` |

### Tipografía
- **Titulares**: Overcame Bold (u opción web equivalente como *Rajdhani SemiBold*).
- **Cuerpo**: Audiowide Regular (fallback *Inter* o *Exo 2*).
- **Código / datos**: Fira Code.

### Patrones y recursos gráficos
- Órbitas y halos luminosos (SVG animados, blur sutil).
- Líneas de circuito y mallas de puntos (backgrounds repetibles).
- Cards con bordes luminosos (1px `rgba(237,32,36,0.4)` + glow exterior `rgba(237,32,36,0.2)`).
- Botones con animación `box-shadow` pulsante y estados de enfoque accesibles.

---

## 6. Arquitectura de Experiencia

### Macro-secciones 
1. **Home / Identidad** — Hero 3D, statement “Ver es entender”, CTAs primarios (Explorar Lab · Ver Cursos). 
2. **Laboratorio** — Strivio, Lighthouse, Jaguar, AI Systems, Academia. Cards modulares con video/demo + métricas.
3. **Docencia** — Clases, syllabus, guías interactivas, bibliografía. Integración directa con `materias/` del repo.
4. **Investigación & Blog** — Artículos técnicos, experimentos, papers.
5. **Recursos** — Datasets, notebooks, prompts, scripts, slide decks.
6. **Contacto & Colaboración** — Newsletter, propuestas, mentoría.

### Micro-interacciones
- Scroll con parallax suave en secciones hero.
- Tabs o chips para filtrar verticales.
- Previsualizaciones de guías (iframe / modal) sin salir del sitio.

---

## 7. Lineamientos Técnicos

- **Framework recomendado**: Astro 4.x + TailwindCSS + islands React/Svelte para componentes interactivos.
- **Búsqueda on-site**: Fuse.js con índice generado desde `content/`.
- **Visualizaciones**: Plotly.js (lazy load) y embebidos Observable/p5.js. Siempre acompañados de tabla de datos accesible.
- **Accesibilidad**: contraste AA, navegación por teclado, `prefers-reduced-motion`, texto alternativo descriptivo.
- **Performance**: LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1. Imágenes optimizadas (AVIF/WebP) y prefetch inteligente.
- **Internacionalización**: contenido principal en español, secciones críticas traducibles al inglés.

---

## 8. Ecosistema de Contenido

| Vertical | Output | Frecuencia | Repositorio |
|----------|--------|------------|-------------|
| Strivio | Casos estudio, dashboards, videoclips | Mensual | `projects/strivio/` |
| Lighthouse Audience | Reportes atención OOH, demos AR | Bimestral | `projects/lighthouse/` |
| Jaguar Orbital | Documentos de conservación, datasets anotados | Trimestral | `projects/jaguar/` |
| AI Systems | Manuales de superagentes, integraciones ERP/CRM | Continua | `projects/ai-systems/` |
| Academia Orbital | Cursos, workshops, handbooks | Semestral | `materias/`, `docs/brand/` |

---

## 9. Código Ético

1. **Transparencia**: siempre declarar fuentes de datos, modelos, limitaciones.
2. **Privacidad**: anonimizar información sensible, seguir protocolos de seguridad.
3. **Inclusión**: ejemplos y datasets representativos; lenguaje no sesgado.
4. **Sostenibilidad**: medir huella de cómputo; optimizar inferencias y almacenamiento.

---

## 10. Ritual Creativo

1. **Observa**: dataset, vídeo, interacción humana.
2. **Dibuja**: wireframes, órbitas, diagramas.
3. **Prototipa**: notebook, script, mockup.
4. **Relata**: escribe la historia y muestra el impacto.
5. **Comparte**: documenta en el repo, publica en la web, conviértelo en clase.

---

## 11. Roadmap de Marca

1. **Q4 2025** — Moodboard definitivo, tokens de diseño (`theme.json`), primeros componentes UI reutilizables.
2. **Q1 2026** — Lanzamiento del site personal (Home + Lab + Docencia), migración de recursos previos.
3. **Q2 2026** — Biblioteca interactiva (search, filtros, previsualizadores). Integración con superagentes.
4. **Q3 2026** — Versión bilingüe y micrositios por vertical.
5. **Q4 2026** — Experiencia 3D inmersiva (WebGL) para storytelling de proyectos.

---

## 12. Cierre

Este manifiesto es contrato creativo. Nos recuerda que cada entrega —guía CRISP-DM, clase, dashboard, pieza audiovisual o superagente— debe resonar con la estética orbital y con la promesa de hacer visible la inteligencia. Cualquier decisión de diseño, narrativa o tecnología tiene una sola pregunta filtro: **¿Ayuda a ver y entender mejor?**

> *Si la respuesta es sí, está en órbita.*
