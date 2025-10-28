# Checklist de Calidad de Datos

## 1. Integridad
- [ ] Sin duplicados según `customerID` (verificar con `df.duplicated().sum()`).
- [x] `TotalCharges` sin nulos tras conversión (pipeline `preparar_dataset_telco.py`).
- [x] Columnas críticas (`Churn`, `Contract`, `PaymentMethod`, `tenure`, `MonthlyCharges`) completas en `telco_prepared.csv`.

## 2. Consistencia
- [x] `TotalCharges` transformado a numérico y coherente con `MonthlyCharges * tenure`.
- [x] Categorías estandarizadas (`No internet service` → `0`, etc.).
- [ ] Rangos numéricos validados (tenure ≥ 0, MonthlyCharges 0-120, TotalCharges ≥ 0).

## 3. Exactitud
- [ ] Revisión de outliers en `MonthlyCharges`, `TotalCharges`, `tenure` y acciones documentadas.
- [ ] Validación cruzada de hipótesis de negocio (contrato, pagos, servicios) con cifras.
- [ ] Reglas específicas del dominio confirmadas con el grupo (ej. significados de “MultipleLines”, “TechSupport”).

## 4. Completitud
- [ ] Conteo y gestión de los 11 registros con TotalCharges vacío.
- [ ] Feature engineering registrado (e.g., `TenureGroup`, `ServicesCount`, codificaciones).
- [ ] Bitácora y supuestos actualizados en `bitacora-transformaciones.md`.

## 5. Disponibilidad de artefactos
- [x] Dataset preparado almacenado en `outputs/telco_prepared.csv`.
- [x] Gráficos clave exportados en `assets/`.
- [x] Script / notebook documentado y reproducible (`scripts/preparar_dataset_telco.py`, `notebooks/01_preparacion_telco.ipynb`).
- [x] Reporte breve completado en `docs/resumen-preparacion.md`.

> Marca cada ítem y agrega notas si quedan pendientes para sesiones siguientes.
