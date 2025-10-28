# Guía Pedagógica: Dataset Telco Customer Churn bajo CRISP-DM

## Resumen Ejecutivo

El dataset **Telco Customer Churn** de Kaggle es un recurso pedagógico excepcional para enseñar minería de datos bajo la metodología CRISP-DM. Contiene 7,043 clientes y 21 características que permiten trabajar de manera estructurada y realista a través de todas las fases del ciclo de minería de datos.

---

## 1. DESCRIPCIÓN GENERAL DEL DATASET

### Estructura Básica
- **Registros**: 7,043 clientes
- **Características**: 21 variables (20 predictoras + 1 variable objetivo)
- **Variable Objetivo**: Churn (cliente se fue o se quedó)
- **Contexto**: Compañía de telecomunicaciones en California
- **Desbalance de clases**: ~73.5% sin abandono vs ~26.5% con abandono

### Tipos de Características

**Variables Demográficas:**
- Gender (género)
- SeniorCitizen (es adulto mayor)
- Partner (tiene pareja)
- Dependents (tiene dependientes)

**Variables de Cuenta:**
- Tenure (meses como cliente)
- Contract (tipo de contrato: mes-a-mes, un año, dos años)
- MonthlyCharges (cargos mensuales)
- TotalCharges (cargos totales)
- PaymentMethod (método de pago)
- PaperlessBilling (facturación sin papel)

**Servicios Suscritos:**
- PhoneService (servicio telefónico)
- MultipleLines (líneas múltiples)
- InternetService (tipo: DSL, Fiber optic, No)
- OnlineSecurity (seguridad en línea)
- OnlineBackup (respaldo en línea)
- DeviceProtection (protección de dispositivo)
- TechSupport (soporte técnico)
- StreamingTV (streaming de TV)
- StreamingMovies (streaming de películas)

---

## 2. FORTALEZAS PEDAGÓGICAS POR FASE CRISP-DM

### FASE 1: COMPRENSIÓN DEL NEGOCIO

#### Objetivos Pedagógicos
- Conectar problemas empresariales reales con análisis de datos
- Entender la importancia estratégica de la retención de clientes
- Formular preguntas de negocio que impulsen el análisis

#### Actividades Sugeridas

**Caso de Negocio:**
"Una compañía de telecomunicaciones ha notado que está perdiendo clientes regularmente. Esto impacta directamente el ingresos recurrente. ¿Cuáles son los patrones de abandono? ¿Qué características predicen mejor quién va a irse? ¿Cómo podemos diseñar estrategias de retención específicas?"

**Preguntas Clave para Estudiantes:**
1. ¿Por qué es importante predecir el churn para una empresa de telecomunicaciones?
2. ¿Cuál es el costo de perder un cliente vs. el costo de retenerlo?
3. ¿Qué estrategias empresariales podríamos implementar si sabemos quién va a dejar el servicio?
4. ¿Cuáles son los objetivos específicos de minería de datos que derivan del objetivo empresarial?

**Proyección de Valor:**
- Calcular el costo estimado de churn (p. ej., si se pierde el 26.5% de clientes mensualmente y cada cliente genera $X de ingresos)
- Proyectar el valor de una reducción del 5%, 10%, 15% en tasa de churn

---

### FASE 2: COMPRENSIÓN DE LOS DATOS

#### Por Qué Este Dataset es Ideal

1. **Complejidad Realista**: Mezcla datos numéricos, categóricos ordinales y nominales
2. **Calidad Relativa**: Pocas valores faltantes (~0.16% en TotalCharges), lo que permite enfocarse en patrones vs. limpieza extrema
3. **Multicolinealidad Interesante**: Tenure, MonthlyCharges y TotalCharges están correlacionados, lo que genera discusiones valiosas
4. **Distribuciones Variadas**: Algunos features tienen distribuciones simétricas, otros sesgadas

#### Actividades Sugeridas

**Exploración Inicial (Laboratorio 1)**
```python
# Estudiantes deben realizar:
- Cargar el dataset
- Visualizar primeras 5 filas
- Obtener info() sobre tipos de datos
- Calcular describe() para estadísticas básicas
- Contar valores nulos
```

