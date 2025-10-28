# Análisis Exploratorio de Datos - Catálogo Netflix

## Descripción del Proyecto

Este proyecto contiene un análisis exploratorio profundo del catálogo de Netflix, con enfoque en insights de negocio. Se analizaron **8,807 títulos** entre películas y series de TV para identificar patrones, tendencias y oportunidades estratégicas.

## Estructura de Archivos

```
2025-10-21-clase-01-analisis-netflix/
├── README.md
├── docs/
│   ├── README_ANALISIS_NETFLIX.md        # Documentación técnica (este archivo)
│   ├── LEEME_PRIMERO.txt                 # Guía de navegación rápida
│   ├── RESUMEN_EJECUTIVO.md              # Resumen para stakeholders
│   ├── REPORTE_NEGOCIO_NETFLIX.txt       # Reporte ejecutivo generado
│   └── INDICE_ANALISIS.md                # Índice completo del proyecto
├── data/
│   ├── netflix_titles.csv                # Dataset original
│   └── netflix_titles_processed.csv      # Dataset procesado (generado)
├── notebooks/
│   ├── netflix_analysis.ipynb            # Notebook de análisis (plantilla)
│   └── netflix_analysis_executed.ipynb   # Notebook ejecutado con resultados
├── outputs/
│   └── netflix_summary_metrics.csv       # Métricas resumen (generado)
└── scripts/
    ├── generate_business_report.py       # Script para reporte ejecutivo
    └── verificar_analisis.sh             # Checklist y verificación
```

## Requisitos

### Entorno Virtual

