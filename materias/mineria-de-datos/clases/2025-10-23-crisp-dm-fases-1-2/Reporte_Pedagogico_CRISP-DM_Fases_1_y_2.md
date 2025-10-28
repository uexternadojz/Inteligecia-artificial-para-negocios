# Reporte Pedagógico: CRISP-DM Fases 1 y 2
## Guía Didáctica con Caso Práctico - Análisis de Supermercado

---

## Introducción al Caso de Estudio

### Contexto del Dataset

Para esta clase utilizaremos el dataset **"SuperMarket Analysis.csv"**, que contiene información real de ventas de una cadena de supermercados. Este dataset representa un caso ideal para aplicar minería de datos en el contexto de retail.

**Características del Dataset:**
- **1,000 registros** de transacciones de ventas
- **17 variables** que describen cada transacción
- **3 sucursales** (Alex, Giza, Cairo) en diferentes ciudades (Yangon, Naypyitaw, Mandalay)
- **Período:** Enero a Marzo 2019
- **6 líneas de productos:** Health and beauty, Electronic accessories, Home and lifestyle, Sports and travel, Food and beverages, Fashion accessories

**Variables disponibles:**
1. Invoice ID - Identificador único de la factura
2. Branch - Sucursal (Alex, Giza, Cairo)
3. City - Ciudad
4. Customer type - Tipo de cliente (Member, Normal)
5. Gender - Género del cliente
6. Product line - Línea de productos
7. Unit price - Precio unitario
8. Quantity - Cantidad comprada
9. Tax 5% - Impuesto aplicado
10. Sales - Venta total
11. Date - Fecha de la transacción
12. Time - Hora de la transacción
13. Payment - Método de pago (Ewallet, Cash, Credit card)
14. cogs - Costo de los bienes vendidos
15. gross margin percentage - Porcentaje de margen bruto (4.76% constante)
16. gross income - Ingreso bruto
17. Rating - Calificación del cliente (escala de satisfacción)

---

## FASE 1: COMPRENSIÓN DEL NEGOCIO (Business Understanding)

### ¿Por qué esta fase es la más crítica?

La Fase 1 es el fundamento de todo proyecto de minería de datos. Un error común es que los equipos técnicos quieren "saltar" directamente a analizar datos y construir modelos, pero **sin una comprensión clara del negocio, el proyecto más sofisticado técnicamente puede ser un completo fracaso comercial**.

> **Analogía para estudiantes:** Es como construir una casa. Puedes ser el mejor arquitecto del mundo, pero si no entiendes qué necesita el cliente (¿una casa familiar? ¿un edificio de oficinas? ¿un hotel?), tu diseño perfecto será inútil.

### Aplicación al Caso del Supermercado

Imaginemos que la gerencia del supermercado nos contrata como consultores de minería de datos. Antes de tocar ningún dato, necesitamos realizar las siguientes tareas:

---

### TAREA 1.1: Determinación de los Objetivos Comerciales

#### 1.1.1 Compilar información de la empresa

**En nuestro caso del supermercado:**

- **Estructura organizacional:** Cadena de 3 supermercados en Myanmar (Yangon, Naypyitaw, Mandalay)
- **Stakeholders clave:**
  - Director General de la cadena (patrocinador del proyecto)
  - Gerente de Marketing (usuario principal)
  - Gerente de Operaciones de cada sucursal
  - Jefe de TI (facilitador de acceso a datos)
- **Unidades afectadas:** Marketing, Ventas, Operaciones, Inventario

#### 1.1.2 Describir el área problemática

**Dominio:** Retail / Supermercados

**Problema identificado en términos generales:**
La gerencia observa que las ventas no crecen al ritmo esperado y sospecha que:
- No conocen bien a sus clientes
- Las promociones son genéricas y poco efectivas
- Algunas líneas de productos tienen bajo desempeño
- La satisfacción del cliente varía mucho entre sucursales

**Solución actual:**
- Reportes mensuales básicos de ventas totales por sucursal
- Decisiones basadas en intuición y experiencia del gerente
- Promociones "copiar-pegar" de lo que hace la competencia

**Limitaciones de la solución actual:**
- No identifica patrones de comportamiento del cliente
- No predice tendencias futuras
- No personaliza estrategias por segmento
- Desperdicia recursos en promociones inefectivas

#### 1.1.3 Definir los objetivos comerciales

**Objetivo Principal:**
"Aumentar la rentabilidad del supermercado en un 15% en los próximos 6 meses mediante el uso inteligente de datos de ventas"

**Objetivos Específicos:**

1. **Segmentación de Clientes**
   - Identificar grupos de clientes con comportamientos similares
   - Personalizar estrategias de marketing para cada segmento

2. **Optimización de Líneas de Producto**
   - Identificar qué líneas de producto son más rentables
   - Determinar qué líneas necesitan impulso o eliminación

3. **Análisis de Satisfacción**
   - Identificar factores que influyen en la satisfacción del cliente (Rating)
   - Mejorar experiencia del cliente para aumentar lealtad

4. **Optimización por Sucursal**
   - Comparar desempeño entre sucursales
   - Replicar mejores prácticas de sucursales exitosas

#### 1.1.4 Establecer criterios de éxito del negocio

**Criterios Objetivos:**
- Aumento del 15% en ventas totales en 6 meses
- Incremento del 20% en la tasa de conversión de clientes normales a miembros
- Mejora del rating promedio de 6.5 a 7.5
- Reducción del 10% en inventario de productos de baja rotación

**Criterios Subjetivos:**
- Los gerentes de sucursal adoptan las recomendaciones del modelo
- El equipo de marketing considera útiles los segmentos identificados
- La dirección percibe valor en invertir en análisis de datos

---

### TAREA 1.2: Evaluación de la Situación

#### 1.2.1 Inventario de recursos

**Recursos de Datos:**
- ✅ Sistema de punto de venta (POS) con datos transaccionales
- ✅ Datos históricos de 3 meses (1,000 transacciones)
- ❌ No hay datos de redes sociales o web
- ❌ No hay datos de inventario detallado
- ✅ Datos estructurados en formato CSV