**Análisis Univariado (Laboratorio 2)**
- **Distribuciones Numéricas**: Histogramas y box plots de tenure, monthly/total charges
  - Insight: El tenure tiene distribución bimodal (muchos clientes nuevos que se van + clientes leales)
  - Insight: MonthlyCharges y TotalCharges siguen distribuciones diferentes (precios no uniformes)

- **Distribuciones Categóricas**: Gráficos de barras para cada variable
  - Insight: ~55% tiene contratos mes-a-mes vs. ~24% tiene dos años
  - Insight: Fibra óptica representa ~44% de clientes de internet

**Análisis Bivariado (Laboratorio 3)**
- Visualizar relación entre cada feature y Churn
  - **Tenure vs Churn**: Gráfico de densidad muestra separación clara. Clientes que se van tienen tenure bajo
  - **Contract vs Churn**: Churn rate muy diferente por tipo de contrato (mes-a-mes ~42%, dos años ~11%)
  - **InternetService vs Churn**: Fibra óptica tiene mayor churn (~42%) vs DSL (~19%)
  - **TechSupport vs Churn**: Sin tech support ~30% churn vs con tech support ~15%
  - **OnlineBackup vs Churn**: Sin backup ~29% churn vs con backup ~12%

**Matriz de Correlación**
- Generar correlación de todas variables numéricas
- Identificar alta correlación entre Tenure-Contract, MonthlyCharges-OnlineSecurity, etc.
- Discutir implicaciones para modelado (multicolinealidad)

---

### FASE 3: PREPARACIÓN DE DATOS

#### Desafíos Pedagógicos Únicos

**1. Manejo de Valores Faltantes**
- TotalCharges tiene 11 valores vacíos (0.16%)
- Oportunidad pedagógica: Discutir por qué ocurre, qué estrategia es mejor (eliminar vs. imputar)

**2. Conversión de Tipos de Datos**
- TotalCharges se importa como string (debido a valores vacíos)
- Necesita conversión a numérico
- Enseña sobre cuidados al importar datos

**3. Codificación de Variables Categóricas**
- One-hot encoding para servicios (OnlineSecurity, TechSupport, etc.)
- Label encoding para variables ordinales (Contract, InternetService)
- Discusión: ¿Cuándo usar cada método?

**4. Escalamiento de Variables**
- MonthlyCharges vs Tenure tienen rangos muy diferentes
- Oportunidad para enseñar normalization/standardization
- Impacto en algoritmos basados en distancia (KNN, KMeans)

**5. Tratamiento del Desbalance de Clases**
- ~26.5% churn vs ~73.5% no churn
- Enseñar técnicas: oversampling, undersampling, SMOTE, ADASYN
- Generar dataset balanceado (50-50) vs. usar pesos en algoritmos

#### Laboratorios Sugeridos

**Laboratorio 4: Limpieza Básica**
```
- Eliminar columnas no relevantes (CustomerID)
- Manejar valores faltantes en TotalCharges
- Verificar y corregir tipos de datos
```

**Laboratorio 5: Feature Engineering**
```
- Crear "AverageMonthlyCharges" = TotalCharges / Tenure
- Crear categoría de "cliente nuevo" (tenure < 6 meses)
- Crear categoría de "cliente leal" (tenure > 24 meses)
```

**Laboratorio 6: Codificación y Escalamiento**
```
- One-hot encoding de variables categóricas
- Standardscaler para variables numéricas
- Visualizar antes/después del escalamiento
```

---

### FASE 4: MODELADO

#### Por Qué Este Dataset Permite Múltiples Enfoques

Este dataset es perfecto para comparar algoritmos:

**Modelos Simples (para enseñar fundamentos)**
- **Logistic Regression**: Interpretable, baseline sólido
  - Accuracy típica: ~80%
  - Ventaja pedagógica: Coeficientes muestran impact de cada variable

- **Decision Trees**: Fácil de visualizar y entender
  - Accuracy típica: ~78-82%
  - Ventaja pedagógica: Feature importance es intuitiva

**Modelos Complejos (para avanzados)**
- **Random Forest**: Ensemble, mejor accuracy
  - Accuracy típica: ~83-85%
  - Ventaja pedagógica: Feature importance más robusta

- **XGBoost/LightGBM**: State-of-the-art para tabular
  - Accuracy típica: ~85-87%
  - Ventaja pedagógica: Trade-off interpretabilidad vs. performance