Se recomienda crear un entorno virtual local (no versionado) e instalar las dependencias compartidas del curso:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r ../../../../herramientas/requirements.txt
pip install matplotlib seaborn wordcloud missingno jupyter
```

### Paquetes Utilizados

- pandas
- numpy
- matplotlib
- seaborn
- plotly
- wordcloud
- missingno
- jupyter

## Uso

> Todos los comandos parten desde la carpeta de la clase `2025-10-21-clase-01-analisis-netflix/`.

### 1. Ver el análisis completo (recomendado)

Abrir el notebook ejecutado con todos los resultados:

```bash
source .venv/bin/activate
jupyter notebook notebooks/netflix_analysis_executed.ipynb
```

### 2. Generar el reporte de negocio

Ejecutar el script para regenerar el reporte ejecutivo en `docs/`:

```bash
source .venv/bin/activate
python scripts/generate_business_report.py
```

Esto actualizará el archivo `docs/REPORTE_NEGOCIO_NETFLIX.txt` con todos los insights.

### 3. Re-ejecutar el análisis desde cero

```bash
source .venv/bin/activate
jupyter nbconvert --to notebook --execute notebooks/netflix_analysis.ipynb --output notebooks/netflix_analysis_nuevo.ipynb
```

## Insights Principales

### 1. Composición del Catálogo
- **69.6%** películas vs **30.4%** series
- Total: **8,807 títulos**
- Ratio Películas:Series = **2.29:1**

### 2. Estrategia Temporal
- **70.6%** del contenido es post-2015 (moderno)
- Tiempo promedio hasta Netflix: **4.7 años**
- Enfoque claro en contenido reciente

### 3. Distribución Geográfica
- **Estados Unidos domina** con 41.9% del catálogo
- **127 países** productores únicos
- Top 3: USA (41.9%), India (11.9%), UK (9.1%)

### 4. Clasificación de Audiencia
- **45.5%** contenido adulto (TV-MA, R)
- **13.5%** contenido familiar (G, PG, TV-Y)
- Predominio de audiencias maduras y adolescentes

### 5. Géneros Principales
- **42 géneros** únicos
- Top 3: International Movies (31.3%), Dramas (27.6%), Comedies (19.0%)
- Fuerte presencia de contenido internacional

### 6. Características del Contenido
- **Películas**: Duración promedio de **100 minutos**
- **Series**: **67%** tienen solo 1 temporada
- Temporadas promedio: **1.8**

### 7. Calidad de Datos
- Completitud general: **96.5%**
- Campos con valores faltantes: Director (29.9%), Country (9.4%), Cast (9.4%)

## Visualizaciones Incluidas

El notebook incluye las siguientes visualizaciones:

1. **Distribución de Contenido**: Gráficos de barras y torta
2. **Evolución Temporal**: Líneas de tendencia por año y década
3. **Adiciones a Netflix**: Heatmaps y distribuciones mensuales
4. **Análisis Geográfico**: Top países productores
5. **Ratings**: Distribución por clasificación de edad
6. **Duración**: Histogramas y box plots para películas
7. **Temporadas**: Distribución de series
8. **Géneros**: Top géneros y word clouds
9. **Directores y Actores**: Rankings de creadores
10. **Descripciones**: Word cloud de temas principales
11. **Patrones**: Correlaciones y análisis de tiempo hasta Netflix
12. **Matriz de Valores Nulos**: Análisis de completitud

## Recomendaciones Estratégicas

### 1. Balance de Contenido
- Incrementar proporción de series para mejorar retención
- Objetivo: Ratio 60:40 (Películas:Series)

### 2. Estrategia de Audiencia
- Desarrollar más contenido familiar (actualmente 13.5%)
- Oportunidad en mercado familiar

### 3. Contenido Internacional
- Continuar invirtiendo en producciones locales
- Mercados clave: India, Corea del Sur, Europa

### 4. Profundidad de Series
- Invertir en series multi-temporada de calidad
- 67% de series tienen solo 1 temporada

### 5. Calidad de Datos
- Completar metadatos faltantes (director, cast, country)
- Mejorar sistemas de captura de información

### 6. Diversificación de Géneros
- Identificar nichos desatendidos
- Experimentar con géneros híbridos
- Potencial en documentales y contenido educativo

## Análisis Futuros Sugeridos

1. **Análisis de Sentimiento**: Procesar descripciones para identificar temas emocionales
2. **Segmentación de Usuarios**: Clustering basado en preferencias
3. **Análisis Predictivo**: Predecir éxito de nuevo contenido
4. **Patrones de Visualización**: Correlacionar con datos de engagement
5. **Análisis de Red Social**: Relaciones entre actores/directores
6. **Estacionalidad**: Patrones de adición por época del año
7. **Competencia**: Comparar con catálogos de otros servicios

## Estructura del Análisis en el Notebook

1. **Importación y Configuración**
2. **Carga de Datos**
3. **Análisis de Calidad de Datos**
4. **Distribución de Contenido**
5. **Análisis Temporal**
6. **Adiciones a Netflix**
7. **Análisis Geográfico**
8. **Ratings**
9. **Duración**
10. **Géneros**
11. **Directores y Actores**
12. **Text Mining de Descripciones**
13. **Correlaciones y Patrones**
14. **Reporte Ejecutivo**
15. **Exportación de Resultados**

## Métricas Clave Exportadas

El análisis genera dos archivos CSV:

### `netflix_titles_processed.csv`
Dataset completo con columnas adicionales:
- `decade`: Década de lanzamiento
- `year_added`: Año de adición a Netflix
- `month_added`: Mes de adición
- `month_name`: Nombre del mes
- `time_to_netflix`: Años entre lanzamiento y adición
- `description_length`: Longitud de la descripción
- `duration_min`: Duración en minutos (películas)
- `seasons`: Número de temporadas (series)

### `netflix_summary_metrics.csv`
Resumen de métricas principales del análisis

## Notas Técnicas

### Tratamiento de Valores Nulos
- Se mantienen los registros con valores nulos
- Se aplica `.dropna()` solo en análisis específicos
- Se documenta el % de valores faltantes por columna

### Manejo de Múltiples Valores
- Campos como `country`, `cast`, `director`, `listed_in` contienen múltiples valores separados por comas
- Se utiliza `.str.split(',').explode()` para análisis individuales

### Codificación
- UTF-8 en todos los archivos generados
- Manejo especial de caracteres especiales en nombres

## Autor y Fecha

- **Análisis realizado**: Octubre 2025
- **Dataset**: Netflix Titles (actualizado hasta Septiembre 2021)
- **Herramientas**: Python 3, Jupyter, Pandas, Matplotlib, Seaborn, Plotly

## Licencia

Este análisis es con fines educativos y de investigación. Los datos pertenecen a Netflix y se utilizan únicamente para análisis académico.

---

**Para cualquier consulta o mejora del análisis, revisar el código en los notebooks o contactar al equipo de análisis.**
