# 📚 Clase 03 - Telco Customer Churn: Entendimiento y Preparación de Datos

**Fecha:** 28 de octubre de 2025  
**Duración estimada:** 2 a 3 horas  
**Fases CRISP-DM:** 3️⃣ Entendimiento de los datos · 4️⃣ Preparación de los datos

---

## 🎯 Objetivos pedagógicos
1. Traducir las preguntas de negocio sobre churn en hipótesis explorables con datos.
2. Construir un pipeline reproducible de limpieza, enriquecimiento y verificación de calidad.
3. Documentar decisiones y dejar artefactos listos para modelado o benchmarking de estrategias de retención.

---

## 🗂️ Estructura de la carpeta

```
clases/2025-10-28-clase-03-preparacion-datos/
├── README.md                      # Esta guía
├── data/                          # Dataset Telco original y derivados
├── scripts/                       # Utilidades para generación de insights
├── assets/                        # Visualizaciones exportadas (PNG)
├── outputs/                       # Tablas y reportes de resultados
└── docs/                          # Brief, checklist, bitácora y resúmenes
```

Dataset principal: `data/WA_Fn-UseC_-Telco-Customer-Churn.csv` (IBM/Kaggle).

---

## ⚙️ Entorno técnico

```bash
cd clases/2025-10-28-clase-03-preparacion-datos
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install pandas numpy seaborn matplotlib scikit-learn pyjanitor openpyxl

# Generar dataset limpio y metadatos
python scripts/preparar_dataset_telco.py

# Re-generar análisis y gráficos explicativos
python scripts/generar_insights_telco.py
```

> El script genera visualizaciones en `assets/` y un resumen cuantitativo en `outputs/telco_insights.md`.

---

## 🧭 Ruta didáctica sugerida

| Bloque | Tiempo | Objetivo | Actividades |
|--------|--------|----------|-------------|
| 1. Del negocio al dato | 30 min | Alinear hipótesis y preguntas | Revisar `docs/brief-caso.md`, explorar `df.info()` y tasas de churn |
| 2. Preparar para el análisis | 75 min | Limpiar, imputar, derivar variables | Convertir `TotalCharges`, crear `TenureGroup`, `ServicesCount`, documentar en bitácora |
| 3. Descubrimiento visual | 30-45 min | Presentar insights por equipos | Usar gráficos generados (contrato, pagos, tenure, pricing, servicios) y proponer acciones |
| Cierre | 15 min | Reflexión CRISP-DM | Responder: ¿Qué buscábamos? ¿Qué aprendimos del dato? ¿Qué dejamos listo para modelar? |

Dinámica sugerida: formar equipos y asignarles un ángulo (contratos, pagos, tiempo, precios, servicios). Cada equipo entrega un mini reporte con **2 visualizaciones + 2 hallazgos + 1 acción de negocio**.

---

## 📊 Resultados preliminares (script `generar_insights_telco.py`)
- **Churn global:** 26.5% (7,043 clientes).
- **Contratos:** Month-to-month → 42.7% churn; Two year → 2.8%.
- **Pagos:** Electronic check → 45.3% (el mayor); métodos automáticos ~16%.
- **Tenure:** 0-6 meses → 54.3%; 48+ meses → 9.6%.
- **Pricing:** 60-90 USD → 33.7% churn; planes económicos (<30 USD) → 9.8%.
- **Servicios:** cuantos más servicios activos, menor churn (≥5 servicios → 12.4%).
- Heatmap evidencia que carecer de online security/tech support aumenta el abandono.

> Visualizaciones generadas:  
> `assets/01_contract_vs_churn.png` … `assets/06_services_heatmap.png`

---

## 📝 Documentación de apoyo
- `docs/brief-caso.md`: contexto del caso, hipótesis y plan de aula.
- `docs/bitacora-transformaciones.md`: registro de decisiones de limpieza/feature engineering.
- `docs/checklist-calidad-datos.md`: guía de validación antes de modelar.
- `docs/resumen-preparacion.md`: síntesis de hallazgos, riesgos y próximos pasos.
- `docs/telco_crisp_dm_guide.md`: recomendaciones pedagógicas extendidas.
- `notebooks/01_preparacion_telco.ipynb`: narrativa paso a paso para estudiantes.

---

## ✅ Entregables esperados al cierre de la sesión
- Dataset preparado (ej. `outputs/telco_prepared.csv`) con criterios documentados.
- Script/notebook reproducible con pipeline de preparación.
- Visualizaciones comentadas que respalden las hipótesis trabajadas en clase.
- Mini reporte por equipo con acciones de retención sugeridas.

---

**Tip docente:** enfatiza que “el dato no solo se limpia, se interpreta”. Antes de pasar a modelar, exige que cada decisión de preparación se conecte explícitamente con la historia del negocio discutida en clases anteriores.
