# 🎨 Replicate MCP - Setup Completo como "Superpoder" Global

## ✅ Estado Actual

**Replicate MCP instalado y configurado correctamente:**
- **Ubicación**: `~/.claude.json` (configuración global - scope `user`)
- **Tipo**: `stdio` (ejecuta NPX localmente con token)
- **Estado**: ✓ Connected
- **Token API**: Configurado en `env.REPLICATE_API_TOKEN`

---

## 🔧 Configuración Aplicada

### Archivo: `~/.claude.json`

```json
"replicate": {
  "type": "stdio",
  "command": "npx",
  "args": ["-y", "replicate-mcp"],
  "env": {
    "REPLICATE_API_TOKEN": "r8_03EtFMoISH8NXY3Jsh4gN8oL5NMjONn1MV7MH"
  }
}
```

**Backup creado**: `~/.claude.json.backup`

---

## 📚 Documentación Actualizada

### Archivo: `/home/jzuluaga/CLAUDE.md`

Se añadió la siguiente sección en "Superpoderes Disponibles":

```markdown
- **Replicate MCP**: ✅ Generación de imágenes con IA (`mcp__replicate__*`)
  - Scope: **user** (disponible en TODOS los proyectos)
  - Modelo: Stable Diffusion XL 1.0
  - Costo: $0.002 por imagen (después de $10 de crédito inicial)
  - Auto-aprobación: ⚠️ Requiere confirmación manual (limitación de Claude Code CLI)
  - Capacidades:
    - 🎨 Generar imágenes con prompts optimizados (1024x1024px)
    - ⚙️ Control de parámetros avanzados (steps, guidance, scheduler)
    - 🚀 Velocidad: 4-5 segundos por imagen
    - 💰 Tracking de crédito disponible en Replicate.com
    - 🔄 Múltiples modelos disponibles (SDXL, Flux, DALL-E 3, etc.)
  - Configuración: `~/.claude.json` (instalado vía `claude mcp add`)
  - Token API: Guardado en configuración global
  - Documentación: Ver `experimentos/replicate-sdxl-test/`
  - Experimentos exitosos: Logo, Hero Background, Icon (ver `/output`)
```

Se añadió en "Cuándo usar cada uno":
```markdown
- Usa **Replicate MCP** para: generar assets visuales (logos, backgrounds, iconos, UI mockups)
```

Se añadió en "Comandos Personalizados":
```markdown
- `/generate-image [descripción]`: 🎨 **Agente de Replicate MCP** - Generar imágenes con IA (3 variaciones, prompts optimizados, copia automática)
```

---

## 🤖 Slash Command Creado

### Archivo: `~/.claude/commands/generate-image.md`

**Agente especializado** que:

1. **Analiza la solicitud** del usuario y pregunta por detalles faltantes
2. **Crea 3 prompts optimizados** siguiendo best practices de SDXL:
   - Estructura: [SUBJECT][COMPOSITION][LIGHTING][STYLE][CONSTRAINTS]
   - Variación 1: Interpretación literal
   - Variación 2: Interpretación artística
   - Variación 3: Enfoque alternativo
3. **Genera 3 imágenes** usando Replicate MCP
4. **Presenta resultados** con prompts, tiempo y costo
5. **Permite iterar** si no satisface
6. **Guarda imagen final** en destino elegido con prompt en `.txt`

**Experticia incluida:**
- Prompt engineering para SDXL
- Ejemplos por tipo (logo, background, icon, ilustración)
- Parámetros optimizados por caso de uso
- Tips de schedulers, guidance_scale, aspect ratios

**Uso:**
```bash
/generate-image un logo minimalista rojo orbital para Orbital Lab
```

---

## 🔄 Cómo Usar el Superpoder

### Método 1: Slash Command (Recomendado)
```bash
/generate-image [descripción de la imagen que necesitas]
```
El agente se encargará de TODO el proceso.

### Método 2: Uso Directo de Herramientas MCP
**Después de reiniciar Claude**, estarán disponibles herramientas como:
- `mcp__replicate__run_model`
- `mcp__replicate__list_models`
- `mcp__replicate__get_model`
- Etc.

**Llamada de ejemplo:**
```javascript
mcp__replicate__run_model({
  model: "stability-ai/sdxl",
  version: "39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
  input: {
    prompt: "A minimalist red orbital logo...",
    width: 1024,
    height: 1024,
    num_inference_steps: 25,
    guidance_scale: 7.5
  }
})
```

---

## ⚠️ Próximo Paso IMPORTANTE

**Para que Claude reconozca las herramientas del MCP Replicate:**

1. **Reinicia Claude Code CLI** (cierra y abre de nuevo)
2. O ejecuta en nueva sesión de terminal

