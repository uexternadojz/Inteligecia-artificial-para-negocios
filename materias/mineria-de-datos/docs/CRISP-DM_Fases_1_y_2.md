<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

## CRISP-DM: Fases 1 y 2 para Minería de Datos

La metodología **CRISP-DM** (Cross-Industry Standard Process for Data Mining) es el estándar de facto más utilizado en proyectos de minería de datos y ciencia de datos. Esta metodología estructura el ciclo de vida de un proyecto en seis fases interrelacionadas e iterativas. Las dos primeras fases, **Comprensión del Negocio** y **Comprensión de los Datos**, son fundamentales para el éxito de cualquier proyecto de minería de datos, ya que establecen los cimientos sobre los cuales se construyen todas las fases posteriores.[^1][^2][^3]

### Fase 1: Comprensión del Negocio (Business Understanding)

La fase de comprensión del negocio es posiblemente la más crítica de toda la metodología. Su objetivo principal es entender los objetivos y requisitos del proyecto desde una perspectiva empresarial y convertir este conocimiento en la definición de un problema de minería de datos con un plan preliminar.[^4][^5][^1]

#### **Tareas principales de la Fase 1**

**1. Determinación de los objetivos comerciales**

Esta tarea busca obtener la máxima información posible sobre los objetivos de negocio que impulsan el proyecto. Es necesario:[^2][^4]

- **Compilar información de la empresa**: Comprender la estructura organizacional, identificar a los responsables clave, determinar quién es el patrocinador del proyecto y qué unidades de negocio se verán afectadas[^2][^4]
- **Describir el área problemática**: Identificar el dominio del problema (marketing, atención al cliente, desarrollo comercial), describir el problema en términos generales y entender los requisitos previos del proyecto[^2]
- **Describir la solución actual**: Documentar cómo se resuelve actualmente el problema, sus ventajas, desventajas y nivel de aceptación en la organización[^2]
- **Definir los objetivos comerciales**: Crear un objetivo principal concreto y acordado por los patrocinadores. Por ejemplo, transformar "reducir la tasa de abandono de clientes" en objetivos específicos y medibles[^4][^2]
- **Establecer criterios de éxito**: Definir criterios de rendimiento tanto objetivos (como un aumento del 10% en detección de fraudes) como subjetivos, asegurando que cada objetivo tenga un criterio de rendimiento relacionado[^4][^2]

**2. Evaluación de la situación**

Esta tarea implica realizar un diagnóstico completo de la situación actual antes de iniciar el proceso de minería de datos:[^1][^4]

- **Inventario de recursos**: Evaluar el hardware disponible, identificar las fuentes de datos y almacenes de conocimiento (tipos, formatos, acceso), y valorar los recursos humanos disponibles (expertos de negocio, administradores de base de datos, personal de apoyo)[^4][^2]
- **Requisitos, supuestos y restricciones**: Determinar restricciones legales y de seguridad, identificar supuestos sobre calidad de datos y factores económicos, y verificar restricciones de acceso y financieras[^2]
- **Análisis de riesgos y contingencias**: Identificar riesgos de programación, financieros, de calidad de datos y de resultados, y elaborar planes de contingencia para cada riesgo potencial[^4][^2]
- **Terminología**: Crear un glosario de términos técnicos y comerciales para asegurar que todos los equipos hablan el mismo idioma[^2]
- **Análisis de costes/beneficios**: Comparar los costes del proyecto (recopilación de datos, despliegue, costes operativos) con los beneficios potenciales[^2]

**3. Determinación de los objetivos de minería de datos**

Aquí se traduce el objetivo comercial en términos técnicos de minería de datos:[^5][^4][^2]

- **Definir objetivos de minería de datos**: Describir el tipo de problema (clasificación, regresión, clustering, asociación) y documentar objetivos técnicos usando unidades específicas. Por ejemplo, convertir "reducir el abandono" en: identificar clientes de alto valor, crear un modelo predictivo de abandono y asignar rangos a cada cliente[^5][^2]
- **Criterios de rendimiento de minería de datos**: Describir los métodos de evaluación (precisión, rendimiento, matriz de confusión), definir puntos de referencia numéricos concretos y considerar el despliegue como parte del rendimiento[^2]

