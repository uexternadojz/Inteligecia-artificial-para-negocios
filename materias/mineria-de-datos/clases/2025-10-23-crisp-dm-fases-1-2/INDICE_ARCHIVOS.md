# 📑 Índice de Archivos del Proyecto

## Guía Interactiva CRISP-DM - Fases 1 y 2

---

## 🎯 Inicio Rápido

### Para Estudiantes:
1. **Abre:** [guia_interactiva_crisp_dm.html](guia_interactiva_crisp_dm.html)
2. **Lee:** [README_GUIA.md](README_GUIA.md) para instrucciones

### Para Profesores:
1. **Revisa:** [Reporte_Pedagogico_CRISP-DM_Fases_1_y_2.md](Reporte_Pedagogico_CRISP-DM_Fases_1_y_2.md)
2. **Proyecta:** [guia_interactiva_crisp_dm.html](guia_interactiva_crisp_dm.html) en clase

---

## 📂 Archivos Principales

### 1. 🌐 Archivo HTML Interactivo
**Nombre:** `guia_interactiva_crisp_dm.html` (221 KB)
- **Descripción:** Guía interactiva principal con visualizaciones
- **Uso:** Abrir en navegador web (Chrome, Firefox, Edge, Safari)
- **Características:**
  - 6 pestañas navegables
  - 11+ visualizaciones interactivas
  - Diseño responsive
  - Funciona sin Internet
- **Estado:** ✅ Listo para usar
- **Abrir con:**
  ```bash
  ./abrir_guia.sh
  # O doble clic en el archivo
  ```

---

### 2. 📝 Reporte Pedagógico (Para Profesor)
**Nombre:** `Reporte_Pedagogico_CRISP-DM_Fases_1_y_2.md` (43 KB)
- **Descripción:** Guía completa para enseñar CRISP-DM Fases 1 y 2
- **Contenido:**
  - Explicaciones detalladas de cada fase
  - Objetivos aplicados al caso del supermercado
  - Ejercicios y actividades para estudiantes
  - Analogías pedagógicas
  - Plan de clase de 2 horas
  - Checklist y consejos de enseñanza
- **Audiencia:** Profesores
- **Formato:** Markdown (leer con cualquier editor o convertir a PDF)
- **Estado:** ✅ Completo

---

### 3. 📖 Documentación de Uso
**Nombre:** `README_GUIA.md` (7.7 KB)
- **Descripción:** Instrucciones completas de uso del material
- **Contenido:**
  - Cómo usar la guía interactiva
  - Características del diseño
  - Objetivos de aprendizaje
  - Actividades sugeridas
  - Recursos adicionales
  - Requisitos técnicos
- **Audiencia:** Estudiantes y Profesores
- **Estado:** ✅ Completo

---

### 4. 📊 Resumen Ejecutivo
**Nombre:** `RESUMEN_PROYECTO.md` (9.0 KB)
- **Descripción:** Resumen completo del proyecto y archivos generados
- **Contenido:**
  - Lista de archivos y su propósito
  - Estadísticas del dataset
  - Objetivos logrados
  - Tecnologías utilizadas
  - Impacto esperado
- **Audiencia:** Todos
- **Estado:** ✅ Completo

---

## 🛠️ Archivos Técnicos

### 5. 🐍 Script de Generación
**Nombre:** `generar_guia_interactiva.py` (wrapper)
- **Descripción:** Script Python que genera la guía (wrapper sobre el generador global)
> Wrapper del generador global ubicado en `herramientas/scripts/generar_guia_crispdm.py`.
 HTML
- **Funcionalidad:**
  - Carga y analiza el dataset CSV
  - Calcula estadísticas descriptivas
  - Genera 11 visualizaciones con Plotly
  - Crea HTML completo con contenido
- **Uso:**
  ```bash
  .venv/bin/python generar_guia_interactiva.py
# o desde la raíz
python herramientas/scripts/generar_guia_crispdm.py -d 'recursos_compartidos/datasets/mineria-de-datos/supermarket_analysis.csv' -o 'materias/mineria-de-datos/clases/2025-10-23-crisp-dm-fases-1-2/guia_interactiva_crisp_dm.html'
  ```
