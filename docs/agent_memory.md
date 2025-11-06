# Agent Memory

Eres un agente CLI colaborando en el repo `docencia`. Objetivo: producir y mantener materiales docentes interactivos reutilizando las herramientas compartidas.

## Instrucciones clave

1. Revisa siempre la estructura principal (`README.md`, `ARCHITECTURE.md`, `materias/`, `recursos_compartidos/`, `herramientas/`, `skills/`, `site/`).
2. Genera guías HTML reutilizando `python herramientas/scripts/generar_guia_crispdm.py -d <dataset> -o <salida>`; si trabajas dentro de una clase usa el wrapper local existente.
3. Centraliza los datasets en `recursos_compartidos/datasets/` (ejemplo: `mineria-de-datos/supermarket_analysis.csv`) y referencia rutas relativas desde las clases.
4. Para nuevas sesiones ejecuta el scaffold `python herramientas/scripts/nueva_clase.py --help` y completa el README generado.
5. Crea entornos locales con `python -m venv .venv` y `pip install -r herramientas/requirements.txt`; nunca subas carpetas `venv/`.
6. Componentes, plantillas y tutoriales comunes deben vivir en `recursos_compartidos/` con documentación actualizada.
7. Cada clase debe documentarse en `materias/<materia>/README.md` y seguir la convención `YYYY-MM-DD-clase-XX-tema`.
8. Mantén consistencia en los assets: si un recurso puede reutilizarse, muévelo a compartidos y enlázalo.

## Crear Nueva Clase en IA para Negocios (Sistema Habilitador)

**Cuando el usuario pida crear una nueva clase para IA para Negocios:**

### 1. Consultar Guía Completa
Leer: `materias/inteligencia-artificial-para-negocios/CREAR_NUEVA_CLASE.md` (instructivo detallado paso a paso)

### 2. Workflow Híbrido Recomendado

**Fase 1: Planificación (20 min - Humano + AI)**
- Revisar syllabus y objetivos pedagógicos
- Definir mood visual (1-2 oraciones descriptivas)
- Curar stack de herramientas (3-6)
- Definir métricas clave (4 métricas balanceadas red/cyan)
- Esbozar casos de uso (2-3)

**Fase 2: Script Automatizado (2 min - Python)**
```bash
python herramientas/scripts/nueva_clase_ia_negocios.py \
  --numero XX \
  --fecha YYYY-MM-DD \
  --tema "Título Clase" \
  --mood "Descripción visual" \
  --stack "Tool1,Tool2,Tool3" \
  --metrics "valor:label:accent,..."
```

Outputs: estructura carpetas, placeholders (spines/halos), templates data/página, actualización course.ts

**Fase 3: Generación Assets (15 min - IA Especializada)**
- Activar skill `image-generation-expert` (automático con keywords)
- Generar vinyl hero (1024x1024) con Flux Dev
- Generar halo background (1920x1080) complementario
- Optimizar PNG → WebP (`cwebp -q 85`)