**4. Producción de un plan de proyecto**

La tarea final de esta fase es crear el plan de proyecto que guiará todo el trabajo de minería de datos:[^4][^2]

- Incluir estimaciones de tiempo para todas las fases y tareas
- Documentar los esfuerzos y recursos necesarios para el despliegue
- Destacar puntos de decisión y solicitudes de revisión
- Resaltar las fases donde suelen ocurrir iteraciones (como modelado)
- Asegurar que el plan ha sido discutido con todos los usuarios implicados[^2]


#### **Aspectos clave a tener en cuenta en la Fase 1**

**Preguntas esenciales para guiar la fase:**

- ¿Qué se espera obtener exactamente de este proyecto?[^6]
- ¿Cuáles son los criterios de éxito desde una perspectiva de negocio?[^7][^2]
- ¿Se dispone de todos los recursos necesarios (presupuesto, personal, datos)?[^4][^2]
- ¿Cómo se puede saber que los resultados son precisos o efectivos?[^2]
- ¿Existen restricciones legales, de seguridad o financieras?[^2]
- ¿Qué factores de riesgo pueden afectar el proyecto y qué planes de contingencia existen?[^2]

**Errores comunes a evitar:**

- **Subestimar esta fase**: Es tentador acelerar para llegar al modelado, pero una comprensión deficiente del negocio puede invalidar todo el proyecto posterior[^8][^9]
- **Objetivos vagos o no medibles**: Los objetivos deben ser específicos, medibles y acordados por todos los stakeholders[^7][^4]
- **No involucrar a los stakeholders clave**: La falta de alineación con el negocio es una causa principal de fracaso en proyectos de minería de datos[^1][^4]
- **Ignorar las restricciones**: No considerar limitaciones de tiempo, presupuesto o acceso a datos puede llevar a expectativas irrealistas[^2]

**Entregables de la Fase 1:**

- Informe de comprensión del negocio
- Objetivos comerciales documentados
- Criterios de éxito definidos
- Inventario de recursos
- Análisis de riesgos y planes de contingencia
- Glosario de términos
- Análisis de costes/beneficios
- Objetivos de minería de datos
- Criterios de rendimiento técnico
- **Plan de proyecto detallado**[^10][^4][^2]


### Fase 2: Comprensión de los Datos (Data Understanding)

La fase de comprensión de los datos comienza con la recopilación inicial de datos y continúa con actividades que permiten familiarizarse con ellos, identificar problemas de calidad, descubrir los primeros conocimientos y formular hipótesis sobre información oculta. Esta fase es crítica porque un mal entendimiento de los datos aumenta el tiempo global del proyecto y reduce las garantías de éxito.[^3][^11][^5][^1]

#### **Tareas principales de la Fase 2**

**1. Recopilación de datos iniciales**

El primer paso es acceder y capturar los datos necesarios para el proyecto:[^12][^13]

- **Obtener acceso a los datos**: Hacerse con los datos identificados como recursos clave del proyecto o, al menos, con la posibilidad de acceder a ellos[^12]
- **Cargar datos en la herramienta de análisis**: Incorporar los datos al entorno de trabajo (por ejemplo, IBM SPSS Modeler, Python, R)[^2]
- **Caracterizar los datasets**: Documentar su localización, los métodos usados para conseguirlos y los problemas encontrados con sus resoluciones[^14][^12]
- **Analizar atributos prometedores**: Identificar qué atributos parecen relevantes y cuáles no lo son, y considerar si hay suficientes datos para conclusiones significativas[^2]

**Entregables de esta tarea:**

- Informe de recopilación de datos iniciales que resume los hallazgos, problemas encontrados y soluciones aplicadas[^12][^2]

**2. Descripción de los datos**

Una vez obtenidos los datos, es necesario realizar una caracterización general:[^11][^12]

