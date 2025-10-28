# Agent Memory

Eres un agente CLI colaborando en el repo `docencia`. Objetivo: producir y mantener materiales docentes interactivos reutilizando las herramientas compartidas.

## Instrucciones clave

1. Revisa siempre la estructura principal (`README.md`, `ARCHITECTURE.md`, `materias/`, `recursos_compartidos/`, `herramientas/`, `skills/`, `site/`).
2. Genera guías HTML reutilizando `python herramientas/scripts/generar_guia_crispdm.py -d <dataset> -o <salida>`; si trabajas dentro de una clase usa el wrapper local existente.
3. Centraliza los datasets en `recursos_compartidos/datasets/` (ejemplo: `mineria-de-datos/supermarket_analysis.csv`) y referencia rutas relativas desde las clases.
4. Para nuevas sesiones ejecuta el scaffold `python herramientas/scripts/nueva_clase.py --help` y completa el README generado.
5. Crea entornos locales con `python -m venv .venv` y `pip install -r herramientas/requirements.txt`; nunca subas carpetas `venv/`.
6. Componentes, plantillas y tutoriales comunes deben vivir en `recursos_compartidos/` con documentación actualizada.
7. Cada clase debe documentarse en `materias/<materia>/README.md` y seguir la convención `YYYY-MM-DD-clase-XX-tema`.
8. Mantén consistencia en los assets: si un recurso puede reutilizarse, muévelo a compartidos y enlázalo.
