# Guía para generar iconos SVG de las verticales

Ubicación de destino: `recursos_compartidos/componentes/orbital_lab/assets/lab/`

Nombres de archivo recomendados:
```
icon-deportes.svg
icon-negocio.svg
icon-biologia.svg
icon-otros.svg
icon-academia.svg
```

## Estilo general
- Monocromo (preferiblemente blanco o rojo orbital) sobre fondo transparente.
- Trazo limpio, grosor uniforme.
- Geometría simple, estilo sci-fi/lineal.
- Tamaño pensado para 128×128 px, pero escalará sin problemas por ser vectorial.

## Instrucciones por vertical

### 1. Deportes (`icon-deportes.svg`)
- Motivo: balón o silueta con líneas de tracking.
- Prompt sugerido: “minimal futuristic sports icon with a holographic soccer ball and orbiting tracking lines, single color line art, no text.”

### 2. Negocio (`icon-negocio.svg`)
- Motivo: skyline/torre con antena o radar indicando audiencias.
- Prompt: “futuristic smart city icon with antenna beams, clean line art, single color, no text.”

### 3. Biología (`icon-biologia.svg`)
- Motivo: ADN estilizado o jaguar con sensores.
- Prompt: “cybernetic jaguar head combined with DNA helix lines, minimal line icon, single stroke.”

### 4. Otros (`icon-otros.svg`)
- Motivo: superagentes/datos corriendo (engranaje + nodos/drones).
- Prompt: “AI automation icon with gear and network nodes, sci-fi line art, monochrome.”

### 5. Academia (`icon-academia.svg`)
- Motivo: libro/hoja orbital con halo.
- Prompt: “futuristic book icon with orbital halo and light rays, minimal line art, single color.”

## Pasos generales
1. Genera cada icono en la herramienta (IA, Figma, Illustrator).
2. Asegúrate de limpiar nodos/convertir a trazos simples.
3. Exporta como `SVG` con fondo transparente.
4. Guarda cada archivo con el nombre indicado en la carpeta `lab/`.
5. Verifica visualmente (`inkscape`/`browser`) antes de marcar la casilla en `docs/brand/assets-checklist.md`.