- **Dependencias:** pandas, plotly, numpy (ver .venv/)
- **Estado:** ✅ Funcional

---

### 6. 📜 Script de Apertura
**Nombre:** `abrir_guia.sh` (990 bytes)
- **Descripción:** Script para abrir la guía en el navegador
- **Compatibilidad:** Linux, macOS, Windows (Git Bash)
- **Uso:**
  ```bash
  ./abrir_guia.sh
  ```
- **Permisos:** Ejecutable (chmod +x)
- **Estado:** ✅ Funcional

---

## 📚 Archivos de Referencia

### 7. 📄 Documento Original
**Nombre:** `CRISP-DM_ Fases 1 y 2 para Minería de Datos.md` (22 KB)
- **Descripción:** Documento inicial de referencia sobre CRISP-DM
- **Fuente:** Investigación con Perplexity
- **Contenido:**
  - Explicación teórica de Fase 1
  - Explicación teórica de Fase 2
  - Referencias bibliográficas
- **Uso:** Referencia complementaria
- **Estado:** ✅ Disponible

---

### 8. 📊 Dataset Original
**Nombre:** `recursos_compartidos/datasets/mineria-de-datos/supermarket_analysis.csv`
- **Descripción:** Datos de ventas de supermercado (dataset compartido)
- **Registros:** 1,000 transacciones
- **Variables:** 17 columnas
- **Período:** Enero - Marzo 2019
- **Tamaño:** ~150 KB
- **Formato:** CSV con encoding UTF-8
- **Estado:** ✅ Disponible

---

## 🔧 Entorno Técnico

### 9. 📦 Entorno Virtual Python
**Carpeta:** `.venv/` (crear local según necesidad)
- **Descripción:** Entorno virtual con dependencias instaladas
- **Dependencias:**
  - pandas 2.3.3
  - plotly 6.3.1
  - numpy 2.3.4
  - narwhals, python-dateutil, pytz, etc.
- **Activar:**
  ```bash
  source .venv/bin/activate
  ```
- **Estado:** ✅ Configurado

---

## 🗺️ Mapa de Navegación

```
📁 PROYECTO CRISP-DM
│
├── 🎯 INICIO RÁPIDO
│   ├── guia_interactiva_crisp_dm.html ⭐ [COMENZAR AQUÍ]
│   └── README_GUIA.md
│
├── 📚 MATERIAL PEDAGÓGICO
│   ├── Reporte_Pedagogico_CRISP-DM_Fases_1_y_2.md [Para Profesor]
│   └── CRISP-DM_ Fases 1 y 2...md [Referencia]
│
├── 📖 DOCUMENTACIÓN
│   ├── RESUMEN_PROYECTO.md
│   └── INDICE_ARCHIVOS.md [Este archivo]
│
├── 🛠️ HERRAMIENTAS
│   ├── generar_guia_interactiva.py
│   ├── abrir_guia.sh
│   └── .venv/
│
└── 📊 DATOS
    └── SuperMarket Analysis.csv
```

---

## ✅ Lista de Verificación

### Para el Profesor:

- [ ] Leer `Reporte_Pedagogico_CRISP-DM_Fases_1_y_2.md`
- [ ] Revisar `guia_interactiva_crisp_dm.html` completo
- [ ] Preparar ejemplos adicionales si se desea
- [ ] Probar que todos los gráficos funcionan
- [ ] Planificar tiempo de clase (sugerido: 2 horas × 3 sesiones)
- [ ] Preparar proyector o compartir pantalla
- [ ] Compartir archivos con estudiantes

### Para el Estudiante:

- [ ] Leer `README_GUIA.md` para orientación
- [ ] Abrir `guia_interactiva_crisp_dm.html` en navegador
- [ ] Explorar las 6 pestañas completamente
- [ ] Interactuar con todos los gráficos
- [ ] Responder preguntas de reflexión
- [ ] Completar actividades sugeridas
- [ ] Formar grupo para ejercicios colaborativos

---

## 🎓 Flujo de Aprendizaje Recomendado

