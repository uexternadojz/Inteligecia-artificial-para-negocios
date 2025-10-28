# 🎓 Guía Interactiva CRISP-DM - Fases 1 y 2

## Material de Aprendizaje Interactivo para Minería de Datos

[![Universidad Externado de Colombia](https://img.shields.io/badge/Universidad-Externado_de_Colombia-blue)](https://www.uexternado.edu.co/)
[![CRISP-DM](https://img.shields.io/badge/Metodología-CRISP--DM-green)](https://www.datascience-pm.com/crisp-dm-2/)
[![Python](https://img.shields.io/badge/Python-3.8+-yellow)](https://www.python.org/)
[![License](https://img.shields.io/badge/Licencia-Uso_Académico-orange)](LICENSE)

---

## 🚀 Inicio Rápido

### Para Estudiantes:

```bash
# Opción 1: Doble clic en el archivo HTML
guia_interactiva_crisp_dm.html

# Opción 2: Desde terminal
./abrir_guia.sh
```

### Para Profesores:

Lee primero: [`Reporte_Pedagogico_CRISP-DM_Fases_1_y_2.md`](Reporte_Pedagogico_CRISP-DM_Fases_1_y_2.md)

---

## 📦 ¿Qué es esto?

Este repositorio contiene **material educativo interactivo** para enseñar y aprender las **Fases 1 y 2 de la metodología CRISP-DM** (Cross-Industry Standard Process for Data Mining) utilizando un caso de estudio real: análisis de datos de una cadena de supermercados.

### ✨ Características Principales:

- 🎨 **Guía HTML Interactiva** - Navegación por pestañas con diseño moderno
- 📊 **11+ Visualizaciones Interactivas** - Gráficos con Plotly (zoom, hover, pan)
- 📝 **Contenido Pedagógico Completo** - Explicaciones, ejercicios y actividades
- 🔍 **Análisis de Datos Real** - 1,000 transacciones del mundo del retail
- 💡 **Insights Prácticos** - Hipótesis y hallazgos basados en datos
- 📱 **Responsive Design** - Funciona en móvil, tablet y desktop
- 🌐 **100% Offline** - No requiere conexión a Internet

---

## 📊 Contenido del Dataset

**SuperMarket Analysis**
- 📝 1,000 transacciones
- 🏢 3 sucursales (Yangon, Naypyitaw, Mandalay)
- 🛍️ 6 líneas de productos
- 💰 $322,966.75 en ventas totales
- 📅 Enero - Marzo 2019
- 📊 17 variables (categóricas, numéricas, temporales)

---

## 🗂️ Estructura de Archivos

```
📁 mineriadedatos/
│
├── ⭐ guia_interactiva_crisp_dm.html    # COMENZAR AQUÍ
│
├── 📚 Documentación
│   ├── README.md                        # Este archivo
│   ├── INICIO_RAPIDO.txt               # Guía de inicio rápido
│   ├── README_GUIA.md                  # Instrucciones detalladas
│   ├── INDICE_ARCHIVOS.md             # Índice completo
│   └── RESUMEN_PROYECTO.md            # Resumen ejecutivo
│
├── 📝 Material Pedagógico
│   ├── Reporte_Pedagogico_CRISP-DM_Fases_1_y_2.md
│   └── CRISP-DM_ Fases 1 y 2 para Minería de Datos.md
│
├── 🛠️ Herramientas
│   ├── generar_guia_interactiva.py     # Wrapper del generador global
│   ├── abrir_guia.sh                   # Script de apertura
│   └── (crea tu venv local bajo demanda)
│
└── 📊 Datos
    └── (dataset centralizado) recursos_compartidos/datasets/mineria-de-datos/supermarket_analysis.csv
```

---

## 🎯 Objetivos de Aprendizaje

Al completar esta guía, podrás:

### Fase 1: Comprensión del Negocio
- ✅ Definir objetivos comerciales claros y medibles
- ✅ Traducir objetivos de negocio a objetivos técnicos
- ✅ Identificar recursos, riesgos y restricciones
- ✅ Crear un plan de proyecto estructurado

### Fase 2: Comprensión de los Datos
- ✅ Realizar análisis exploratorio de datos (EDA)
- ✅ Clasificar variables y entender sus características
- ✅ Detectar problemas de calidad de datos
- ✅ Formular hipótesis preliminares
- ✅ Crear visualizaciones efectivas

---

## 💻 Requisitos

### Para Ver la Guía (Estudiantes):
- ✅ Navegador web moderno (Chrome, Firefox, Edge, Safari)
- ✅ JavaScript habilitado
- ❌ NO requiere Internet

### Para Modificar la Guía (Avanzado):
- ✅ Python 3.8+
- ✅ Entorno virtual (incluido en `.venv/` (crear local según necesidad))
- ✅ Pandas, Plotly, NumPy (ya instalados)

---

## 📖 Guías de Uso

### 📘 Para Estudiantes

1. **Abre la guía interactiva:**
   ```bash
   # Doble clic en:
   guia_interactiva_crisp_dm.html
   ```

2. **Navega por las pestañas:**
   - 🏠 Introducción al dataset
   - 📋 Fase 1: Comprensión del Negocio
   - 📊 Fase 2: Comprensión de los Datos
   - 🔍 Exploración (EDA completo)
   - ✅ Calidad de datos
   - 💡 Insights y próximos pasos

3. **Interactúa con los gráficos:**
   - Pasa el mouse para ver detalles
   - Haz zoom con scroll
   - Pan arrastrando
   - Doble clic para resetear

4. **Completa las actividades:**
   - Responde preguntas de reflexión
   - Identifica patrones adicionales
   - Propón nuevas visualizaciones

### 📗 Para Profesores

1. **Preparación:**
   - Lee [`Reporte_Pedagogico_CRISP-DM_Fases_1_y_2.md`](Reporte_Pedagogico_CRISP-DM_Fases_1_y_2.md)
   - Revisa la guía HTML completa
   - Prepara ejemplos adicionales si lo deseas

2. **En Clase:**
   - Proyecta la guía interactiva
   - Usa el plan de clase sugerido (3 sesiones × 2 horas)
   - Propón los ejercicios incluidos
   - Facilita discusiones grupales

3. **Evaluación:**
   - Usa las preguntas de reflexión
   - Asigna ejercicios prácticos
   - Evalúa comprensión con presentaciones

---

## 🔧 Regenerar la Guía (Opcional)

Si deseas modificar o actualizar la guía:

```bash
# 1. Activar entorno virtual (opcional si trabajas con uno)
source .venv/bin/activate

# 2. (Opcional) Personalizar el wrapper local
nano generar_guia_interactiva.py

# 3. Ejecutar el generador compartido (desde la raíz del repo)
python herramientas/scripts/generar_guia_crispdm.py     -d "recursos_compartidos/datasets/mineria-de-datos/supermarket_analysis.csv"     -o "materias/mineria-de-datos/clases/2025-10-23-crisp-dm-fases-1-2/guia_interactiva_crisp_dm.html"

# (Alternativa) Ejecutar el wrapper local estando en la carpeta de la clase
python generar_guia_interactiva.py

# 4. Se creará un nuevo guia_interactiva_crisp_dm.html

# 5. Desactivar entorno
deactivate
```

---

## 📊 Visualizaciones Incluidas

1. **Distribución de Ventas** - Histograma interactivo
2. **Análisis por Sucursal** - Comparación múltiple
3. **Ventas por Producto** - Barras coloreadas por rating
4. **Tipos de Cliente** - Members vs Normal
5. **Métodos de Pago** - Distribución de preferencias
6. **Evolución Temporal** - Serie de tiempo diaria
7. **Ventas por Hora** - Identificación de horas pico
8. **Distribución de Ratings** - Satisfacción del cliente
9. **Heatmap Producto×Sucursal** - Mapa de calor 2D
10. **Scatter Multivariado** - Precio vs Cantidad vs Rating
11. **Tarjetas de KPIs** - Estadísticas principales

---

## 🎓 Plan de Clase Sugerido

### Sesión 1: Introducción y Fase 1 (2 horas)
- Introducción al dataset
- Explicación de Fase 1: Comprensión del Negocio
- Ejercicio grupal: definir objetivos
- Discusión de riesgos y recursos

### Sesión 2: Fase 2 y Exploración (2 horas)
- Explicación de Fase 2: Comprensión de los Datos
- Demostración de EDA con visualizaciones
- Ejercicio: identificar patrones
- Formulación de hipótesis

### Sesión 3: Calidad e Insights (2 horas)
- Verificación de calidad de datos
- Análisis de insights principales
- Presentaciones grupales
- Reflexión sobre próximos pasos (Fases 3-6)

---

## 💡 Insights Principales del Análisis

- 🏆 **Categoría Líder:** Food and beverages
- ⏰ **Hora Pico:** 7:00 PM
- ⭐ **Rating Más Común:** 7.0
- 💳 **Pago Preferido:** Ewallet
- 👥 **Cliente Dominante:** 50.1% Members
- 📊 **Variabilidad:** 53.7% coeficiente de variación

*Ver la guía completa para análisis detallado*

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.13** - Lenguaje de programación
- **Pandas 2.3.3** - Manipulación de datos
- **Plotly 6.3.1** - Visualizaciones interactivas
- **NumPy 2.3.4** - Cálculos numéricos
- **HTML5/CSS3** - Diseño de la guía
- **JavaScript** - Interactividad

---

## 📚 Recursos Adicionales

### Documentación CRISP-DM:
- [CRISP-DM Official Guide](https://www.datascience-pm.com/crisp-dm-2/)
- [IBM CRISP-DM Manual](https://www.ibm.com/docs/en/spss-modeler/saas?topic=dm-crisp-help-overview)

### Tutoriales de Herramientas:
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Plotly Python](https://plotly.com/python/)
- [Python for Data Analysis](https://wesmckinney.com/book/)

### Cursos Recomendados:
- [Data Science Methodology - Coursera](https://www.coursera.org/learn/data-science-methodology)
- [Exploratory Data Analysis - DataCamp](https://www.datacamp.com/courses/exploratory-data-analysis-in-python)

---

## 🤝 Contribuir

Este material es de uso académico. Si deseas mejorarlo:

1. Modifica `generar_guia_interactiva.py`
2. Regenera la guía
3. Comparte tus mejoras con la comunidad educativa

---

## 📧 Contacto

**Universidad Externado de Colombia**
Curso: Minería de Datos

Para preguntas sobre este material, consulta con tu profesor.

---

## 📄 Licencia

Material educativo de uso libre para fines académicos.

**Nota:** El dataset "SuperMarket Analysis" es de dominio público para uso educativo.

---

## 🙏 Agradecimientos

- Universidad Externado de Colombia
- Comunidad de Ciencia de Datos
- Desarrolladores de Pandas, Plotly y NumPy
- Estudiantes que utilizan este material

---

## 📈 Estadísticas del Proyecto

- **Archivos generados:** 10
- **Líneas de código:** ~680 (Python)
- **Visualizaciones:** 11
- **Páginas de documentación:** ~80 (equivalente)
- **Tamaño total:** ~420 KB (sin venv)

---

## 🎉 ¡Comienza tu Aprendizaje!

👉 **Abre [`guia_interactiva_crisp_dm.html`](guia_interactiva_crisp_dm.html) y comienza a explorar!**

---

<div align="center">

**¡Disfruta el viaje en el mundo de la Minería de Datos!** 📊🎓

*Creado con ❤️ para la comunidad educativa*

---

[![Hecho con Python](https://img.shields.io/badge/Hecho_con-Python-blue?logo=python)](https://www.python.org/)
[![Visualizaciones con Plotly](https://img.shields.io/badge/Viz_con-Plotly-3F4F75?logo=plotly)](https://plotly.com/)
[![Análisis con Pandas](https://img.shields.io/badge/Análisis_con-Pandas-150458?logo=pandas)](https://pandas.pydata.org/)

*Última actualización: Octubre 2025 | Versión 1.0*

</div>
