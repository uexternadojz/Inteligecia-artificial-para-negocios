#!/usr/bin/env python3
"""
Script de prueba para Nano Banana API (Gemini 2.5 Flash Image)
Genera 3 imágenes de prueba para validar conexión y calidad
"""

import os
from pathlib import Path
import time
import sys

# Verificar instalación de dependencias
try:
    from google import genai
    from google.genai import types
    from PIL import Image
    from io import BytesIO
except ImportError as e:
    print("❌ Error: Falta instalar dependencias")
    print("\n📦 Ejecuta:")
    print("   python -m venv venv")
    print("   source venv/bin/activate  # En Windows: venv\\Scripts\\activate")
    print("   pip install -r requirements.txt")
    sys.exit(1)


def load_api_key():
    """Busca API key en orden de prioridad"""

    # 1. Variable de entorno GOOGLE_API_KEY
    key = os.getenv("GOOGLE_API_KEY")
    if key:
        print("✅ API key encontrada en variable de entorno GOOGLE_API_KEY")
        return key

    # 2. Variable de entorno GEMINI_API_KEY (alternativa)
    key = os.getenv("GEMINI_API_KEY")
    if key:
        print("✅ API key encontrada en variable de entorno GEMINI_API_KEY")
        return key

    # 3. Archivo .env local
    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        print("📄 Leyendo .env local...")
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line.startswith("GOOGLE_API_KEY="):
                    key = line.split("=", 1)[1].strip().strip('"').strip("'")
                    if key:
                        print("✅ API key encontrada en .env local")
                        return key

    # No se encontró
    raise ValueError(
        "❌ No se encontró API key.\n\n"
        "📝 Opciones para configurar:\n"
        "   1. Variable de entorno (recomendado):\n"
        "      export GOOGLE_API_KEY='tu_api_key'\n\n"
        "   2. Archivo .env local:\n"
        "      cp .env.example .env\n"
        "      # Edita .env y añade tu API key\n\n"
        "🔑 Obtén tu API key GRATIS en: https://aistudio.google.com"
    )


def generate_test_image(client, prompt, filename, description):
    """Genera una imagen de prueba con Nano Banana"""

    print(f"\n{'='*70}")
    print(f"🎨 Test {filename.split('_')[1].split('.')[0]}: {description}")
    print(f"{'='*70}")
    print(f"📝 Prompt (primeras líneas):")
    print(f"   {prompt.strip().split(chr(10))[1][:60]}...")

    start_time = time.time()

    try:
        # Llamada a la API usando Gemini con capacidad de generación de imágenes
        # Usar gemini-2.5-flash-image-preview que funciona con API key simple
        model = client.models.generate_content(
            model='gemini-2.5-flash-image-preview',
            contents=prompt
        )

        elapsed = time.time() - start_time

        # Crear directorio de salida
        output_dir = Path(__file__).parent / "output"
        output_dir.mkdir(exist_ok=True)

        # Procesar respuesta de Gemini con imagen
        image_saved = False
        for candidate in model.candidates:
            for part in candidate.content.parts:
                if hasattr(part, 'inline_data') and part.inline_data:
                    # Extraer datos de imagen
                    img = Image.open(BytesIO(part.inline_data.data))
                    output_path = output_dir / filename
                    img.save(output_path)

                    print(f"\n✅ Imagen generada exitosamente!")
                    print(f"   📂 Guardada en: {output_path}")
                    print(f"   📐 Dimensiones: {img.size[0]}x{img.size[1]}px")
                    print(f"   ⏱️  Tiempo: {elapsed:.2f}s")
                    print(f"   💰 Costo estimado: $0.039")
                    print(f"   🆓 Free tier: ✓ (cuenta para tus 1,500 requests/día)")

                    image_saved = True
                    return output_path
                elif hasattr(part, 'text') and part.text:
                    print(f"   💬 Respuesta de texto: {part.text[:100]}...")

        if not image_saved:
            print("   ❌ Error: La respuesta no contiene imagen")
            return None

    except Exception as e:
        elapsed = time.time() - start_time
        print(f"\n❌ Error en generación:")
        print(f"   {type(e).__name__}: {str(e)}")
        print(f"   ⏱️  Tiempo hasta error: {elapsed:.2f}s")
        return None


