# Herramientas

Scripts y utilidades para automatizar la creación de materiales docentes.

## Estructura

- `scripts/`: código reutilizable (por ejemplo, generadores de guías HTML, extractores de datasets, automatizadores de clase).
- (próximo) `plantillas/`: archivos base para clonación rápida (`cookiecutter`, `copier`, etc.).
- (próximo) `cli/`: comandos personalizados para scaffolding.

## Ideas Inmediatas

1. Extraer de las clases existentes los scripts generadores (`generar_guia_interactiva.py`) y convertirlos en módulos reutilizables.
2. Crear un comando `./scripts/nueva_clase.sh` que levante la estructura mínima.
3. Documentar dependencias globales en `requirements.txt` o `pyproject.toml`.
4. Añadir tests sencillos/anotaciones para asegurar que los generadores funcionan tras cambios.

---

Centralizar aquí la automatización permitirá escalar a múltiples materias sin reinventar la rueda.

## Scripts disponibles

- `scripts/generar_guia_crispdm.py`: Genera la guía interactiva CRISP-DM (Fases 1 y 2). Ejecutar con `python herramientas/scripts/generar_guia_crispdm.py -d <dataset> -o <salida>`
- `scripts/nueva_clase.py`: crea la estructura base de una clase (`python herramientas/scripts/nueva_clase.py --materia ...`).