**Recursos de Hardware/Software:**
- Python con pandas, matplotlib, scikit-learn (disponible)
- Computadora con capacidad suficiente para 1,000 registros
- Sin necesidad de infraestructura de big data

**Recursos Humanos:**
- 1 Científico de datos (nosotros)
- Expertos de negocio disponibles para consultas
- Equipo de TI para acceso a datos

#### 1.2.2 Requisitos, supuestos y restricciones

**Requisitos:**
- Modelo debe ser interpretable (gerentes deben entender las recomendaciones)
- Resultados deben entregarse en 2 meses
- Presupuesto: limitado (solo herramientas open source)

**Supuestos:**
- Los datos del POS son precisos y completos
- El comportamiento de clientes en los 3 meses es representativo
- Las condiciones del mercado se mantendrán estables

**Restricciones:**
- ⚠️ **Legal:** Cumplimiento con protección de datos personales (aunque el dataset está anonimizado)
- ⚠️ **Temporal:** Solo 2 meses para el proyecto completo
- ⚠️ **Datos:** Solo 3 meses de historia (ideal sería tener al menos 1 año)
- ⚠️ **Financiera:** Sin presupuesto para herramientas comerciales

#### 1.2.3 Análisis de riesgos y contingencias

| Riesgo | Probabilidad | Impacto | Plan de Contingencia |
|--------|--------------|---------|---------------------|
| Datos insuficientes para algunos análisis | Media | Alto | Limitar alcance del proyecto, enfocarse en análisis descriptivo más que predictivo |
| Datos de mala calidad | Alta | Alto | Incluir fase extendida de limpieza de datos |
| Resistencia al cambio de gerentes | Media | Alto | Workshops de sensibilización, involucrar gerentes desde fase 1 |
| Resultados no generalizables (solo 3 meses) | Alta | Medio | Comunicar claramente las limitaciones, validar con datos futuros |
| Cambios en el mercado durante el proyecto | Baja | Medio | Monitoreo continuo de tendencias externas |

#### 1.2.4 Glosario de términos

Para asegurar comunicación efectiva entre equipo técnico y negocio:

**Términos de Negocio:**
- **Member vs Normal:** Member = cliente con tarjeta de fidelización; Normal = cliente ocasional
- **Product line:** Categoría de productos (6 categorías principales)
- **Branch:** Sucursal física del supermercado
- **Rating:** Calificación de satisfacción del cliente (1-10)
- **COGS:** Cost of Goods Sold = costo de los productos vendidos

**Términos Técnicos:**
- **Clustering:** Agrupación automática de clientes por similitud
- **Segmentación:** División de clientes en grupos con características comunes
- **Variable categórica:** Variable con valores discretos (ej: género, tipo de pago)
- **Variable numérica:** Variable con valores continuos (ej: precio, cantidad)
- **Outlier:** Valor atípico o extremo

#### 1.2.5 Análisis de costes/beneficios

**Costos del Proyecto:**
- Personal (científico de datos): 2 meses × salario
- Herramientas: $0 (software libre)
- Tiempo de gerentes para reuniones: ~20 horas
- **Total estimado:** Principalmente costo de personal

**Beneficios Esperados:**
- Aumento de ventas 15% = $X adicionales
- Reducción de inventario muerto = ahorro de $Y
- Mejora en satisfacción = mayor retención = $Z en valor de vida del cliente
- **Total estimado:** ROI positivo en 6 meses

---

### TAREA 1.3: Determinación de los Objetivos de Minería de Datos

Ahora traducimos los objetivos de negocio en objetivos técnicos de minería de datos:

#### Objetivo de Negocio → Objetivo de Minería de Datos

| Objetivo de Negocio | Tipo de Problema | Objetivo Técnico | Métrica de Éxito |
|---------------------|------------------|------------------|------------------|
| Segmentar clientes para marketing personalizado | **Clustering** (no supervisado) | Agrupar clientes en 3-5 segmentos basados en patrones de compra | Coeficiente de Silhouette > 0.5 |
| Predecir qué clientes se volverán Members | **Clasificación** (supervisado) | Construir modelo que prediga probabilidad de conversión a Member | Accuracy > 75%, Precision > 70% |
| Identificar factores de satisfacción | **Regresión / Análisis** | Modelar Rating en función de otras variables | R² > 0.6 |
| Optimizar mix de productos por sucursal | **Análisis Descriptivo** | Identificar productos top y bottom por sucursal | Reportes claros con recomendaciones accionables |
| Detectar patrones de compra por hora | **Minería de Reglas de Asociación** | Descubrir qué productos se compran juntos y cuándo | Lift > 1.5, Confidence > 60% |

#### Criterios de Rendimiento Técnico

**Para el modelo de clustering:**
- Coeficiente de Silhouette > 0.5
- Los clusters deben ser interpretables (con características claras)
- Cada cluster debe tener al menos 10% del total de clientes

**Para el modelo de clasificación:**
- Accuracy mínima: 75%
- Precision mínima: 70% (para evitar falsos positivos costosos)
- Recall mínimo: 65%
- Matriz de confusión balanceada

**Para el análisis descriptivo:**
- Visualizaciones claras y comprensibles para no-técnicos
- Insights accionables (no solo estadísticas)
- Validación con expertos de negocio

---

### TAREA 1.4: Producción del Plan de Proyecto

#### Cronograma Estimado (8 semanas)

```
Semana 1-2: FASE 1 - Comprensión del Negocio ✓
├── Reuniones con stakeholders
├── Definición de objetivos
└── Aprobación del plan

Semana 2-3: FASE 2 - Comprensión de los Datos
├── Carga de datos
├── Análisis exploratorio (EDA)
├── Verificación de calidad
└── Informe de hallazgos preliminares

Semana 3-4: FASE 3 - Preparación de Datos
├── Limpieza de datos
├── Transformación de variables
├── Ingeniería de características
└── Selección de atributos

Semana 4-6: FASE 4 - Modelado
├── Selección de técnicas
├── Construcción de modelos
├── Evaluación y ajuste
└── Iteración (puede volver a Fase 3)

Semana 7: FASE 5 - Evaluación
├── Evaluación de resultados vs objetivos de negocio
├── Revisión con stakeholders
└── Ajustes finales

Semana 8: FASE 6 - Despliegue
├── Documentación
├── Presentación de resultados
├── Plan de implementación
└── Plan de monitoreo
```