**Fase 4: Contenido (60-90 min - Humano + AI Guiado)**
Completar `clase-XX-data.ts`:
- heroData (métricas, CTAs)
- fundamentals (4-6 items Bento Grid)
- tools (2-4 herramientas con specs)
- workflow (4-6 pasos, opcional)
- useCases (2-3 casos reales)
- promptExamples (5-7 categorizados)
- bestPractices (6 DOs + 6 DON'Ts)
- videoData (si aplica)
- resources (3-5 links)

**Fase 5: Testing (10 min - Humano)**
```bash
cd site/
npm run dev  # http://localhost:4321
```
Verificar checklist en CREAR_NUEVA_CLASE.md

**Fase 6: Commit y Deploy (5 min)**
```bash
git add .
git commit -m "feat: Add Clase XX - [Tema] with full content and assets"
git push origin main
```

### 3. Brand System (Crítico)

**Paleta Orbital Lab:**
- Negro: #000000 / #0b0b0f
- Rojo: #ED2024 (acción, urgencia)
- Cyan: #00D4FF (datos, tech)

**Verticales (NO proyectos):**
1. Deportes (ej: Strivio)
2. Negocio (ej: Lighthouse)
3. Biología (ej: Jaguar)
4. Otros (ej: AI Systems)
5. Academia (ej: Academia Orbital)

**Naming:** Siempre por vertical (`deportes-icon.svg`), NUNCA por proyecto (`strivio-icon.svg`)

### 4. Capacidades MCP Disponibles

- **Image Generation Expert Skill:** Flux Dev ($0.0035/img), SDXL, Flux Pro
- **Playwright MCP:** Screenshots de logos, testing browser
- **Google Drive MCP:** Embed de videos con preview
- **Context7 MCP:** Documentación actualizada de librerías

### 5. Pasos Creativos vs Mecánicos

**Automatizables (script):**
- Estructura de carpetas
- Placeholders (spines/halos con Pillow)
- Templates data/página
- Actualización course.ts

**Asistidos (IA guiada):**
- Prompts para vinyl/halo (basados en mood)
- Generación de imágenes (Flux Dev)
- Optimización WebP
- Selección de iconos emoji

**Requieren expertise (humano/AI):**
- Redacción fundamentals (narrativa pedagógica)
- Diseño workflow steps (estructura única)
- Casos de uso (conexión Orbital Lab)
- Biblioteca de prompts (experiencia práctica)
- Best practices (errores comunes de clase real)

### 6. Referencias Clave

- **Instructivo completo:** `materias/inteligencia-artificial-para-negocios/CREAR_NUEVA_CLASE.md`
- **Script automatizado:** `herramientas/scripts/nueva_clase_ia_negocios.py`
- **Brand manifesto:** `docs/brand/manifesto.md`
- **Verticales reference:** `docs/brand/VERTICALES_REFERENCE.md`
- **Concepto diseño:** `materias/inteligencia-artificial-para-negocios/site/CONCEPTO.md`
- **Clases existentes (ejemplos):** `site/src/data/clase-02-data.ts`, `clase-03-data.ts`, `clase-04-data.ts`

### 7. Tiempos Estimados

| Fase | Tiempo | Acumulado |
|------|--------|-----------|
| Planificación | 20 min | 20 min |
| Script automatizado | 2 min | 22 min |
| Generación assets | 15 min | 37 min |
| Contenido | 60-90 min | 97-127 min |
| Testing | 10 min | 107-137 min |
| Commit/Deploy | 5 min | **112-142 min (~2h)** |

vs Manual completo: ~3h
**Ahorro: 38-68 min (21-38%)**

### 8. Troubleshooting

- **Imagen no cumple expectativas:** Iterar prompt 2-3 veces, ajustar keywords
- **Logo faltante:** Descargar oficial (Press Kit) o usar Playwright screenshot
- **Video no embebe:** Verificar permisos Drive ("Anyone with link"), usar `/preview` no `/view`
- **course.ts error:** Verificar sintaxis array, ejecutar `npm run build` para validar
- **Build falla:** Probar `npm run build` local, verificar imports de assets

### 9. Cuándo Usar el Sistema

**Usar cuando:**
- Usuario pide "crear nueva clase", "añadir clase", "clase XX"
- Hay material pedagógico listo (README, transcript, video)
- Stack de herramientas ya definido

**NO usar cuando:**
- Solo se pide actualizar contenido existente
- Es otra materia (no IA para Negocios)
- Material pedagógico no está preparado

### 10. Notas Importantes

- Cada clase debe tener **personalidad visual propia** (no copy-paste)
- Métricas deben ser **específicas del tema** (no genéricas)
- Fundamentals con **narrativa adaptada** al contenido
- Tools con **specs técnicas reales** y pricing actualizado
- Use cases deben **conectar con proyectos Orbital Lab** cuando sea posible
- Best practices basadas en **experiencia real de clase** (no genéricas)
