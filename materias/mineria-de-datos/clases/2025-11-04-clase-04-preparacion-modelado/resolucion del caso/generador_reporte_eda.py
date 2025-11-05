
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO
import numpy as np
from tabulate import tabulate

def df_to_html_table(df, table_id="table"):
    """Convierte un DataFrame de pandas a una tabla HTML con un ID específico."""
    return df.to_html(classes="table table-striped table-hover", table_id=table_id, border=0)

def fig_to_base64(fig):
    """Convierte una figura de Matplotlib a una cadena base64."""
    buf = BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    return base64.b64encode(buf.getvalue()).decode('utf-8')

def create_eda_report(df):
    """Genera un reporte EDA en formato HTML con tema navideño."""
    
    # --- Inicio del HTML ---
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Reporte EDA Navideño - Attrition</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Mountains+of+Christmas:wght@400;700&family=Roboto:wght@300;400;700&display=swap');

            body {
                font-family: 'Roboto', sans-serif;
                background-color: #f4f4f4;
                color: #333;
                margin: 0;
                padding: 20px;
                background: linear-gradient(135deg, #c8102e, #1d8c44);
                overflow-x: hidden;
            }

            h1, h2, h3 {
                font-family: 'Mountains of Christmas', cursive;
                color: #fff;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
            }

            h1 { font-size: 4em; text-align: center; }
            h2 { font-size: 3em; border-bottom: 2px solid #fff; padding-bottom: 10px; margin-top: 40px; }
            h3 { font-size: 2em; color: #ffc72c; }

            .container {
                max-width: 1200px;
                margin: auto;
                background: rgba(255, 255, 255, 0.9);
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            }
            
            .card {
                background: #fff;
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 20px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                animation: fadeIn 1s ease-in-out;
            }

            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }

            .plot-container {
                text-align: center;
                margin-top: 20px;
            }

            img {
                max-width: 100%;
                height: auto;
                border-radius: 8px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            }
            
table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                padding: 12px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }
            th {
                background-color: #c8102e;
                color: white;
            }
            tr:hover {
                background-color: #f5f5f5;
            }

            /* Animaciones Navideñas */
            .snowflake {
                color: #fff;
                font-size: 1em;
                font-family: Arial;
                text-shadow: 0 0 5px #000;
                position: fixed;
                top: -10%;
                z-index: 9999;
                -webkit-user-select: none;
                -moz-user-select: none;
                -ms-user-select: none;
                user-select: none;
                cursor: default;
                -webkit-animation-name: snowflakes-fall, snowflakes-shake;
                -webkit-animation-duration: 10s, 3s;
                -webkit-animation-timing-function: linear, ease-in-out;
                -webkit-animation-iteration-count: infinite, infinite;
                -webkit-animation-play-state: running, running;
                animation-name: snowflakes-fall, snowflakes-shake;
                animation-duration: 10s, 3s;
                animation-timing-function: linear, ease-in-out;
                animation-iteration-count: infinite, infinite;
                animation-play-state: running, running;
            }
            .snowflake:nth-of-type(0) { left: 1%; -webkit-animation-delay: 0s, 0s; animation-delay: 0s, 0s }
            .snowflake:nth-of-type(1) { left: 10%; -webkit-animation-delay: 1s, 1s; animation-delay: 1s, 1s }
            .snowflake:nth-of-type(2) { left: 20%; -webkit-animation-delay: 6s, .5s; animation-delay: 6s, .5s }
            .snowflake:nth-of-type(3) { left: 30%; -webkit-animation-delay: 4s, 2s; animation-delay: 4s, 2s }
            .snowflake:nth-of-type(4) { left: 40%; -webkit-animation-delay: 2s, 2s; animation-delay: 2s, 2s }
            .snowflake:nth-of-type(5) { left: 50%; -webkit-animation-delay: 8s, 3s; animation-delay: 8s, 3s }
            .snowflake:nth-of-type(6) { left: 60%; -webkit-animation-delay: 6s, 2s; animation-delay: 6s, 2s }
            .snowflake:nth-of-type(7) { left: 70%; -webkit-animation-delay: 2.5s, 1s; animation-delay: 2.5s, 1s }
            .snowflake:nth-of-type(8) { left: 80%; -webkit-animation-delay: 1s, 0s; animation-delay: 1s, 0s }
            .snowflake:nth-of-type(9) { left: 90%; -webkit-animation-delay: 3s, 1.5s; animation-delay: 3s, 1.5s }

            @keyframes snowflakes-fall {
                0% { top: -10% }
                100% { top: 100% }
            }
            @keyframes snowflakes-shake {
                0%, 100% { transform: translateX(0) }
                50% { transform: translateX(80px) }
            }
        </style>
    </head>
    <body>
        <div class="snowflakes" aria-hidden="true">
            <div class="snowflake">❅</div> <div class="snowflake">❆</div>
            <div class="snowflake">❅</div> <div class="snowflake">❆</div>
            <div class="snowflake">❅</div> <div class="snowflake">❆</div>
            <div class="snowflake">❅</div> <div class="snowflake">❆</div>
            <div class="snowflake">❅</div> <div class="snowflake">❆</div>
        </div>

        <h1>🎄 Reporte Navideño de Rotación de Empleados 🎄</h1>
        <div class="container">
    """

    # --- 1. Vista General del Dataset ---
    html += "<h2>1. Vista General del Dataset</h2>"
    html += "<div class='card'>"
    html += "<h3>Primeras 5 filas:</h3>"
    html += df_to_html_table(df.head())
    html += "<h3>Información del Dataset:</h3>"
    info_df = pd.DataFrame({
        'Column': df.columns,
        'Non-Null Count': df.count().values,
        'Dtype': df.dtypes.values
    })
    html += tabulate(info_df, headers='keys', tablefmt='html', showindex=False)
    html += "<h3>Estadísticas Descriptivas:</h3>"
    html += df_to_html_table(df.describe())
    html += "</div>"

    # --- 2. Análisis de la Variable Objetivo: Attrition ---
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x='Attrition', data=df, palette=['#1d8c44', '#c8102e'], ax=ax)
    ax.set_title('Distribución de Attrition', fontsize=16)
    ax.set_xlabel('Attrition', fontsize=12)
    ax.set_ylabel('Cantidad', fontsize=12)
    attrition_plot = fig_to_base64(fig)
    plt.close(fig)

    html += "<h2>2. Análisis de la Variable Objetivo: Attrition</h2>"
    html += "<div class='card'>"
    html += "<h3>Distribución de la Rotación</h3>"
    html += f"<div class='plot-container'><img src='data:image/png;base64,{attrition_plot}' alt='Attrition Plot'></div>"
    html += "<p>Observamos un desbalance en las clases, con una mayor cantidad de empleados que no han rotado.</p>"
    html += "</div>"

    # --- 3. Visualizaciones Clave ---
    html += "<h2>3. Visualizaciones Clave</h2>"

    # Attrition vs OverTime
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x='OverTime', hue='Attrition', data=df, palette=['#1d8c44', '#c8102e'])
    ax.set_title('Rotación vs. Horas Extra', fontsize=16)
    plot_overtime = fig_to_base64(fig)
    plt.close(fig)
    html += "<div class='card'><h3>Rotación vs. Horas Extra</h3>"
    html += f"<div class='plot-container'><img src='data:image/png;base64,{plot_overtime}'></div>"
    html += "<p>Los empleados que trabajan horas extra tienen una tasa de rotación notablemente más alta.</p></div>"

    # Attrition vs JobRole
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.countplot(y='JobRole', hue='Attrition', data=df, palette=['#1d8c44', '#c8102e'])
    ax.set_title('Rotación por Rol de Trabajo', fontsize=16)
    plt.tight_layout()
    plot_jobrole = fig_to_base64(fig)
    plt.close(fig)
    html += "<div class='card'><h3>Rotación por Rol de Trabajo</h3>"
    html += f"<div class='plot-container'><img src='data:image/png;base64,{plot_jobrole}'></div>"
    html += "<p>Roles como 'Sales Representative' y 'Laboratory Technician' muestran altas tasas de rotación.</p></div>"

    # Attrition vs MonthlyIncome
    fig, ax = plt.subplots(figsize=(10, 7))
    sns.boxplot(x='Attrition', y='MonthlyIncome', data=df, palette=['#1d8c44', '#c8102e'])
    ax.set_title('Rotación vs. Ingreso Mensual', fontsize=16)
    plot_income = fig_to_base64(fig)
    plt.close(fig)
    html += "<div class='card'><h3>Rotación vs. Ingreso Mensual</h3>"
    html += f"<div class='plot-container'><img src='data:image/png;base64,{plot_income}'></div>"
    html += "<p>Los empleados que rotan tienden a tener ingresos mensuales más bajos.</p></div>"
    
    # --- 4. Correlaciones ---
    numeric_df = df.select_dtypes(include=np.number)
    corr_matrix = numeric_df.corr()
    fig, ax = plt.subplots(figsize=(18, 15))
    sns.heatmap(corr_matrix, cmap='Greens', ax=ax)
    ax.set_title('Matriz de Correlación de Variables Numéricas', fontsize=16)
    corr_plot = fig_to_base64(fig)
    plt.close(fig)
    
    html += "<h2>4. Matriz de Correlación</h2>"
    html += "<div class='card'>"
    html += "<h3>Correlación entre variables numéricas</h3>"
    html += f"<div class='plot-container'><img src='data:image/png;base64,{corr_plot}'></div>"
    html += "<p>La matriz de correlación nos ayuda a identificar relaciones lineales entre las variables. Por ejemplo, 'JobLevel' y 'MonthlyIncome' están fuertemente correlacionados.</p>"
    html += "</div>"


    # --- Fin del HTML ---
    html += """
        </div>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    # Cargar el dataset
    try:
        df = pd.read_csv('/home/jzuluaga/code/education-research/externado/docencia/materias/mineria-de-datos/clases/2025-11-04-clase-04-preparacion-modelado/WA_Fn-UseC_-HR-Employee-Attrition.csv')
        
        # Generar el reporte
        reporte_html = create_eda_report(df)
        
        # Guardar el reporte
        with open("reporte_navideno_eda.html", "w", encoding="utf-8") as f:
            f.write(reporte_html)
            
        print("¡Reporte HTML 'reporte_navideno_eda.html' generado exitosamente!")
        
    except FileNotFoundError:
        print("Error: El archivo 'WA_Fn-UseC_-HR-Employee-Attrition.csv' no se encontró.")
        print("Asegúrate de que el script se ejecute desde la carpeta 'resolucion del caso'.")