#### Puntos de Decisión Clave

- **Fin de Fase 2:** ¿Los datos son suficientes y de calidad adecuada?
  - SI → Continuar a Fase 3
  - NO → Buscar fuentes adicionales o ajustar objetivos

- **Fin de Fase 4:** ¿El modelo cumple criterios técnicos?
  - SI → Continuar a Fase 5
  - NO → Iterar (volver a Fase 3 o ajustar enfoque)

- **Fin de Fase 5:** ¿El modelo cumple objetivos de negocio?
  - SI → Proceder al despliegue
  - NO → Decisión: ajustar o cancelar proyecto

---

## 🎯 ENTREGABLES DE LA FASE 1

Al finalizar la Fase 1, deberías tener los siguientes documentos:

1. ✅ **Informe de Comprensión del Negocio**
   - Contexto organizacional
   - Problema de negocio detallado
   - Objetivos comerciales SMART

2. ✅ **Inventario de Recursos**
   - Fuentes de datos disponibles
   - Hardware y software
   - Equipo humano

3. ✅ **Análisis de Riesgos y Contingencias**
   - Matriz de riesgos
   - Planes de mitigación

4. ✅ **Glosario de Términos**
   - Términos de negocio y técnicos

5. ✅ **Objetivos de Minería de Datos**
   - Traducción técnica de objetivos
   - Métricas de éxito

6. ✅ **Plan de Proyecto Detallado**
   - Cronograma con hitos
   - Recursos asignados
   - Puntos de decisión

---

## 💡 CONSEJOS PEDAGÓGICOS PARA FASE 1

### Para explicar en clase:

1. **Usa la analogía del médico:**
   - Un médico no receta sin diagnosticar
   - Primero pregunta síntomas, historial, examina
   - Luego ordena exámenes específicos
   - Finalmente diagnostica y receta
   - En minería de datos: Fase 1 = diagnóstico completo del negocio

2. **Ejercicio práctico para estudiantes:**
   - Divide la clase en grupos
   - Cada grupo es una "consultora" contratada por el supermercado
   - Dales 20 minutos para:
     - Listar 5 preguntas que harían al director del supermercado
     - Definir 1 objetivo de negocio SMART
     - Identificar 3 riesgos del proyecto
   - Comparte y discute las respuestas

3. **Errores comunes a destacar:**
   - ❌ "Vamos a hacer clustering porque es interesante"
   - ✅ "El negocio necesita segmentar clientes, clustering es la herramienta adecuada"
   - ❌ "Tenemos estos datos, veamos qué encontramos"
   - ✅ "Necesitamos estos objetivos, busquemos los datos apropiados"

4. **Preguntas para generar discusión:**
   - ¿Por qué es peligroso saltar directo a los datos?
   - ¿Qué pasaría si construimos un modelo perfecto que no resuelve el problema del negocio?
   - ¿Cómo convencerías a un gerente escéptico del valor de invertir tiempo en esta fase?

---

---

## FASE 2: COMPRENSIÓN DE LOS DATOS (Data Understanding)

### ¿Por qué esta fase es crítica?

La Fase 2 es donde finalmente "conocemos" los datos. Es como una primera cita: necesitamos conocer sus características, sus virtudes y sus defectos antes de comprometernos. **El 60-75% de los problemas en proyectos de minería de datos vienen de no entender bien los datos**.

> **Analogía para estudiantes:** Es como conocer a una persona. En la primera conversación descubres su personalidad, sus gustos, sus contradicciones. Si no prestas atención a estas señales, tu relación tendrá problemas después.

### Conexión con Fase 1

Los objetivos definidos en la Fase 1 guían qué buscar en los datos:
- Si queremos segmentar clientes → buscamos variables de comportamiento de compra
- Si queremos predecir satisfacción → nos enfocamos en Rating y sus posibles predictores
- Si queremos optimizar inventario → analizamos Product line y Quantity

---

### TAREA 2.1: Recopilación de Datos Iniciales

#### 2.1.1 Obtener acceso a los datos

**En nuestro caso:**
- ✅ Datos obtenidos del sistema POS del supermercado
- ✅ Exportados en formato CSV (fácil de trabajar)
- ✅ Datos anonimizados (Invoice ID en lugar de nombres de clientes)
- ✅ Período: Enero-Marzo 2019

**Método de obtención:**
```
Fuente: Sistema POS → Exportación manual por TI
Formato: CSV (comma-separated values)
Codificación: UTF-8
Tamaño: 1,000 registros × 17 columnas
```

#### 2.1.2 Caracterización inicial del dataset

**Primera inspección:**
- **Número de registros:** 1,000 transacciones
- **Número de variables:** 17 columnas
- **Tamaño del archivo:** Aproximadamente 150 KB
- **Período temporal:** 3 meses (2019-01-01 a 2019-03-29)

#### 2.1.3 Problemas encontrados y resoluciones

| Problema | Solución Aplicada |
|----------|-------------------|
| Caracteres extraños en primera línea (BOM) | Identificado, se limpiará en Fase 3 |
| Espacios en nombres de columnas | Renombrar columnas en Fase 3 |
| Formato de fecha inconsistente (M/D/YYYY) | Convertir a formato estándar |
| Nombres de ciudades en idioma extranjero | Mantener, son categorías válidas |

#### 2.1.4 Atributos prometedores (primera impresión)

**Muy relevantes para nuestros objetivos:**
- ✨ Customer type (Member/Normal) - clave para segmentación
- ✨ Rating - variable objetivo para análisis de satisfacción
- ✨ Product line - esencial para análisis de productos
- ✨ Sales - métrica principal de negocio
- ✨ Branch/City - para comparaciones geográficas
- ✨ Date/Time - para análisis temporal
- ✨ Payment - comportamiento de pago

