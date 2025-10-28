# 📚 Clase 2 - CRISP-DM: Fases 1 y 2

**Fecha:** 23 de Octubre de 2025
**Curso:** Minería de Datos
**Universidad:** Externado de Colombia
**Tema:** Metodología CRISP-DM - Comprensión del Negocio y Comprensión de los Datos

---

## 🎯 Objetivos de la Clase

1. Comprender la **Fase 1: Comprensión del Negocio**
2. Comprender la **Fase 2: Comprensión de los Datos**
3. Aplicar ambas fases a un caso real de análisis de supermercado
4. Realizar análisis exploratorio de datos (EDA) con visualizaciones interactivas

---

## 📦 Contenido de esta Carpeta

### 🌐 Archivo Principal para Estudiantes
**`guia_interactiva_crisp_dm.html`** (224 KB)
- Guía interactiva con 11+ visualizaciones
- 6 pestañas navegables
- Funciona en cualquier navegador
- **COMENZAR AQUÍ** ⭐

### 📊 Datos
**Dataset compartido:** `recursos_compartidos/datasets/mineria-de-datos/supermarket_analysis.csv`
- 1,000 transacciones de supermercado
- 17 variables
- Período: Enero-Marzo 2019

### 📚 Material Pedagógico
- **`Reporte_Pedagogico_CRISP-DM_Fases_1_y_2.md`** - Guía completa para el profesor
- **`README.md`** - Documentación general del proyecto
- **`README_GUIA.md`** - Instrucciones de uso
- **`INDICE_ARCHIVOS.md`** - Índice completo de archivos
- **`INICIO_RAPIDO.txt`** - Guía rápida visual

### 🛠️ Herramientas
- **`generar_guia_interactiva.py`** - Wrapper que invoca el generador global de la guía
- **`abrir_guia.sh`** - Script para abrir la guía automáticamente
- **`.venv/` (crear local según necesidad)** - Entorno virtual Python con dependencias

### 📄 Documentación
- **`RESUMEN_PROYECTO.md`** - Resumen ejecutivo del proyecto

---

## 🚀 Inicio Rápido para Estudiantes

### Opción 1: Abre la Guía Interactiva (Recomendado)
```bash
# Doble clic en:
guia_interactiva_crisp_dm.html

# O desde terminal:
./abrir_guia.sh
```

### Opción 2: Explora los Datos
```bash
# Abre el CSV en Excel o LibreOffice
recursos_compartidos/datasets/mineria-de-datos/supermarket_analysis.csv
```

### Opción 3: Lee el Material Pedagógico
```bash
# Para entender la teoría
Reporte_Pedagogico_CRISP-DM_Fases_1_y_2.md
```

---

## 📖 Estructura de la Guía Interactiva

### Pestaña 1: 🏠 Introducción
- Contexto del dataset
- Estadísticas generales
- Variables del dataset

### Pestaña 2: 📋 Fase 1: Comprensión del Negocio
- Determinación de objetivos comerciales
- Evaluación de la situación
- Objetivos de minería de datos
- Plan de proyecto

### Pestaña 3: 📊 Fase 2: Comprensión de los Datos
- Recopilación de datos
- Descripción de datos
- Tipos de variables

### Pestaña 4: 🔍 Exploración (EDA)
- 11 visualizaciones interactivas
- Análisis univariado
- Análisis bivariado
- Análisis multivariado

### Pestaña 5: ✅ Calidad de Datos
- Checklist de calidad
- Problemas detectados
- Recomendaciones para Fase 3

### Pestaña 6: 💡 Insights
- Hallazgos principales
- Hipótesis preliminares
- Próximos pasos
- Actividades de aprendizaje

---

## 📊 Dataset: SuperMarket Analysis

### Información General
- **Registros:** 1,000 transacciones
- **Variables:** 17 columnas
- **Período:** Enero - Marzo 2019 (88 días)
- **Sucursales:** 3 (Alex, Giza, Cairo)
- **Ciudades:** Yangon, Naypyitaw, Mandalay
- **Categorías de Productos:** 6

### Variables Principales
- **Transaccionales:** Invoice ID, Date, Time
- **Ubicación:** Branch, City
- **Cliente:** Customer type, Gender
- **Producto:** Product line, Unit price, Quantity
- **Financiero:** Sales, Tax, COGS, Gross income
- **Satisfacción:** Rating (1-10)
- **Pago:** Payment method

### Estadísticas Clave
- **Total Ventas:** $322,966.75
- **Ticket Promedio:** $322.97
- **Rating Promedio:** 6.97/10
- **Transacciones por Día:** ~11.4

---

## 🎓 Plan de Clase (6 horas / 3 sesiones)

### Sesión 1: Introducción y Fase 1 (2 horas)
**Contenido:**
1. Introducción a CRISP-DM (30 min)
2. Fase 1: Comprensión del Negocio (60 min)
3. Ejercicio grupal: Definir objetivos (30 min)

