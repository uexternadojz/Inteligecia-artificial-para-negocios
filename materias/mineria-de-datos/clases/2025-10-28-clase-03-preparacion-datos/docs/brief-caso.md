# Brief del Caso - Clase 03

## 1. Contexto
- **Dominio:** Telecomunicaciones (Telco Customer Churn - IBM).
- **Fases CRISP-DM:** Entendimiento de los Datos (Fase 3) y Preparación de los Datos (Fase 4).
- **Propósito pedagógico:** conectar las preguntas de negocio sobre churn con la exploración y limpieza temprana del dataset, reforzando el puente “del negocio al dato”.

## 2. Preguntas de negocio prioritarias
1. ¿Qué características comparten los clientes que abandonan el servicio?
2. ¿Cómo impactan el tipo de contrato, el método de pago y la antigüedad en la tasa de churn?
3. ¿Qué combinaciones de servicios (internet, soporte, streaming, seguridad) retienen mejor a los clientes?

## 3. Hipótesis de partida
- Los contratos mes a mes presentan mayor churn frente a contratos de uno o dos años.
- Los clientes que pagan con cheque electrónico abandonan con mayor frecuencia.
- Tenure bajo (clientes recientes) incrementa el riesgo de churn.
- Clientes con cargos mensuales altos y pocos servicios activos perciben menor valor.

## 4. Entradas de datos
- **Dataset principal:** `data/WA_Fn-UseC_-Telco-Customer-Churn.csv` (Kaggle - Telco Customer Churn, IBM).
- **Variables clave:** información demográfica, detalles de cuenta (tenure, contrato, cargos), servicios suscritos y variable objetivo `Churn`.
- **Complementos opcionales:** documentación oficial IBM/Kaggle para glosario de campos y reglas de negocio.

## 5. Entregables previstos para la clase
- Notebook o script en `notebooks/` o `scripts/` con el pipeline de limpieza y exploración.
- Dataset preparado en `outputs/` listo para modelado/EDA avanzado.
- Visualizaciones en `assets/` que soporten discusiones de aula.
- Documentación actualizada (`checklist-calidad-datos.md`, `bitacora-transformaciones.md`, `resumen-preparacion.md`).

## 6. Estructura sugerida de la sesión
- **Bloque 1 (30 min):** repaso del caso de negocio, hipótesis y lectura guiada del dataset (`df.info`, `df.head`, desbalance).
- **Bloque 2 (75 min):** limpieza y preparación (tipos, nulos, feature engineering, codificación). Registrar decisiones en bitácora.
- **Bloque 3 (30-45 min):** visualizaciones por equipos (contrato, pagos, tenure, precios, servicios) y discusión plenaria.
- **Cierre:** reflexión CRISP-DM (qué se buscaba, qué se aprendió, qué queda listo para modelar).

## 7. Notas pedagógicas
- Fomentar que cada equipo traduzca su hipótesis de negocio a una verificación con datos.
- Remarcar la diferencia entre correlación y causalidad en las conclusiones.
- Invitar a plantear acciones de retención basadas en los insights obtenidos (mini reporte o exposición relámpago).
