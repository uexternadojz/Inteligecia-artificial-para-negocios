#!/usr/bin/env python3
import os
from pathlib import Path
import replicate
import requests
from PIL import Image
from io import BytesIO

# Cargar token desde .env
env_file = Path(__file__).parent / ".env"
with open(env_file) as f:
    for line in f:
        if line.startswith("REPLICATE_API_TOKEN="):
            token = line.split("=", 1)[1].strip()
            os.environ["REPLICATE_API_TOKEN"] = token
            break

prompt = "A minimalist red orbital logo symbol on pure black background, centered composition, geometric circular design with orbital rings, studio lighting, ultra sharp focus, 4K resolution, modern tech brand identity, Orbital Lab aesthetic, clean and professional, no text, no gradients, high contrast, vector-style clarity"

print("🎨 Generando logo...")
output = replicate.run(
    "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
    input={"prompt": prompt, "width": 1024, "height": 1024}
)

if output:
    response = requests.get(output[0])
    img = Image.open(BytesIO(response.content))
    output_path = Path("output/test_01_logo.png")
    img.save(output_path)
    print(f"✅ Logo generado: {output_path}")
    print(f"📐 Dimensiones: {img.size}")
    print(f"🔗 URL: {output[0]}")
