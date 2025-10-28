#!/usr/bin/env python3
"""Generador de insights y visualizaciones para el caso Telco Churn."""

from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
ASSETS_DIR = BASE_DIR / "assets"
OUTPUTS_DIR = BASE_DIR / "outputs"


def preparar_directorios() -> None:
    ASSETS_DIR.mkdir(exist_ok=True)
    OUTPUTS_DIR.mkdir(exist_ok=True)


def cargar_dataset() -> pd.DataFrame:
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"No se encontró el dataset en {DATA_PATH}. "
            "Copia o sincroniza el archivo antes de ejecutar este script."
        )

    df = pd.read_csv(DATA_PATH)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["TotalCharges"] = df["TotalCharges"].fillna(df["MonthlyCharges"] * df["tenure"])
    df["ChurnFlag"] = df["Churn"].map({"Yes": 1, "No": 0})
    bins = [0, 6, 12, 24, 48, df["tenure"].max() + 1]
    labels = ["0-6 m", "6-12 m", "12-24 m", "24-48 m", "48+ m"]
    df["TenureGroup"] = pd.cut(df["tenure"], bins=bins, labels=labels, right=False)
    df["MonthlySegment"] = pd.cut(
        df["MonthlyCharges"],
        bins=[0, 30, 60, 90, 120],
        labels=["0-30", "30-60", "60-90", "90-120"],
        right=False,
    )

    service_cols = [
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
    ]
    df_services = df[service_cols].eq("Yes").astype(int)
    df["ServicesCount"] = df_services.sum(axis=1)
    return df


