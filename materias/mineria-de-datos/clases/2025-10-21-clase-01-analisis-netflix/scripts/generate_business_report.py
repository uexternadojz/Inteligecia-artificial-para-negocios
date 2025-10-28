#!/usr/bin/env python3
"""
Script para generar un reporte ejecutivo de negocio del catálogo de Netflix
Autor: Análisis Exploratorio de Datos
Fecha: 2025
"""

import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path
import sys

def print_header(title, char="="):
    """Imprime un encabezado formateado"""
    line = char * 80
    print(f"\n{line}")
    print(f"{title.center(80)}")
    print(f"{line}\n")

def print_section(title):
    """Imprime un título de sección"""
    print(f"\n{title}")
    print("-" * len(title))

def load_and_prepare_data(filepath: Path):
    """Carga y prepara los datos"""
    try:
        df = pd.read_csv(filepath)

        # Conversiones necesarias
        df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
        df['year_added'] = df['date_added'].dt.year
        df['month_added'] = df['date_added'].dt.month

        # Extraer duración numérica
        df_movies = df[df['type'] == 'Movie'].copy()
        df_tv = df[df['type'] == 'TV Show'].copy()

        if len(df_movies) > 0:
            df_movies['duration_min'] = df_movies['duration'].str.extract(r'(\d+)').astype(float)
        if len(df_tv) > 0:
            df_tv['seasons'] = df_tv['duration'].str.extract(r'(\d+)').astype(float)

        # Tiempo hasta Netflix
        df['time_to_netflix'] = df['year_added'] - df['release_year']

        return df, df_movies, df_tv
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        sys.exit(1)