**Actividades:**
- Presentación del caso del supermercado
- Discusión de objetivos comerciales
- Identificación de riesgos y recursos

### Sesión 2: Fase 2 y Exploración (2 horas)
**Contenido:**
1. Fase 2: Comprensión de los Datos (45 min)
2. Análisis Exploratorio de Datos (60 min)
3. Ejercicio: Identificar patrones (15 min)

**Actividades:**
- Demostración de la guía interactiva
- Exploración de visualizaciones
- Formulación de hipótesis

### Sesión 3: Calidad e Insights (2 horas)
**Contenido:**
1. Verificación de calidad de datos (30 min)
2. Análisis de insights principales (45 min)
3. Presentaciones grupales (45 min)

**Actividades:**
- Discusión de problemas de calidad
- Análisis de hipótesis
- Presentación de hallazgos

---

## 💡 Actividades para Estudiantes

### Actividad 1: Exploración Guiada (Individual)
**Tiempo:** 30 minutos
**Tarea:**
1. Abre la guía interactiva
2. Navega por las 6 pestañas
3. Anota 5 insights que encuentres
4. Responde las preguntas de reflexión

### Actividad 2: Definición de Objetivos (Grupal)
**Tiempo:** 45 minutos
**Tarea:**
1. Formar grupos de 3-4 personas
2. Definir un objetivo de negocio alternativo para el supermercado
3. Traducirlo a un objetivo técnico de minería de datos
4. Presentar al resto de la clase

### Actividad 3: Análisis de Calidad (Grupal)
**Tiempo:** 30 minutos
**Tarea:**
1. Revisar la pestaña "Calidad"
2. Identificar 3 problemas de calidad adicionales
3. Proponer soluciones
4. Discutir en clase

### Actividad 4: Hipótesis (Individual)
**Tiempo:** 20 minutos
**Tarea:**
1. Formular 3 hipótesis propias basadas en las visualizaciones
2. Explicar cómo las validarías
3. Compartir con un compañero

---

## 🔧 Para Regenerar la Guía (Opcional)

Si deseas modificar la guía:

```bash
# 1. Activar entorno virtual
source .venv/bin/activate

# 2. (Opcional) Editar el script
nano generar_guia_interactiva.py

# 3. Regenerar
python generar_guia_interactiva.py
# o directamente desde la raíz
python herramientas/scripts/generar_guia_crispdm.py -d 'recursos_compartidos/datasets/mineria-de-datos/supermarket_analysis.csv' -o 'materias/mineria-de-datos/clases/2025-10-23-crisp-dm-fases-1-2/guia_interactiva_crisp_dm.html'

# 4. Desactivar entorno
deactivate
```

---

## 📚 Recursos Adicionales

### Documentación de CRISP-DM
- [CRISP-DM Official Guide](https://www.datascience-pm.com/crisp-dm-2/)
- [IBM CRISP-DM Manual](https://www.ibm.com/docs/en/spss-modeler/saas?topic=dm-crisp-help-overview)

### Tutoriales de Herramientas
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Plotly Python](https://plotly.com/python/)

### Cursos Relacionados
- [Data Science Methodology - Coursera](https://www.coursera.org/learn/data-science-methodology)
- [Exploratory Data Analysis - DataCamp](https://www.datacamp.com/courses/exploratory-data-analysis-in-python)

---

## 📧 Soporte

Para preguntas sobre este material:
1. Consulta los archivos de documentación incluidos
2. Revisa la guía interactiva completa
3. Contacta al profesor del curso

---

## ✅ Checklist para la Clase

### Antes de la Clase (Profesor)
- [ ] Revisar la guía interactiva completa
- [ ] Leer el reporte pedagógico
- [ ] Preparar proyector/pantalla compartida
- [ ] Probar que el HTML funciona correctamente
- [ ] Preparar ejemplos adicionales si es necesario

### Antes de la Clase (Estudiantes)
- [ ] Descargar todos los archivos de la carpeta
- [ ] Abrir y explorar `guia_interactiva_crisp_dm.html`
- [ ] Leer la introducción y objetivos
- [ ] Tener lista una aplicación para tomar notas

### Durante la Clase
- [ ] Tomar apuntes de conceptos clave
- [ ] Participar en ejercicios grupales
- [ ] Hacer preguntas cuando algo no esté claro
- [ ] Explorar las visualizaciones interactivas

### Después de la Clase
- [ ] Completar actividades pendientes
- [ ] Revisar material adicional
- [ ] Practicar con otro dataset
- [ ] Prepararse para las Fases 3-6

---

## 🎉 ¡Bienvenidos a la Clase 2!

Este material está diseñado para facilitar tu aprendizaje de las Fases 1 y 2 de CRISP-DM mediante un caso práctico y visualizaciones interactivas.

**¡Disfruta explorando los datos! 📊🎓**

---

*Material creado para el curso de Minería de Datos*
*Universidad Externado de Colombia - 2025*
