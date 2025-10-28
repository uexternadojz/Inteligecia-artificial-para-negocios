# Glosario de Assets — Orbital Vinyl Collection

Organización y seguimiento de los recursos visuales que alimentarán el micrositio de la materia.

## 1. Estructura de carpetas

```
assets/
├── hero/                  # Hero principal y loops asociados
├── vinyls/
│   ├── clase-01/          # Portadas y loops Clase 01
│   ├── clase-02/          # Portadas y loops Clase 02
│   ├── clase-03/          # Portadas y loops Clase 03
│   └── futuras/           # Reservas para próximas clases
├── spines/                # Texturas verticales de “lomo” por clase
├── halos/                 # Fondos y halos para modales / overlays
├── banners/               # Ilustraciones conceptuales de secciones
├── icons/                 # Iconos lineales de herramientas y HUDs
└── patterns/              # Texturas genéricas (circuitos, espectrogramas)
```

## 2. Tabla de control de assets

| Categoría | Asset | Formato esperado | Ubicación objetivo | Estado | Notas |
|-----------|-------|------------------|--------------------|--------|-------|
| Hero | Ilustración hero estática | `.webp` (≥2400px ancho) | `assets/hero/hero-lab.webp` | ☑ Listo | Recorte + upscale 2048×1280 desde Gemini (2025-10-28) |
| Hero | Loop hero animado (opcional) | `.webm` / `.mp4` (≤8s) | `assets/hero/hero-loop.webm` | ☑ Listo | Loop generado (Hailuo → recorte 4:5, ffmpeg, 2025-10-28) |
| Clase 01 | Portada vinilo | `.webp` (`@1x/@2x`) | `assets/vinyls/clase-01/vinilo.webp` | ☑ Listo | Imagen actualizada (Gemini) — prompt ajustado “corporate ai control room…” (2025-10-26) |
| Clase 01 | Loop hover | `.webm` / `.mp4` | `assets/vinyls/clase-01/vinilo-loop.webm` | ☐ Pendiente | Rotación / glow |
| Clase 01 | Spine | `.png` (transparente) | `assets/spines/clase-01.png` | ☑ Placeholder | Gradiente base generado con Pillow (2025-10-28). Reemplazar por textura final. |
| Clase 01 | Fondo modal | `.webp` | `assets/halos/clase-01.webp` | ☑ Placeholder | Gradiente oscuro orbital (script local, 2025-10-28). |
| Clase 02 | Portada vinilo | `.webp` | `assets/vinyls/clase-02/vinilo.webp` | ☑ Placeholder | Arte temporal generado con Pillow (2025-10-28). Sustituir por ilustración IA. |
| Clase 02 | Loop hover | `.webm` / `.mp4` | `assets/vinyls/clase-02/vinilo-loop.webm` | ☐ Pendiente | DJ coding |
| Clase 02 | Spine | `.png` | `assets/spines/clase-02.png` | ☑ Placeholder | Lomo placeholder gradiente (Pillow, 2025-10-28). |
| Clase 02 | Fondo modal | `.webp` | `assets/halos/clase-02.webp` | ☑ Placeholder | Glow rojizo base (script local, 2025-10-28). |
| Clase 03 | Portada vinilo | `.webp` | `assets/vinyls/clase-03/vinilo.webp` | ☑ Placeholder | Arte temporal generado con Pillow (2025-10-28). Sustituir por ilustración IA. |
| Clase 03 | Loop hover | `.webm` / `.mp4` | `assets/vinyls/clase-03/vinilo-loop.webm` | ☐ Pendiente | Galería IA |
| Clase 03 | Spine | `.png` | `assets/spines/clase-03.png` | ☑ Placeholder | Lomo placeholder gradiente (Pillow, 2025-10-28). |
| Clase 03 | Fondo modal | `.webp` | `assets/halos/clase-03.webp` | ☑ Placeholder | Glow cian base (script local, 2025-10-28). |
| Secciones | Banner Metodología | `.webp` | `assets/banners/metodologia.webp` | ☐ Pendiente | 16:9 o 3:2 |
| Secciones | Banner Herramientas | `.webp` | `assets/banners/herramientas.webp` | ☐ Pendiente | |
| Secciones | Banner Casos Orbital | `.webp` | `assets/banners/casos-orbital.webp` | ☐ Pendiente | |
| Iconos | Lovable | `.svg` | `assets/icons/lovable.svg` | ☐ Pendiente | Lineal rojo/cian |
| Iconos | Replit | `.svg` | `assets/icons/replit.svg` | ☐ Pendiente | |
| Iconos | v0.dev | `.svg` | `assets/icons/v0.svg` | ☐ Pendiente | |
| Iconos | Claude | `.svg` | `assets/icons/claude.svg` | ☐ Pendiente | |
| Iconos | Otros (placeholder) | `.svg` | `assets/icons/otros.svg` | ☐ Pendiente | Expandible |
| Patrones | Circuitos | `.webp` | `assets/patterns/circuitos.webp` | ☐ Pendiente | Para fondos |
| Patrones | Malla datos | `.webp` | `assets/patterns/malla-datos.webp` | ☐ Pendiente | |

> Marca cada asset como completado (`☑`) y agrega notas relevantes (prompt usado, versión IA, fecha) para mantener trazabilidad.

## 3. Notas operativas
- Mantener cada carpeta con archivos finales optimizados; reservar derivados (PSD/PNG sin comprimir) en carpeta externa si se requieren.
- Nombrar versiones adicionales con sufijo `-alt` o `-v2`.
- Registrar prompts y ajustes de post-proceso en `notes.md` dentro de cada carpeta si se necesita historial creativo.
