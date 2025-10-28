# 🎯 Referencia Rápida: Verticales de Orbital Lab

**Última actualización:** Octubre 28, 2025

---

## ⚠️ IMPORTANTE: Verticales vs Proyectos

### Las 5 Verticales (Categorías Permanentes)

Las **verticales** son las **áreas de enfoque** de Orbital Lab. Son categorías genéricas que NO cambian:

| # | Vertical | Descripción |
|---|----------|-------------|
| 1 | **Deportes** | Analítica deportiva con visión por computador |
| 2 | **Negocio** | Soluciones de inteligencia empresarial y marketing |
| 3 | **Biología** | Conservación ambiental y monitoreo de biodiversidad |
| 4 | **Otros** | Automatización corporativa y sistemas de IA |
| 5 | **Academia** | Formación y educación en IA aplicada |

### Proyectos Actuales (Ejemplos por Vertical)

Los **proyectos** son implementaciones específicas dentro de cada vertical. Estos **pueden cambiar** con el tiempo:

| Vertical | Proyecto Ejemplo Actual | Descripción |
|----------|------------------------|-------------|
| Deportes | Strivio | Tracking multijugador, clips automáticos, heatmaps |
| Negocio | Lighthouse Audience | Analítica de audiencias para publicidad OOH |
| Biología | Jaguar Orbital | Monitoreo de fauna con cámaras trampa + IA |
| Otros | AI Systems / Superagents | RAG, agentes CLI, integraciones ERP/CRM |
| Academia | Academia Orbital | Cursos aplicados, talleres, formación continua |

---

## Nomenclatura Consistente

### Para Assets (archivos):
```bash
# ✅ CORRECTO: Usar nombre de VERTICAL (categoría genérica)
icon-deportes.svg
icon-negocio.svg
icon-biologia.svg
icon-otros.svg
icon-academia.svg

deportes-loop.mp4
negocio-background.jpg
biologia-hero.png

# ❌ INCORRECTO: NO usar nombres de proyectos específicos
# strivio-icon.png          ← NO
# lighthouse-loop.mp4       ← NO
# jaguar-background.jpg     ← NO
```

### Para Referencias en Código:
```javascript
// ✅ CORRECTO: Las verticales son las categorías permanentes
const verticals = [
  { id: 'deportes', name: 'Deportes', currentProject: 'Strivio' },
  { id: 'negocio', name: 'Negocio', currentProject: 'Lighthouse Audience' },
  { id: 'biologia', name: 'Biología', currentProject: 'Jaguar Orbital' },
  { id: 'otros', name: 'Otros', currentProject: 'AI Systems / Superagents' },
  { id: 'academia', name: 'Academia', currentProject: 'Academia Orbital' }
];
```

### Para Documentación:
```markdown
# ✅ CORRECTO: Referenciar vertical con proyecto como ejemplo
- **Deportes** (ej. Strivio: analítica deportiva)
- **Negocio** (ej. Lighthouse Audience: audiencias OOH)
- **Biología** (ej. Jaguar Orbital: conservación)
- **Otros** (ej. AI Systems: automatización)
- **Academia** (ej. Academia Orbital: formación)

# ❌ INCORRECTO: Tratar proyectos como verticales
- **Strivio**              ← Esto es un proyecto, no una vertical
- **Lighthouse Audience**  ← Esto es un proyecto, no una vertical
```

---

## Conceptos Visuales por Vertical

### 1. Deportes
**Keywords para generación:**
- Balón deportivo, redes neuronales, tracking
- Heatmaps, trayectorias de movimiento
- Métricas deportivas, análisis táctico
- Geometría de cancha, posiciones
- **Ejemplo actual:** Strivio (analítica deportiva)