- **Cuantificar los datos**: Determinar el número de registros y campos por registro, el volumen total de datos[^13][^12]
- **Calificar los datos**: Identificar el significado de cada campo, describir el formato inicial de los datos (CSV, JSON, bases de datos relacionales), documentar los tipos de datos (numéricos, categóricos, temporales)[^12]
- **Evaluar si los datos satisfacen los requerimientos**: Verificar que los datos obtenidos cumplen con los requisitos identificados en la fase anterior[^12]
- **Calcular estadísticos básicos**: Obtener medidas de tendencia central, dispersión y distribución para cada atributo de interés[^2]

**Entregables de esta tarea:**

- Informe de descripción de datos que detalla formato, dimensiones, características relevantes, tipos de datos, estadísticos descriptivos y priorización de atributos[^12][^2]

**3. Exploración de datos (Análisis Exploratorio de Datos - EDA)**

Esta es una de las tareas más importantes de la fase, donde se realiza un análisis preliminar profundo:[^15][^12]

- **Utilizar herramientas de visualización**: Emplear gráficos, tablas, histogramas, diagramas de dispersión y otras visualizaciones para entender las distribuciones de los datos[^16][^12]
- **Analizar distribuciones de atributos clave**: Observar cómo se distribuyen los valores, detectar posibles sesgos y asimetrías[^12]
- **Identificar relaciones entre atributos**: Buscar correlaciones, dependencias y patrones entre subconjuntos de variables[^15][^12]
- **Analizar subpoblaciones**: Estudiar las propiedades de determinados grupos dentro del total de los datos[^12]
- **Formular hipótesis iniciales**: Basándose en los patrones observados, proponer hipótesis que guiarán las transformaciones posteriores[^12][^2]

El **Análisis Exploratorio de Datos (EDA)** es fundamental para entender qué pueden revelar los datos más allá del modelado formal, ayudando a identificar errores obvios, comprender patrones, detectar valores atípicos y encontrar relaciones interesantes entre variables.[^16]

**Entregables de esta tarea:**

- Informe de exploración de datos que incluye hipótesis formuladas, atributos más prometedores, nuevas características reveladas, cambios en hipótesis iniciales y subconjuntos de datos identificados para análisis específicos[^12][^2]

**4. Verificación de la calidad de los datos**

La última tarea de esta fase se centra en examinar y documentar los problemas de calidad de los datos:[^13][^12]

- **Evaluar la completitud**: Verificar si los datos cubren todos los casos requeridos, identificar campos vacíos o registros incompletos[^13][^12]
- **Detectar errores**: Buscar valores incorrectos, inconsistencias de codificación, errores tipográficos y metadatos erróneos[^12][^2]
- **Analizar valores ausentes (missing values)**: Determinar cómo se representan, dónde ocurren y con qué frecuencia[^13][^12]
- **Identificar valores fuera de rango**: Detectar outliers que pueden constituir ruido o errores de medición[^13]
- **Evaluar consistencia**: Verificar la coherencia en formatos, delimitadores y esquemas de codificación[^2]

**Entregables de esta tarea:**

- Informe de calidad de datos que detalla todos los problemas identificados: datos perdidos, errores, inconsistencias, valores atípicos y recomendaciones para abordarlos en la siguiente fase[^13][^12][^2]


#### **Aspectos clave a tener en cuenta en la Fase 2**

**Preguntas esenciales para guiar la fase:**

- ¿Se han identificado y accedido correctamente a todos los orígenes de datos?[^2]
- ¿Se han identificado atributos clave que ayuden a formular hipótesis?[^2]
- ¿Se puede utilizar un subconjunto de datos cuando sea conveniente?[^2]
- ¿Los estadísticos básicos han revelado información de interés?[^2]
- ¿Los gráficos de exploración han reformulado alguna hipótesis inicial?[^2]
- ¿Cuáles fueron los principales problemas de calidad encontrados?[^2]
- ¿Están claras las tareas de preparación de datos necesarias?[^2]

**Mejores prácticas:**

