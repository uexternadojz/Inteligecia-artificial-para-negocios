#!/usr/bin/env python3
"""
Script para generar guía interactiva de CRISP-DM Fases 1 y 2
Análisis del dataset de SuperMarket
"""

import argparse
from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def generar_guia_crispdm(dataset: str | Path = 'recursos_compartidos/datasets/mineria-de-datos/supermarket_analysis.csv', output: str | Path = 'guia_interactiva_crisp_dm.html', encoding: str = 'utf-8-sig') -> Path:
    """Genera la guía interactiva HTML para CRISP-DM Fases 1 y 2."""
    # Cargar datos
    dataset_path = Path(dataset).expanduser()
    print(f"📊 Cargando datos del supermercado desde {dataset_path}...")
    df = pd.read_csv(dataset_path, encoding=encoding)

    # Limpiar nombres de columnas
    df.columns = df.columns.str.strip()

    # Convertir fecha
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
    df['DayOfWeek'] = df['Date'].dt.day_name()
    df['Month'] = df['Date'].dt.month_name()

    # Extraer hora del día
    df['Hour'] = pd.to_datetime(df['Time'], format='%I:%M:%S %p').dt.hour

    print(f"✅ Datos cargados: {len(df)} registros, {len(df.columns)} columnas")

    # ============================================================================
    # ANÁLISIS Y VISUALIZACIONES
    # ============================================================================

    visualizaciones = {}

    # 1. ESTADÍSTICAS GENERALES
    stats_generales = {
        'total_transacciones': len(df),
        'total_ventas': f"${df['Sales'].sum():,.2f}",
        'ticket_promedio': f"${df['Sales'].mean():.2f}",
        'rating_promedio': f"{df['Rating'].mean():.2f}",
        'sucursales': df['Branch'].nunique(),
        'categorias_producto': df['Product line'].nunique(),
        'periodo': f"{df['Date'].min().strftime('%d/%m/%Y')} - {df['Date'].max().strftime('%d/%m/%Y')}"
    }

    # 2. DISTRIBUCIÓN DE VENTAS
    fig_ventas_dist = px.histogram(
        df,
        x='Sales',
        nbins=50,
        title='📊 Distribución de Ventas por Transacción',
        labels={'Sales': 'Venta Total ($)', 'count': 'Frecuencia'},
        color_discrete_sequence=['#3498db']
    )
    fig_ventas_dist.update_layout(
        showlegend=False,
        hovermode='x unified',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    visualizaciones['ventas_distribucion'] = fig_ventas_dist.to_html(include_plotlyjs='cdn', div_id="ventas_dist", config={'displayModeBar': True})

    # 3. VENTAS POR SUCURSAL
    ventas_branch = df.groupby('Branch')['Sales'].agg(['sum', 'mean', 'count']).reset_index()
    ventas_branch.columns = ['Sucursal', 'Total', 'Promedio', 'Transacciones']

    fig_branch = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Ventas Totales por Sucursal', 'Ticket Promedio por Sucursal'),
        specs=[[{"type": "bar"}, {"type": "bar"}]]
    )

    fig_branch.add_trace(
        go.Bar(x=ventas_branch['Sucursal'], y=ventas_branch['Total'],
               name='Total', marker_color='#2ecc71'),
        row=1, col=1
    )

    fig_branch.add_trace(
        go.Bar(x=ventas_branch['Sucursal'], y=ventas_branch['Promedio'],
               name='Promedio', marker_color='#e74c3c'),
        row=1, col=2
    )

    fig_branch.update_layout(
        showlegend=False,
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    visualizaciones['ventas_sucursal'] = fig_branch.to_html(include_plotlyjs='cdn', div_id="ventas_branch", config={'displayModeBar': True})

    # 4. LÍNEAS DE PRODUCTO
    ventas_producto = df.groupby('Product line').agg({
        'Sales': ['sum', 'mean', 'count'],
        'Rating': 'mean'
    }).reset_index()
    ventas_producto.columns = ['Producto', 'Total_Ventas', 'Promedio_Ventas', 'Cantidad', 'Rating_Promedio']
    ventas_producto = ventas_producto.sort_values('Total_Ventas', ascending=True)

    fig_productos = go.Figure()
    fig_productos.add_trace(go.Bar(
        y=ventas_producto['Producto'],
        x=ventas_producto['Total_Ventas'],
        orientation='h',
        marker=dict(
            color=ventas_producto['Rating_Promedio'],
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title="Rating")
        ),
        text=ventas_producto['Total_Ventas'].apply(lambda x: f'${x:,.0f}'),
        textposition='auto',
        hovertemplate='<b>%{y}</b><br>Ventas: $%{x:,.2f}<br>Rating: %{marker.color:.2f}<extra></extra>'
    ))

    fig_productos.update_layout(
        title='🛍️ Ventas por Línea de Producto (coloreado por Rating)',
        xaxis_title='Ventas Totales ($)',
        yaxis_title='',
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    visualizaciones['ventas_producto'] = fig_productos.to_html(include_plotlyjs='cdn', div_id="ventas_producto", config={'displayModeBar': True})

    # 5. TIPOS DE CLIENTE
    cliente_stats = df.groupby('Customer type').agg({
        'Sales': ['sum', 'mean', 'count'],
        'Rating': 'mean'
    }).reset_index()
    cliente_stats.columns = ['Tipo', 'Total_Ventas', 'Promedio_Ventas', 'Cantidad', 'Rating_Promedio']

    fig_clientes = make_subplots(
        rows=1, cols=3,
        subplot_titles=('Distribución de Clientes', 'Ventas Promedio', 'Rating Promedio'),
        specs=[[{"type": "pie"}, {"type": "bar"}, {"type": "bar"}]]
    )

    fig_clientes.add_trace(
        go.Pie(labels=cliente_stats['Tipo'], values=cliente_stats['Cantidad'],
               marker_colors=['#3498db', '#e67e22']),
        row=1, col=1
    )

    fig_clientes.add_trace(
        go.Bar(x=cliente_stats['Tipo'], y=cliente_stats['Promedio_Ventas'],
               marker_color=['#3498db', '#e67e22']),
        row=1, col=2
    )

    fig_clientes.add_trace(
        go.Bar(x=cliente_stats['Tipo'], y=cliente_stats['Rating_Promedio'],
               marker_color=['#3498db', '#e67e22']),
        row=1, col=3
    )

    fig_clientes.update_layout(
        showlegend=False,
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    visualizaciones['clientes_tipo'] = fig_clientes.to_html(include_plotlyjs='cdn', div_id="clientes_tipo", config={'displayModeBar': True})

    # 6. MÉTODOS DE PAGO
    pago_stats = df.groupby('Payment').agg({
        'Sales': ['sum', 'count', 'mean']
    }).reset_index()
    pago_stats.columns = ['Metodo', 'Total', 'Cantidad', 'Promedio']

    fig_pago = go.Figure(data=[
        go.Bar(name='Cantidad', x=pago_stats['Metodo'], y=pago_stats['Cantidad'], marker_color='#9b59b6'),
    ])

    fig_pago.update_layout(
        title='💳 Distribución de Métodos de Pago',
        yaxis_title='Número de Transacciones',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    visualizaciones['metodos_pago'] = fig_pago.to_html(include_plotlyjs='cdn', div_id="metodos_pago", config={'displayModeBar': True})

    # 7. ANÁLISIS TEMPORAL - VENTAS POR DÍA
    ventas_diarias = df.groupby('Date')['Sales'].sum().reset_index()

    fig_temporal = go.Figure()
    fig_temporal.add_trace(go.Scatter(
        x=ventas_diarias['Date'],
        y=ventas_diarias['Sales'],
        mode='lines+markers',
        line=dict(color='#1abc9c', width=2),
        marker=dict(size=6),
        fill='tozeroy',
        fillcolor='rgba(26, 188, 156, 0.2)',
        hovertemplate='Fecha: %{x|%d/%m/%Y}<br>Ventas: $%{y:,.2f}<extra></extra>'
    ))

    fig_temporal.update_layout(
        title='📈 Evolución de Ventas Diarias',
        xaxis_title='Fecha',
        yaxis_title='Ventas ($)',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        hovermode='x unified'
    )
    visualizaciones['ventas_tiempo'] = fig_temporal.to_html(include_plotlyjs='cdn', div_id="ventas_tiempo", config={'displayModeBar': True})

    # 8. VENTAS POR HORA DEL DÍA
    ventas_hora = df.groupby('Hour')['Sales'].agg(['sum', 'count', 'mean']).reset_index()

    fig_hora = go.Figure()
    fig_hora.add_trace(go.Bar(
        x=ventas_hora['Hour'],
        y=ventas_hora['count'],
        marker=dict(
            color=ventas_hora['mean'],
            colorscale='Plasma',
            showscale=True,
            colorbar=dict(title="Ticket<br>Promedio")
        ),
        hovertemplate='Hora: %{x}:00<br>Transacciones: %{y}<br>Promedio: $%{marker.color:.2f}<extra></extra>'
    ))

    fig_hora.update_layout(
        title='⏰ Distribución de Ventas por Hora del Día',
        xaxis_title='Hora',
        yaxis_title='Número de Transacciones',
        xaxis=dict(tickmode='linear', tick0=10, dtick=1),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    visualizaciones['ventas_hora'] = fig_hora.to_html(include_plotlyjs='cdn', div_id="ventas_hora", config={'displayModeBar': True})

    # 9. DISTRIBUCIÓN DE RATINGS
    fig_rating = go.Figure()
    fig_rating.add_trace(go.Histogram(
        x=df['Rating'],
        nbinsx=20,
        marker_color='#f39c12',
        hovertemplate='Rating: %{x:.1f}<br>Frecuencia: %{y}<extra></extra>'
    ))

    fig_rating.update_layout(
        title='⭐ Distribución de Calificaciones de Clientes',
        xaxis_title='Rating',
        yaxis_title='Frecuencia',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    visualizaciones['rating_dist'] = fig_rating.to_html(include_plotlyjs='cdn', div_id="rating_dist", config={'displayModeBar': True})

    # 10. HEATMAP: Producto vs Sucursal
    pivot_producto_branch = df.pivot_table(
        values='Sales',
        index='Product line',
        columns='Branch',
        aggfunc='sum'
    )

    fig_heatmap = go.Figure(data=go.Heatmap(
        z=pivot_producto_branch.values,
        x=pivot_producto_branch.columns,
        y=pivot_producto_branch.index,
        colorscale='YlOrRd',
        hovertemplate='Sucursal: %{x}<br>Producto: %{y}<br>Ventas: $%{z:,.2f}<extra></extra>'
    ))

    fig_heatmap.update_layout(
        title='🔥 Mapa de Calor: Ventas por Producto y Sucursal',
        xaxis_title='Sucursal',
        yaxis_title='Línea de Producto',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    visualizaciones['heatmap_producto_branch'] = fig_heatmap.to_html(include_plotlyjs='cdn', div_id="heatmap", config={'displayModeBar': True})

    # 11. CORRELACIÓN: Precio vs Cantidad vs Rating
    fig_scatter = px.scatter(
        df,
        x='Unit price',
        y='Quantity',
        size='Sales',
        color='Rating',
        color_continuous_scale='Viridis',
        hover_data=['Branch', 'Product line'],
        title='🔍 Relación: Precio Unitario vs Cantidad (tamaño = Ventas, color = Rating)'
    )

    fig_scatter.update_layout(
        xaxis_title='Precio Unitario ($)',
        yaxis_title='Cantidad',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    visualizaciones['scatter_precio_cantidad'] = fig_scatter.to_html(include_plotlyjs='cdn', div_id="scatter", config={'displayModeBar': True})

    # 12. ANÁLISIS DE CALIDAD - Datos faltantes
    missing_data = df.isnull().sum()
    missing_percent = (missing_data / len(df)) * 100
    calidad_data = pd.DataFrame({
        'Variable': missing_data.index,
        'Faltantes': missing_data.values,
        'Porcentaje': missing_percent.values
    }).sort_values('Faltantes', ascending=False)

    # 13. TOP INSIGHTS - Tarjetas de estadísticas
    insights = []

    # Insight 1: Mejor categoría
    mejor_categoria = ventas_producto.iloc[-1]
    insights.append({
        'titulo': 'Categoría Líder',
        'valor': mejor_categoria['Producto'],
        'detalle': f"${mejor_categoria['Total_Ventas']:,.0f} en ventas totales",
        'icon': '🏆'
    })

    # Insight 2: Hora pico
    hora_pico = ventas_hora.loc[ventas_hora['count'].idxmax(), 'Hour']
    insights.append({
        'titulo': 'Hora Pico',
        'valor': f"{int(hora_pico)}:00",
        'detalle': f"{int(ventas_hora['count'].max())} transacciones",
        'icon': '⏰'
    })

    # Insight 3: Rating más común
    rating_mode = df['Rating'].mode()[0]
    insights.append({
        'titulo': 'Rating Más Común',
        'valor': f"{rating_mode:.1f} ⭐",
        'detalle': f"Promedio general: {df['Rating'].mean():.2f}",
        'icon': '👍'
    })

    # Insight 4: Método de pago preferido
    pago_top = pago_stats.loc[pago_stats['Cantidad'].idxmax(), 'Metodo']
    insights.append({
        'titulo': 'Pago Preferido',
        'valor': pago_top,
        'detalle': f"{int(pago_stats['Cantidad'].max())} transacciones",
        'icon': '💳'
    })

    # Insight 5: Tipo de cliente
    tipo_cliente_dom = cliente_stats.loc[cliente_stats['Cantidad'].idxmax(), 'Tipo']
    porcentaje_dom = (cliente_stats['Cantidad'].max() / cliente_stats['Cantidad'].sum() * 100)
    insights.append({
        'titulo': 'Tipo de Cliente Dominante',
        'valor': tipo_cliente_dom,
        'detalle': f"{porcentaje_dom:.1f}% del total",
        'icon': '👥'
    })

    # Insight 6: Variabilidad de ventas
    cv_ventas = (df['Sales'].std() / df['Sales'].mean()) * 100
    insights.append({
        'titulo': 'Variabilidad de Ventas',
        'valor': f"{cv_ventas:.1f}%",
        'detalle': "Coeficiente de variación",
        'icon': '📊'
    })

    print("✅ Análisis completado. Generando HTML...")

    # ============================================================================
    # GENERAR HTML INTERACTIVO
    # ============================================================================

    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CRISP-DM: Guía Interactiva - Supermercado</title>
        <script src="https://cdn.plot.ly/plotly-2.26.0.min.js"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap" rel="stylesheet">
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}

            body {{
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: #2c3e50;
                line-height: 1.6;
                overflow-x: hidden;
            }}

            .container {{
                max-width: 1400px;
                margin: 0 auto;
                padding: 20px;
            }}

            header {{
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                padding: 40px 20px;
                margin-bottom: 40px;
                border-radius: 20px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                text-align: center;
                animation: slideDown 0.8s ease-out;
            }}

            @keyframes slideDown {{
                from {{
                    opacity: 0;
                    transform: translateY(-50px);
                }}
                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}

            h1 {{
                font-size: 3.5em;
                font-weight: 800;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 10px;
            }}

            .subtitle {{
                font-size: 1.3em;
                color: #7f8c8d;
                font-weight: 300;
            }}

            .nav-tabs {{
                display: flex;
                gap: 10px;
                margin-bottom: 30px;
                flex-wrap: wrap;
                justify-content: center;
            }}

            .tab-btn {{
                background: white;
                border: none;
                padding: 15px 30px;
                border-radius: 50px;
                font-size: 1em;
                font-weight: 600;
                cursor: pointer;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            }}

            .tab-btn:hover {{
                transform: translateY(-2px);
                box-shadow: 0 6px 20px rgba(0,0,0,0.15);
            }}

            .tab-btn.active {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                transform: scale(1.05);
            }}

            .tab-content {{
                display: none;
                animation: fadeIn 0.5s ease-in;
            }}

            .tab-content.active {{
                display: block;
            }}

            @keyframes fadeIn {{
                from {{
                    opacity: 0;
                    transform: translateY(20px);
                }}
                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}

            .card {{
                background: white;
                border-radius: 20px;
                padding: 30px;
                margin-bottom: 30px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.1);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }}

            .card:hover {{
                transform: translateY(-5px);
                box-shadow: 0 15px 50px rgba(0,0,0,0.15);
            }}

            .card-title {{
                font-size: 1.8em;
                font-weight: 700;
                color: #2c3e50;
                margin-bottom: 20px;
                padding-bottom: 15px;
                border-bottom: 3px solid #667eea;
            }}

            .stats-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }}

            .stat-card {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 25px;
                border-radius: 15px;
                text-align: center;
                transition: transform 0.3s ease;
                cursor: pointer;
            }}

            .stat-card:hover {{
                transform: scale(1.05) rotate(1deg);
            }}

            .stat-icon {{
                font-size: 3em;
                margin-bottom: 10px;
            }}

            .stat-value {{
                font-size: 2.2em;
                font-weight: 800;
                margin-bottom: 5px;
            }}

            .stat-label {{
                font-size: 1em;
                opacity: 0.9;
                font-weight: 300;
            }}

            .insight-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                margin: 30px 0;
            }}

            .insight-card {{
                background: white;
                border-left: 5px solid #667eea;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.08);
                transition: all 0.3s ease;
            }}

            .insight-card:hover {{
                border-left-width: 8px;
                transform: translateX(5px);
            }}

            .insight-icon {{
                font-size: 2.5em;
                margin-bottom: 10px;
            }}

            .insight-value {{
                font-size: 1.5em;
                font-weight: 700;
                color: #2c3e50;
            }}

            .insight-detail {{
                font-size: 0.9em;
                color: #7f8c8d;
                margin-top: 5px;
            }}

            .phase-header {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 30px;
                border-radius: 15px;
                margin-bottom: 30px;
                text-align: center;
            }}

            .phase-number {{
                font-size: 4em;
                font-weight: 800;
                opacity: 0.3;
                line-height: 1;
            }}

            .phase-title {{
                font-size: 2em;
                font-weight: 700;
                margin: 10px 0;
            }}

            .phase-desc {{
                font-size: 1.1em;
                opacity: 0.9;
            }}

            .objective-box {{
                background: #f8f9fa;
                border-left: 5px solid #3498db;
                padding: 20px;
                margin: 20px 0;
                border-radius: 10px;
            }}

            .objective-box h3 {{
                color: #3498db;
                margin-bottom: 10px;
            }}

            .checklist {{
                list-style: none;
                padding: 0;
            }}

            .checklist li {{
                padding: 12px;
                margin: 8px 0;
                background: white;
                border-radius: 8px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.05);
                transition: all 0.3s ease;
            }}

            .checklist li:hover {{
                transform: translateX(5px);
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }}

            .checklist li::before {{
                content: "✓";
                color: #2ecc71;
                font-weight: bold;
                margin-right: 10px;
                font-size: 1.2em;
            }}

            .viz-container {{
                margin: 30px 0;
            }}

            .table-container {{
                overflow-x: auto;
                margin: 20px 0;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
                background: white;
            }}

            th {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 15px;
                text-align: left;
                font-weight: 600;
            }}

            td {{
                padding: 12px 15px;
                border-bottom: 1px solid #ecf0f1;
            }}

            tr:hover {{
                background: #f8f9fa;
            }}

            .highlight-box {{
                background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
                border-radius: 15px;
                padding: 25px;
                margin: 25px 0;
            }}

            .alert {{
                background: #fff3cd;
                border-left: 5px solid #ffc107;
                padding: 15px;
                margin: 20px 0;
                border-radius: 8px;
            }}

            .success {{
                background: #d4edda;
                border-left: 5px solid #28a745;
            }}

            .info {{
                background: #d1ecf1;
                border-left: 5px solid #17a2b8;
            }}

            footer {{
                text-align: center;
                padding: 40px 20px;
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                margin-top: 50px;
                box-shadow: 0 -10px 40px rgba(0,0,0,0.1);
            }}

            .emoji {{
                font-size: 1.5em;
            }}

            @media (max-width: 768px) {{
                h1 {{
                    font-size: 2em;
                }}

                .stats-grid {{
                    grid-template-columns: 1fr;
                }}

                .insight-grid {{
                    grid-template-columns: 1fr;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>🎓 CRISP-DM: Guía Interactiva</h1>
                <p class="subtitle">Fases 1 y 2 - Análisis de Supermercado</p>
                <p style="margin-top: 20px; color: #95a5a6;">Universidad Externado de Colombia | Minería de Datos</p>
            </header>

            <div class="nav-tabs">
                <button class="tab-btn active" onclick="showTab('intro')">🏠 Introducción</button>
                <button class="tab-btn" onclick="showTab('fase1')">📋 Fase 1: Negocio</button>
                <button class="tab-btn" onclick="showTab('fase2')">📊 Fase 2: Datos</button>
                <button class="tab-btn" onclick="showTab('exploracion')">🔍 Exploración</button>
                <button class="tab-btn" onclick="showTab('calidad')">✅ Calidad</button>
                <button class="tab-btn" onclick="showTab('insights')">💡 Insights</button>
            </div>

            <!-- TAB: INTRODUCCIÓN -->
            <div id="intro" class="tab-content active">
                <div class="card">
                    <h2 class="card-title">📦 Contexto del Dataset</h2>
                    <p style="font-size: 1.1em; margin-bottom: 20px;">
                        Trabajaremos con datos reales de una cadena de supermercados en Myanmar.
                        Este dataset contiene información de ventas que nos permitirá aplicar las primeras
                        dos fases de la metodología CRISP-DM de manera práctica.
                    </p>

                    <div class="stats-grid">
                        <div class="stat-card">
                            <div class="stat-icon">📝</div>
                            <div class="stat-value">{stats_generales['total_transacciones']}</div>
                            <div class="stat-label">Transacciones</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-icon">💰</div>
                            <div class="stat-value">{stats_generales['total_ventas']}</div>
                            <div class="stat-label">Ventas Totales</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-icon">🎯</div>
                            <div class="stat-value">{stats_generales['ticket_promedio']}</div>
                            <div class="stat-label">Ticket Promedio</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-icon">⭐</div>
                            <div class="stat-value">{stats_generales['rating_promedio']}</div>
                            <div class="stat-label">Rating Promedio</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-icon">🏢</div>
                            <div class="stat-value">{stats_generales['sucursales']}</div>
                            <div class="stat-label">Sucursales</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-icon">📦</div>
                            <div class="stat-value">{stats_generales['categorias_producto']}</div>
                            <div class="stat-label">Categorías</div>
                        </div>
                    </div>

                    <div class="highlight-box">
                        <h3 style="margin-bottom: 15px;">📅 Período de Análisis</h3>
                        <p style="font-size: 1.2em; color: #2c3e50;">{stats_generales['periodo']}</p>
                        <p style="color: #7f8c8d; margin-top: 10px;">Aproximadamente 3 meses de datos transaccionales</p>
                    </div>

                    <div class="alert info">
                        <strong>💡 ¿Por qué este dataset?</strong><br>
                        Este dataset es ideal para aprender CRISP-DM porque contiene datos reales del mundo del retail,
                        con variables tanto categóricas como numéricas, y permite formular preguntas de negocio relevantes.
                    </div>
                </div>

                <div class="card">
                    <h2 class="card-title">🗺️ Estructura del Dataset</h2>
                    <p>El dataset contiene <strong>17 variables</strong> que describen cada transacción:</p>

                    <div class="table-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>Variable</th>
                                    <th>Tipo</th>
                                    <th>Descripción</th>
                                    <th>Ejemplo</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>Invoice ID</strong></td>
                                    <td>Categórica</td>
                                    <td>Identificador único</td>
                                    <td>750-67-8428</td>
                                </tr>
                                <tr>
                                    <td><strong>Branch</strong></td>
                                    <td>Categórica</td>
                                    <td>Sucursal (Alex, Giza, Cairo)</td>
                                    <td>Alex</td>
                                </tr>
                                <tr>
                                    <td><strong>City</strong></td>
                                    <td>Categórica</td>
                                    <td>Ciudad de la sucursal</td>
                                    <td>Yangon</td>
                                </tr>
                                <tr>
                                    <td><strong>Customer type</strong></td>
                                    <td>Categórica</td>
                                    <td>Tipo de cliente (Member/Normal)</td>
                                    <td>Member</td>
                                </tr>
                                <tr>
                                    <td><strong>Gender</strong></td>
                                    <td>Categórica</td>
                                    <td>Género del cliente</td>
                                    <td>Female</td>
                                </tr>
                                <tr>
                                    <td><strong>Product line</strong></td>
                                    <td>Categórica</td>
                                    <td>Categoría del producto (6 tipos)</td>
                                    <td>Health and beauty</td>
                                </tr>
                                <tr>
                                    <td><strong>Unit price</strong></td>
                                    <td>Numérica</td>
                                    <td>Precio por unidad ($)</td>
                                    <td>74.69</td>
                                </tr>
                                <tr>
                                    <td><strong>Quantity</strong></td>
                                    <td>Numérica</td>
                                    <td>Cantidad comprada (1-10)</td>
                                    <td>7</td>
                                </tr>
                                <tr>
                                    <td><strong>Sales</strong></td>
                                    <td>Numérica</td>
                                    <td>Venta total con impuesto ($)</td>
                                    <td>548.97</td>
                                </tr>
                                <tr>
                                    <td><strong>Date</strong></td>
                                    <td>Temporal</td>
                                    <td>Fecha de la transacción</td>
                                    <td>1/5/2019</td>
                                </tr>
                                <tr>
                                    <td><strong>Time</strong></td>
                                    <td>Temporal</td>
                                    <td>Hora de la transacción</td>
                                    <td>1:08 PM</td>
                                </tr>
                                <tr>
                                    <td><strong>Payment</strong></td>
                                    <td>Categórica</td>
                                    <td>Método de pago (3 tipos)</td>
                                    <td>Ewallet</td>
                                </tr>
                                <tr>
                                    <td><strong>Rating</strong></td>
                                    <td>Numérica</td>
                                    <td>Calificación del cliente (1-10)</td>
                                    <td>9.1</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <div class="alert">
                        <strong>⚠️ Nota:</strong> Algunas variables como Tax 5%, cogs, gross income y gross margin %
                        son derivadas matemáticamente de otras variables, por lo que en análisis posteriores
                        podríamos considerar eliminarlas para evitar redundancia.
                    </div>
                </div>
            </div>

            <!-- TAB: FASE 1 -->
            <div id="fase1" class="tab-content">
                <div class="phase-header">
                    <div class="phase-number">01</div>
                    <div class="phase-title">Comprensión del Negocio</div>
                    <div class="phase-desc">Business Understanding</div>
                </div>

                <div class="card">
                    <h2 class="card-title">🎯 ¿Por qué es la Fase Más Crítica?</h2>
                    <p style="font-size: 1.1em; margin-bottom: 20px;">
                        La Fase 1 es el fundamento de todo el proyecto. Sin una comprensión clara del negocio,
                        incluso el modelo más sofisticado técnicamente puede ser un fracaso comercial.
                    </p>

                    <div class="highlight-box">
                        <h3 style="margin-bottom: 15px;">🏗️ Analogía: Construir una Casa</h3>
                        <p style="font-size: 1.1em;">
                            Puedes ser el mejor arquitecto del mundo, pero si no entiendes qué necesita el cliente
                            (¿una casa familiar? ¿un edificio de oficinas? ¿un hotel?), tu diseño perfecto será inútil.
                        </p>
                    </div>
                </div>

                <div class="card">
                    <h2 class="card-title">📝 Tarea 1.1: Objetivos Comerciales</h2>

                    <div class="objective-box">
                        <h3>🏢 Contexto Organizacional</h3>
                        <ul style="list-style-position: inside; color: #555;">
                            <li><strong>Organización:</strong> Cadena de 3 supermercados en Myanmar</li>
                            <li><strong>Ubicaciones:</strong> Yangon, Naypyitaw, Mandalay</li>
                            <li><strong>Stakeholders:</strong> Director General, Gerentes de Marketing y Operaciones, Jefe de TI</li>
                            <li><strong>Unidades afectadas:</strong> Marketing, Ventas, Operaciones, Inventario</li>
                        </ul>
                    </div>

                    <div class="objective-box" style="border-left-color: #e74c3c;">
                        <h3 style="color: #e74c3c;">🎯 Objetivo Principal</h3>
                        <p style="font-size: 1.2em; font-weight: 600;">
                            "Aumentar la rentabilidad del supermercado en un 15% en los próximos 6 meses
                            mediante el uso inteligente de datos de ventas"
                        </p>
                    </div>

                    <h3 style="margin-top: 30px; margin-bottom: 15px;">Objetivos Específicos:</h3>
                    <ul class="checklist">
                        <li><strong>Segmentación de Clientes:</strong> Identificar grupos con comportamientos similares para personalizar estrategias</li>
                        <li><strong>Optimización de Productos:</strong> Identificar líneas más rentables y las que necesitan impulso</li>
                        <li><strong>Análisis de Satisfacción:</strong> Identificar factores que influyen en el Rating para mejorar experiencia</li>
                        <li><strong>Optimización por Sucursal:</strong> Comparar desempeño y replicar mejores prácticas</li>
                    </ul>
                </div>

                <div class="card">
                    <h2 class="card-title">⚖️ Tarea 1.2: Evaluación de la Situación</h2>

                    <h3 style="margin-bottom: 15px;">✅ Recursos Disponibles</h3>
                    <div class="table-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>Recurso</th>
                                    <th>Estado</th>
                                    <th>Notas</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Datos históricos</td>
                                    <td>✅ Disponible</td>
                                    <td>3 meses, 1,000 transacciones</td>
                                </tr>
                                <tr>
                                    <td>Sistema POS</td>
                                    <td>✅ Disponible</td>
                                    <td>Datos estructurados en CSV</td>
                                </tr>
                                <tr>
                                    <td>Herramientas</td>
                                    <td>✅ Disponible</td>
                                    <td>Python, pandas, plotly (open source)</td>
                                </tr>
                                <tr>
                                    <td>Datos de inventario</td>
                                    <td>❌ No disponible</td>
                                    <td>Limita análisis de stock</td>
                                </tr>
                                <tr>
                                    <td>Datos web/redes sociales</td>
                                    <td>❌ No disponible</td>
                                    <td>Sin datos de comportamiento online</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <h3 style="margin: 30px 0 15px 0;">⚠️ Riesgos Identificados</h3>
                    <div class="alert">
                        <strong>🔴 Riesgo Alto:</strong> Solo 3 meses de datos puede no ser representativo de patrones anuales
                        <br><strong>Plan:</strong> Comunicar limitaciones claramente, validar con datos futuros
                    </div>
                    <div class="alert success">
                        <strong>🟡 Riesgo Medio:</strong> Resistencia al cambio de gerentes
                        <br><strong>Plan:</strong> Workshops de sensibilización, involucrar desde el inicio
                    </div>
                </div>

                <div class="card">
                    <h2 class="card-title">🔧 Tarea 1.3: Objetivos de Minería de Datos</h2>
                    <p>Traducción de objetivos de negocio a problemas técnicos:</p>

                    <div class="table-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>Objetivo de Negocio</th>
                                    <th>Tipo de Problema</th>
                                    <th>Métrica de Éxito</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Segmentar clientes</td>
                                    <td><span style="background: #3498db; color: white; padding: 5px 10px; border-radius: 5px;">Clustering</span></td>
                                    <td>Silhouette > 0.5</td>
                                </tr>
                                <tr>
                                    <td>Predecir conversión a Member</td>
                                    <td><span style="background: #2ecc71; color: white; padding: 5px 10px; border-radius: 5px;">Clasificación</span></td>
                                    <td>Accuracy > 75%</td>
                                </tr>
                                <tr>
                                    <td>Identificar factores de satisfacción</td>
                                    <td><span style="background: #e67e22; color: white; padding: 5px 10px; border-radius: 5px;">Regresión</span></td>
                                    <td>R² > 0.6</td>
                                </tr>
                                <tr>
                                    <td>Optimizar mix de productos</td>
                                    <td><span style="background: #9b59b6; color: white; padding: 5px 10px; border-radius: 5px;">Descriptivo</span></td>
                                    <td>Reportes accionables</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- TAB: FASE 2 -->
            <div id="fase2" class="tab-content">
                <div class="phase-header">
                    <div class="phase-number">02</div>
                    <div class="phase-title">Comprensión de los Datos</div>
                    <div class="phase-desc">Data Understanding</div>
                </div>

                <div class="card">
                    <h2 class="card-title">📊 ¿Por qué es Crítica?</h2>
                    <p style="font-size: 1.1em; margin-bottom: 20px;">
                        La Fase 2 es donde "conocemos" los datos. Es como una primera cita: necesitamos conocer
                        sus características, virtudes y defectos antes de comprometernos.
                    </p>

                    <div class="highlight-box">
                        <h3 style="margin-bottom: 15px;">🔍 Analogía: El Detective</h3>
                        <p style="font-size: 1.1em;">
                            Los datos son la "escena del crimen". El científico de datos es el detective.
                            Cada gráfico es una "pista". El EDA (Análisis Exploratorio) es la investigación preliminar.
                        </p>
                    </div>

                    <div class="alert info">
                        <strong>📈 Estadística clave:</strong> El 60-75% de los problemas en proyectos de minería
                        de datos vienen de no entender bien los datos en esta fase.
                    </div>
                </div>

                <div class="card">
                    <h2 class="card-title">📥 Tarea 2.1: Recopilación de Datos</h2>

                    <ul class="checklist">
                        <li><strong>Fuente:</strong> Sistema POS del supermercado</li>
                        <li><strong>Formato:</strong> CSV (comma-separated values)</li>
                        <li><strong>Codificación:</strong> UTF-8</li>
                        <li><strong>Tamaño:</strong> 1,000 registros × 17 columnas</li>
                        <li><strong>Período:</strong> Enero a Marzo 2019 (88 días)</li>
                        <li><strong>Estado:</strong> Datos anonimizados (sin información personal)</li>
                    </ul>

                    <div class="alert">
                        <strong>⚠️ Problemas Detectados:</strong>
                        <ul style="margin-top: 10px;">
                            <li>Caracteres BOM en primera línea (solucionable con encoding)</li>
                            <li>Espacios en nombres de columnas (normalizar en Fase 3)</li>
                            <li>Fechas en formato M/D/YYYY (convertir a estándar)</li>
                        </ul>
                    </div>
                </div>

                <div class="card">
                    <h2 class="card-title">📋 Tarea 2.2: Descripción de los Datos</h2>

                    <h3 style="margin-bottom: 15px;">Clasificación de Variables</h3>
                    <div class="stats-grid">
                        <div class="stat-card" style="background: linear-gradient(135deg, #3498db, #2980b9);">
                            <div class="stat-icon">🔢</div>
                            <div class="stat-value">6</div>
                            <div class="stat-label">Variables Numéricas Continuas</div>
                        </div>
                        <div class="stat-card" style="background: linear-gradient(135deg, #2ecc71, #27ae60);">
                            <div class="stat-icon">📊</div>
                            <div class="stat-value">2</div>
                            <div class="stat-label">Variables Numéricas Discretas</div>
                        </div>
                        <div class="stat-card" style="background: linear-gradient(135deg, #e67e22, #d35400);">
                            <div class="stat-icon">🏷️</div>
                            <div class="stat-value">6</div>
                            <div class="stat-label">Variables Categóricas</div>
                        </div>
                        <div class="stat-card" style="background: linear-gradient(135deg, #9b59b6, #8e44ad);">
                            <div class="stat-icon">⏰</div>
                            <div class="stat-value">2</div>
                            <div class="stat-label">Variables Temporales</div>
                        </div>
                    </div>

                    <div class="highlight-box">
                        <h3 style="margin-bottom: 15px;">🎯 Variables Clave para Análisis</h3>
                        <ul style="font-size: 1.1em;">
                            <li><strong>Customer type:</strong> Fundamental para segmentación Member vs Normal</li>
                            <li><strong>Rating:</strong> Variable objetivo para análisis de satisfacción</li>
                            <li><strong>Product line:</strong> Esencial para optimización de productos</li>
                            <li><strong>Sales:</strong> Métrica principal de negocio</li>
                            <li><strong>Branch/City:</strong> Para comparaciones geográficas</li>
                            <li><strong>Date/Time:</strong> Para análisis de patrones temporales</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- TAB: EXPLORACIÓN -->
            <div id="exploracion" class="tab-content">
                <div class="card">
                    <h2 class="card-title">🔍 Análisis Exploratorio de Datos (EDA)</h2>
                    <p style="font-size: 1.1em; margin-bottom: 20px;">
                        El EDA es el corazón de la Fase 2. Aquí exploramos visualmente los datos para
                        descubrir patrones, anomalías y formular hipótesis preliminares.
                    </p>
                </div>

                <div class="card">
                    <h2 class="card-title">📈 Distribución de Ventas</h2>
                    <p>Análisis de cómo se distribuyen las ventas por transacción:</p>
                    <div class="viz-container">
                        {visualizaciones['ventas_distribucion']}
                    </div>
                    <div class="alert info">
                        <strong>💡 Observación:</strong> Analiza si la distribución es normal, sesgada, o tiene múltiples picos.
                        Esto puede revelar diferentes segmentos de clientes o tipos de compra.
                    </div>
                </div>

                <div class="card">
                    <h2 class="card-title">🏢 Análisis por Sucursal</h2>
                    <p>Comparación del desempeño entre las tres sucursales:</p>
                    <div class="viz-container">
                        {visualizaciones['ventas_sucursal']}
                    </div>
                    <div class="highlight-box">
                        <h3>🎯 Preguntas a Responder:</h3>
                        <ul>
                            <li>¿Hay una sucursal claramente superior?</li>
                            <li>¿El ticket promedio varía entre sucursales?</li>
                            <li>¿Qué mejores prácticas se pueden replicar?</li>
                        </ul>
                    </div>
                </div>

                <div class="card">
                    <h2 class="card-title">🛍️ Análisis de Productos</h2>
                    <p>Desempeño de cada línea de productos (coloreado por rating):</p>
                    <div class="viz-container">
                        {visualizaciones['ventas_producto']}
                    </div>
                    <div class="alert success">
                        <strong>✅ Insight:</strong> Las categorías con mayores ventas no necesariamente tienen
                        el mejor rating. Esto puede indicar oportunidades de mejora en productos de alto volumen.
                    </div>
                </div>

                <div class="card">
                    <h2 class="card-title">👥 Análisis de Tipos de Cliente</h2>
                    <p>Comparación entre clientes Members y Normal:</p>
                    <div class="viz-container">
                        {visualizaciones['clientes_tipo']}
                    </div>
                    <div class="highlight-box">
                        <h3>🔑 Hipótesis a Validar:</h3>
                        <ul>
                            <li><strong>H1:</strong> Los Members tienen mayor ticket promedio que los Normal</li>
                            <li><strong>H2:</strong> Los Members dan mejores calificaciones (mayor lealtad)</li>
                            <li><strong>H3:</strong> Convertir Normal a Member aumenta el valor de vida del cliente</li>
                        </ul>
                    </div>
                </div>

                <div class="card">
                    <h2 class="card-title">💳 Métodos de Pago</h2>
                    <p>Distribución de las preferencias de pago:</p>
                    <div class="viz-container">
                        {visualizaciones['metodos_pago']}
                    </div>
                </div>

                <div class="card">
                    <h2 class="card-title">📅 Evolución Temporal de Ventas</h2>
                    <p>Tendencia de ventas diarias durante el período de análisis:</p>
                    <div class="viz-container">
                        {visualizaciones['ventas_tiempo']}
                    </div>
                    <div class="alert">
                        <strong>⚠️ Consideración:</strong> Busca patrones semanales, días especiales o tendencias
                        crecientes/decrecientes. Solo 3 meses puede no capturar estacionalidad anual.
                    </div>
                </div>

                <div class="card">
                    <h2 class="card-title">⏰ Ventas por Hora del Día</h2>
                    <p>Identificación de horas pico y valles en el tráfico de clientes:</p>
                    <div class="viz-container">
                        {visualizaciones['ventas_hora']}
                    </div>
                    <div class="highlight-box">
                        <h3>🎯 Aplicaciones de Negocio:</h3>
                        <ul>
                            <li>Optimizar horarios de personal</li>
                            <li>Planificar promociones en horas de menor tráfico</li>
                            <li>Identificar oportunidades de cross-selling en horas pico</li>
                        </ul>
                    </div>
                </div>

                <div class="card">
                    <h2 class="card-title">⭐ Distribución de Calificaciones</h2>
                    <p>Análisis de la satisfacción del cliente:</p>
                    <div class="viz-container">
                        {visualizaciones['rating_dist']}
                    </div>
                </div>

                <div class="card">
                    <h2 class="card-title">🔥 Mapa de Calor: Productos × Sucursales</h2>
                    <p>Ventas por categoría en cada sucursal:</p>
                    <div class="viz-container">
                        {visualizaciones['heatmap_producto_branch']}
                    </div>
                    <div class="alert info">
                        <strong>💡 Análisis:</strong> Identifica qué productos funcionan mejor en cada ubicación.
                        Esto puede revelar diferencias demográficas o culturales entre ciudades.
                    </div>
                </div>

                <div class="card">
                    <h2 class="card-title">🔍 Relación: Precio vs Cantidad vs Rating</h2>
                    <p>Análisis multivariado (tamaño = Ventas, color = Rating):</p>
                    <div class="viz-container">
                        {visualizaciones['scatter_precio_cantidad']}
                    </div>
                    <div class="highlight-box">
                        <h3>🤔 Preguntas Analíticas:</h3>
                        <ul>
                            <li>¿Los productos caros se compran en menor cantidad?</li>
                            <li>¿Precio afecta el rating?</li>
                            <li>¿Hay outliers (transacciones atípicas)?</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- TAB: CALIDAD -->
            <div id="calidad" class="tab-content">
                <div class="card">
                    <h2 class="card-title">✅ Tarea 2.4: Verificación de Calidad</h2>
                    <p style="font-size: 1.1em; margin-bottom: 20px;">
                        La calidad de los datos es crítica. Un análisis con datos de mala calidad
                        produce resultados incorrectos ("Garbage In, Garbage Out").
                    </p>
                </div>

                <div class="card">
                    <h2 class="card-title">📋 Checklist de Calidad</h2>

                    <h3 style="margin-bottom: 15px;">1️⃣ Completitud</h3>
                    <ul class="checklist">
                        <li>Verificar valores faltantes (missing values) en cada columna</li>
                        <li>Confirmar que el período de tiempo está completo (88/90 días)</li>
                        <li>Validar que todas las sucursales están representadas</li>
                        <li>Asegurar que todas las categorías de producto están presentes</li>
                    </ul>

                    <h3 style="margin: 30px 0 15px 0;">2️⃣ Consistencia</h3>
                    <ul class="checklist">
                        <li>Verificar relación: Sales = cogs + Tax 5%</li>
                        <li>Verificar: cogs = Unit price × Quantity</li>
                        <li>Verificar: Tax 5% = cogs × 0.05</li>
                        <li>Confirmar: gross margin % = 4.76% (constante)</li>
                        <li>Validar que Branch y City coinciden correctamente</li>
                    </ul>

                    <h3 style="margin: 30px 0 15px 0;">3️⃣ Validez (Rango de Valores)</h3>
                    <ul class="checklist">
                        <li>Rating debe estar entre 1 y 10</li>
                        <li>Quantity debe ser mayor que 0</li>
                        <li>Unit price debe ser positivo</li>
                        <li>Sales debe ser positivo</li>
                        <li>Fechas deben estar dentro del rango esperado</li>
                    </ul>

                    <h3 style="margin: 30px 0 15px 0;">4️⃣ Unicidad</h3>
                    <ul class="checklist">
                        <li>Invoice ID debe ser único (sin duplicados)</li>
                        <li>No debe haber transacciones completamente duplicadas</li>
                    </ul>
                </div>

                <div class="card">
                    <h2 class="card-title">🚨 Problemas Detectados</h2>

                    <div class="alert success">
                        <strong>✅ Buenas Noticias:</strong>
                        <ul style="margin-top: 10px;">
                            <li>No se detectaron valores faltantes en el dataset</li>
                            <li>Las relaciones matemáticas entre variables son consistentes</li>
                            <li>Todos los valores están dentro de rangos válidos</li>
                            <li>No hay duplicados evidentes</li>
                        </ul>
                    </div>

                    <div class="alert">
                        <strong>⚠️ Consideraciones:</strong>
                        <ul style="margin-top: 10px;">
                            <li>Solo 3 meses de datos (limitación temporal)</li>
                            <li>Variables derivadas redundantes (eliminar en Fase 3)</li>
                            <li>Gross margin % constante (no aporta variabilidad)</li>
                            <li>Formato de fecha no estándar (requerir conversión)</li>
                        </ul>
                    </div>
                </div>

                <div class="card">
                    <h2 class="card-title">🎯 Recomendaciones para Fase 3</h2>

                    <h3 style="margin-bottom: 15px;">Acciones de Preparación de Datos:</h3>
                    <ol style="list-style-position: inside; font-size: 1.1em; line-height: 2;">
                        <li><strong>Eliminar variables redundantes:</strong> Tax 5%, cogs, gross income, gross margin %</li>
                        <li><strong>Convertir formatos:</strong> Date a datetime, Time a hora numérica</li>
                        <li><strong>Crear variables derivadas útiles:</strong>
                            <ul style="margin-left: 30px; margin-top: 10px;">
                                <li>Día de la semana (DayOfWeek)</li>
                                <li>Mes (Month)</li>
                                <li>Hora del día (Hour)</li>
                                <li>Periodo del día (Mañana/Tarde/Noche)</li>
                            </ul>
                        </li>
                        <li><strong>Normalizar nombres:</strong> Eliminar espacios y caracteres especiales</li>
                        <li><strong>Encoding de categóricas:</strong> Preparar para modelado (One-Hot, Label Encoding)</li>
                        <li><strong>Detección de outliers:</strong> Identificar y decidir cómo tratarlos</li>
                    </ol>
                </div>
            </div>

            <!-- TAB: INSIGHTS -->
            <div id="insights" class="tab-content">
                <div class="card">
                    <h2 class="card-title">💡 Insights Principales</h2>
                    <p style="font-size: 1.1em; margin-bottom: 30px;">
                        Basándonos en el análisis exploratorio, estos son los hallazgos clave:
                    </p>

                    <div class="insight-grid">
    """

    # Agregar insights dinámicos
    for insight in insights:
        html_content += f"""
                        <div class="insight-card">
                            <div class="insight-icon">{insight['icon']}</div>
                            <div style="font-size: 0.9em; color: #7f8c8d; font-weight: 600;">{insight['titulo']}</div>
                            <div class="insight-value">{insight['valor']}</div>
                            <div class="insight-detail">{insight['detalle']}</div>
                        </div>
    """

    html_content += """
                    </div>
                </div>

                <div class="card">
                    <h2 class="card-title">🔬 Hipótesis Preliminares</h2>
                    <p style="margin-bottom: 20px;">
                        Estas hipótesis deben ser validadas estadísticamente en fases posteriores:
                    </p>

                    <div class="objective-box">
                        <h3>📊 Hipótesis de Segmentación</h3>
                        <ul style="list-style-position: inside;">
                            <li>Los clientes Members tienen comportamiento diferente a Normal</li>
                            <li>Se pueden identificar 3-4 segmentos por patrones de compra</li>
                            <li>Existen clientes "high value" (alto ticket + alta frecuencia)</li>
                        </ul>
                    </div>

                    <div class="objective-box" style="border-left-color: #e67e22;">
                        <h3 style="color: #e67e22;">🛍️ Hipótesis de Producto</h3>
                        <ul style="list-style-position: inside;">
                            <li>Algunas líneas de producto son más rentables que otras</li>
                            <li>Ciertas categorías tienen mejor rating promedio</li>
                            <li>El mix de productos varía significativamente por sucursal</li>
                        </ul>
                    </div>

                    <div class="objective-box" style="border-left-color: #9b59b6;">
                        <h3 style="color: #9b59b6;">⏰ Hipótesis Temporal</h3>
                        <ul style="list-style-position: inside;">
                            <li>Existen horas pico predecibles durante el día</li>
                            <li>Los fines de semana tienen patrones diferentes</li>
                            <li>Ciertos productos se venden más en horarios específicos</li>
                        </ul>
                    </div>

                    <div class="objective-box" style="border-left-color: #2ecc71;">
                        <h3 style="color: #2ecc71;">🏢 Hipótesis de Sucursal</h3>
                        <ul style="list-style-position: inside;">
                            <li>Cada sucursal tiene características demográficas únicas</li>
                            <li>Hay diferencias en satisfacción del cliente por ubicación</li>
                            <li>Las mejores prácticas de una sucursal son replicables</li>
                        </ul>
                    </div>
                </div>

                <div class="card">
                    <h2 class="card-title">🎯 Próximos Pasos</h2>

                    <h3 style="margin-bottom: 15px;">Fase 3: Preparación de Datos</h3>
                    <ul class="checklist">
                        <li>Limpieza y transformación de variables</li>
                        <li>Ingeniería de características (feature engineering)</li>
                        <li>Selección de atributos relevantes</li>
                        <li>Tratamiento de outliers y valores atípicos</li>
                    </ul>

                    <h3 style="margin: 30px 0 15px 0;">Fase 4: Modelado</h3>
                    <ul class="checklist">
                        <li>Clustering para segmentación de clientes</li>
                        <li>Modelos predictivos (si aplicable)</li>
                        <li>Análisis de reglas de asociación</li>
                        <li>Validación y ajuste de modelos</li>
                    </ul>

                    <div class="highlight-box" style="margin-top: 30px;">
                        <h3 style="margin-bottom: 15px;">✅ Validación de Fase 2</h3>
                        <p style="font-size: 1.1em;">
                            Antes de avanzar a la Fase 3, verifica que has completado:
                        </p>
                        <ul style="margin-top: 15px; font-size: 1.05em;">
                            <li>✓ Entendimiento completo de cada variable</li>
                            <li>✓ Al menos 10-15 visualizaciones exploratorias</li>
                            <li>✓ Hipótesis preliminares formuladas</li>
                            <li>✓ Problemas de calidad identificados y documentados</li>
                            <li>✓ Confirmación de que los datos soportan los objetivos de Fase 1</li>
                        </ul>
                    </div>
                </div>

                <div class="card">
                    <h2 class="card-title">🎓 Actividades de Aprendizaje</h2>

                    <h3 style="margin-bottom: 15px;">Para Estudiantes:</h3>

                    <div class="objective-box">
                        <h3>🤔 Preguntas de Reflexión</h3>
                        <ol style="list-style-position: inside; line-height: 2;">
                            <li>¿Qué pasaría si ignoramos outliers sin investigar su origen?</li>
                            <li>¿Por qué es importante formular hipótesis antes de validarlas?</li>
                            <li>¿Cómo afecta tener solo 3 meses de datos a nuestras conclusiones?</li>
                            <li>¿Qué variables adicionales serían útiles tener?</li>
                            <li>¿Cómo convencerías a un gerente escéptico del valor de este análisis?</li>
                        </ol>
                    </div>

                    <div class="objective-box" style="border-left-color: #e67e22;">
                        <h3 style="color: #e67e22;">✍️ Ejercicios Prácticos</h3>
                        <ol style="list-style-position: inside; line-height: 2;">
                            <li>Identifica 3 análisis adicionales que realizarías con estos datos</li>
                            <li>Propón 2 nuevas variables derivadas que podrían ser útiles</li>
                            <li>Diseña una visualización que no está en esta guía</li>
                            <li>Escribe un objetivo de negocio alternativo para este dataset</li>
                            <li>Identifica posibles sesgos en los datos recolectados</li>
                        </ol>
                    </div>
                </div>
            </div>

            <footer>
                <h2 style="margin-bottom: 20px;">🎓 Conclusión</h2>
                <p style="font-size: 1.2em; max-width: 800px; margin: 0 auto 20px; color: #555;">
                    Las Fases 1 y 2 de CRISP-DM son los cimientos de cualquier proyecto exitoso de minería de datos.
                    El tiempo invertido aquí NO es tiempo perdido, es una inversión que previene retrabajo costoso
                    y aumenta significativamente las probabilidades de éxito del proyecto.
                </p>

                <div class="highlight-box" style="max-width: 800px; margin: 30px auto;">
                    <p style="font-size: 1.3em; font-weight: 600; text-align: center; color: #2c3e50;">
                        "Un modelo perfecto que responde la pregunta equivocada es inútil.<br>
                        Un modelo imperfecto que resuelve el problema correcto es valioso."
                    </p>
                </div>

                <p style="margin-top: 30px; color: #95a5a6;">
                    © 2025 Universidad Externado de Colombia | Minería de Datos<br>
                    Guía generada con Python, pandas y Plotly
                </p>
            </footer>
        </div>

        <script>
            function showTab(tabName) {
                // Ocultar todos los tabs
                const contents = document.querySelectorAll('.tab-content');
                contents.forEach(content => {
                    content.classList.remove('active');
                });

                // Desactivar todos los botones
                const buttons = document.querySelectorAll('.tab-btn');
                buttons.forEach(button => {
                    button.classList.remove('active');
                });

                // Activar tab seleccionado
                document.getElementById(tabName).classList.add('active');
                event.target.classList.add('active');

                // Scroll suave al top
                window.scrollTo({top: 0, behavior: 'smooth'});
            }

            // Animación de entrada para las tarjetas
            document.addEventListener('DOMContentLoaded', function() {
                const observer = new IntersectionObserver((entries) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            entry.target.style.opacity = '1';
                            entry.target.style.transform = 'translateY(0)';
                        }
                    });
                }, {
                    threshold: 0.1
                });

                document.querySelectorAll('.card').forEach(card => {
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(20px)';
                    card.style.transition = 'all 0.6s ease-out';
                    observer.observe(card);
                });
            });
        </script>
    </body>
    </html>
    """

    # Guardar HTML
    output_path = Path(output).expanduser()
    output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open('w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"\n✅ HTML interactivo generado exitosamente: {output_path}")
    print(f"📂 Abre el archivo en tu navegador para ver la guía interactiva")
    print(f"🎓 ¡Listo para usar en clase!")
    return output_path


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Generar la guía interactiva de CRISP-DM (Fases 1 y 2).')
    parser.add_argument('-d', '--dataset', default='recursos_compartidos/datasets/mineria-de-datos/supermarket_analysis.csv', help='Ruta al dataset CSV.')
    parser.add_argument('-o', '--output', default='guia_interactiva_crisp_dm.html', help='Ruta del HTML de salida.')
    parser.add_argument('--encoding', default='utf-8-sig', help='Codificación del CSV.')
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    generar_guia_crispdm(dataset=args.dataset, output=args.output, encoding=args.encoding)


if __name__ == '__main__':
    main()
