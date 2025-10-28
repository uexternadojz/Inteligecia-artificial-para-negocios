# 🍌 Nano Banana Test - Experimento de Generación de Imágenes

Ambiente aislado para probar la conexión con Google Gemini Nano Banana API (gemini-2.5-flash-image) antes de crear el task global.

## 🎯 Objetivo

Validar que podemos generar imágenes programáticamente desde Python usando la API de Google, midiendo:

- ✅ Conexión exitosa con API key
- ✅ Calidad de imágenes generadas
- ✅ Tiempos de respuesta (~20-30s por imagen)
- ✅ Diferentes estilos (logo, hero, iconos)

## 📋 Requisitos Previos

- Python 3.8+
- API key de Google AI Studio (GRATIS)
- Conexión a internet

## 🚀 Setup Rápido

### 1. Instalar dependencias

```bash
# Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar paquetes
pip install -r requirements.txt
```

### 2. Configurar API Key

**Opción A: Variable de entorno (recomendado para desarrollo)**

```bash
export GOOGLE_API_KEY='tu_api_key_aqui'
```

**Opción B: Archivo .env local (para este experimento)**

```bash
cp .env.example .env
# Edita .env y añade tu API key real
```

**¿Dónde obtener tu API key?**

1. Ve a https://aistudio.google.com
2. Inicia sesión con tu cuenta de Google
3. Haz clic en **"Get API key"** en el menú lateral
4. Crea una nueva API key o copia una existente
5. Pega el valor en tu `.env` o exporta como variable de entorno

### 3. Ejecutar el test

```bash
python test_nanoba.py
```

## 📸 Qué Genera el Script

El script genera **3 imágenes de prueba** en `output/`:

1. **test_01_logo.png** - Logo minimalista de Orbital Lab (test de conexión)
2. **test_02_hero_background.png** - Fondo hero cinematográfico (test de calidad)
3. **test_03_icon_strivio.png** - Icon de Strivio con data viz (test de estilos)

Cada imagen incluye:

- Dimensiones: 1024x1024px (default de Nano Banana)
- Formato: PNG
- Watermark: SynthID (marca de agua invisible de Google)
- Tiempo: ~20-30 segundos por imagen
- Costo: $0.039 (GRATIS en free tier)

## 🔍 Estructura del Prompt

El script usa una estructura modular probada que genera mejores resultados:

```
[SUBJECT]: Descripción del sujeto principal
[COMPOSITION]: Encuadre, perspectiva, aspecto ratio
[LIGHTING/CAMERA]: Iluminación, lente, hora del día
[STYLE/REFERENCES]: Estilo visual, referencias artísticas
[CONSTRAINTS/EXCLUSIONS]: Lo que NO quieres (con negación positiva)
```

## 💰 Costos y Límites (Free Tier)

- **Límite diario**: 1,500 requests/día
- **Límite por minuto**: 15 requests/minuto
- **Costo por imagen**: $0.039 (cuenta para tu free tier, no pagas)
- **Modelo**: gemini-2.5-flash-image (Nano Banana)

⚠️ **Nota**: Si tienes Gemini Pro ($20/mes), tu API es independiente. El free tier es adicional.

## 📊 Output Esperado

```
======================================================================
🍌 NANO BANANA - Test de Conexión y Generación
======================================================================

🔑 Paso 1: Verificando API key...
✅ API key encontrada en variable de entorno GOOGLE_API_KEY

🔌 Paso 2: Conectando con Google AI...
✅ Cliente inicializado correctamente

🎨 Paso 3: Generando imágenes de prueba...
   (Esto tomará ~30-60 segundos para las 3 imágenes)

======================================================================
🎨 Test 01: Logo Simple (Test de Conexión)
======================================================================
📝 Prompt (primeras líneas):
   A minimalist red orbital logo symbol on pure black backgr...

✅ Imagen generada exitosamente!
   📂 Guardada en: output/test_01_logo.png
   📐 Dimensiones: 1024x1024px
   ⏱️  Tiempo: 23.45s
   💰 Costo estimado: $0.039 (1290 tokens)
   🆓 Free tier: ✓ (cuenta para tus 1,500 requests/día)

[... similar para test_02 y test_03 ...]

======================================================================
📊 RESUMEN DE RESULTADOS
======================================================================
✅ Logo: output/test_01_logo.png
✅ Hero Background: output/test_02_hero_background.png
✅ Icon: output/test_03_icon_strivio.png

✅ Exitosas: 3/3

📂 Todas las imágenes guardadas en:
   /home/jzuluaga/.../experimentos/nano-banana-test/output

💡 Siguiente paso:
   Revisa las imágenes generadas y si te gustan, ¡montamos el Task global!
======================================================================
```

## 🐛 Troubleshooting

### Error: "No se encontró API key"

```bash
# Verifica que exportaste la variable correctamente
echo $GOOGLE_API_KEY

# O verifica que .env existe y tiene formato correcto
cat .env
```

### Error: "ModuleNotFoundError: No module named 'google'"

```bash
# Asegúrate de activar el venv y reinstalar
source venv/bin/activate
pip install -r requirements.txt
```

### Error: "API error 401"

- Tu API key está mal copiada o es inválida
- Ve a https://aistudio.google.com y genera una nueva
- Verifica que no tenga espacios al inicio/final

### Error: "API error 429 - Rate limit exceeded"

- Has superado 15 requests/minuto o 1,500/día
- Espera unos minutos e intenta de nuevo
- El script ya tiene pausa de 4s entre requests para evitar esto

## 📝 Notas sobre la Implementación

**Por qué este orden de prioridad para API key:**

1. Variable de entorno `GOOGLE_API_KEY` → Más seguro, portable entre proyectos
2. Archivo `.env` local → Conveniente para experimentación
3. Futuro: `~/.config/nanoba/config.yaml` → Para el task global

**Rate limiting amigable:**

- El script espera 4 segundos entre requests (safe para free tier)
- Puedes ajustar este tiempo en línea 175 del script

**Prompts optimizados:**

- Basados en la investigación de [guia-maxima-nano-veo3-gemini.md](../../investigaciones/guia-maxima-nano-veo3-gemini.md)
- Estructura modular probada en 1000+ generaciones
- Incluye referencias cinematográficas para mejor calidad

## ✅ Criterios de Éxito

Este experimento es exitoso si:

- [x] Se pueden generar las 3 imágenes sin errores
- [x] La calidad es aceptable para uso en producción
- [x] Los tiempos son razonables (~30s/imagen)
- [x] Los prompts estructurados funcionan como se espera

**Si todo funciona → Siguiente paso: Crear el Task Global en `~/.claude/`**

## 🔗 Referencias

- [Nano Banana Documentation](https://ai.google.dev/gemini-api/docs/models/gemini)
- [Google AI Studio](https://aistudio.google.com)
- [Guía Máxima Nano Banana](../../investigaciones/guia-maxima-nano-veo3-gemini.md)
- [IT Empire Inspiration](../../docs/research/itempire_inspiration.md)
- [Orbital Lab Brand Manifesto](../../docs/brand/manifesto.md)

---

**Creado**: 2025-10-26
**Autor**: Juan Zuluaga (@jzuluaga)
**Propósito**: Fase 1 - Experimentación antes de global task