def churn_rate(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    grouped = (
        df.groupby(group_col, observed=True)
        .agg(
            clientes=("customerID", "count"),
            churn_rate=("ChurnFlag", "mean"),
        )
        .sort_values("churn_rate", ascending=False)
    )
    grouped["churn_rate"] = grouped["churn_rate"] * 100
    return grouped


def generar_graficos(df: pd.DataFrame) -> None:
    sns.set_theme(style="whitegrid", palette="deep")

    contract = churn_rate(df, "Contract").sort_values("churn_rate", ascending=False)
    plt.figure(figsize=(8, 5))
    sns.barplot(
        data=contract.reset_index(),
        x="churn_rate",
        y="Contract",
        hue="Contract",
        dodge=False,
        legend=False,
    )
    plt.xlabel("Tasa de churn (%)")
    plt.ylabel("Tipo de contrato")
    plt.title("Churn por tipo de contrato")
    plt.tight_layout()
    plt.savefig(ASSETS_DIR / "01_contract_vs_churn.png", dpi=300)
    plt.close()

    payment = churn_rate(df, "PaymentMethod").sort_values("churn_rate")
    plt.figure(figsize=(9, 5))
    sns.barplot(
        data=payment.reset_index(),
        x="churn_rate",
        y="PaymentMethod",
        color=sns.color_palette()[1],
    )
    plt.xlabel("Tasa de churn (%)")
    plt.ylabel("Método de pago")
    plt.title("Churn por método de pago")
    plt.tight_layout()
    plt.savefig(ASSETS_DIR / "02_payment_vs_churn.png", dpi=300)
    plt.close()

    tenure = churn_rate(df, "TenureGroup")
    plt.figure(figsize=(7, 4))
    sns.barplot(
        data=tenure.reset_index(),
        x="TenureGroup",
        y="churn_rate",
        color=sns.color_palette()[2],
    )
    plt.xlabel("Grupo de tenure (meses)")
    plt.ylabel("Tasa de churn (%)")
    plt.title("Churn según antigüedad del cliente")
    plt.tight_layout()
    plt.savefig(ASSETS_DIR / "03_tenure_vs_churn.png", dpi=300)
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.kdeplot(
        data=df,
        x="MonthlyCharges",
        hue="Churn",
        fill=True,
        common_norm=False,
        alpha=0.4,
    )
    plt.xlabel("Cargos mensuales (USD)")
    plt.ylabel("Densidad")
    plt.title("Distribución de MonthlyCharges por clase de churn")
    plt.tight_layout()
    plt.savefig(ASSETS_DIR / "04_monthlycharges_density.png", dpi=300)
    plt.close()

    services = churn_rate(df, "ServicesCount").sort_index()
    plt.figure(figsize=(7, 4))
    sns.lineplot(
        data=services.reset_index(),
        x="ServicesCount",
        y="churn_rate",
        marker="o",
    )
    plt.xlabel("Número de servicios activos")
    plt.ylabel("Tasa de churn (%)")
    plt.title("Relación entre diversidad de servicios y churn")
    plt.tight_layout()
    plt.savefig(ASSETS_DIR / "05_services_count_vs_churn.png", dpi=300)
    plt.close()

    service_cols = [
        "OnlineSecurity",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
    ]
    heatmap_data = (
        df.assign(
            OnlineSecurity=lambda d: d["OnlineSecurity"].replace(
                {"No internet service": "No"}
            ),
            TechSupport=lambda d: d["TechSupport"].replace(
                {"No internet service": "No"}
            ),
            StreamingTV=lambda d: d["StreamingTV"].replace(
                {"No internet service": "No"}
            ),
            StreamingMovies=lambda d: d["StreamingMovies"].replace(
                {"No internet service": "No"}
            ),
        )
        .groupby(service_cols, observed=True)["ChurnFlag"]
        .mean()
        .mul(100)
        .unstack("StreamingMovies")
    )
    plt.figure(figsize=(6, 5))
    sns.heatmap(
        heatmap_data,
        annot=True,
        fmt=".1f",
        cmap="RdYlBu_r",
        cbar_kws={"label": "Churn (%)"},
    )
    plt.title("Churn (%) por combinaciones de servicios clave")
    plt.tight_layout()
    plt.savefig(ASSETS_DIR / "06_services_heatmap.png", dpi=300)
    plt.close()


def generar_tablas(df: pd.DataFrame) -> dict[str, list[dict[str, float]]]:
    tablas = {
        "global": [
            {
                "metric": "Clientes",
                "value": int(df.shape[0]),
            },
            {
                "metric": "Tasa de churn (%)",
                "value": round(df["ChurnFlag"].mean() * 100, 2),
            },
            {
                "metric": "Tenure mediana (meses)",
                "value": round(df["tenure"].median(), 0),
            },
            {
                "metric": "MonthlyCharges promedio (USD)",
                "value": round(df["MonthlyCharges"].mean(), 2),
            },
            {
                "metric": "TotalCharges promedio (USD)",
                "value": round(df["TotalCharges"].mean(), 2),
            },
        ]
    }

    tablas["contract"] = churn_rate(df, "Contract").reset_index().to_dict("records")
    tablas["payment"] = churn_rate(df, "PaymentMethod").reset_index().to_dict("records")
    tablas["tenure_group"] = (
        churn_rate(df, "TenureGroup").reset_index().to_dict("records")
    )
    tablas["monthly_segment"] = (
        churn_rate(df, "MonthlySegment")
        .dropna()
        .sort_values("MonthlySegment")
        .reset_index()
        .to_dict("records")
    )
    tablas["services_count"] = (
        churn_rate(df, "ServicesCount").reset_index().to_dict("records")
    )
    return tablas


def guardar_resumen(tablas: dict[str, list[dict[str, float]]]) -> None:
    md_path = OUTPUTS_DIR / "telco_insights.md"
    with md_path.open("w", encoding="utf-8") as fh:
        fh.write("# Resumen de Insights - Telco Churn\n\n")
        fh.write("## Métricas globales\n")
        for item in tablas["global"]:
            fh.write(f"- **{item['metric']}**: {item['value']}\n")
        fh.write("\n## Churn por contrato\n")
        for row in tablas["contract"]:
            fh.write(
                f"- {row['Contract']}: {row['churn_rate']:.1f}% (n={row['clientes']})\n"
            )
        fh.write("\n## Churn por método de pago (Top 4)\n")
        for row in tablas["payment"]:
            fh.write(
                f"- {row['PaymentMethod']}: {row['churn_rate']:.1f}% (n={row['clientes']})\n"
            )
        fh.write("\n## Churn por grupo de tenure\n")
        for row in tablas["tenure_group"]:
            fh.write(
                f"- {row['TenureGroup']}: {row['churn_rate']:.1f}% (n={row['clientes']})\n"
            )
        fh.write("\n## Churn por segmento de MonthlyCharges\n")
        for row in tablas["monthly_segment"]:
            fh.write(
                f"- {row['MonthlySegment']}: {row['churn_rate']:.1f}% (n={row['clientes']})\n"
            )
        fh.write("\n## Churn por número de servicios activos\n")
        for row in tablas["services_count"]:
            fh.write(
                f"- {int(row['ServicesCount'])} servicios: {row['churn_rate']:.1f}% "
                f"(n={row['clientes']})\n"
            )

    json_path = OUTPUTS_DIR / "telco_metrics.json"
    json_path.write_text(json.dumps(tablas, indent=2), encoding="utf-8")


def main() -> None:
    preparar_directorios()
    df = cargar_dataset()
    generar_graficos(df)
    tablas = generar_tablas(df)
    guardar_resumen(tablas)
    print("✅ Insights generados en assets/ y outputs/")


if __name__ == "__main__":
    main()