- **Documentar exhaustivamente**: Cada hallazgo, por pequeño que parezca, debe documentarse porque puede ser relevante en fases posteriores[^13][^12]
- **Usar múltiples técnicas de visualización**: Diferentes visualizaciones revelan diferentes aspectos de los datos[^16][^7]
- **Colaborar con expertos del dominio**: Los especialistas del negocio pueden explicar anomalías aparentes que en realidad son características normales del dominio[^1][^4]
- **No apresurarse**: Esta fase junto con la preparación de datos suele consumir el 60-75% del tiempo total del proyecto[^9][^5]

**Herramientas útiles para EDA y visualización:**

- **Python**: pandas, matplotlib, seaborn, plotly
- **R**: ggplot2, dplyr, tidyverse
- **Visualización de datos**: Tableau, Power BI, Qlik
- **Análisis estadístico**: SPSS, SAS, IBM SPSS Modeler[^17][^3][^2]

**Errores comunes a evitar:**

- **Asumir que los datos están listos**: Raramente los datos están en condiciones óptimas desde el inicio[^5][^13]
- **Ignorar valores atípicos prematuramente**: Los outliers pueden ser errores, pero también pueden contener información valiosa[^16][^12]
- **No validar supuestos sobre los datos**: Las creencias sobre los datos deben verificarse empíricamente[^16][^2]
- **Subestimar problemas de calidad**: Los errores no detectados se propagan a la fase de modelado y reducen la exactitud de los modelos[^5]


### Interacción entre la Fase 1 y la Fase 2

Una característica fundamental de CRISP-DM es su **naturaleza iterativa y cíclica**. Las fases no se ejecutan de manera estrictamente lineal, sino que existe una constante retroalimentación entre ellas:[^18][^3][^1]

**Retroalimentación de Fase 2 a Fase 1:**

- Los descubrimientos durante la exploración de datos pueden revelar que los objetivos originales no son realistas o necesitan ajustarse[^1][^5]
- Problemas de calidad de datos pueden requerir revisar el inventario de recursos y considerar fuentes de datos alternativas[^12][^2]
- La falta de datos clave puede obligar a reformular los objetivos de minería de datos[^1][^2]

**Flujo de Fase 1 a Fase 2:**

- Los objetivos de negocio guían qué datos recopilar y qué atributos priorizar en la exploración[^4][^12]
- El conocimiento del dominio adquirido en la Fase 1 ayuda a interpretar patrones encontrados en los datos[^1][^12]
- Las restricciones identificadas en la Fase 1 determinan qué volumen de datos es factible procesar[^2]

**Ejemplo de iteración:**

Durante la comprensión de datos de un proyecto de predicción de abandono de clientes, el equipo descubre que no dispone de datos sobre interacciones de servicio al cliente, identificadas como clave en la fase de comprensión del negocio. Esto obliga a volver a la Fase 1 para:

- Revisar los objetivos (¿se pueden lograr sin estos datos?)
- Actualizar el inventario de recursos (¿dónde conseguir estos datos?)
- Ajustar el plan de proyecto (tiempo adicional para obtener/integrar nuevos datos)[^5][^1][^2]


### Transición a la Fase 3: Preparación de Datos

Al finalizar la Fase 2, deberías tener:

- **Comprensión clara de la viabilidad del proyecto**: Los datos disponibles permiten alcanzar los objetivos establecidos[^5][^1]
- **Idea clara de los resultados esperados**: Basada en el análisis exploratorio realizado[^1]
- **Documentación completa de problemas de calidad**: Lista de todas las tareas de limpieza y transformación necesarias[^12][^2]
- **Hipótesis preliminares**: Que guiarán la construcción de nuevas variables y la selección de atributos[^12]

**Preguntas clave antes de avanzar:**

- ¿El nivel de comprensión de los datos es suficiente?[^2]
- ¿Se sabe qué orígenes de datos deben fusionarse?[^2]
- ¿Están identificados los atributos que deben filtrarse o seleccionarse?[^2]
- ¿Las fases de preparación de datos están claras?[^2]