**Colores característicos:**
- Primario: Rojo Orbital (#ED2024)
- Secundario: Verde campo, líneas blancas
- Acento: Cyan para datos (#00D4FF)

### 2. Negocio
**Keywords para generación:**
- Skyline urbano, edificios, antena/faro
- Rayos de luz, análisis de audiencias
- Publicidad exterior, vallas, pantallas
- Flujos de personas, heatmaps urbanos
- **Ejemplo actual:** Lighthouse Audience (audiencias OOH)

**Colores característicos:**
- Primario: Rojo Orbital (#ED2024)
- Secundario: Gris urbano, luces de ciudad
- Acento: Cyan (#00D4FF), amarillo publicitario

### 3. Biología
**Keywords para generación:**
- Silueta de jaguar, fauna silvestre
- Selva, naturaleza, ecosistemas
- Sensores ambientales, cámaras trampa
- Patrón de ADN, biodiversidad
- Nodos de monitoreo
- **Ejemplo actual:** Jaguar Orbital (conservación)

**Colores característicos:**
- Primario: Rojo Orbital (#ED2024)
- Secundario: Verde selva, negros profundos
- Acento: Cyan para sensores (#00D4FF)

### 4. Otros
**Keywords para generación:**
- Engranajes cerebrales, redes neuronales
- Automatización, flujos de datos
- Terminales, integraciones de sistemas
- Nodos conectados, arquitectura distribuida
- ERP/CRM visuales, dashboards corporativos
- **Ejemplo actual:** AI Systems / Superagents (automatización)

**Colores característicos:**
- Primario: Rojo Orbital (#ED2024)
- Secundario: Gris metálico, azul corporativo
- Acento: Cyan para conexiones (#00D4FF)

### 5. Academia
**Keywords para generación:**
- Libro, conocimiento, educación
- Circuitos de datos emanando
- Aula holográfica, símbolos educativos
- Orbitas de aprendizaje
- Ética digital, pensamiento crítico
- **Ejemplo actual:** Academia Orbital (formación)

**Colores característicos:**
- Primario: Rojo Orbital (#ED2024)
- Secundario: Dorado educativo, blanco académico
- Acento: Cyan para innovación (#00D4FF)

---

## Prompts Base para Generación

### Estructura Estándar
```
[VERTICAL_NAME] icon: [CONCEPT] in minimalist futuristic style,
geometric linework on black background with red orbital accents (#ED2024),
cyan highlights (#00D4FF) for tech elements,
clean vector-style illustration, sharp edges,
512x512 resolution, high contrast,
no text, no borders, professional tech aesthetic
```

### Ejemplos Específicos por Vertical

**Deportes:**
```
Sports analytics icon: soccer ball with neural network tracking lines,
geometric heatmap patterns, minimalist futuristic style,
red and black palette with cyan data accents,
clean vector illustration, 512x512
```

**Negocio:**
```
Business analytics icon: city skyline with data beacon emitting
audience analysis rays, architectural minimal tech style,
red orbital accents on black, cyan data streams,
512x512 vector illustration
```

**Biología:**
```
Conservation icon: wildlife silhouette with DNA pattern and orbital sensors,
nature-technology fusion, organic tech lines,
red and black with green accent, cyan tech elements,
512x512 minimal illustration
```

**Otros:**
```
Automation icon: brain-gear hybrid with connected nodes,
intelligent systems representation, mechanical-neural style,
red orbital on black, cyan connection lines,
512x512 tech illustration
```

**Academia:**
```
Education icon: orbital book with data circuits emanating,
knowledge technology fusion, educational-futuristic style,
red and black with golden educational accent, cyan innovation,
512x512 vector illustration
```

---

## Archivos de Documentación Oficial

1. **Identidad de Marca:** `docs/orbital_lab.md`
2. **Submarcas Detalladas:** `docs/submarcas_orbital.md`
3. **Manifesto Completo:** `docs/brand/manifesto.md`
4. **Checklist de Assets:** `docs/brand/assets-checklist.md`
5. **Esta Referencia:** `docs/brand/VERTICALES_REFERENCE.md`

---

## Uso en Generación de Assets

**Al generar assets para Orbital Lab, SIEMPRE:**

1. ✅ Usar las 5 **verticales** (categorías genéricas: Deportes, Negocio, Biología, Otros, Academia)
2. ✅ Nombrar archivos con el nombre de la **vertical**, NO del proyecto
3. ✅ Aplicar paleta consistente (Negro + Rojo #ED2024 + Cyan #00D4FF)
4. ✅ Mantener estilo futurista minimalista
5. ✅ Usar formato lowercase-hyphenated: `deportes-icon.svg`, `negocio-loop.mp4`

**Evitar:**
- ❌ Inventar nuevas verticales/categorías
- ❌ Usar nombres de proyectos en archivos (strivio, lighthouse, jaguar)
- ❌ Mezclar conceptos entre verticales
- ❌ Usar paletas de color inconsistentes

**Recordatorio Clave:**
- 🔵 **Vertical** = Categoría permanente (Deportes, Negocio, Biología, Otros, Academia)
- 🟢 **Proyecto** = Implementación específica temporal (Strivio, Lighthouse, Jaguar, etc.)
- 📁 **Assets** = Siempre se nombran por vertical, NO por proyecto

---

**Este documento es la fuente de verdad para las verticales de Orbital Lab.**