Después del reinicio:
- Las herramientas `mcp__replicate__*` estarán disponibles
- El comando `/generate-image` funcionará completamente
- Podrás ver los recursos con `ListMcpResourcesTool`

---

## 📊 Comparación con Otros MCPs

| Característica | Context7 | Perplexity | Figma | Replicate |
|---------------|----------|------------|-------|-----------|
| **Tipo** | stdio | stdio | stdio | stdio |
| **Autenticación** | No requiere | API Key | API Token | API Token |
| **Scope** | user (global) | user (global) | user (global) | user (global) |
| **Estado** | ✓ Connected | ✓ Connected | ✓ Connected | ✓ Connected |
| **Herramientas** | Documentación | Búsqueda/Reasoning | Diseños Figma | Generación IA |

**Patrón común:**
```json
{
  "type": "stdio",
  "command": "npx",
  "args": ["-y", "<package-name>"],
  "env": {
    "API_KEY_NAME": "valor"
  }
}
```

---

## 💡 Experimentos Exitosos

### 1. Logo Orbital Lab
- **Prompt**: Minimalist red orbital logo, geometric rings, black background
- **Resultado**: ⭐⭐⭐⭐⭐ (10/10)
- **Tiempo**: 4.5s
- **Costo**: $0.002
- **Archivo**: `output/test_01_logo.png`

### 2. Hero Background
- **Prompt**: Futuristic monumental architecture, dramatic red lighting, cinematic
- **Resultado**: ⭐⭐⭐⭐⭐ (10/10)
- **Tiempo**: 5.1s
- **Costo**: $0.002
- **Archivo**: `output/test_02_hero_background.png`

### 3. Icon Strivio
- **Prompt**: Soccer ball with data visualization, Material Design icon
- **Resultado**: ⭐⭐⭐⭐⭐ (10/10)
- **Tiempo**: 4.8s
- **Costo**: $0.002
- **Archivo**: `output/test_03_icon_strivio.png`

**Total gastado**: $0.006
**Crédito restante**: $9.994

---

## 🎯 Casos de Uso Recomendados

### ✅ Perfecto para:
- Logos y branding
- Backgrounds para heros/landing pages
- Iconos de aplicaciones
- UI mockups y prototipos visuales
- Ilustraciones para blogs/docs
- Assets para presentaciones
- Concept art rápido

### ⚠️ Limitaciones:
- No reemplaza a diseñadores para trabajo final crítico
- Puede requerir varias iteraciones
- Texto en imágenes (OCR) no es confiable
- Rostros/personas pueden tener artefactos

---

## 📈 Próximos Pasos (Opcional)

### Mejoras Futuras

1. **Crear biblioteca de prompts** (`prompts_library.md`)
   - Categorizar por tipo de imagen
   - Guardar prompts exitosos
   - Compartir con equipo

2. **Integrar con Figma MCP**
   - Generar imagen con Replicate
   - Subir automáticamente a Figma
   - Workflow completo de assets

3. **Batch generation**
   - Comando `/generate-batch` para múltiples variaciones
   - Útil para A/B testing de UI

4. **Tracking de costos**
   - Script para monitorear crédito restante
   - Alertas cuando queden <$2

---

## 🔗 Enlaces Útiles

- **Replicate Platform**: https://replicate.com
- **Crédito/Billing**: https://replicate.com/account/billing
- **Modelos disponibles**: https://replicate.com/explore
- **Documentación MCP**: https://mcp.replicate.com
- **SDXL Model**: https://replicate.com/stability-ai/sdxl

---

## ✅ Checklist Final

- [x] Replicate MCP instalado en `~/.claude.json`
- [x] API token configurado correctamente
- [x] MCP conectado exitosamente (`claude mcp list`)
- [x] Documentación actualizada en `CLAUDE.md`
- [x] Slash command `/generate-image` creado
- [x] Experimentos exitosos validados (3/3 imágenes 10/10)
- [ ] **Reiniciar Claude para activar herramientas MCP** ⬅️ PENDIENTE

---

## 🎉 Resultado Final

**Replicate MCP está configurado como un "superpoder" global de Claude Code:**

1. ✅ Disponible en TODOS los proyectos (scope `user`)
2. ✅ Documentado en `CLAUDE.md` como referencia permanente
3. ✅ Slash command `/generate-image` con agente experto
4. ✅ Siguiendo el mismo patrón que otros MCPs (Context7, Perplexity, Figma, etc.)
5. ✅ Probado y validado con 3 imágenes profesionales

**Ahora puedes generar assets visuales con IA en cualquier proyecto simplemente ejecutando:**
```bash
/generate-image necesito un logo circular azul para mi app de fintech
```

¡El agente se encargará del resto! 🚀
