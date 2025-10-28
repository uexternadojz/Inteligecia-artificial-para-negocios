# ✅ Setup Completo - Nano Banana Test

## 📦 Archivos Creados

```
experimentos/nano-banana-test/
├── test_nanoba.py          ✅ Script principal (244 líneas)
├── .env.example            ✅ Plantilla de configuración
├── requirements.txt        ✅ Dependencias Python
├── README.md               ✅ Documentación completa
├── SETUP_COMPLETO.md       ✅ Este archivo
└── output/                 ✅ Carpeta para imágenes generadas
```

## 🎯 Estado Actual

### ✅ Completado

1. **Script de prueba** (`test_nanoba.py`):
   - Sistema de carga de API key (3 niveles de fallback)
   - Generación de 3 imágenes de prueba
   - Prompts estructurados con formato modular
   - Manejo de errores y logging detallado
   - Rate limiting automático (4s entre requests)
   - Resumen de resultados al final

2. **Archivos de soporte**:
   - `.env.example` con instrucciones claras
   - `requirements.txt` con versiones específicas
   - `README.md` con guía completa de setup
   - `.gitignore` en la raíz del repo (protege .env, output/, venv/)

3. **Documentación**:
   - Troubleshooting completo
   - Explicación de costos y límites
   - Criterios de éxito
   - Referencias a documentación oficial

### ⏳ Pendiente (Requiere Usuario)

1. **Obtener API Key**:
   - Ve a: https://aistudio.google.com
   - Inicia sesión con tu cuenta de Google
   - Crea una nueva API key (botón "Get API key" en menú lateral)
   - Es **GRATIS** (free tier: 1,500 requests/día)

2. **Configurar API Key** (elige una opción):

   **Opción A - Variable de entorno (recomendado):**
   ```bash
   export GOOGLE_API_KEY='tu_api_key_aqui'
   ```

   **Opción B - Archivo .env local:**
   ```bash
   cd experimentos/nano-banana-test
   cp .env.example .env
   # Edita .env y añade tu API key
   ```

3. **Instalar dependencias**:
   ```bash
   cd experimentos/nano-banana-test
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Ejecutar el test**:
   ```bash
   python test_nanoba.py
   ```

## 🎨 Qué Esperar

El script generará **3 imágenes** en `output/`:

1. **test_01_logo.png**
   - Logo minimalista de Orbital Lab
   - Fondo negro, símbolo rojo orbital
   - Test de conexión básica

2. **test_02_hero_background.png**
   - Arquitectura futurista con iluminación roja
   - Estilo Blade Runner 2049
   - Test de calidad alta

3. **test_03_icon_strivio.png**
   - Icono de analytics deportivos
   - Balón de fútbol + gráficas
   - Test de diferentes estilos

**Métricas por imagen:**
- Tiempo: ~20-30 segundos
- Dimensiones: 1024x1024px
- Costo: $0.039 (GRATIS en free tier)
- Watermark: SynthID invisible

**Total para 3 imágenes:**
- Tiempo: ~60-90 segundos
- Costo: $0.117 (GRATIS en free tier)
- Rate limiting: 4s de pausa entre requests

## 📋 Checklist de Ejecución

- [ ] Obtener API key de https://aistudio.google.com
- [ ] Configurar API key (env var o .env)
- [ ] Instalar dependencias en venv
- [ ] Ejecutar `python test_nanoba.py`
- [ ] Revisar las 3 imágenes generadas en `output/`
- [ ] Evaluar calidad y tiempos
- [ ] Decidir si montamos el Task Global

## ✅ Criterios de Éxito

Este experimento es exitoso si:

- ✅ Se generan las 3 imágenes sin errores
- ✅ La calidad es aceptable para producción (suficiente detalle, colores correctos)
- ✅ Los tiempos son razonables (~30s/imagen)
- ✅ Los prompts estructurados funcionan como se espera
- ✅ El sistema de API key es fácil de configurar

**Si todo esto se cumple → Crear Task Global en `~/.claude/commands/`**

## 🚀 Fase 2 - Task Global (Futuro)

Una vez validado el experimento, crearemos:

```
~/.claude/
├── commands/
│   └── generate-image.md          # Slash command /generate-image
├── scripts/
│   └── nanoba_generator/
│       ├── generator.py           # Script principal
│       ├── prompts.py             # Templates de prompts
│       └── config.yaml            # Configuración global
└── docs/
    └── nanoba_usage.md            # Guía de uso
```

**Uso desde cualquier proyecto:**

```bash
# Desde cualquier sesión de Claude Code
/generate-image "A futuristic hero background with red lighting"

# O programáticamente
python ~/.claude/scripts/nanoba_generator/generator.py \
  --prompt "..." \
  --output "./assets/hero.png"
```

## 🔗 Referencias Rápidas

- **API Key**: https://aistudio.google.com
- **Documentación Nano Banana**: https://ai.google.dev/gemini-api/docs
- **Free Tier Limits**: 1,500 req/día, 15 req/min
- **Guía Completa**: [../../investigaciones/guia-maxima-nano-veo3-gemini.md](../../investigaciones/guia-maxima-nano-veo3-gemini.md)

---

**Siguiente comando a ejecutar:**

```bash
cd experimentos/nano-banana-test && python test_nanoba.py
```

¡Todo listo para probar! 🍌
