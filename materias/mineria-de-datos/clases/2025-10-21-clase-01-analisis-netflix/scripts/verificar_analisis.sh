#!/bin/bash

set -euo pipefail

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "================================================================================"
echo "           VERIFICACIÓN DEL ANÁLISIS EXPLORATORIO - NETFLIX                   "
echo "================================================================================"
echo ""

echo "📁 ARCHIVOS GENERADOS:"
echo "------------------------------------------------------------"

files=(
    "notebooks/netflix_analysis.ipynb:Notebook de análisis (plantilla)"
    "notebooks/netflix_analysis_executed.ipynb:Notebook ejecutado con visualizaciones"
    "scripts/generate_business_report.py:Script Python para generar reporte"
    "docs/REPORTE_NEGOCIO_NETFLIX.txt:Reporte ejecutivo de negocio"
    "docs/README_ANALISIS_NETFLIX.md:Documentación completa del análisis"
    "docs/RESUMEN_EJECUTIVO.md:Resumen ejecutivo para stakeholders"
    "docs/INDICE_ANALISIS.md:Índice completo del proyecto"
    "docs/LEEME_PRIMERO.txt:Guía de navegación inicial"
    "data/netflix_titles.csv:Dataset original"
    "data/netflix_titles_processed.csv:Dataset procesado con columnas adicionales"
    "outputs/netflix_summary_metrics.csv:KPIs y métricas resumen"
)

for file_info in "${files[@]}"; do
    IFS=':' read -r file desc <<< "$file_info"
    full_path="${BASE_DIR}/${file}"
    if [ -e "$full_path" ]; then
        size=$(du -h "$full_path" 2>/dev/null | cut -f1)
        echo "  ✅ ${file}"
        echo "     └─ ${desc}"
        echo "     └─ Tamaño: ${size}"
    else
        echo "  ❌ ${file} - NO ENCONTRADO"
    fi
    echo ""
done

echo "================================================================================"
echo "📊 RESUMEN DEL ANÁLISIS:"
echo "------------------------------------------------------------"
echo ""

REPORTE_PATH="${BASE_DIR}/docs/REPORTE_NEGOCIO_NETFLIX.txt"
if [ -f "${REPORTE_PATH}" ]; then
    echo "MÉTRICAS CLAVE (del reporte):"
    echo ""
    grep -A 15 "RESUMEN DE MÉTRICAS CLAVE" "${REPORTE_PATH}" | tail -n 13 | head -n 12
else
    echo "⚠️  Reporte no encontrado en docs/REPORTE_NEGOCIO_NETFLIX.txt"
fi

echo ""
echo "================================================================================"
echo "🚀 SIGUIENTES PASOS:"
echo "------------------------------------------------------------"
echo ""
echo "1. Activar entorno y abrir el notebook ejecutado:"
echo "   python -m venv .venv && source .venv/bin/activate  # si no existe entorno"
echo "   pip install -r ../../../../herramientas/requirements.txt"
echo "   jupyter notebook notebooks/netflix_analysis_executed.ipynb"
echo ""
echo "2. Leer el reporte completo de negocio:"
echo "   less docs/REPORTE_NEGOCIO_NETFLIX.txt"
echo ""
echo "3. Regenerar el reporte ejecutivo desde el script:"
echo "   source .venv/bin/activate"
echo "   python scripts/generate_business_report.py"
echo ""
echo "4. Consultar la documentación:"
echo "   cat docs/README_ANALISIS_NETFLIX.md"
echo ""
echo "================================================================================"
echo "✅ Análisis completado exitosamente!"
echo "================================================================================"