**Menos relevantes (pero mantener):**
- Tax 5% y gross margin percentage (constantes)
- cogs (derivado de Sales)
- Invoice ID (identificador único, no aporta patrones)

---

### TAREA 2.2: Descripción de los Datos

#### 2.2.1 Cuantificar los datos

**Dimensiones del dataset:**
- **Registros (filas):** 1,000 transacciones
- **Atributos (columnas):** 17 variables
- **Puntos de datos totales:** 17,000 valores
- **Período:** 88 días (casi 3 meses)
- **Transacciones por día:** Promedio de ~11.4 transacciones/día

#### 2.2.2 Calificar los datos - Diccionario de Variables

| Variable | Tipo | Descripción | Valores Posibles | Rol en Análisis |
|----------|------|-------------|------------------|----------------|
| **Invoice ID** | Categórica (nominal) | Identificador único de factura | Formato: XXX-XX-XXXX | Identificador (no usar en modelos) |
| **Branch** | Categórica (nominal) | Sucursal del supermercado | Alex, Giza, Cairo | Variable independiente |
| **City** | Categórica (nominal) | Ciudad de la sucursal | Yangon, Naypyitaw, Mandalay | Variable independiente |
| **Customer type** | Categórica (binaria) | Tipo de cliente | Member, Normal | Variable independiente **CLAVE** |
| **Gender** | Categórica (binaria) | Género del cliente | Male, Female | Variable independiente |
| **Product line** | Categórica (nominal) | Categoría del producto | 6 categorías | Variable independiente **CLAVE** |
| **Unit price** | Numérica (continua) | Precio por unidad | 10.08 - 99.96 | Variable independiente |
| **Quantity** | Numérica (discreta) | Cantidad comprada | 1 - 10 | Variable independiente |
| **Tax 5%** | Numérica (continua) | Impuesto aplicado (5%) | Calculado: (Unit price × Qty) × 0.05 | Derivada (redundante) |
| **Sales** | Numérica (continua) | Venta total con impuesto | Calculado: cogs + Tax 5% | Variable objetivo / métrica de negocio |
| **Date** | Temporal (fecha) | Fecha de transacción | 2019-01-01 a 2019-03-29 | Variable temporal **CLAVE** |
| **Time** | Temporal (hora) | Hora de transacción | 10:00 AM - 9:00 PM | Variable temporal |
| **Payment** | Categórica (nominal) | Método de pago | Ewallet, Cash, Credit card | Variable independiente |
| **cogs** | Numérica (continua) | Costo de bienes vendidos | Unit price × Quantity | Derivada (redundante) |
| **gross margin %** | Numérica (constante) | Porcentaje de margen bruto | 4.76% (constante) | Constante (no informativa) |
| **gross income** | Numérica (continua) | Ingreso bruto (ganancia) | Calculado: Sales - cogs | Derivada (igual que Tax 5%) |
| **Rating** | Numérica (discreta) | Calificación del cliente | Escala 1-10 (observados: 4.0-10.0) | Variable objetivo **CLAVE** |

#### 2.2.3 Clasificación por tipos de datos

**Variables Numéricas Continuas (6):**
- Unit price, Tax 5%, Sales, cogs, gross income
- **Análisis apropiado:** Estadísticos descriptivos, correlaciones, regresión

**Variables Numéricas Discretas (2):**
- Quantity (1-10), Rating (escala 1-10)
- **Análisis apropiado:** Frecuencias, visualización de distribución

**Variables Categóricas Nominales (6):**
- Invoice ID, Branch, City, Product line, Payment
- **Análisis apropiado:** Tablas de frecuencia, gráficos de barras, chi-cuadrado

**Variables Categóricas Binarias (2):**
- Customer type, Gender
- **Análisis apropiado:** Proporciones, comparaciones entre grupos

**Variables Temporales (2):**
- Date, Time
- **Análisis apropiado:** Series de tiempo, patrones estacionales

**Variables Derivadas/Redundantes (4):**
- Tax 5% = cogs × 0.05
- cogs = Unit price × Quantity
- gross income = Tax 5%
- gross margin % = constante (4.76%)

> **Nota pedagógica:** En la Fase 3 (Preparación de Datos) eliminaremos las variables redundantes para evitar multicolinealidad y simplificar el modelo.

#### 2.2.4 Estadísticos básicos esperados

**Para variables numéricas principales:**

| Variable | Min Esperado | Max Esperado | Media Estimada | Notas |
|----------|--------------|--------------|----------------|-------|
| Unit price | ~$10 | ~$100 | ~$55 | Rango razonable para retail |
| Quantity | 1 | 10 | ~5-6 | Compras típicas de supermercado |
| Sales | ~$10 | ~$1,000 | ~$300 | Depende de precio y cantidad |
| Rating | 4.0 | 10.0 | ~7.0 | Sesgo hacia calificaciones altas |

**Para variables categóricas:**

| Variable | Distribución Esperada |
|----------|-----------------------|
| Branch | Relativamente balanceada (33% cada una aprox.) |
| Customer type | Más Members que Normal (lealtad) o viceversa? |
| Gender | Aproximadamente 50-50 |
| Product line | Desbalanceada (algunos productos más populares) |
| Payment | Distribución a investigar (¿efectivo más común?) |

---

### TAREA 2.3: Exploración de Datos (EDA - Análisis Exploratorio)

Esta es **la tarea más importante de la Fase 2**. Aquí es donde realmente "conversamos" con los datos.

#### 2.3.1 Análisis Univariado (variable por variable)

**Variables numéricas - Preguntas a responder:**

1. **Unit price:**
   - ¿Cuál es la distribución de precios? (¿Normal? ¿Sesgada?)
   - ¿Hay outliers (productos muy caros o muy baratos)?
   - ¿Cuál es el rango de precios más común?

2. **Quantity:**
   - ¿Los clientes compran de 1 en 1 o en mayor cantidad?
   - ¿Hay un patrón (ej: picos en 5, 10)?
   - ¿La mayoría compra poco o mucho?

3. **Sales:**
   - ¿Cuál es el ticket promedio?
   - ¿Hay grandes variaciones en ventas?
   - ¿Distribución normal o sesgada?

