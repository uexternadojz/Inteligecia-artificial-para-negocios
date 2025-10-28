<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# estoy enseñando una clase de mineria de datos bajo metodologia crisp dm, quiero que investigues sobre este dataset, y como los hallazgos o approaches pedagogicos para enseñlar desde ahi: [https://www.kaggle.com/datasets/blastchar/telco-customer-churn?utm_source=chatgpt.com](https://www.kaggle.com/datasets/blastchar/telco-customer-churn?utm_source=chatgpt.com)

Perfect! Now let me create a summary document with teaching recommendations:

# Guía Pedagógica: Dataset Telco Customer Churn bajo Metodología CRISP-DM

## Introducción

El dataset **Telco Customer Churn** es un recurso excepcional para enseñar minería de datos bajo la metodología CRISP-DM. Con 7,043 clientes y 21 características, permite a los estudiantes trabajar de manera realista a través de todas las fases del ciclo de análisis de datos.[^1][^2][^3]

***

## Visión General del Dataset

**Estructura Fundamental**[^1]

- 7,043 registros de clientes
- 21 características (20 predictoras + 1 variable objetivo)
- Variable objetivo: Churn (clientes que se fueron vs. se quedaron)
- Contexto empresarial: Compañía de telecomunicaciones en California
- Desbalance de clases: ~73.5% sin abandono vs. ~26.5% con abandono[^4]

**Composición de Variables**[^5][^6]
El dataset incluye información demográfica (género, edad, estado civil, dependientes), detalles de cuenta (meses como cliente, tipo de contrato, métodos de pago, cargos), y servicios suscritos (telefonía, internet, seguridad en línea, respaldo, protección de dispositivos, soporte técnico, streaming).

![CRISP-DM Cycle with Telco Customer Churn Dataset - Pedagogical Framework](https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/47139dd9df1578cd2192e3bba8ba95a8/26b8b13d-1781-4a50-8a24-c1308dc8dd46/1fc8febb.png)

CRISP-DM Cycle with Telco Customer Churn Dataset - Pedagogical Framework

***

## FASE 1: Comprensión del Negocio

### Objetivo Pedagógico

Conectar problemas empresariales reales con preguntas analíticas específicas y objetivos de minería de datos.[^7][^8]

### Actividades Sugeridas

**Contexto Empresarial**: "Una compañía de telecomunicaciones pierde clientes regularmente, impactando directamente los ingresos recurrentes. Necesita entender patrones de abandono y desarrollar estrategias de retención".[^8]

**Preguntas Clave para Estudiantes**:

- ¿Por qué es crítico predecir churn para una empresa de telecomunicaciones?
- ¿Cuál es el costo de perder un cliente versus el costo de retenerlo?
- ¿Qué estrategias empresariales podemos implementar si identificamos a clientes en riesgo?
- ¿Cómo traducimos el objetivo empresarial en objetivos específicos de minería de datos?

**Cálculo de Valor**: Los estudiantes deben proyectar el impacto financiero de reducir churn en 5%, 10% o 15%, considerando ingresos por cliente y costos de adquisición.[^9]

***

## FASE 2: Comprensión de los Datos

### Por Qué Este Dataset es Ideal para Enseñanza

**Complejidad Realista**: Mezcla datos numéricos (tenure, charges), categóricos nominales (gender, internet service), y ordinales (contract type).[^5]

**Calidad Relativa**: Tiene muy pocos valores faltantes (~0.16% en TotalCharges), permitiendo que los estudiantes se enfoquen en patrones versus limpieza extrema.[^10]

**Patrones Educativos Naturales**: Contiene multicolinealidad interesante (tenure, monthly charges y total charges están correlacionados), distribuciones variadas, y relaciones no-lineales.[^5]

### Laboratorios Recomendados

**Análisis Univariado**[^5]

- Distribuciones numéricas muestran bimodalidad en tenure (muchos clientes nuevos que se van + clientes leales)
- MonthlyCharges y TotalCharges siguen distribuciones diferentes revelando estructura de precios
- Aproximadamente 55% de clientes tienen contratos mes-a-mes versus 24% con contratos de dos años[^5]