Solo cuando se puedan responder afirmativamente estas preguntas se debe avanzar a la Fase 3 (Preparación de Datos), que típicamente consume el mayor esfuerzo (aproximadamente 50-70% del tiempo del proyecto).[^19][^9][^5]

### Conclusión

Las fases 1 y 2 de CRISP-DM son los cimientos de cualquier proyecto exitoso de minería de datos. La **Fase 1: Comprensión del Negocio** asegura que el proyecto esté alineado con las necesidades reales de la organización y tenga objetivos claros y medibles. La **Fase 2: Comprensión de los Datos** garantiza que se conozcan a fondo los datos disponibles, sus limitaciones y su potencial para responder a las preguntas de negocio planteadas.

Ambas fases requieren:

- **Documentación exhaustiva** de todos los hallazgos y decisiones
- **Colaboración estrecha** entre equipos técnicos y de negocio
- **Flexibilidad** para iterar y ajustar objetivos según los descubrimientos
- **Paciencia** para no apresurarse hacia el modelado sin bases sólidas

El tiempo invertido en estas fases iniciales se recupera con creces al evitar retrabajo, reducir riesgos y aumentar significativamente las probabilidades de que el proyecto genere valor real para la organización.[^8][^9][^19][^5][^1]
<span style="display:none">[^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^30][^31][^32][^33][^34][^35][^36][^37][^38][^39][^40][^41][^42][^43][^44][^45][^46][^47][^48][^49][^50][^51][^52][^53][^54][^55][^56]</span>

<div align="center">⁂</div>

[^1]: https://www.iic.uam.es/innovacion/metodologia-crisp-dm-ciencia-de-datos/

[^2]: https://www.ibm.com/docs/es/SS3RA7_18.5.0/nl/es/pdf/ModelerCRISPDM.pdf

[^3]: https://www.ibm.com/docs/es/spss-modeler/saas?topic=dm-crisp-help-overview

[^4]: https://www.mikelnino.com/2016/11/crisp-dm-metodologia-data-mining-comprension-negocio-business-understanding.html

[^5]: https://adictosaltrabajo.com/2021/01/14/metodologia-crisp-dm/

[^6]: https://www.nisum.com/es/nisum-knows/best-way-leverage-cross-industry-standard-process-data-mining-crisp-dm

[^7]: https://www.mytaskpanel.com/la-metodologia-crisp-dm-desarrollo-de-modelos-de-machine-learning/

[^8]: https://healthdataminer.com/data-mining/crisp-dm-una-metodologia-para-mineria-de-datos-en-salud/

[^9]: https://blog.mbauspesalq.com/es/crisp-dm-las-6-etapas-de-la-metodologia-del-futuro/

[^10]: https://ipmoguide.com/fases-de-la-metodologia-crisp-dm/

[^11]: https://www.dataprix.com/es/metodologia-crisp-dm-para-mineria-de-datos/el-modelo-de-referencia-crisp-dm

[^12]: https://www.mikelnino.com/2016/11/crisp-dm-metodologia-data-mining-comprension-datos-data-understanding.html

[^13]: https://es.scribd.com/document/882263945/Crisp-DM-Documento-Completo

[^14]: https://gc.scalahed.com/recursos/files/r161r/w25341w/MetodologiaDesarrollo_proyectos_Mineria_de_Datos_RS4.pdf

[^15]: https://blog.smartupdigital.com/crisp-dm-6-pasos-proceso-data-mining

[^16]: https://www.ibm.com/es-es/think/topics/exploratory-data-analysis

[^17]: http://portal.amelica.org/ameli/journal/602/6023721001/

[^18]: https://martescoach.oscarschmitz.com/p/crisp-dm-la-guia-definitiva-para

[^19]: https://www.danalyticspro.com/proyectos-analitica-de-datos-con-crispdm/

[^20]: https://e-archivo.uc3m.es/bitstreams/714c5452-962e-44cf-993f-ebb3088d4aa5/download

[^21]: https://aws.amazon.com/es/what-is/data-mining/