#### Laboratorios Sugeridos

**Laboratorio 7: Preparar Datos para Modelado**
```
- Split train/test (80-20)
- Crear X (features) e y (target)
- Aplicar transformaciones solo en training set
```

**Laboratorio 8: Logistic Regression Baseline**
```
- Entrenar modelo simple
- Obtener coeficientes y discutir interpretación
- Generar matriz de confusión y ROC-AUC
- Calcular precision, recall, F1-score
```

**Laboratorio 9: Comparar Múltiples Algoritmos**
```
- Entrenar Decision Tree, Random Forest, XGBoost
- Comparar métricas de rendimiento
- Analizar feature importance de cada modelo
```

**Laboratorio 10: Optimización de Hiperparámetros**
```
- GridSearch/RandomSearch para Random Forest
- Validación cruzada (5-fold o 10-fold)
- Graficar curvas de learning
```

---

### FASE 5: EVALUACIÓN

#### Métricas Clave para Este Dataset

**Problema de Clasificación Desbalanceado:**

1. **Accuracy**: Engañoso aquí (73.5% baseline si predice "No Churn" siempre)
   - Métrica a usar: Importante pero insuficiente

2. **Precision**: De los que predije como "Churn", ¿cuántos realmente churned?
   - Costo de falso positivo: recursos de retención gastados en error
   - Métrica crítica

3. **Recall**: De todos los que realmente churned, ¿cuántos identifiqué?
   - Costo de falso negativo: pierdo clientes que podría haber retenido
   - Métrica crítica

4. **F1-Score**: Balance entre precision y recall
   - Métrica de resumen útil

5. **ROC-AUC**: Curva ROC vs. clasificador aleatorio
   - Métrica robusta a desbalance
   - Interpretable: probabilidad que el modelo rankea un positivo más alto que un negativo

6. **Matriz de Confusión**: Visualización clara de TP, FP, TN, FN
   - Facilita cálculo de precision, recall

#### Laboratorios Sugeridos

**Laboratorio 11: Evaluación Exhaustiva**
```python
from sklearn.metrics import (
    classification_report, confusion_matrix, 
    roc_auc_score, roc_curve, precision_recall_curve
)

# Generar reporte completo
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Graficar ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
```

**Laboratorio 12: Análisis de Trade-offs**
```
- Visualizar matriz de confusión para cada modelo
- Calcular costo empresarial: 
  - Falso positivo = $X en recursos de retención
  - Falso negativo = $Y en ingresos perdidos
- Seleccionar threshold óptimo basado en costos reales
```

**Laboratorio 13: Validación Cruzada y Generalizacion**
```
- Comparar performance en train vs. test
- Usar cross-validation para estimar varianza
- Graficar learning curves (train size vs. score)
```

---

### FASE 6: DESPLIEGUE

#### Aplicaciones Prácticas

**1. Scoring de Riesgo de Churn**
```
- Para cada cliente en production, generar probabilidad de churn
- Segmentar en categorías: Alto riesgo (>70%), Medio (40-70%), Bajo (<40%)
- Priorizar acciones de retención por riesgo
```

**2. Explicabilidad para Stakeholders**
```
- "Cliente X tiene 68% probabilidad de churn porque:"
  - Tiene contrato mes-a-mes
  - No tiene tech support
  - Recientemente aumentaron sus charges
- Generar recomendaciones personalizadas de retención
```

**3. Análisis de Rentabilidad**
```
- Estimar Customer Lifetime Value (CLV) para cada cliente
- Calcular ROI de intervenciones de retención
- Identificar clientes "no vale la pena retener" (bajo CLV)
```

#### Laboratorios Sugeridos

**Laboratorio 14: Construir Pipeline de Producción**
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('rf', RandomForestClassifier(n_estimators=100))
])

