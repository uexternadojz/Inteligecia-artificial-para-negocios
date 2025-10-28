#!/usr/bin/env python3
"""Wrapper para regenerar la guía interactiva reutilizando el generador global."""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from herramientas.scripts.generar_guia_crispdm import generar_guia_crispdm


def main() -> None:
    clase_dir = Path(__file__).resolve().parent
    shared_dataset = REPO_ROOT / 'recursos_compartidos/datasets/mineria-de-datos/supermarket_analysis.csv'
    dataset = shared_dataset if shared_dataset.exists() else clase_dir / 'SuperMarket Analysis.csv'
    salida = clase_dir / 'guia_interactiva_crisp_dm.html'
    generar_guia_crispdm(dataset=dataset, output=salida)


if __name__ == '__main__':
    main()