[^22]: https://www.youtube.com/watch?v=UyKkSsEbXkw

[^23]: https://www.studocu.com/es-mx/document/instituto-tecnologico-y-de-estudios-superiores-de-monterrey/matematicas-y-ciencia-de-datos-para-la-toma-de-decisiones/fase-1-entendimiento-del-negocio/40437910

[^24]: https://openaccess.uoc.edu/server/api/core/bitstreams/20b39332-4ac7-49e6-b9cc-c34c4401d380/content

[^25]: https://bsginstitute.com/bs-campus/blog/Metodología-CRISP-DM-Guía-para-Científicos-de-Datos-0

[^26]: https://repository.umng.edu.co/items/471987be-811e-4ad1-98c6-57ab4325da92

[^27]: https://rpubs.com/mavaleriacc/1075094

[^28]: https://ojs.unipamplona.edu.co/index.php/rcta/article/view/2822/6609

[^29]: https://www.datascience-pm.com/crisp-dm-2/

[^30]: https://www.ideca.gov.co/sites/default/files/MetodologiaAnaliticaDatos_0.pdf

[^31]: https://campusgrado.fi.uba.ar/pluginfile.php/76211/mod_resource/content/1/Resumen%20Crisp-DM.pdf

[^32]: https://es.scribd.com/document/506994502/Metodologia-Crisp-y-Ejemplo

[^33]: https://territoriosia.mintic.gov.co/inventario/analisis_seguridad.html

[^34]: https://revistas.utp.edu.co/index.php/revistaciencia/article/view/9241/6281

[^35]: https://www.rpubs.com/AnaCastillo/1254079

[^36]: http://oa.upm.es/88465/1/PFG_ALBERTO_ANTONIO_LOPEZ_PEREZVILLAMIL.pdf

[^37]: https://territoriosia.mintic.gov.co/cuaderno-seguridad/

[^38]: https://www.hiberus.com/crecemos-contigo/adaptacion-de-scrum-para-business-analytics/

[^39]: https://www.xmslatam.com/analisis-de-datos-guia-practica/

[^40]: https://ignaciogavilan.com/metodologia-para-machine-learning-i-crisp-dm/

[^41]: https://es.scribd.com/document/891664738/Presentacion-M3-Clase-1-Introduccion-EDA-2

[^42]: https://es.scribd.com/document/812248940/Examen-Final-Primer-Intento

[^43]: https://es.scribd.com/document/889601537/Tema-3-Ejemplos-de-Proyectos-de-CRISP-DM-pptx

[^44]: https://www.studocu.com/cl/quiz/crisp-dm-resumen-en-espanol/1070242

[^45]: https://www.ibm.com/docs/es/SS3RA7_18.3.0/pdf/ModelerCRISPDM.pdf

[^46]: https://es.linkedin.com/pulse/quieres-saber-cuales-son-las-fases-de-la-metodología-mora-caballero

[^47]: https://www.studocu.com/co/document/fundacion-universitaria-del-area-andina/big-data/a-practicar-la-mineria-de-datos-para-el-analisis/89806393

[^48]: https://es.scribd.com/document/860062967/Fase2-Crisp-DM-ConocerDatos

[^49]: https://bibdigital.epn.edu.ec/bitstream/15000/26484/1/CD 15034.pdf

[^50]: https://libros.ecotec.edu.ec/index.php/editorial/catalog/download/2/2/29-1?inline=1

[^51]: https://es.linkedin.com/pulse/impacto-de-crispdm-en-proyectos-ia-y-su-vigencia-frente-jesús-mejía-70wif

[^52]: https://www.cienciadedatospuebla.com/infodatathon.html

[^53]: https://www.linkedin.com/pulse/metodología-crisp-dm-la-guía-definitiva-para-minería-de-arias-xyusf

[^54]: https://www.scribd.com/document/561027316/CRISP-DM-Business-Understanding

[^55]: https://es.scribd.com/document/904251067/METODOLOGIA-CRISP-DM

[^56]: https://start.agilytic.com/crisp-dm