**Análisis Bivariado con Churn**[^11][^5]

- **Tenure vs Churn**: Separación clara en densidades. Los que se van tienen tenure bajo
- **Contract vs Churn**: Churn rate de ~42% para mes-a-mes vs ~11% para dos años (odds ratio 4.06x)[^11]
- **Internet Service vs Churn**: Fibra óptica ~42% vs DSL ~19% (odds ratio 2.31x)[^11]
- **Tech Support vs Churn**: Sin support ~30% vs con support ~15%
- **Online Backup/Security vs Churn**: Sin servicios ~29% vs con servicios ~12%[^5]

***

## FASE 3: Preparación de Datos

### Desafíos Pedagógicos Únicos

**Conversión de Tipos de Datos**: TotalCharges se importa como string debido a valores vacíos, enseñando cuidados en importación de datos.[^12]

**Manejo de Valores Faltantes**: 11 valores faltantes en TotalCharges (0.16%). Discusión valiosa: ¿eliminar vs. imputar? ¿Qué estrategia es más apropiada?[^10]

**Codificación de Categóricas**: One-hot encoding para servicios binarios (OnlineSecurity, TechSupport, etc.) versus label encoding para ordinales (Contract types).[^12]

**Tratamiento del Desbalance**: ~26.5% churn vs 73.5% sin churn. Enseñar oversampling, undersampling, SMOTE, ADASYN, y class weights.[^4]

**Escalamiento**: MonthlyCharges (~26-111) vs Tenure (~1-72) tienen rangos muy diferentes. Impacta algoritmos basados en distancia.[^13]

### Laboratorios Sugeridos

1. **Limpieza Básica**: Eliminar CustomerID, manejar TotalCharges, verificar tipos
2. **Feature Engineering**: Crear AverageMonthlyCharges, categorías de cliente nuevo/leal
3. **Codificación y Escalamiento**: One-hot encoding, standardization
4. **Tratamiento de Desbalance**: Generar dataset balanceado y comparar performance

***

## FASE 4: Modelado

### Múltiples Enfoques Pedagógicamente Valiosos

**Modelos Simples** (Fundamentos)[^2]

- **Logistic Regression**: Accuracy típica ~80%, coeficientes muestran impacto de cada variable
- **Decision Trees**: Fácil visualización, feature importance intuitiva, accuracy ~78-82%

**Modelos Complejos** (Avanzados)[^14]

- **Random Forest**: Accuracy típica ~83-85%, feature importance más robusta
- **XGBoost/LightGBM**: ~85-87% accuracy, trade-off entre interpretabilidad y performance[^14]

Esta progresión permite enseñar trade-offs fundamentales: simplicidad vs. accuracy, interpretabilidad vs. performance.[^2]

***

## FASE 5: Evaluación

### Métricas Apropiadas para Este Problema

En un problema desbalanceado, la accuracy (76.5% baseline si siempre predice "No Churn") es engañosa.[^2]

**Métricas Críticas**:


| Métrica | Por Qué Importa | Costo del Error |
| :-- | :-- | :-- |
| Precision | De predichos como churn, ¿cuántos realmente lo son? | Falso positivo = recursos de retención desperdiciados |
| Recall | De todos los que churnaron, ¿cuántos identifiqué? | Falso negativo = ingresos perdidos |
| ROC-AUC | Ranking de modelos robusto al desbalance | Probabilidad que model rankea positivo > negativo |
| F1-Score | Balance entre precision y recall | Métrica de resumen robusta |

![Key Factors Associated with Customer Churn Rates in Telco Dataset](https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/47139dd9df1578cd2192e3bba8ba95a8/ed691d30-3761-4afc-9af2-f5c84acab275/a684ea2d.png)

Key Factors Associated with Customer Churn Rates in Telco Dataset

***

## FASE 6: Despliegue

### Aplicaciones Prácticas

