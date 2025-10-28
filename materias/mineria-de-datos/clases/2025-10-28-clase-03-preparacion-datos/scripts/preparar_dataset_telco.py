#!/usr/bin/env python3
"""
Pipeline reproducible para preparar el dataset Telco Customer Churn.

Pasos principales:
1. Carga el CSV original y normaliza tipos.
2. Gestiona valores faltantes y columnas binarias (Yes/No → 1/0).
3. Construye variables derivadas relevantes para el caso de negocio.
4. Codifica variables categóricas y exporta un dataset listo para modelado.

Outputs:
- outputs/telco_prepared.csv
- outputs/telco_feature_metadata.json
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
OUTPUTS_DIR = BASE_DIR / "outputs"

# Columnas con respuestas Yes/No (más la categoría "No internet service"/"No phone service")
BINARY_COLS = [
    "Partner",
    "Dependents",
    "PhoneService",
    "PaperlessBilling",
    "Churn",
]

SERVICE_COLS = [
    "MultipleLines",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
]

CAT_COLS_FOR_DUMMIES = [
    "Contract",
    "InternetService",
    "PaymentMethod",
]


def preparar_directorios() -> None:
    OUTPUTS_DIR.mkdir(exist_ok=True)


def cargar_csv() -> pd.DataFrame:
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"No se encontró el dataset original en {DATA_PATH}. "
            "Descarga el archivo desde Kaggle antes de ejecutar este script."
        )
    df = pd.read_csv(DATA_PATH)
    return df


def limpiar_total_charges(df: pd.DataFrame) -> pd.DataFrame:
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    missing_total = df["TotalCharges"].isna()
    if missing_total.any():
        df.loc[missing_total, "TotalCharges"] = (
            df.loc[missing_total, "MonthlyCharges"] * df.loc[missing_total, "tenure"]
        )
    return df


def normalizar_columnas_binarias(df: pd.DataFrame) -> pd.DataFrame:
    for col in BINARY_COLS:
        df[col] = df[col].map({"Yes": 1, "No": 0}).astype("int64")

    df["ChurnFlag"] = df["Churn"]

    service_map = {"Yes": 1, "No": 0, "No internet service": 0, "No phone service": 0}
    for col in SERVICE_COLS:
        df[col] = df[col].map(service_map).fillna(0).astype("int64")

    df["SeniorCitizen"] = df["SeniorCitizen"].astype(int)
    return df


def crear_variables_derivadas(df: pd.DataFrame) -> pd.DataFrame:
    bins = [0, 6, 12, 24, 48, df["tenure"].max() + 1]
    labels = ["0-6 m", "6-12 m", "12-24 m", "24-48 m", "48+ m"]
    df["TenureGroup"] = pd.cut(df["tenure"], bins=bins, labels=labels, right=False)

    price_bins = [0, 30, 60, 90, 120]
    price_labels = ["0-30", "30-60", "60-90", "90-120"]
    df["MonthlySegment"] = pd.cut(
        df["MonthlyCharges"], bins=price_bins, labels=price_labels, right=False
    )

    df["ServicesCount"] = df[SERVICE_COLS].sum(axis=1)
    df["IsAutoPayment"] = df["PaymentMethod"].str.contains("automatic", case=False).astype(int)
    df["CustomerTenureYears"] = (df["tenure"] / 12).round(2)
    tenure_numeric = pd.to_numeric(df["tenure"], errors="coerce").astype(float)
    tenure_without_zero = tenure_numeric.replace(0, np.nan)
    average_monthly = df["TotalCharges"].astype(float) / tenure_without_zero
    df["AverageMonthlyCharges"] = average_monthly.fillna(df["MonthlyCharges"]).round(2)
    return df


def codificar_categoricas(df: pd.DataFrame) -> pd.DataFrame:
    dummies = pd.get_dummies(
        df[CAT_COLS_FOR_DUMMIES + ["TenureGroup", "MonthlySegment"]],
        prefix_sep="=",
        drop_first=True,
    )

    df_numeric = df.drop(columns=CAT_COLS_FOR_DUMMIES + ["TenureGroup", "MonthlySegment"])
    prepared = pd.concat([df_numeric, dummies], axis=1)

    # eliminar columnas que ya no son necesarias para modelado
    prepared = prepared.drop(columns=["customerID"])
    return prepared


def generar_metadata(df_original: pd.DataFrame, df_prepared: pd.DataFrame) -> Dict[str, List[str]]:
    metadata: Dict[str, List[str]] = {
        "original_columns": df_original.columns.tolist(),
        "prepared_columns": df_prepared.columns.tolist(),
        "binary_columns": BINARY_COLS + SERVICE_COLS + ["ChurnFlag", "IsAutoPayment"],
        "engineered_features": [
            "TenureGroup",
            "MonthlySegment",
            "ServicesCount",
            "IsAutoPayment",
            "CustomerTenureYears",
            "AverageMonthlyCharges",
        ],
        "dummy_columns": [
            col for col in df_prepared.columns if "=" in col
        ],
    }
    return metadata


def guardar_resultados(df_prepared: pd.DataFrame, metadata: Dict[str, List[str]]) -> None:
    csv_path = OUTPUTS_DIR / "telco_prepared.csv"
    df_prepared.to_csv(csv_path, index=False)

    meta_path = OUTPUTS_DIR / "telco_feature_metadata.json"
    meta_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")


def main() -> None:
    preparar_directorios()
    df_original = cargar_csv()

    df = df_original.copy()
    df = limpiar_total_charges(df)
    df = normalizar_columnas_binarias(df)
    df = crear_variables_derivadas(df)
    df_prepared = codificar_categoricas(df)

    metadata = generar_metadata(df_original, df_prepared)
    guardar_resultados(df_prepared, metadata)

    print("✅ Dataset preparado exportado en outputs/telco_prepared.csv")
    print("📄 Metadata guardada en outputs/telco_feature_metadata.json")
    print(f"🔢 Total de variables preparadas: {df_prepared.shape[1]}")


if __name__ == "__main__":
    main()
