# Recursos Compartidos

Activos transversales que pueden usarse en cualquier materia o clase.

## Carpetas

- `componentes/`: bloques HTML/CSS/JS reutilizables (menús, layouts, widgets interactivos).
- `datasets/`: fuentes de datos originales/factores comunes. Organiza por materia (`mineria-de-datos/`, `nlp/`, etc.).
- `plantillas/`: bases para README, guías, presentaciones o notebooks.
- `tutoriales/`: guías transversales como instalación de herramientas o flujos de trabajo.
- `bibliografia/`: referencias académicas, papers, libros recomendados.

## Uso Recomendado

1. Cuando un recurso pueda servir en otra materia, muévelo aquí y reemplaza en la clase por una referencia relativa.
2. Documenta en un README dentro de cada subcarpeta cómo integrar el recurso.
3. Mantén versiones claras si un dataset o componente requiere actualizaciones (por ejemplo, `dataset_v2025-10.csv`).
4. Evita duplicar archivos pesados; centraliza en esta carpeta y crea symlinks o instrucciones para descargarlos.

## Pendiente

- Crear índice automático de tutoriales disponibles.
- Establecer convención de nomenclatura para componentes (`tipo-usecase-version`).
- Añadir scripts para sincronizar datasets a la web pública (`site/`).

---

Este módulo es clave para acelerar la creación de clases sin duplicar trabajo.
