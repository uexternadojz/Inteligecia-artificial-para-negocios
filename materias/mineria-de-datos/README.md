# Materia: Minería de Datos

## Panorama

- **Institución:** Universidad Externado de Colombia
- **Profesor:** Juan Zuluaga
- **Metodología eje:** CRISP-DM con énfasis práctico e iterativo
- **Formato:** Clases presenciales con recursos interactivos HTML, handbooks y casos aplicados

## Clases Publicadas

| Fecha | Clase | Tema | Recursos clave |
|-------|-------|------|----------------|
| 2025-10-28 | Clase 03 | Preparación de Datos | Pipeline de limpieza, brief del caso |
| 2025-10-23 | Clase 02 | CRISP-DM Fases 1 y 2 | Guía interactiva Plotly, reporte pedagógico |
| 2025-10-21 | Clase 01 | Exploración EDA Netflix | Reporte ejecutivo, notebooks, dataset |

## Estructura de la Materia

```
mineria-de-datos/
├── docs/                # Documentación pedagógica, glosarios, bibliografía
├── clases/              # Sesiones cronológicas de la materia
│   ├── 2025-10-21-clase-01-analisis-netflix/
│   ├── 2025-10-23-crisp-dm-fases-1-2/
│   └── 2025-10-28-clase-03-preparacion-datos/
└── recursos/            # Handbooks, tutoriales o componentes específicos
```

## Cómo Añadir Una Nueva Clase

1. Clona la plantilla de clase dentro de `clases/<yyyy-mm-dd-clase-XX-tema>/` (pendiente de automatizar).
2. Ajusta el `README.md` de la clase con objetivos, agenda y materiales.
3. Guarda datasets en `datasets/` dentro de la clase o referencia los globales en `recursos_compartidos/datasets/`.
4. Documenta scripts o notebooks en la carpeta `tools/` o `notebooks/` de la clase, según aplique.
5. Actualiza la tabla de “Clases Publicadas” con la nueva sesión.

## Recursos Complementarios

- `docs/CRISP-DM_Fases_1_y_2.md`: base teórica para Comprensión del Negocio y de los Datos.
- `recursos/tutoriales/`: tutoriales transversales como instalación de CLIs y agentes.
- `recursos_compartidos/`: datasets, componentes y plantillas compartidas por todas las materias.

## Próximos Pasos (Sugeridos)

- Diseñar la Clase 03 (2025-10-28) enfocada en Preparación de Datos.
- Crear handbooks específicos (ej. “Checklist CRISP-DM”, “EDA acelerado”).
- Mover dependencias a un `requirements-materia.txt` para evitar `venv/` versionados.
- Empezar a extraer componentes HTML reutilizables para la página maestra del curso.

---

Este README debe evolucionar conforme se agreguen más clases, módulos y automatizaciones.