4. **Rating:**
   - ¿Los clientes son generosos con las calificaciones?
   - ¿Hay un sesgo hacia valores altos o bajos?
   - ¿La distribución es uniforme o concentrada?

**Herramientas de visualización:**
- Histogramas para ver distribuciones
- Box plots para detectar outliers
- Gráficos de densidad para suavizar distribuciones

**Variables categóricas - Preguntas a responder:**

1. **Branch / City:**
   - ¿Alguna sucursal tiene muchas más transacciones?
   - ¿Hay desbalance significativo?

2. **Customer type:**
   - ¿Qué porcentaje son Members vs Normal?
   - ¿El programa de membresía es exitoso?

3. **Gender:**
   - ¿Hay diferencia en frecuencia de compra por género?

4. **Product line:**
   - ¿Cuáles son las categorías más vendidas?
   - ¿Alguna categoría tiene ventas muy bajas?

5. **Payment:**
   - ¿Cuál es el método de pago preferido?
   - ¿Hay tendencia hacia pagos digitales?

**Herramientas de visualización:**
- Gráficos de barras para frecuencias
- Gráficos de pastel para proporciones
- Tablas de frecuencia

**Variables temporales:**

1. **Date:**
   - ¿Hay tendencia creciente/decreciente en ventas?
   - ¿Hay estacionalidad (días de semana vs fin de semana)?
   - ¿Algún día con pico de ventas (ej: inicio de mes)?

2. **Time:**
   - ¿Cuáles son las horas pico de compra?
   - ¿Hay diferencia entre mañana, tarde, noche?

**Herramientas de visualización:**
- Series de tiempo para Date
- Histograma por hora para Time

#### 2.3.2 Análisis Bivariado (relaciones entre variables)

**Relaciones numéricas - Correlaciones a investigar:**

1. **Unit price vs Quantity:**
   - Hipótesis: ¿Los productos caros se compran en menor cantidad?
   - Método: Gráfico de dispersión + correlación de Pearson

2. **Sales vs Rating:**
   - Hipótesis: ¿Compras grandes están asociadas a mayor satisfacción?
   - Método: Gráfico de dispersión + correlación

3. **Unit price vs Rating:**
   - Hipótesis: ¿Productos caros tienen mejor/peor rating?
   - Método: Gráfico de dispersión

**Relaciones categóricas vs numéricas:**

1. **Customer type vs Sales:**
   - Hipótesis: ¿Los Members gastan más por transacción?
   - Método: Box plot comparativo, prueba t-test

2. **Product line vs Sales:**
   - Hipótesis: ¿Qué categoría genera más ventas por transacción?
   - Método: Box plot por categoría

3. **Branch vs Rating:**
   - Hipótesis: ¿Alguna sucursal tiene mejor satisfacción?
   - Método: Box plot comparativo, ANOVA

4. **Payment vs Sales:**
   - Hipótesis: ¿El método de pago está relacionado con el monto?
   - Método: Box plot por método de pago

5. **Gender vs Product line:**
   - Hipótesis: ¿Hay preferencias de categoría por género?
   - Método: Tabla de contingencia, prueba chi-cuadrado

**Relaciones categóricas vs categóricas:**

1. **Customer type vs Payment:**
   - ¿Los Members usan más métodos digitales?
   - Método: Tabla cruzada, chi-cuadrado

2. **Branch vs Product line:**
   - ¿Cada sucursal tiene mix de productos diferente?
   - Método: Tabla cruzada

**Análisis temporal:**

1. **Date vs Sales:**
   - ¿Tendencia de ventas en el tiempo?
   - Método: Serie de tiempo

2. **Time vs Product line:**
   - ¿Ciertos productos se compran más en ciertas horas?
   - Método: Heatmap hora × categoría

3. **Day of week vs Sales:**
   - ¿Hay días con más ventas?
   - Método: Box plot por día de semana

#### 2.3.3 Análisis Multivariado

**Relaciones complejas a explorar:**

1. **Customer type × Product line × Sales:**
   - ¿Los Members prefieren ciertas categorías y gastan más en ellas?
   - Método: Gráfico de barras agrupadas

2. **Branch × Time × Traffic:**
   - ¿Cada sucursal tiene patrones horarios diferentes?
   - Método: Heatmap múltiple

3. **Gender × Product line × Rating:**
   - ¿La satisfacción varía por género y categoría?
   - Método: Gráfico de facetas

#### 2.3.4 Hipótesis Preliminares (para guiar la Fase 3)

Basándonos en el análisis exploratorio, formulamos hipótesis:

**Hipótesis de Segmentación:**
1. Los clientes Members tienen comportamiento diferente a Normal
2. Se pueden identificar 3-4 segmentos por patrones de compra
3. Hay clientes "high value" (alto ticket, alta frecuencia)

**Hipótesis de Producto:**
1. Algunas líneas de producto son más rentables que otras
2. Ciertas categorías tienen mejor rating
3. Productos caros tienen menor cantidad pero igual/mayor satisfacción

**Hipótesis Temporal:**
1. Hay horas pico de compra (ej: mediodía, tarde)
2. Los fines de semana tienen mayor tráfico
3. Inicio de mes tiene mayores ventas (día de pago)

**Hipótesis de Sucursal:**
1. Cada sucursal tiene características únicas
2. Alguna sucursal tiene mejor desempeño general
3. El mix de productos varía por localidad

> **Nota pedagógica:** Estas hipótesis NO están confirmadas todavía. En la Fase 3 las validaremos con análisis estadístico riguroso.

---

### TAREA 2.4: Verificación de la Calidad de los Datos

Esta tarea es **crucial** porque los problemas de calidad destruyen la validez de cualquier análisis posterior.

#### 2.4.1 Evaluar la Completitud

**Preguntas a responder:**

1. **¿Hay valores faltantes (missing values)?**
   - Revisar cada columna
   - Calcular porcentaje de datos faltantes
   - Identificar patrones (¿faltan al azar o sistemáticamente?)

2. **¿Los datos cubren el período esperado?**
   - Esperábamos: Enero-Marzo 2019 (90 días)
   - Tenemos: 88 días de datos
   - ¿Faltan días completos? ¿Ciertos días de semana?

