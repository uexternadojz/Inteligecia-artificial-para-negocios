# Bitácora de Transformaciones de Datos

| Paso | Fecha/Hora | Responsable | Descripción | Artefacto | Checks |
|------|------------|-------------|-------------|-----------|--------|
| 001 | 2025-10-27 | Equipo docente | Conversión de `TotalCharges` a float + imputación controlada de nulos | `scripts/preparar_dataset_telco.py` | [x] Missing [x] Tipos |
| 002 | 2025-10-27 | Equipo docente | Exportar dataset limpio `telco_prepared.csv` | `outputs/telco_prepared.csv` | [x] Negocio |
| 003 | 2025-10-27 | Equipo docente | Codificar categorías clave (contrato, InternetService, PaymentMethod, tenure, pricing) | `scripts/preparar_dataset_telco.py` | [x] |
| 004 | 2025-10-27 | Equipo docente | Feature engineering: `TenureGroup`, `ServicesCount`, `IsAutoPayment`, `AverageMonthlyCharges` | `scripts/preparar_dataset_telco.py` | [x] |
| 005 | _pendiente_ | _pendiente_ | Validar checklist de calidad y documentar decisiones finales | `docs/checklist-calidad-datos.md` | [ ] |

> Actualiza esta tabla a medida que se ejecuten transformaciones. Si una tarea deriva en script, documenta el comando exacto o celda del notebook.