**Scoring de Riesgo**: Generar probabilidad de churn para cada cliente, segmentando en alto (>70%), medio (40-70%), bajo (<40%) riesgo.[^9]

**Explicabilidad**: "Cliente X tiene 68% probabilidad de churn porque: (1) contrato mes-a-mes, (2) sin tech support, (3) cargos recientemente aumentaron".[^9]

**Rentabilidad**: Estimar CLV por cliente, calcular ROI de intervenciones, identificar clientes "no vale la pena retener".[^11]

***

## Hallazgos Esperados para Discusión en Clase

### Factores Fuertemente Asociados con Churn[^5][^11]

| Factor | Churn Rate | Implicación |
| :-- | :-- | :-- |
| Contrato Mes-a-Mes | ~42% | Flexibilidad permite cambio fácil |
| Fibra Óptica | ~42% | ¿Problemas de servicio pese a mejor tech? |
| Tenure <6 meses | ~50% | Primeros meses críticos para retención |
| Sin Tech Support | ~30% | Soporte proactivo mejora lealtad |
| Tenure >24 meses | ~8% | Clientes establecidos son leales |

### Hallazgos Contra-Intuitivos

**Paradoja de Fibra Óptica**: Mejor tecnología pero mayor churn que DSL. Pregunta pedagógica: ¿Por qué? Posibles respuestas incluyen problemas de instalación, precio vs. perceived value, o problemas de servicio.[^11]

**Efecto Protector del No Internet**: Clientes sin servicio de internet tienen MENOS churn que con DSL. Discusión: ¿Qué aprendemos sobre segmentación?[^11]

***

## Ventajas Pedagógicas Resumen

1. **Realismo**: Refleja problemas que enfrentan negocios reales
2. **Complejidad Manejable**: Tamaño suficiente (~7k filas) pero no abrumador
3. **Múltiples Caminos**: Desde Logistic Regression (simple) hasta XGBoost (avanzado)[^2]
4. **Conversaciones Valiosas**: Genera debates sobre causalidad vs. correlación, ética en segmentación, trade-offs de modelos
5. **Resultados Visibles**: Los estudiantes ven rápidamente que el análisis produce insights empresariales útiles
6. **Estructurado para CRISP-DM**: Todas las seis fases tienen actividades naturales y progresivas

***

## Variantes Pedagógicas

**Enfoque Incremental** (Principiantes):

- Semana 1: Fases 1-2 (Negocio y Exploración)
- Semana 2: Fase 3 (Preparación)
- Semana 3: Fase 4 (Modelado Simple)
- Semana 4: Fase 5 (Evaluación)
- Semana 5: Fase 6 (Despliegue)

**Enfoque Comparativo** (Avanzados):

- Dividir clase en grupos; cada uno explora diferentes algoritmos
- Presentación final comparando resultados y trade-offs

**Enfoque de Desbalance** (Especializado):

- Enfoque en técnicas para datasets desbalanceados
- Comparar: baseline vs. oversampling vs. SMOTE vs. class_weight

***

## Conclusión

El dataset **Telco Customer Churn** es un recurso pedagógico superior para enseñanza de minería de datos bajo CRISP-DM porque combina realismo empresarial, complejidad técnica educativa, y la capacidad de generar insights tangibles. Proporciona una base sólida para que los estudiantes entiendan cómo el proceso metodológico transforma datos en decisiones de negocio accionables.[^7][^8][^9]
<span style="display:none">[^15][^16][^17][^18][^19][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^30][^31][^32][^33][^34][^35][^36][^37][^38][^39][^40][^41][^42][^43][^44]</span>

<div align="center">⁂</div>

[^1]: https://www.kaggle.com/datasets/blastchar/telco-customer-churn

[^2]: https://365datascience.com/tutorials/python-tutorials/how-to-build-a-customer-churn-prediction-model-in-python/

[^3]: https://www.kaggle.com/code/supratimhaldar/telco-customer-churn-exploratory-data-analysis

[^4]: https://www.naturalspublishing.com/files/published/i4925e47vyg47p.pdf

[^5]: https://towardsdatascience.com/telco-customer-churnrate-analysis-d412f208cbbf/