def main():
    """Función principal de prueba"""

    print("\n" + "="*70)
    print("🍌 NANO BANANA - Test de Conexión y Generación")
    print("="*70)
    print("📦 Modelo: gemini-2.5-flash-image (Nano Banana)")
    print("🆓 Free tier: 1,500 requests/día | 15 requests/minuto")
    print("💰 Costo: $0.039 por imagen (GRATIS en free tier)")
    print("="*70)

    # Paso 1: Cargar API key
    print("\n🔑 Paso 1: Verificando API key...")
    try:
        api_key = load_api_key()
    except ValueError as e:
        print(str(e))
        return 1

    # Paso 2: Inicializar cliente
    print("\n🔌 Paso 2: Conectando con Google AI...")
    try:
        client = genai.Client(api_key=api_key)
        print("✅ Cliente inicializado correctamente")
    except Exception as e:
        print(f"❌ Error al inicializar cliente: {e}")
        return 1

    # Paso 3: Generar imágenes de prueba
    print("\n🎨 Paso 3: Generando imágenes de prueba...")
    print("   (Esto tomará ~30-60 segundos para las 3 imágenes)")

    results = []

    # Test 1: Logo simple (conexión básica)
    prompt1 = """
[SUBJECT]: A minimalist red orbital logo symbol on pure black background
[COMPOSITION]: Centered composition, geometric circular design with orbital rings
[LIGHTING/CAMERA]: Studio lighting, ultra sharp focus, 4K resolution
[STYLE/REFERENCES]: Modern tech brand identity, Orbital Lab aesthetic, clean and professional
[CONSTRAINTS/EXCLUSIONS]: No text, no gradients, high contrast, vector-style clarity
"""
    result1 = generate_test_image(
        client, prompt1,
        "test_01_logo.png",
        "Logo Simple (Test de Conexión)"
    )
    results.append(("Logo", result1))

    # Esperar 4 segundos entre requests (rate limiting friendly)
    if result1:
        print("\n⏳ Esperando 4 segundos (rate limiting)...")
        time.sleep(4)

    # Test 2: Hero background (calidad alta)
    prompt2 = """
[SUBJECT]: Futuristic monumental architecture with dramatic red orbital lighting illumination
[COMPOSITION]: Wide aerial establishing shot, cinematic perspective with deep depth of field
[LIGHTING/CAMERA]: Golden hour sunset lighting, shot on 24mm cinema lens, atmospheric fog and rays
[STYLE/REFERENCES]: Blade Runner 2049 cinematography, desaturated palette with vibrant red accent, sci-fi architecture
[CONSTRAINTS/EXCLUSIONS]: No people, no text overlays, no vehicles, dramatic shadows, crystal clear focus on main structure
"""
    result2 = generate_test_image(
        client, prompt2,
        "test_02_hero_background.png",
        "Hero Background (Test de Calidad)"
    )
    results.append(("Hero Background", result2))

    if result2:
        print("\n⏳ Esperando 4 segundos (rate limiting)...")
        time.sleep(4)

    # Test 3: Icon (estilo diferente)
    prompt3 = """
[SUBJECT]: Sports analytics icon featuring a soccer ball integrated with data visualization elements and graphs
[COMPOSITION]: Icon design format, 512x512 pixels, clean centered symbol with breathing room
[LIGHTING/CAMERA]: Flat design lighting, vector-style rendering, modern Material Design aesthetic
[STYLE/REFERENCES]: Google Material Design icons, tech startup branding, Strivio sports analytics identity
[CONSTRAINTS/EXCLUSIONS]: Simple and recognizable at small sizes, no complex details, bold shapes, no text
"""
    result3 = generate_test_image(
        client, prompt3,
        "test_03_icon_strivio.png",
        "Icon Strivio (Test de Estilos)"
    )
    results.append(("Icon", result3))

    # Resumen final
    print("\n" + "="*70)
    print("📊 RESUMEN DE RESULTADOS")
    print("="*70)

    successful = sum(1 for _, path in results if path is not None)
    total = len(results)

    for name, path in results:
        status = "✅" if path else "❌"
        print(f"{status} {name}: {path if path else 'Error'}")

    print(f"\n✅ Exitosas: {successful}/{total}")

    if successful > 0:
        output_dir = Path(__file__).parent / "output"
        print(f"\n📂 Todas las imágenes guardadas en:")
        print(f"   {output_dir.absolute()}")
        print(f"\n💡 Siguiente paso:")
        print(f"   Revisa las imágenes generadas y si te gustan, ¡montamos el Task global!")
    else:
        print(f"\n⚠️  No se generó ninguna imagen exitosamente.")
        print(f"   Revisa los errores arriba y verifica tu API key.")

    print("="*70)

    return 0 if successful > 0 else 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
