#!/usr/bin/env python3
"""Scaffolding rápido para crear la estructura base de una nueva clase."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
from string import Template

REPO_ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_PATH = REPO_ROOT / 'recursos_compartidos/plantillas/clase/README.md.tpl'


MONTHS_ES = {
    1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril', 5: 'mayo', 6: 'junio',
    7: 'julio', 8: 'agosto', 9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'
}


def humanize_date(date_str: str) -> str:
    dt = datetime.strptime(date_str, '%Y-%m-%d')
    return f"{dt.day:02d} de {MONTHS_ES[dt.month]} de {dt.year}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Crear scaffolding para una clase nueva.')
    parser.add_argument('--materia', required=True, help='Slug de la materia (ej: mineria-de-datos).')
    parser.add_argument('--titulo', required=True, help='Título breve de la clase.')
    parser.add_argument('--fecha', required=True, help='Fecha en formato YYYY-MM-DD.')
    parser.add_argument('--numero', type=int, required=True, help='Número de clase (ej: 3).')
    parser.add_argument('--slug', required=True, help='Slug del tema principal (ej: preparacion-datos).')
    parser.add_argument('--materia-nombre', help='Nombre legible de la materia (por defecto se deriva del slug).')
    parser.add_argument('--institucion', default='Universidad Externado de Colombia', help='Nombre de la institución.')
    parser.add_argument('--profesor', default='Juan Zuluaga', help='Nombre del profesor.')
    return parser.parse_args()


def slug_to_name(slug: str) -> str:
    return slug.replace('-', ' ').title()


def build_class_dir(args: argparse.Namespace) -> Path:
    clases_dir = REPO_ROOT / 'materias' / args.materia / 'clases'
    folder_name = f"{args.fecha}-clase-{args.numero:02d}-{args.slug}"
    return clases_dir / folder_name


def main() -> None:
    args = parse_args()

    plantilla = TEMPLATE_PATH.read_text()
    clase_dir = build_class_dir(args)
    clase_dir.mkdir(parents=True, exist_ok=True)

    for sub in ['docs', 'assets', 'data', 'notebooks', 'scripts', 'outputs']:
        (clase_dir / sub).mkdir(exist_ok=True)

    ruta_relativa = clase_dir.relative_to(REPO_ROOT)
    materia_nombre = args.materia_nombre or slug_to_name(args.materia)

    contexto = {
        'numero_formateado': f"Clase {args.numero:02d}",
        'titulo': args.titulo,
        'fecha_humana': humanize_date(args.fecha),
        'materia_nombre': materia_nombre,
        'institucion': args.institucion,
        'profesor': args.profesor,
        'ruta_relativa': ruta_relativa.as_posix()
    }

    contenido = Template(plantilla).substitute(contexto)
    (clase_dir / 'README.md').write_text(contenido)

    print(f"✅ Clase creada en: {clase_dir}")
    print("├── README.md (plantilla base)")
    print("├── docs/ | assets/ | data/ | notebooks/ | scripts/ | outputs/")
    print("ℹ️ Completa el README y añade materiales según sea necesario.")


if __name__ == '__main__':
    main()
