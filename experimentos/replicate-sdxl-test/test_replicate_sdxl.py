#!/usr/bin/env python3
"""
Script de prueba para Replicate + Stable Diffusion XL
Genera 3 imágenes de prueba para validar conexión y calidad
"""

import os
from pathlib import Path
import time
import sys

# Verificar instalación de dependencias
try:
    import replicate
    from PIL import Image
    import requests
    from io import BytesIO
except ImportError as e:
    print("❌ Error: Falta instalar dependencias")
    print("\n📦 Ejecuta:")
    print("   python -m venv venv")
    print("   source venv/bin/activate  # En Windows: venv\\Scripts\\activate")
    print("   pip install -r requirements.txt")
    sys.exit(1)


def load_api_token():
    """Busca API token en orden de prioridad"""

    # 1. Variable de entorno REPLICATE_API_TOKEN
    token = os.getenv("REPLICATE_API_TOKEN")
    if token and token != "PEGA_AQUI_EL_TOKEN_QUE_COPIASTE":
        print("✅ API token encontrado en variable de entorno REPLICATE_API_TOKEN")
        return token

    # 2. Archivo .env local
    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        print("📄 Leyendo .env local...")
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line.startswith("REPLICATE_API_TOKEN="):
                    token = line.split("=", 1)[1].strip().strip('"').strip("'")
                    if token and token != "PEGA_AQUI_EL_TOKEN_QUE_COPIASTE":
                        print("✅ API token encontrado en .env local")
                        return token

    # No se encontró
    raise ValueError(
        "❌ No se encontró API token.\n\n"
        "📝 Opciones para configurar:\n"
        "   1. Variable de entorno (recomendado):\n"
        "      export REPLICATE_API_TOKEN='tu_token'\n\n"
        "   2. Archivo .env local:\n"
        "      cp .env.example .env\n"
        "      # Edita .env y añade tu token\n\n"
        "🔑 Obtén tu token GRATIS en: https://replicate.com/account/api-tokens"
    )


def generate_test_image(prompt, filename, description):
    """Genera una imagen de prueba con SDXL"""

    print(f"\n{'='*70}")
    print(f"🎨 Test {filename.split('_')[1].split('.')[0]}: {description}")
    print(f"{'='*70}")
    print(f"📝 Prompt:")
    print(f"   {prompt[:100]}...")

    start_time = time.time()

    try:
        # Llamada a la API de Replicate con SDXL
        output = replicate.run(
            "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
            input={
                "prompt": prompt,
                "width": 1024,
                "height": 1024,
                "num_outputs": 1,
                "num_inference_steps": 25,  # Balance calidad/velocidad
                "guidance_scale": 7.5,
                "scheduler": "K_EULER"
            }
        )

        elapsed = time.time() - start_time

        # Crear directorio de salida
        output_dir = Path(__file__).parent / "output"
        output_dir.mkdir(exist_ok=True)

        # Descargar y guardar imagen
        if output and len(output) > 0:
            image_url = output[0]

            # Descargar imagen
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))

            output_path = output_dir / filename
            img.save(output_path)

            print(f"\n✅ Imagen generada exitosamente!")
            print(f"   📂 Guardada en: {output_path}")
            print(f"   📐 Dimensiones: {img.size[0]}x{img.size[1]}px")
            print(f"   ⏱️  Tiempo: {elapsed:.2f}s")
            print(f"   💰 Costo estimado: $0.002")
            print(f"   🆓 Free tier: ✓ (cuenta para tus $5 de crédito)")
            print(f"   🔗 URL: {image_url}")

            return output_path
        else:
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
    print("🚀 REPLICATE + SDXL - Test de Conexión y Generación")
    print("="*70)
    print("📦 Modelo: Stable Diffusion XL 1.0")
    print("🆓 Free tier: $5 de crédito gratis = 2,500 imágenes")
    print("💰 Costo: $0.002 por imagen (después del crédito)")
    print("="*70)

    # Paso 1: Cargar API token
    print("\n🔑 Paso 1: Verificando API token...")
    try:
        api_token = load_api_token()
    except ValueError as e:
        print(str(e))
        return 1

    # Paso 2: Configurar cliente de Replicate
    print("\n🔌 Paso 2: Configurando cliente de Replicate...")
    try:
        os.environ["REPLICATE_API_TOKEN"] = api_token
        print("✅ Cliente configurado correctamente")
    except Exception as e:
        print(f"❌ Error al configurar cliente: {e}")
        return 1

    # Paso 3: Generar imágenes de prueba
    print("\n🎨 Paso 3: Generando imágenes de prueba...")
    print("   (Esto tomará ~15-30 segundos para las 3 imágenes)")

    results = []

    # Test 1: Logo simple (conexión básica)
    prompt1 = (
        "A minimalist red orbital logo symbol on pure black background, "
        "centered composition, geometric circular design with orbital rings, "
        "studio lighting, ultra sharp focus, 4K resolution, "
        "modern tech brand identity, Orbital Lab aesthetic, clean and professional, "
        "no text, no gradients, high contrast, vector-style clarity"
    )
    result1 = generate_test_image(
        prompt1,
        "test_01_logo.png",
        "Logo Simple (Test de Conexión)"
    )
    results.append(("Logo", result1))

    # Esperar 2 segundos entre requests (rate limiting friendly)
    if result1:
        print("\n⏳ Esperando 2 segundos...")
        time.sleep(2)

    # Test 2: Hero background (calidad alta)
    prompt2 = (
        "Futuristic monumental architecture with dramatic red orbital lighting illumination, "
        "wide aerial establishing shot, cinematic perspective with deep depth of field, "
        "golden hour sunset lighting, shot on 24mm cinema lens, atmospheric fog and rays, "
        "Blade Runner 2049 cinematography, desaturated palette with vibrant red accent, "
        "sci-fi architecture, no people, no text overlays, no vehicles, "
        "dramatic shadows, crystal clear focus on main structure"
    )
    result2 = generate_test_image(
        prompt2,
        "test_02_hero_background.png",
        "Hero Background (Test de Calidad)"
    )
    results.append(("Hero Background", result2))

    if result2:
        print("\n⏳ Esperando 2 segundos...")
        time.sleep(2)

    # Test 3: Icon (estilo diferente)
    prompt3 = (
        "Sports analytics icon featuring a soccer ball integrated with data visualization "
        "elements and graphs, icon design format, 512x512 pixels, clean centered symbol "
        "with breathing room, flat design lighting, vector-style rendering, "
        "modern Material Design aesthetic, Google Material Design icons, "
        "tech startup branding, Strivio sports analytics identity, "
        "simple and recognizable at small sizes, no complex details, bold shapes, no text"
    )
    result3 = generate_test_image(
        prompt3,
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
        print(f"\n📂 Todas las imágenes guardadas en:")
        output_dir = Path(__file__).parent / "output"
        print(f"   {output_dir.absolute()}")

        print(f"\n💰 Costo total: ${successful * 0.002:.3f}")
        print(f"   Crédito restante: ${5 - (successful * 0.002):.3f}")

        print(f"\n💡 Siguiente paso:")
        print(f"   Revisa las imágenes generadas y si te gustan,")
        print(f"   ¡montamos el Task global para usarlo en cualquier proyecto!")
    else:
        print(f"\n⚠️  No se generó ninguna imagen exitosamente.")
        print(f"   Revisa los errores arriba y verifica tu token.")

    print("="*70)

    return 0 if successful > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