3. **¿Todas las sucursales están representadas?**
   - ¿Las 3 sucursales tienen similar cantidad de registros?
   - ¿O hay desbalance que deba considerarse?

**Checklist de completitud:**

| Aspecto | Estado | Notas |
|---------|--------|-------|
| Valores faltantes en columnas | ✓ A verificar | Inspección necesaria |
| Cobertura temporal | ✓ 88/90 días | Casi completo |
| Representación de sucursales | ✓ A verificar | Debe ser balanceado |
| Todas las categorías de productos | ✓ 6 categorías presentes | Completo |
| Rango completo de horas | ✓ 10 AM - 9 PM | Horario comercial |

#### 2.4.2 Detectar Errores

**Tipos de errores a buscar:**

1. **Errores de rango:**
   - ¿Hay ratings fuera de 1-10?
   - ¿Hay cantidades negativas o cero?
   - ¿Hay precios negativos o cero?

2. **Errores de consistencia:**
   - Verificar: Sales = cogs + Tax 5%
   - Verificar: cogs = Unit price × Quantity
   - Verificar: Tax 5% = cogs × 0.05
   - Verificar: gross margin % = 4.76% (constante)

3. **Errores tipográficos:**
   - ¿Nombres de ciudades mal escritos?
   - ¿Categorías con typos?
   - ¿Variaciones en nombres (ej: "E-wallet" vs "Ewallet")?

4. **Errores de formato:**
   - ¿Fechas en formato consistente?
   - ¿Horas en formato AM/PM correcto?

**Plan de verificación:**

```python
# Pseudocódigo para verificar calidad

# 1. Valores faltantes
missing_values = dataset.isnull().sum()

# 2. Rango de valores
assert all(Rating >= 1 & Rating <= 10)
assert all(Quantity > 0)
assert all(Unit_price > 0)

# 3. Consistencia matemática
assert all(Sales ≈ cogs + Tax)
assert all(cogs ≈ Unit_price × Quantity)

# 4. Categorías válidas
valid_branches = ['Alex', 'Giza', 'Cairo']
assert all(Branch in valid_branches)
```

#### 2.4.3 Analizar Valores Ausentes (Missing Values)

**Si encontramos valores faltantes:**

| Variable | % Faltante | Acción Sugerida (Fase 3) |
|----------|-----------|--------------------------|
| Rating | <5% | Imputar con mediana o eliminar filas |
| Product line | <1% | Eliminar filas (crítico para análisis) |
| Gender | 5-10% | Crear categoría "Unknown" o imputar con moda |
| Payment | <1% | Eliminar filas |
| Cualquier numérica | <5% | Imputar con mediana del grupo |

**Patrones de datos faltantes:**
- ¿Faltan al azar (MCAR - Missing Completely At Random)?
- ¿Faltan por alguna razón (MAR - Missing At Random)?
- ¿Hay patrón sistemático (MNAR - Missing Not At Random)?

Ejemplo: Si Rating falta más en sucursal Cairo → patrón sistemático → investigar causa

#### 2.4.4 Identificar Valores Fuera de Rango (Outliers)

**Outliers NO siempre son errores**, pueden ser:
- **Errores de medición:** Price = $0.01 (probablemente error)
- **Valores legítimos extremos:** Sale = $950 (compra grande válida)
- **Datos especiales:** Promociones, devoluciones

**Método de detección:**

1. **Método estadístico (IQR - Rango Intercuartílico):**
   - Calcular Q1 (percentil 25) y Q3 (percentil 75)
   - IQR = Q3 - Q1
   - Outliers: valores < Q1 - 1.5×IQR o > Q3 + 1.5×IQR

2. **Método visual:**
   - Box plots para cada variable numérica
   - Los puntos fuera de los "bigotes" son outliers potenciales

3. **Método basado en dominio:**
   - Unit price > $100 → revisar (¿artículo de lujo?)
   - Quantity > 10 → revisar (¿compra institucional?)
   - Rating = 1 → revisar (¿cliente muy insatisfecho?)

**Decisiones sobre outliers (para Fase 3):**
- ✅ Mantener: Si son valores legítimos y raros
- 🔧 Transformar: Aplicar log o winsorización
- ❌ Eliminar: Si son errores claros y pocos

#### 2.4.5 Evaluar Consistencia

**Aspectos de consistencia:**

1. **Formatos:**
   - Fechas: todas en M/D/YYYY
   - Horas: todas en formato 12h con AM/PM
   - Nombres: capitalización consistente

2. **Escalas:**
   - Rating: escala 1-10 (o 0-10?)
   - Precios: en misma moneda

3. **Relaciones lógicas:**
   - Si Branch = "Alex" → City debe ser "Yangon"
   - Si Branch = "Giza" → City debe ser "Naypyitaw"
   - Si Branch = "Cairo" → City debe ser "Mandalay"

4. **Cardinalidad esperada:**
   - 1,000 Invoice IDs únicos (si no hay devoluciones)
   - 3 Branches únicos
   - 3 Cities únicas
   - 6 Product lines únicos
   - 3 Payment methods únicos
   - 2 Customer types únicos
   - 2 Genders únicos

---

## 🎯 ENTREGABLES DE LA FASE 2

Al finalizar la Fase 2, deberías tener:

1. ✅ **Informe de Recopilación de Datos Iniciales**
   - Descripción de fuentes
   - Métodos de obtención
   - Problemas encontrados y resoluciones

2. ✅ **Informe de Descripción de Datos**
   - Diccionario de variables completo
   - Dimensiones del dataset
   - Tipos de datos
   - Estadísticos descriptivos básicos

3. ✅ **Informe de Exploración de Datos (EDA)**
   - Visualizaciones clave (20-30 gráficos)
   - Análisis univariado de todas las variables
   - Análisis bivariado de relaciones importantes
   - Hipótesis preliminares formuladas
   - Insights iniciales

4. ✅ **Informe de Calidad de Datos**
   - Reporte de valores faltantes
   - Identificación de outliers
   - Errores detectados
   - Problemas de consistencia
   - Recomendaciones para Fase 3

