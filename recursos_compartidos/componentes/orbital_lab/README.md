# Orbital Lab · Sistema Compartido

Este módulo concentra tokens y utilidades visuales para aplicar el branding Orbital en cualquier proyecto (web, guías, agentes CLI, presentaciones).

## Estructura

```
orbital_lab/
├─ tokens/
│  └─ theme.json          # Paleta, tipografías, spacing, sombras
├─ components/
│  └─ base.css            # Variables CSS + clases utilitarias
└─ assets/                # Logos, patterns, SVGs, moodboards (en progreso)
```

## Uso rápido

1. **Importa los tokens** en proyectos Astro/React/Svelte leyendo `tokens/theme.json` o cargando `components/base.css`.
2. **Aplica la clase** `body.orbital-theme` para establecer el fondo y la tipografía por defecto.
3. Usa `.orbital-card`, `.orbital-btn`, `.orbital-tag` y `.orbital-hero` como bloques base para cards, botones, chips y secciones hero.

```html
<link rel="stylesheet" href="/recursos_compartidos/componentes/orbital_lab/components/base.css" />
<body class="orbital-theme">
  <section class="orbital-hero">
    <h1 class="orbital-heading">Ver es entender</h1>
    <a class="orbital-btn" href="#clases">Explorar clases</a>
  </section>
</body>
```

## Próximos pasos

- Añadir `theme.json` como módulo npm local o paquete para importarlo en Astro.
- Documentar componentes adicionales (cards de proyecto, timelines, layouts de clase).
- Incluir versiones optimizadas de logos y patrones en `assets/`.
- Implementar pruebas visuales / Storybook ligero.
```
