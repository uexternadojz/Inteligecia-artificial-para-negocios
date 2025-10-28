# Glows - Notas de Post-Procesamiento

## Estado Actual

Los glows fueron generados con **Flux Dev** que produce imágenes con **fondo negro sólido** (no alpha transparency nativa).

## Archivos Generados

| Archivo | Fecha | Modelo | Resolución | Tamaño | Estado Alpha |
|---------|-------|--------|------------|--------|--------------|
| `glow-red-01.png` | 2025-10-28 | Flux Dev | 1024x1024 | 622KB | ❌ Negro sólido |
| `glow-red-02.png` | Pendiente | Flux Dev | 1024x1024 | ~600KB | ❌ Negro sólido |
| `glow-cyan-01.png` | Pendiente | Flux Dev | 1024x1024 | ~600KB | ❌ Negro sólido |
| `glow-red-wide.png` | Pendiente | Flux Dev | 1920x1080 | ~800KB | ❌ Negro sólido |

## Uso Actual (Sin Post-Procesamiento)

Los glows **funcionan correctamente** usando blend modes CSS:

```css
.glow-overlay {
  mix-blend-mode: screen;  /* Ignora el negro, solo muestra luminosidad */
  /* O también: */
  mix-blend-mode: add;
  mix-blend-mode: lighten;
}
```

**Ventaja:** No requiere post-proceso, funciona directo en web.

---

## Post-Procesamiento (Si Se Necesita Alpha Transparency)

### Caso de Uso

Si necesitas **alpha channel real** (por ejemplo, para usar en canvas, video compositing, o sin blend modes), realizar este proceso:

### Script de Conversión (ImageMagick)

```bash
# Instalar ImageMagick si no está disponible
sudo apt install imagemagick

# Convertir negro a transparente (threshold ajustable)
convert glow-red-01.png \
  -fuzz 15% \
  -transparent black \
  glow-red-01-alpha.png

# Batch para todos los glows
for file in glow-*.png; do
  convert "$file" \
    -fuzz 15% \
    -transparent black \
    "${file%.png}-alpha.png"
done
```

### Parámetros Ajustables

- **`-fuzz 15%`**: Tolerancia para detectar "casi negro" (ajustar si hay halos residuales)
- **`-transparent black`**: Convierte negro a alpha
- **Salida:** Genera versiones `-alpha.png` con transparencia real

### Optimización Adicional

```bash
# Optimizar tamaño final con pngquant
pngquant --quality=80-95 glow-red-01-alpha.png -o glow-red-01-optimized.png
```

---

## Prompts Originales

### glow-red-01.png
```
Circular red energy flare for web overlay, intense red glow (#ED2024) radiating from bright center point, smooth gradient falloff to transparent edges, volumetric lighting rays, lens flare effect, no background (alpha transparency), circular composition 1024x1024, suitable for blend mode screen or add, ultra detailed light particles, cinematic quality, high contrast center to soft edges, orbital lab aesthetic
```

**Modelo:** Flux Dev
**Costo:** $0.003
**Generación:** ~5s

---

## TODO: Post-Procesamiento

- [ ] Evaluar si se necesita alpha transparency real
- [ ] Si sí: ejecutar script de conversión con ImageMagick
- [ ] Generar versiones optimizadas con pngquant
- [ ] Actualizar referencias en documentación
- [ ] Crear comparativa visual (blend mode vs alpha)

---

**Última actualización:** 2025-10-28
**Responsable:** Claude + Julián