5. ✅ **Dashboard Exploratorio** (opcional pero recomendado)
   - Visualizaciones interactivas
   - Filtros por sucursal, fecha, categoría
   - Métricas clave del negocio

---

## 🔄 INTERACCIÓN ENTRE FASE 1 Y FASE 2

### Retroalimentación Fase 2 → Fase 1

Durante la exploración de datos, podrías descubrir:

**Escenario 1: Datos insuficientes**
- **Descubrimiento:** Solo 1,000 transacciones en 3 meses = ~11 transacciones/día
- **Impacto:** Puede ser insuficiente para modelos predictivos complejos
- **Acción:** Volver a Fase 1, ajustar objetivos o solicitar más datos históricos

**Escenario 2: Variables clave faltantes**
- **Descubrimiento:** No hay información de productos específicos, solo categorías
- **Impacto:** No podemos hacer análisis de canasta de mercado a nivel producto
- **Acción:** Volver a Fase 1, ajustar alcance del proyecto

**Escenario 3: Problemas de calidad graves**
- **Descubrimiento:** 30% de ratings faltantes, inconsistencias en fechas
- **Impacto:** Análisis de satisfacción no será confiable
- **Acción:** Volver a Fase 1, revisar inventario de recursos, buscar fuentes alternativas

**Escenario 4: Descubrimientos inesperados**
- **Descubrimiento:** Hay patrón claro de compras por hora del día
- **Impacto:** Oportunidad para nuevo objetivo de negocio (optimizar staffing)
- **Acción:** Volver a Fase 1, añadir objetivo nuevo al proyecto

### Flujo Fase 1 → Fase 2

Los objetivos de Fase 1 guían el EDA:

| Objetivo de Negocio (Fase 1) | Enfoque en EDA (Fase 2) |
|------------------------------|-------------------------|
| Segmentar clientes | Analizar Customer type, Product line, Sales, Payment patterns |
| Predecir satisfacción | Explorar distribución de Rating y sus correlaciones |
| Optimizar inventario | Analizar Product line vs Sales, identificar categorías top/bottom |
| Comparar sucursales | Comparar Branch en todas las métricas clave |
| Análisis temporal | Explorar Date y Time, buscar estacionalidad |

---

## 💡 CONSEJOS PEDAGÓGICOS PARA FASE 2

### Estrategias para explicar EDA en clase:

1. **Usa la metáfora del detective:**
   - Los datos son la "escena del crimen"
   - El científico de datos es el detective
   - Cada gráfico es una "pista"
   - El EDA es la "investigación preliminar"
   - No sacamos conclusiones finales, solo hipótesis

2. **Ejercicio práctico con el dataset:**
   - Da a los estudiantes 5 filas del CSV
   - Pídeles que identifiquen:
     - ¿Qué variables son categóricas vs numéricas?
     - ¿Qué variables son redundantes?
     - ¿Qué 3 gráficos harías primero?
     - ¿Qué pregunta de negocio responderían?

3. **Demostración en vivo:**
   - Carga el CSV en Python/R en clase
   - Haz un análisis exploratorio en tiempo real
   - Comenta en voz alta tu proceso de pensamiento
   - Muestra errores y cómo los corriges
   - Esto desmitifica el proceso

4. **Galería de horrores (errores comunes):**
   - Mostrar ejemplos de gráficos mal hechos
   - Enseñar a detectar problemas de calidad
   - Casos reales de proyectos que fallaron por mala calidad de datos

### Preguntas para generar discusión:

1. **Sobre exploración:**
   - ¿Por qué no podemos saltar directo a construir modelos?
   - ¿Qué pasaría si ignoramos outliers sin investigar?
   - ¿Cómo sabes cuándo has explorado "suficiente"?

2. **Sobre calidad:**
   - ¿Es peor tener datos faltantes o datos incorrectos? ¿Por qué?
   - ¿Deberías eliminar o imputar valores faltantes? Depende de qué?
   - ¿Un outlier es siempre un error?

3. **Sobre hipótesis:**
   - ¿Cuál es la diferencia entre una hipótesis y una conclusión?
   - ¿Por qué formular hipótesis en Fase 2 si las validamos en Fase 4?
   - ¿Cómo evitas el sesgo de confirmación en EDA?

### Ejercicios para estudiantes:

**Ejercicio 1: Detective de Calidad (15 min)**
- Da un CSV pequeño con 5 errores plantados
- Los estudiantes deben encontrar todos los errores
- Discutir métodos de detección

**Ejercicio 2: Galería de Gráficos (20 min)**
- Da el dataset del supermercado
- Cada grupo crea 3 visualizaciones diferentes
- Presenta y explica qué insight revela cada una
- Vota por la más informativa

**Ejercicio 3: Formulación de Hipótesis (15 min)**
- Basándose en el diccionario de variables (sin ver datos)
- Cada grupo formula 5 hipótesis sobre relaciones entre variables
- Ejemplo: "Los Members gastan más que los Normal"
- Luego verifican con los datos reales

**Ejercicio 4: Plan de EDA (20 min)**
- Dado un nuevo objetivo de negocio
- Los estudiantes diseñan un plan de exploración:
  - ¿Qué variables analizarían primero?
  - ¿Qué gráficos crearían?
  - ¿Qué relaciones investigarían?
  - ¿Qué checks de calidad harían?

---

## 📊 EJEMPLO DE FLUJO COMPLETO FASE 1 → FASE 2

### CASO: "Aumentar conversión de clientes Normal a Members"

**FASE 1 - Comprensión del Negocio:**

1. **Objetivo de Negocio:**
   - Aumentar membresías en 20% en 6 meses
   - Aumentar gasto promedio de miembros en 10%

2. **Objetivo de Minería de Datos:**
   - Construir modelo de clasificación: ¿Qué diferencia a Members de Normal?
   - Identificar características de "high-potential Normal customers"

3. **Métricas de Éxito:**
   - Precision > 70% (evitar falsos positivos)
   - Modelo debe identificar top 20% de clientes Normal con mayor potencial

**FASE 2 - Comprensión de los Datos:**