pipeline.fit(X_train, y_train)
# Guardar para usar en producción
import joblib
joblib.dump(pipeline, 'churn_model.pkl')
```

**Laboratorio 15: Crear Dashboard de Monitoreo**
```
- Visualizar distribución de scores de churn
- Monitorear drift (cambios en distribución de features)
- Rastrear performance del modelo en tiempo real
- Alertar si accuracy cae por debajo de umbral
```

**Laboratorio 16: Documentar Hallazgos**
```
- Resumen ejecutivo: ¿Qué aprendimos?
- Key insights: Top 5 factores de churn
- Recomendaciones: Qué hacer para reducir churn
- Limitaciones: Qué el modelo no puede predecir
```

---

## 3. HALLAZGOS ESPERADOS (PARA ENSEÑANZA)

### Factores Fuertemente Correlacionados con Churn

| Factor | Efecto | Odds Ratio |
|--------|--------|-----------|
| Contrato Mes-a-Mes | +++ (muy positivo) | 4.06x vs. 2-años |
| Internet Fibra Óptica | ++ (positivo) | 2.31x vs. DSL |
| Tenure Bajo (<6 meses) | +++ (muy positivo) | 8-10x vs. 2+ años |
| Sin Tech Support | ++ (positivo) | ~2x con support |
| Sin Online Security | ++ (positivo) | ~2x con security |
| Sin Online Backup | ++ (positivo) | ~2x con backup |
| Cargos Mensuales Altos | + (moderado) | Correlación positiva |
| Sin Internet Service | --- (muy negativo) | 0.5x con DSL |
| Ser Adulto Mayor | + (moderado) | 1.3x vs. joven |

### Hallazgos Contra-Intuitivos para Discusión

1. **Paradoja de Fibra Óptica**: Tecnología mejor (fibra) pero mayor churn
   - Pregunta: ¿Por qué?
   - Posibles respuestas: problemas de instalación, precio alto vs. perceived value, problemas de servicio
   - Lección: Mejor tecnología ≠ mejor retención. Importa la experiencia del cliente

2. **Efecto Protector del "No Internet Service"**
   - Clientes sin internet tienen MENOS churn que con DSL/Fibra
   - Pregunta: ¿Qué significa esto?
   - Posible respuesta: Clientes satisfechos con servicio telefónico únicamente tienen menos razón para irse
   - Lección: Contexto importa. No todos los servicios benefician a todos los clientes

3. **Primeros 6 Meses Críticos**
   - La mayoría de churns ocurren en los primeros 6 meses
   - Pregunta: ¿Cómo debería cambiar la estrategia?
   - Implicación: Inversión en onboarding, support inicial, contratos iniciales

---

## 4. PREGUNTAS DE INVESTIGACIÓN PROGRESIVAS

### Nivel Principiante (Fases 1-2)
1. ¿Cuál es la tasa de churn general?
2. ¿Cuál es la edad promedio de un cliente que abandona?
3. ¿Qué tipos de contrato son más comunes?
4. ¿Hay diferencia de churn entre géneros?

### Nivel Intermedio (Fases 3-4)
5. ¿Qué combinación de servicios predicen mejor el churn?
6. ¿Cuál es la edad de clientes con mayor riesgo de abandono?
7. ¿Cuánto tiempo tarda típicamente en abandonar a alguien con contrato mes-a-mes?
8. ¿Cómo varía el churn según la combinación de internet service + tech support?

### Nivel Avanzado (Fases 5-6)
9. ¿Podemos segmentar clientes en perfiles con diferentes patrones de churn?
10. ¿Cuál sería el ROI de ofrecer descuentos a alto-riesgo de churn?
11. ¿Cómo cambiaría nuestro modelo si agregamos datos de satisfacción del cliente (NPS)?
12. ¿Podemos predecir cuándo específicamente va a irse un cliente?

---

## 5. VARIANTES PEDAGÓGICAS

### Variante A: Enfoque Incremental (Recomendado para Principiantes)
- Semana 1: Fases 1-2 (Negocio y Exploración)
- Semana 2: Fase 3 (Limpieza y Preparación)
- Semana 3: Fase 4 (Modelado Simple: Logistic Regression)
- Semana 4: Fase 5 (Evaluación, Comparación con Baselines)
- Semana 5: Fase 6 (Despliegue, Storytelling)

### Variante B: Enfoque Comparativo (Para Avanzados)
- Dividir clase en 3 grupos
- Grupo A: Logistic Regression
- Grupo B: Decision Trees + Random Forest
- Grupo C: XGBoost + LightGBM
- Fin: Comparar resultados, debatir trade-offs

### Variante C: Enfoque de Proyecto Real
- Simular que son "data scientists" contratados por la telco
- Entregar dataset sin decir que es "churn"
- Ellos deben formular preguntas (Fase 1)
- Presentar hallazgos y recomendaciones finales

### Variante D: Enfoque de Desbalance (Avanzado)
- Especializar en técnicas para datasets desbalanceados
- Comparar: no hacer nada vs. oversampling vs. undersampling vs. SMOTE vs. class_weight
- Medir impacto en precision/recall

---

## 6. RECURSOS Y CÓDIGO EJEMPLO

### Importar Dataset
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(f"Dataset shape: {df.shape}")
print(df.info())
print(df['Churn'].value_counts())
```