### Sesión 1: Introducción y Fase 1 (2 horas)
1. Abrir pestaña "Introducción"
2. Revisar estadísticas del dataset
3. Leer pestaña "Fase 1: Negocio"
4. Discutir objetivos comerciales
5. Ejercicio grupal: definir objetivos propios

### Sesión 2: Fase 2 y Exploración (2 horas)
1. Leer pestaña "Fase 2: Datos"
2. Explorar pestaña "Exploración"
3. Interactuar con cada visualización
4. Formular hipótesis propias
5. Ejercicio: identificar patrones no mencionados

### Sesión 3: Calidad e Insights (2 horas)
1. Revisar pestaña "Calidad"
2. Leer pestaña "Insights"
3. Discusión grupal de hallazgos
4. Presentaciones de equipos
5. Reflexión sobre próximos pasos

---

## 💡 Consejos de Uso

### Para Máxima Efectividad:

1. **No te apresures:** Dedica tiempo a cada sección
2. **Interactúa:** Explora cada gráfico con el mouse
3. **Anota:** Toma notas de insights importantes
4. **Discute:** Comparte hallazgos con compañeros
5. **Practica:** Intenta replicar análisis con otro dataset

### Solución de Problemas:

**Problema:** La guía HTML no se abre
- **Solución:** Usa `./abrir_guia.sh` o doble clic en el archivo

**Problema:** Los gráficos no son interactivos
- **Solución:** Asegúrate de tener JavaScript habilitado en el navegador

**Problema:** Quiero modificar la guía
- **Solución:** Edita `generar_guia_interactiva.py` y ejecuta el script

**Problema:** Necesito regenerar la guía
- **Solución:**
  ```bash
  source .venv/bin/activate
  python generar_guia_interactiva.py
# o desde la raíz
python herramientas/scripts/generar_guia_crispdm.py -d 'recursos_compartidos/datasets/mineria-de-datos/supermarket_analysis.csv' -o 'materias/mineria-de-datos/clases/2025-10-23-crisp-dm-fases-1-2/guia_interactiva_crisp_dm.html'
  ```

---

## 📊 Estadísticas del Proyecto

- **Archivos generados:** 9
- **Tamaño total:** ~420 KB (sin venv)
- **Líneas de código Python:** ~680
- **Visualizaciones creadas:** 11
- **Páginas de documentación:** ~80 (equivalente)
- **Tiempo de desarrollo:** ~2 horas
- **Tecnologías usadas:** 4 (Python, HTML, CSS, JavaScript)

---

## 🎯 Objetivos Cumplidos

✅ Material interactivo generado
✅ Visualizaciones con datos reales
✅ Contenido pedagógico completo
✅ Documentación exhaustiva
✅ Scripts automatizados
✅ Entorno reproducible
✅ Diseño profesional
✅ Funciona offline

---

## 🚀 Extensiones Futuras

### Ideas para Mejorar:

1. **Agregar quiz interactivo** al final de cada fase
2. **Incluir videos explicativos** embebidos
3. **Crear ejercicios autocorregibles** con JavaScript
4. **Agregar comparación** con otros datasets
5. **Traducir a inglés** para audiencia internacional
6. **Crear versión PDF** descargable
7. **Añadir modo oscuro** (dark mode)
8. **Desarrollar Fases 3-6** de CRISP-DM

---

## 📧 Soporte

Para preguntas o problemas:

1. **Primero:** Consulta este índice y el README
2. **Luego:** Revisa la documentación específica
3. **Si persiste:** Contacta al profesor del curso

---

## 📄 Licencia y Créditos

- **Material educativo:** Uso libre para fines académicos
- **Universidad:** Externado de Colombia
- **Curso:** Minería de Datos
- **Dataset:** SuperMarket Analysis (dominio público)
- **Herramientas:** Python (PSF), Plotly (MIT), Pandas (BSD)

---

## 🎉 ¡Éxito en tu Aprendizaje!

Este material ha sido diseñado con cuidado para facilitar tu comprensión de CRISP-DM. Aprovecha al máximo las herramientas interactivas y no dudes en explorar más allá de lo presentado.

**¡Disfruta el viaje en el mundo de la Minería de Datos! 📊🎓**

---

*Última actualización: Octubre 2025*
*Versión: 1.0*