1. **Recopilación:**
   - ✅ Variable objetivo: Customer type (Member/Normal)
   - ✅ Features potenciales: Sales, Product line, Payment, Rating, Quantity

2. **Exploración dirigida por objetivo:**
   - Comparar Members vs Normal en:
     - Sales promedio (¿Members gastan más?)
     - Frecuencia de compra (si tuviéramos dato)
     - Product line preferido (¿diferentes gustos?)
     - Rating promedio (¿Members más satisfechos?)
     - Payment method (¿Members usan más digital?)

3. **Hipótesis clave a validar:**
   - H1: Members tienen mayor ticket promedio
   - H2: Members compran más en ciertas categorías
   - H3: Members dan mejores ratings
   - H4: Members prefieren pagos digitales

4. **Hallazgo que afecta Fase 1:**
   - **Problema:** Solo tenemos Customer type en el momento de compra
   - **Implicación:** No podemos predecir conversión futura, solo caracterizar diferencias actuales
   - **Acción:** Volver a Fase 1, ajustar objetivo a "Caracterizar clientes Member para campañas dirigidas" en lugar de "Predecir conversión"

---

## 🎓 RESUMEN EJECUTIVO PARA ESTUDIANTES

### Checklist de supervivencia CRISP-DM Fases 1 y 2:

**FASE 1 - ¿Qué preguntas respondo?**
- ✅ ¿Qué quiere lograr el negocio?
- ✅ ¿Cómo se mide el éxito?
- ✅ ¿Qué recursos tengo?
- ✅ ¿Qué riesgos existen?
- ✅ ¿Cómo traduzco esto a un problema técnico?

**FASE 2 - ¿Qué preguntas respondo?**
- ✅ ¿Qué datos tengo realmente?
- ✅ ¿Cómo son estos datos (tipos, distribuciones)?
- ✅ ¿Qué relaciones existen entre variables?
- ✅ ¿Qué problemas de calidad tengo?
- ✅ ¿Los datos son suficientes para mis objetivos?

### Errores mortales a evitar:

**En Fase 1:**
- ❌ Definir objetivos vagos ("mejorar las ventas")
- ❌ No involucrar stakeholders del negocio
- ❌ Ignorar restricciones y riesgos
- ❌ No traducir objetivos de negocio a técnicos

**En Fase 2:**
- ❌ No hacer EDA completo (ir directo a modelar)
- ❌ Ignorar problemas de calidad de datos
- ❌ No verificar si los datos soportan los objetivos
- ❌ No documentar hallazgos y supuestos

### Señales de que lo estás haciendo bien:

**Fase 1:**
- ✅ Puedes explicar el proyecto a tu abuela
- ✅ Los stakeholders están de acuerdo con los objetivos
- ✅ Tienes métricas concretas de éxito
- ✅ Has identificado al menos 3 riesgos principales

**Fase 2:**
- ✅ Entiendes cada variable del dataset
- ✅ Has creado al menos 10-15 visualizaciones
- ✅ Has encontrado al menos 3 insights interesantes
- ✅ Sabes qué problemas de calidad debes arreglar en Fase 3
- ✅ Has confirmado que los datos soportan los objetivos (o has ajustado objetivos)

---

## 📚 RECURSOS ADICIONALES PARA LA CLASE

### Datasets alternativos para practicar:
1. **Titanic** (clasificación: supervivencia)
2. **Iris** (clustering: especies de flores)
3. **Housing prices** (regresión: predicción de precios)
4. **Netflix movies** (análisis exploratorio)

### Herramientas recomendadas:
- **Python:** pandas, matplotlib, seaborn, plotly
- **R:** ggplot2, dplyr, tidyr
- **Visualización:** Tableau Public, Power BI
- **Notebooks:** Jupyter, Google Colab (gratis)

### Lecturas complementarias:
1. Manual CRISP-DM oficial de IBM
2. "R for Data Science" - Hadley Wickham
3. "Python for Data Analysis" - Wes McKinney
4. "Data Science for Business" - Provost & Fawcett

---

## 🎯 CONCLUSIÓN

Las Fases 1 y 2 de CRISP-DM son los **cimientos** de cualquier proyecto exitoso de minería de datos:

- **Fase 1** asegura que construyas la casa correcta
- **Fase 2** asegura que la construyas en terreno sólido

El tiempo invertido aquí NO es tiempo perdido, es una **inversión** que:
- Previene retrabajo costoso
- Aumenta la probabilidad de éxito
- Genera confianza con stakeholders
- Produce insights valiosos desde el inicio

**Recuerda:** Un modelo perfecto que responde la pregunta equivocada es inútil. Un modelo imperfecto que resuelve el problema correcto es valioso.

---

## 📝 NOTAS PARA EL PROFESOR

### Timing sugerido para la clase (2 horas):

**Primera hora: Fase 1**
- 0:00-0:15: Introducción a CRISP-DM y presentación del caso
- 0:15-0:30: Explicación de Fase 1 con ejemplos del supermercado
- 0:30-0:45: Ejercicio grupal: definir objetivos de negocio
- 0:45-1:00: Discusión de resultados y Q&A

**Segunda hora: Fase 2**
- 1:00-1:15: Explicación de Fase 2 y EDA
- 1:15-1:30: Demostración en vivo con el dataset
- 1:30-1:45: Ejercicio: identificar problemas de calidad
- 1:45-2:00: Resumen, conexión entre fases, próximos pasos

### Materiales a preparar:
- ✅ Proyector con Jupyter Notebook
- ✅ CSV del supermercado compartido con estudiantes
- ✅ Plantillas de documentos de Fase 1 y 2
- ✅ Ejemplos de buenos y malos gráficos
- ✅ Quiz rápido para evaluación

### Evaluación sugerida:
- **Tarea 1:** Análisis de Fase 1 para un caso de negocio
- **Tarea 2:** EDA completo con visualizaciones y reporte
- **Proyecto integrador:** Fases 1-6 completas en un dataset real

---

**¡Éxito en tu clase!** 🎓📊

*Este reporte fue diseñado como guía pedagógica práctica para enseñar CRISP-DM con un caso real contextualizado.*
