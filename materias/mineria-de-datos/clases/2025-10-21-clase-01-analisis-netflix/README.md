# 📚 Clase 01 - Introducción y EDA con el Catálogo de Netflix

**Fecha:** 21 de octubre de 2025  
**Materia:** Minería de Datos  
**Institución:** Universidad Externado de Colombia  
**Profesor:** Juan Zuluaga

---

## 🎯 Propósito de la Sesión
- Presentar la metodología del curso a través de un caso real de análisis exploratorio.
- Comprender cómo transformar datos crudos en insights accionables de negocio.
- Practicar lectura de reportes ejecutivos, navegación de notebooks y uso de scripts auxiliares.

---

## 📂 Qué encontrarás en esta carpeta

| Categoría | Ruta | Descripción |
|-----------|------|-------------|
| Documentación | `docs/` | Guía rápida (`LEEME_PRIMERO.txt`), índice navegable, resumen ejecutivo y reporte de negocio completo. |
| Notebooks | `notebooks/` | `netflix_analysis.ipynb` (plantilla) y `netflix_analysis_executed.ipynb` (resultado con 45+ visualizaciones). |
| Scripts | `scripts/` | `generate_business_report.py` para regenerar el informe ejecutivo y `verificar_analisis.sh` como checklist automatizada. |
| Datos | `data/` | Dataset original (`netflix_titles.csv`) y versión procesada con variables derivadas. |
| Salidas | `outputs/` | Métricas resumidas (`netflix_summary_metrics.csv`) listas para dashboards. |

---

## 🔄 Flujo sugerido
1. **Lectura ejecutiva (10 min):** `docs/RESUMEN_EJECUTIVO.md` → `docs/REPORTE_NEGOCIO_NETFLIX.txt`.
2. **Checklist rápida (2 min):** `scripts/verificar_analisis.sh`.
3. **Exploración visual (60 min):** abrir `notebooks/netflix_analysis_executed.ipynb`.
4. **Regenerar entregables (opcional):** ejecutar `python scripts/generate_business_report.py`.
5. **Experimentación técnica (90+ min):** reutilizar la plantilla `notebooks/netflix_analysis.ipynb` con filtros o métricas adicionales.

---

## 🛠️ Requisitos técnicos
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r ../../../../herramientas/requirements.txt
pip install matplotlib seaborn wordcloud missingno jupyter
```

> Tip: mantén este entorno fuera del repositorio (no versionado) y reutilízalo para futuras clases enfocadas en EDA.

---

## 📊 Dataset
- **Fuente:** Netflix Titles (Kaggle, actualización septiembre 2021)  
- **Registros:** 8,807 títulos (películas y series)  
- **Variables derivadas:** década, tiempo hasta Netflix, duración en minutos, número de temporadas, longitud de descripción, entre otras.
- **Ubicación:** `data/netflix_titles.csv` (raw) y `data/netflix_titles_processed.csv` (enriquecido).

---

## ✅ Entregables principales
- `docs/RESUMEN_EJECUTIVO.md`: visión de 1 página con top 10 insights.
- `docs/REPORTE_NEGOCIO_NETFLIX.txt`: reporte completo con recomendaciones estratégicas.
- `notebooks/netflix_analysis_executed.ipynb`: storytelling interactivo con 45+ visualizaciones.
- `outputs/netflix_summary_metrics.csv`: KPIs listos para dashboards o quick checks.

---

## 🔗 Referencias cruzadas
- Metodología CRISP-DM: profundiza en `docs/CRISP-DM_Fases_1_y_2.md` (carpeta de la Clase 02).
- Plantilla para nuevas clases: ver `herramientas/scripts/nueva_clase.py`.
- Datasets compartidos del curso: `recursos_compartidos/datasets/mineria-de-datos/`.

---

## 📬 Siguientes pasos sugeridos
1. Evaluar qué visualizaciones y hallazgos se pueden reutilizar en dashboards ejecutivos.
2. Diseñar una actividad práctica donde los estudiantes modifiquen filtros y recomputen KPIs.
3. Preparar comparativo con otro catálogo (ej. Disney+, HBO) para la sesión de benchmarking.

---

¿Dudas o mejoras? Documentarlas en `logs/` del curso o coordinarlas mediante el plan de trabajo docente.﻿
