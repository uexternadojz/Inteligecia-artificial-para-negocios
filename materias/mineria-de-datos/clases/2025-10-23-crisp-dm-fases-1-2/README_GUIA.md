# 🎓 Guía Interactiva CRISP-DM - Fases 1 y 2

## Material de Aprendizaje para Estudiantes

Esta guía interactiva ha sido creada para facilitar el aprendizaje de las Fases 1 y 2 de la metodología CRISP-DM utilizando un caso real de análisis de datos de supermercado.

---

## 📦 Archivos Generados

1. **`guia_interactiva_crisp_dm.html`** - Guía interactiva principal (abrir en navegador)
2. **`generar_guia_interactiva.py`** - Script Python que genera la guía
> Nota: este script actúa como wrapper del generador compartido `herramientas/scripts/generar_guia_crispdm.py`.
3. **`Reporte_Pedagogico_CRISP-DM_Fases_1_y_2.md`** - Documento pedagógico detallado para el profesor
4. **`.venv/` (crear local según necesidad)** - Entorno virtual Python con dependencias

---

## 🚀 Cómo Usar la Guía

### Para Estudiantes:

1. **Abrir la guía interactiva:**
   - Localiza el archivo `guia_interactiva_crisp_dm.html`
   - Doble clic para abrir en tu navegador web
   - No requiere conexión a Internet (funciona offline)

2. **Navegar por las pestañas:**
   - 🏠 **Introducción:** Contexto del dataset y estadísticas generales
   - 📋 **Fase 1: Negocio:** Comprensión del negocio aplicada al caso
   - 📊 **Fase 2: Datos:** Comprensión de los datos y tipos de variables
   - 🔍 **Exploración:** Visualizaciones interactivas del análisis exploratorio
   - ✅ **Calidad:** Verificación de calidad de datos
   - 💡 **Insights:** Hallazgos principales y próximos pasos

3. **Interactuar con los gráficos:**
   - Pasa el mouse sobre los gráficos para ver detalles
   - Haz zoom, pan y explora las visualizaciones
   - Todos los gráficos son interactivos gracias a Plotly

### Para Profesores:

1. **Usar en clase:**
   - Proyecta el HTML en pantalla grande
   - Navega entre pestañas para explicar cada fase
   - Usa las visualizaciones para ilustrar conceptos

2. **Personalizar la guía:**
   - Edita `generar_guia_interactiva.py` para modificar el contenido
   - Ejecuta: `.venv/bin/python generar_guia_interactiva.py`
   - Se regenerará el HTML con tus cambios

3. **Material de apoyo:**
   - Lee `Reporte_Pedagogico_CRISP-DM_Fases_1_y_2.md` para contexto pedagógico
   - Contiene ejercicios, analogías y consejos de enseñanza

---

## 🎨 Características de la Guía

### Diseño Interactivo:
- ✨ Navegación por pestañas intuitiva
- 🎨 Diseño moderno con gradientes y animaciones
- 📱 Responsive (funciona en móviles, tablets y desktop)
- 🎭 Animaciones suaves al hacer scroll

### Visualizaciones Incluidas:
1. **Distribución de ventas** - Histograma interactivo
2. **Análisis por sucursal** - Comparación de desempeño
3. **Líneas de producto** - Ventas coloreadas por rating
4. **Tipos de cliente** - Members vs Normal
5. **Métodos de pago** - Preferencias de pago
6. **Evolución temporal** - Series de tiempo
7. **Ventas por hora** - Identificación de horas pico
8. **Distribución de ratings** - Satisfacción del cliente
9. **Mapa de calor** - Productos × Sucursales
10. **Scatter plot multivariado** - Precio vs Cantidad vs Rating

### Contenido Educativo:
- 📊 Estadísticas generales del dataset
- 🎯 Objetivos de negocio aplicados al caso
- 📝 Checklist de tareas de cada fase
- 💡 Hipótesis preliminares a validar
- ✅ Verificación de calidad de datos
- 🎓 Actividades y preguntas de reflexión

---

## 🔧 Regenerar la Guía (Opcional)

Si quieres modificar o actualizar la guía:

```bash
# 1. Activar el entorno virtual
source .venv/bin/activate

# 2. (Opcional) Editar el script Python
# nano generar_guia_interactiva.py

# 3. Ejecutar el script
python generar_guia_interactiva.py

# 4. Se generará un nuevo guia_interactiva_crisp_dm.html
```

> También puedes ejecutar directamente el generador global desde la raíz: `python herramientas/scripts/generar_guia_crispdm.py -d <dataset> -o <salida>`.

---

## 📊 Sobre el Dataset