### Análisis Exploratorio Básico
```python
# Churn rate general
churn_rate = (df['Churn'] == 'Yes').sum() / len(df)
print(f"Churn rate: {churn_rate:.2%}")

# Visualizar distribución
sns.countplot(x='Churn', data=df)
plt.title('Distribución de Churn')

# Comparar Tenure por Churn
sns.histplot(data=df, x='tenure', hue='Churn', kde=True)
plt.title('Distribución de Tenure por Churn')
```

### Pipeline Básico de Modelado
```python
# Preparar datos
X = df.drop(['customerID', 'Churn'], axis=1)
y = (df['Churn'] == 'Yes').astype(int)

# Codificar categóricas
X_encoded = pd.get_dummies(X, drop_first=True)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42
)

# Escalar
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Entrenar modelos
lr = LogisticRegression()
lr.fit(X_train_scaled, y_train)

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Evaluar
print("Logistic Regression")
print(classification_report(y_test, lr.predict(X_test_scaled)))
print("\nRandom Forest")
print(classification_report(y_test, rf.predict(X_test)))
```

---

## 7. MÉTRICAS DE ÉXITO PEDAGÓGICO

### Para Estudiantes
- ✓ Entender por qué cada fase CRISP-DM es necesaria
- ✓ Practicar toma de decisiones en preparación de datos
- ✓ Comparar múltiples algoritmos y entender trade-offs
- ✓ Comunicar resultados a audiencias no-técnicas
- ✓ Reconocer que mejor accuracy ≠ mejor solución

### Para Instructores
- ✓ Transición suave de teoría a aplicación
- ✓ Estudiantes pueden ver resultados tangibles rápidamente
- ✓ Muchos "momentos "aha"" donde intuición se confirma cuantitativamente
- ✓ Debate natural sobre trade-offs y ética (¿segmentamos por edad?)

---

## 8. EXTENSIONES Y CAMINOS AVANZADOS

### Análisis RFM (Recency, Frequency, Monetary)
```
- Recency: Cuándo fue última actividad
- Frequency: Con qué frecuencia interactúa
- Monetary: Cuánto gastan
- Segmentar clientes y ver perfiles de churn por segmento
```

### Ingeniería de Features Temporal
```
- Si tuviéramos datos históricos: tendencia de charges (up/down)
- Cambios recientes en servicios
- Velocidad de cambios en comportamiento
```

### NLP en Textos de Soporte
```
- Si hubiera comentarios de clientes: sentiment analysis
- Palabras clave asociadas con churn
- Análisis de satisfacción
```

### Causalidad vs. Correlación
```
- ¿Fibra óptica CAUSA churn o son clientes de fibra los que más se van?
- Discusión sobre que necesitaríamos para probar causalidad
- Experimentos (A/B testing) sugeridos
```

### Predicción Temporal
```
- En lugar de "¿churnarán?", predecir "¿cuándo churnarán?"
- Usar survival analysis
- Análisis de tiempo hasta evento
```

---

## Conclusión

El dataset **Telco Customer Churn** es excepcional para enseñanza porque:

1. **Realismo**: Refleja problemas reales que enfrentan empresas
2. **Complejidad Manejable**: Tamaño suficiente pero no abrumador
3. **Múltiples Enfoques**: Permite enseñar desde simple (Logistic Regression) hasta avanzado (XGBoost)
4. **Conversaciones Valiosas**: Genera preguntas sobre negocio, ética, causalidad, trade-offs
5. **Resultados Visibles**: Los estudiantes ven rápidamente que el análisis arroja insights útiles

Usarlo en su clase de minería de datos bajo CRISP-DM proporciona una base sólida para que los estudiantes entiendan cómo el proceso metodológico transforma datos en decisiones de negocio.