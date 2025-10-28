# Resumen Ejecutivo - Preparación de Datos (Telco Churn)

## 1. Objetivo del proceso
Traducir las hipótesis de negocio sobre churn en pasos concretos de exploración y preparación de datos. Se convirtió `TotalCharges` a numérico, se evaluaron nulos, se generaron agrupaciones de tenure, se cuantificó la diversidad de servicios y se midieron tasas de churn por contrato, métodos de pago y combinaciones de servicios.

## 2. Hallazgos clave (exploración preliminar)
- **Contratos:** clientes “Month-to-month” concentran una tasa de churn del 42.7%, frente a 11.3% (1 año) y 2.8% (2 años).
- **Pagos:** el pago con “Electronic check” eleva el churn al 45.3%; métodos automáticos oscilan entre 15-17%.
- **Tenure:** los primeros 6 meses son críticos (54.3% churn). A partir de 24 meses la tasa cae por debajo del 21%.
- **Pricing:** cargos mensuales entre 60-120 USD tienen tasas superiores al 32%, en contraste con planes <30 USD (9.8%).
- **Servicios:** a mayor número de servicios contratados, menor churn. Los clientes con ≥5 servicios caen por debajo del 12.5%.

## 3. Riesgos y pendientes
- Formalizar el dataset preparado (`outputs/telco_prepared.csv`) tras acordar estrategia de imputación final.
- Evaluar el impacto del desbalance (~26.5% churn) antes del modelado (oversampling/weights).
- Documentar posibles sesgos (ej. clientes sin internet vs. fibra óptica) y validar con el equipo de negocio.

## 4. Próximos pasos sugeridos
1. Completar codificaciones (one-hot/label) y escalamientos según algoritmo seleccionado.
2. Preparar notebook de modelado base (train/test split, baseline con regresión logística).
3. Diseñar rúbrica de mini-reporte por equipos (2 visualizaciones + acción recomendada).

## 5. Artefactos entregados
- Script reproductible: `scripts/generar_insights_telco.py`
- Visualizaciones: `assets/01_contract_vs_churn.png` … `assets/06_services_heatmap.png`
- Reporte cuantitativo: `outputs/telco_insights.md`, `outputs/telco_metrics.json`
- Documentación de soporte: `docs/brief-caso.md`, `docs/checklist-calidad-datos.md`, `docs/bitacora-transformaciones.md`