**Nombre:** SuperMarket Analysis
**Fuente:** Cadena de supermercados en Myanmar
**Período:** Enero - Marzo 2019
**Registros:** 1,000 transacciones
**Variables:** 17 columnas

### Variables Principales:
- **Transaccionales:** Invoice ID, Date, Time
- **Ubicación:** Branch, City
- **Cliente:** Customer type, Gender
- **Producto:** Product line, Unit price, Quantity
- **Financiero:** Sales, Tax, COGS, Gross income
- **Satisfacción:** Rating (1-10)
- **Pago:** Payment method

---

## 🎯 Objetivos de Aprendizaje

Al finalizar el estudio de esta guía, los estudiantes deberán:

### Fase 1 - Comprensión del Negocio:
1. ✅ Comprender la importancia de definir objetivos claros
2. ✅ Saber traducir objetivos de negocio a objetivos técnicos
3. ✅ Identificar recursos, riesgos y restricciones
4. ✅ Crear un plan de proyecto estructurado

### Fase 2 - Comprensión de los Datos:
1. ✅ Realizar análisis exploratorio de datos (EDA)
2. ✅ Identificar tipos de variables y sus características
3. ✅ Detectar problemas de calidad de datos
4. ✅ Formular hipótesis preliminares basadas en datos
5. ✅ Crear visualizaciones efectivas

---

## 💡 Consejos para Estudiantes

### Al estudiar la guía:
1. **No te apresures:** Tómate tiempo para entender cada concepto
2. **Interactúa:** Explora los gráficos, haz zoom, observa patrones
3. **Reflexiona:** Responde las preguntas de reflexión al final
4. **Practica:** Intenta replicar el análisis con otro dataset
5. **Pregunta:** Si algo no queda claro, consulta con el profesor

### Errores comunes a evitar:
- ❌ Saltar directo a los gráficos sin leer el contexto
- ❌ No formular hipótesis propias antes de ver los insights
- ❌ Ignorar la importancia de la calidad de datos
- ❌ No conectar los hallazgos con objetivos de negocio

---

## 🎓 Actividades Sugeridas

### Individual:
1. Lee toda la guía de principio a fin
2. Identifica 3 insights que no están mencionados
3. Propón un objetivo de negocio alternativo
4. Diseña una visualización adicional
5. Responde las preguntas de reflexión

### Grupal:
1. Debatir cuál es la categoría de producto más prometedora
2. Proponer estrategias de marketing basadas en los datos
3. Identificar sesgos potenciales en el dataset
4. Crear un plan de acción para la Fase 3

---

## 📚 Recursos Adicionales

### Documentación de Herramientas:
- **Pandas:** https://pandas.pydata.org/docs/
- **Plotly:** https://plotly.com/python/
- **CRISP-DM:** https://www.datascience-pm.com/crisp-dm-2/

### Lecturas Recomendadas:
- Manual CRISP-DM de IBM
- "Python for Data Analysis" - Wes McKinney
- "R for Data Science" - Hadley Wickham

---

## 🛠️ Requisitos Técnicos

### Para Ver la Guía:
- ✅ Navegador web moderno (Chrome, Firefox, Edge, Safari)
- ✅ JavaScript habilitado
- ✅ No requiere Internet (funciona offline)

### Para Regenerar la Guía:
- Python 3.8+
- Pandas
- Plotly
- NumPy

---

## 📝 Notas para el Profesor

### Sugerencias de uso en clase:

1. **Sesión 1 (2 horas):**
   - Introducción + Fase 1
   - Ejercicio grupal de definición de objetivos
   - Discusión de riesgos y recursos

2. **Sesión 2 (2 horas):**
   - Fase 2 + Exploración
   - Demostración en vivo de EDA
   - Ejercicio de identificación de patrones

3. **Sesión 3 (2 horas):**
   - Calidad + Insights
   - Formulación de hipótesis
   - Presentaciones grupales

### Evaluación sugerida:
- **Participación:** 20% (discusiones en clase)
- **Ejercicios prácticos:** 30% (identificación de patrones)
- **Proyecto grupal:** 50% (EDA completo de otro dataset)

---

## 🔄 Próximas Fases

Esta guía cubre las **Fases 1 y 2** de CRISP-DM. Las siguientes fases son:

- **Fase 3:** Preparación de Datos (Data Preparation)
- **Fase 4:** Modelado (Modeling)
- **Fase 5:** Evaluación (Evaluation)
- **Fase 6:** Despliegue (Deployment)

---

## 📧 Contacto

**Universidad Externado de Colombia**
Curso: Minería de Datos

Para preguntas o sugerencias sobre esta guía, consulta con tu profesor.

---

## 📄 Licencia

Este material educativo es de uso libre para fines académicos.

---

**¡Disfruta explorando los datos! 📊🎓**

*Última actualización: Enero 2025*