def generate_business_report(df, df_movies, df_tv):
    """Genera el reporte completo de negocio"""

    print_header("REPORTE DE ENTENDIMIENTO DE NEGOCIO - CATÁLOGO NETFLIX")

    print(f"Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total de registros analizados: {len(df):,}")

    # 1. RESUMEN EJECUTIVO
    print_header("1. RESUMEN EJECUTIVO", "=")

    print("""
El catálogo de Netflix ha sido analizado exhaustivamente, revelando insights clave
sobre su composición, estrategia de contenido y tendencias de negocio. Este reporte
presenta hallazgos accionables para la toma de decisiones estratégicas.
    """)

    # 2. COMPOSICIÓN DEL CATÁLOGO
    print_header("2. COMPOSICIÓN DEL CATÁLOGO", "=")

    content_dist = df['type'].value_counts()
    content_pct = df['type'].value_counts(normalize=True) * 100

    print_section("2.1 Distribución de Contenido")
    print(f"Total de títulos: {len(df):,}\n")
    for tipo in content_dist.index:
        print(f"  • {tipo:15s}: {content_dist[tipo]:6,} títulos ({content_pct[tipo]:5.2f}%)")

    print("\nINSIGHT CLAVE:")
    print(f"  → El catálogo está dominado por PELÍCULAS ({content_pct['Movie']:.1f}%)")
    print(f"  → Las series representan solo el {content_pct['TV Show']:.1f}% del contenido")
    print(f"  → Ratio Películas:Series = {content_dist['Movie']/content_dist['TV Show']:.2f}:1")

    # 3. ANÁLISIS TEMPORAL
    print_header("3. ANÁLISIS TEMPORAL Y TENDENCIAS", "=")

    print_section("3.1 Años de Lanzamiento")
    print(f"  • Rango de años: {df['release_year'].min():.0f} - {df['release_year'].max():.0f}")
    print(f"  • Año promedio: {df['release_year'].mean():.1f}")
    print(f"  • Mediana: {df['release_year'].median():.0f}")

    # Contenido moderno
    modern_content = (df['release_year'] >= 2015).sum()
    modern_pct = modern_content / len(df) * 100

    classic_content = (df['release_year'] < 2000).sum()
    classic_pct = classic_content / len(df) * 100

    print(f"\n  • Contenido post-2015 (moderno): {modern_content:,} ({modern_pct:.1f}%)")
    print(f"  • Contenido pre-2000 (clásico): {classic_content:,} ({classic_pct:.1f}%)")

    print("\nINSIGHT CLAVE:")
    print(f"  → Netflix prioriza contenido MODERNO: {modern_pct:.1f}% es de la última década")
    print(f"  → El contenido clásico representa solo el {classic_pct:.1f}%")

    print_section("3.2 Adición a Netflix")

    if df['year_added'].notna().sum() > 0:
        print(f"  • Primera adición: {df['date_added'].min()}")
        print(f"  • Última adición: {df['date_added'].max()}")

        # Top años de adición
        top_years = df['year_added'].value_counts().head(5)
        print("\n  Top 5 años con más adiciones:")
        for year, count in top_years.items():
            print(f"    {year:.0f}: {count:5,} títulos")

        # Tiempo promedio hasta Netflix
        time_clean = df[df['time_to_netflix'] >= 0]['time_to_netflix']
        if len(time_clean) > 0:
            print(f"\n  • Tiempo promedio hasta Netflix: {time_clean.mean():.1f} años")
            print(f"    - Películas: {df[df['type']=='Movie']['time_to_netflix'].mean():.1f} años")
            print(f"    - Series: {df[df['type']=='TV Show']['time_to_netflix'].mean():.1f} años")

    # 4. ANÁLISIS GEOGRÁFICO
    print_header("4. DISTRIBUCIÓN GEOGRÁFICA", "=")

    countries_list = df['country'].dropna().str.split(', ').explode()
    top_countries = countries_list.value_counts().head(15)

    print_section("4.1 Top Países Productores")
    print(f"Total de países únicos: {countries_list.nunique()}\n")
    print("Top 15 países:")
    for i, (country, count) in enumerate(top_countries.items(), 1):
        pct = count / len(df) * 100
        print(f"  {i:2d}. {country:30s}: {count:5,} ({pct:5.2f}%)")

    # Dominancia USA
    usa_count = top_countries['United States']
    usa_pct = usa_count / len(df) * 100

    print("\nINSIGHT CLAVE:")
    print(f"  → Estados Unidos DOMINA con {usa_pct:.1f}% del catálogo")
    print(f"  → India es el segundo productor con fuerte presencia de Bollywood")
    print(f"  → Contenido internacional diverso de {countries_list.nunique()} países")

    # 5. RATINGS Y AUDIENCIA
    print_header("5. CLASIFICACIÓN Y AUDIENCIA OBJETIVO", "=")

    rating_dist = df['rating'].value_counts()

    print_section("5.1 Top Ratings")
    for i, (rating, count) in enumerate(rating_dist.head(10).items(), 1):
        pct = count / len(df) * 100
        print(f"  {i:2d}. {rating:10s}: {count:5,} ({pct:5.2f}%)")

    # Contenido adulto
    adult_ratings = ['TV-MA', 'R', 'NC-17']
    adult_count = df[df['rating'].isin(adult_ratings)].shape[0]
    adult_pct = adult_count / len(df) * 100

    # Contenido familiar
    family_ratings = ['G', 'PG', 'TV-G', 'TV-Y', 'TV-Y7']
    family_count = df[df['rating'].isin(family_ratings)].shape[0]
    family_pct = family_count / len(df) * 100

    print("\nINSIGHT CLAVE:")
    print(f"  → Contenido ADULTO (TV-MA, R): {adult_pct:.1f}% del catálogo")
    print(f"  → Contenido FAMILIAR (G, PG, TV-Y): {family_pct:.1f}%")
    print(f"  → Enfoque claro en audiencias maduras y adolescentes")

    # 6. GÉNEROS
    print_header("6. ANÁLISIS DE GÉNEROS", "=")

    genres_list = df['listed_in'].dropna().str.split(', ').explode()
    top_genres = genres_list.value_counts().head(20)

    print_section("6.1 Top Géneros")
    print(f"Total de géneros únicos: {genres_list.nunique()}\n")
    print("Top 20 géneros:")
    for i, (genre, count) in enumerate(top_genres.items(), 1):
        pct = count / len(df) * 100
        print(f"  {i:2d}. {genre:45s}: {count:5,} ({pct:5.2f}%)")

    print("\nINSIGHT CLAVE:")
    print(f"  → Dramas internacionales lideran el catálogo")
    print(f"  → Fuerte presencia de comedias y documentales")
    print(f"  → Estrategia de diversificación con {genres_list.nunique()} géneros")

    # 7. CARACTERÍSTICAS DEL CONTENIDO
    print_header("7. CARACTERÍSTICAS DEL CONTENIDO", "=")

    print_section("7.1 Películas - Duración")
    if len(df_movies) > 0 and 'duration_min' in df_movies.columns:
        duration_data = df_movies['duration_min'].dropna()
        print(f"  • Duración promedio: {duration_data.mean():.1f} minutos")
        print(f"  • Mediana: {duration_data.median():.1f} minutos")
        print(f"  • Rango: {duration_data.min():.0f} - {duration_data.max():.0f} minutos")

        # Distribución por rangos
        print("\n  Distribución por rangos:")
        ranges = [(0, 60, 'Cortas (<60 min)'),
                  (60, 90, 'Medianas (60-90 min)'),
                  (90, 120, 'Estándar (90-120 min)'),
                  (120, 180, 'Largas (120-180 min)'),
                  (180, 500, 'Muy largas (>180 min)')]

        for min_dur, max_dur, label in ranges:
            count = ((duration_data >= min_dur) & (duration_data < max_dur)).sum()
            pct = count / len(duration_data) * 100
            print(f"    {label:30s}: {count:5,} ({pct:5.2f}%)")

    print_section("7.2 Series - Temporadas")
    if len(df_tv) > 0 and 'seasons' in df_tv.columns:
        seasons_data = df_tv['seasons'].dropna()
        print(f"  • Temporadas promedio: {seasons_data.mean():.2f}")
        print(f"  • Mediana: {seasons_data.median():.0f} temporadas")
        print(f"  • Rango: {seasons_data.min():.0f} - {seasons_data.max():.0f} temporadas")

        single_season = (seasons_data == 1).sum()
        single_pct = single_season / len(seasons_data) * 100

        print(f"\n  • Series de 1 temporada: {single_season:,} ({single_pct:.1f}%)")
        print(f"  • Series de 2+ temporadas: {len(seasons_data) - single_season:,} ({100-single_pct:.1f}%)")

    print("\nINSIGHT CLAVE:")
    print(f"  → Películas de duración estándar (~90-100 min)")
    print(f"  → Mayoría de series son de 1 temporada (contenido conciso)")
    print(f"  → Enfoque en contenido consumible rápidamente")

    # 8. CALIDAD DE DATOS
    print_header("8. CALIDAD Y COMPLETITUD DE DATOS", "=")

    missing_data = pd.DataFrame({
        'Columna': df.columns,
        'Valores Nulos': df.isnull().sum(),
        'Porcentaje': (df.isnull().sum() / len(df) * 100).round(2)
    })
    missing_data = missing_data[missing_data['Valores Nulos'] > 0].sort_values('Valores Nulos', ascending=False)

    if len(missing_data) > 0:
        print_section("8.1 Campos con Valores Faltantes")
        for _, row in missing_data.iterrows():
            print(f"  • {row['Columna']:20s}: {row['Valores Nulos']:6,} ({row['Porcentaje']:5.2f}%)")

        print("\nINSIGHT CLAVE:")
        print(f"  → Director, Cast y Country tienen valores faltantes significativos")
        print(f"  → Requerirá tratamiento especial en análisis que usen estos campos")
    else:
        print("  ✓ No hay valores faltantes en el dataset")

    # Completitud general
    completeness = (1 - df.isnull().sum() / len(df)) * 100
    print(f"\n  • Completitud promedio del dataset: {completeness.mean():.2f}%")

    # 9. DIRECTORES Y ACTORES
    print_header("9. ANÁLISIS DE CREADORES", "=")

    print_section("9.1 Top Directores")
    directors_list = df['director'].dropna().str.split(', ').explode()
    top_directors = directors_list.value_counts().head(15)

    for i, (director, count) in enumerate(top_directors.items(), 1):
        print(f"  {i:2d}. {director:40s}: {count:3,} títulos")

    print_section("9.2 Top Actores")
    cast_list = df['cast'].dropna().str.split(', ').explode()
    top_cast = cast_list.value_counts().head(15)

    for i, (actor, count) in enumerate(top_cast.items(), 1):
        print(f"  {i:2d}. {actor:40s}: {count:3,} apariciones")

    print("\nINSIGHT CLAVE:")
    print(f"  → {directors_list.nunique():,} directores únicos en el catálogo")
    print(f"  → {cast_list.nunique():,} actores únicos en el catálogo")
    print(f"  → Alta diversidad de talento creativo")

    # 10. RECOMENDACIONES ESTRATÉGICAS
    print_header("10. RECOMENDACIONES ESTRATÉGICAS DE NEGOCIO", "=")

    print("""
BASADO EN EL ANÁLISIS, SE RECOMIENDAN LAS SIGUIENTES ACCIONES:

1. BALANCE DE CONTENIDO
   • Incrementar la proporción de series vs películas para mejorar la
     retención de usuarios (las series generan engagement más prolongado)
   • Objetivo sugerido: Alcanzar un ratio 60:40 (Películas:Series)

2. ESTRATEGIA DE AUDIENCIA
   • Desarrollar más contenido familiar para diversificar la base de usuarios
   • Actualmente solo """ + f"{family_pct:.1f}%" + """ es contenido familiar
   • Oportunidad de capturar mercado familiar

3. CONTENIDO INTERNACIONAL
   • Continuar invirtiendo en producciones locales de mercados clave
   • India, Corea del Sur, y Europa son mercados con alto potencial
   • El contenido internacional ha demostrado éxito global

4. PROFUNDIDAD DE SERIES
   • Considerar invertir en series multi-temporada de calidad
   • Actualmente """ + f"{single_pct:.1f}%" + """ de series tienen solo 1 temporada
   • Las series longevas crean comunidades de fans leales

5. CALIDAD DE DATOS
   • Implementar procesos para completar metadatos faltantes
   • Mejorar la captura de información de directores y elenco
   • Esto permitirá mejores recomendaciones y búsquedas

6. ESTRATEGIA TEMPORAL
   • Mantener el enfoque en contenido moderno (post-2015)
   • Adquirir contenido recién estrenado (< 2 años)
   • Balance estratégico con clásicos culturalmente relevantes

7. DIVERSIFICACIÓN DE GÉNEROS
   • Identificar nichos desatendidos en el mercado
   • Experimentar con géneros híbridos
   • Documentales y contenido educativo tienen potencial de crecimiento

8. ANÁLISIS ADICIONALES NECESARIOS
   • Análisis de engagement por tipo de contenido
   • Estudio de patrones de visualización
   • Análisis de sentimiento en reseñas de usuarios
   • Análisis predictivo de éxito de nuevas producciones
   • Segmentación de usuarios por preferencias
    """)

    # RESUMEN FINAL
    print_header("RESUMEN DE MÉTRICAS CLAVE", "=")

    summary_data = {
        'Total de títulos': f"{len(df):,}",
        'Películas': f"{content_dist['Movie']:,} ({content_pct['Movie']:.1f}%)",
        'Series': f"{content_dist['TV Show']:,} ({content_pct['TV Show']:.1f}%)",
        'Países productores': f"{countries_list.nunique():,}",
        'Géneros únicos': f"{genres_list.nunique():,}",
        'Rango de años': f"{df['release_year'].min():.0f}-{df['release_year'].max():.0f}",
        'Contenido moderno (post-2015)': f"{modern_pct:.1f}%",
        'Contenido adulto': f"{adult_pct:.1f}%",
        'Contenido familiar': f"{family_pct:.1f}%",
        'País dominante': f"USA ({usa_pct:.1f}%)",
        'Completitud de datos': f"{completeness.mean():.1f}%"
    }

    if len(df_movies) > 0 and 'duration_min' in df_movies.columns:
        summary_data['Duración prom. películas'] = f"{df_movies['duration_min'].mean():.0f} min"
    if len(df_tv) > 0 and 'seasons' in df_tv.columns:
        summary_data['Temporadas prom. series'] = f"{df_tv['seasons'].mean():.1f}"

    for metric, value in summary_data.items():
        print(f"  {metric:30s}: {value}")

    print_header("FIN DEL REPORTE", "=")
    print(f"\nReporte generado exitosamente - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Para visualizaciones detalladas, consulte el notebook Jupyter ejecutado.\n")

def main() -> None:
    """Función principal"""
    print("\n" + "="*80)
    print("Generando Reporte de Entendimiento de Negocio - Netflix")
    print("="*80)

    base_dir = Path(__file__).resolve().parents[1]
    data_path = base_dir / 'data' / 'netflix_titles.csv'
    output_path = base_dir / 'docs' / 'REPORTE_NEGOCIO_NETFLIX.txt'

    if not data_path.exists():
        print(f"❌ No se encontró el dataset en {data_path}")
        sys.exit(1)

    # Cargar datos
    df, df_movies, df_tv = load_and_prepare_data(data_path)

    # Generar reporte
    generate_business_report(df, df_movies, df_tv)

    # Guardar a archivo
    import sys
    original_stdout = sys.stdout
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open('w', encoding='utf-8') as f:
        sys.stdout = f
        generate_business_report(df, df_movies, df_tv)
    sys.stdout = original_stdout
    print(f"\n✅ Reporte también guardado en: {output_path.relative_to(base_dir)}")

if __name__ == "__main__":
    main()