[^6]: https://www.geeksforgeeks.org/machine-learning/python-customer-churn-analysis-prediction/

[^7]: https://www.studocu.com/latam/document/instituto-tecnologico-de-las-americas/mineria-de-datos/investigacion-sobre-metodologia-crisp-dm/118070025

[^8]: https://blog.mbauspesalq.com/es/crisp-dm-las-6-etapas-de-la-metodologia-del-futuro/

[^9]: https://www.linkedin.com/pulse/navigating-customer-churn-using-machine-learning-enoch-taylor-nketiah

[^10]: https://www.sciencedirect.com/science/article/pii/S2666720723001443

[^11]: https://franciscobustamante.com.br/portfolio/2022-06-project_churn_prediction/

[^12]: https://github.com/egecandrsn/telco-customer-churn

[^13]: https://github.com/Geo-y20/Telco-Customer-Churn-

[^14]: https://www.informingscience.org/Publications/5192

[^15]: https://www.iic.uam.es/innovacion/metodologia-crisp-dm-ciencia-de-datos/

[^16]: https://www.ibm.com/docs/es/spss-modeler/saas?topic=dm-crisp-help-overview

[^17]: https://www.youtube.com/watch?v=UyKkSsEbXkw

[^18]: https://www.youtube.com/watch?v=dZM_aGaLW8g

[^19]: https://insight7.io/how-to-predict-customer-churn-with-text-mining/

[^20]: https://es.scribd.com/document/489687667/crisp-dm-una-metodologia-para-proyectos-de-data-mining

[^21]: https://www.interviewquery.com/p/customer-churn-datasets

[^22]: https://enterprise-knowledge.com/understanding-the-role-of-knowledge-intelligence-in-the-crisp-dm-framework-a-guide-for-data-science-projects/

[^23]: https://ieeexplore.ieee.org/document/8649494/

[^24]: https://healthdataminer.com/data-mining/crisp-dm-una-metodologia-para-mineria-de-datos-en-salud/

[^25]: https://www.kaggle.com/datasets/abdallahwagih/telco-customer-churn

[^26]: https://start.agilytic.com/crisp-dm

[^27]: https://www.sciencedirect.com/science/article/abs/pii/S1568494622000436

[^28]: https://e-archivo.uc3m.es/bitstreams/714c5452-962e-44cf-993f-ebb3088d4aa5/download

[^29]: https://www.datascience-pm.com/crisp-dm-2/

[^30]: https://pdfs.semanticscholar.org/b5f8/47fc4962e7b7d4d8bc46ac90f31035cd2c12.pdf

[^31]: https://www.kaggle.com/code/praxitelisk/telco-customer-churn-eda-ml

[^32]: https://www.kaggle.com/code/emineyetm/telco-customer-churn

[^33]: https://www.ewadirect.com/proceedings/ace/article/view/13851

[^34]: https://info.mheducation.com/rs/128-SJW-347/images/Business Analytics September 24 2021, final.pdf

[^35]: https://carpentries-incubator.github.io/python-business/11-crisp/index.html

[^36]: https://ieeexplore.ieee.org/document/10537927/

[^37]: https://www.linkedin.com/learning/data-science-foundations-data-mining-in-r/the-crisp-dm-data-mining-model

[^38]: https://www.futurelearn.com/info/courses/data-science-for-climate-change/0/steps/346847

[^39]: https://keithmccormick.com/wp-content/uploads/CRISP-DM No Brand.pdf

[^40]: https://onlinelibrary.wiley.com/doi/abs/10.1111/dsji.12222

[^41]: https://www.kaggle.com/code/adaramit/customer-churn-working-with-imbalanced-dataset

[^42]: https://www.kaggle.com/code/redpen12/churn-prediction-in-depth-eda-and-interpretations

[^43]: https://www.kaggle.com/code/faridrizqis/telecom-churn-dealing-with-imbalance-data

[^44]: https://observablehq.com/@ealecho/end-to-end-machine-learning-project-telco-customer-churn

