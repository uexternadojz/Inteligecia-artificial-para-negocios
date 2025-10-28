#!/bin/bash

# Script para abrir la guía interactiva en el navegador

echo "🎓 Abriendo Guía Interactiva CRISP-DM..."

# Detectar sistema operativo y abrir navegador apropiado
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    if command -v xdg-open &> /dev/null; then
        xdg-open guia_interactiva_crisp_dm.html
    elif command -v sensible-browser &> /dev/null; then
        sensible-browser guia_interactiva_crisp_dm.html
    else
        echo "❌ No se pudo detectar un navegador. Abre manualmente: guia_interactiva_crisp_dm.html"
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    open guia_interactiva_crisp_dm.html
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
    # Windows (Git Bash, Cygwin)
    start guia_interactiva_crisp_dm.html
else
    echo "❌ Sistema operativo no reconocido. Abre manualmente: guia_interactiva_crisp_dm.html"
fi

echo "✅ Si no se abrió automáticamente, abre el archivo: guia_interactiva_crisp_dm.html"
