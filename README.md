# 🎯 E-commerce Churn Prediction Model

## 📋 Descripción del Proyecto

Sistema completo de análisis y predicción de churn (abandono de clientes) para empresas de e-commerce. El proyecto incluye análisis exploratorio de datos, modelado predictivo, segmentación de clientes y generación de insights accionables para mejorar la retención.

---

## 🚀 Características Principales

- **Análisis Exploratorio de Datos (EDA)**: Limpieza, normalización y análisis de correlaciones
- **Modelado Predictivo**: Comparación de múltiples algoritmos de ML
- **Segmentación de Clientes**: Clasificación por riesgo de abandono (Alto, Medio, Bajo)
- **Dashboard Analítico**: Visualización de métricas clave y resultados del modelo
- **Recomendaciones de Negocio**: Estrategias accionables basadas en datos

---

## 📊 Variables Utilizadas

El dataset contiene **3,941 clientes** con las siguientes variables:

### Variables Numéricas
| Variable | Descripción |
|----------|-------------|
| **Tenure** | Antigüedad del cliente en la plataforma (meses) |
| **WarehouseToHome** | Distancia del almacén al domicilio del cliente (km) |
| **NumberOfDeviceRegistered** | Número de dispositivos registrados |
| **SatisfactionScore** | Puntuación de satisfacción del cliente (1-5) |
| **NumberOfAddress** | Número de direcciones registradas |
| **Complain** | Si el cliente ha presentado quejas (0=No, 1=Sí) |
| **DaySinceLastOrder** | Días desde la última compra |
| **CashbackAmount** | Monto promedio de cashback recibido |

### Variables Categóricas
| Variable | Descripción |
|----------|-------------|
| **PreferedOrderCat** | Categoría de producto preferida |
| **MaritalStatus** | Estado civil del cliente |

### Variable Objetivo
| Variable | Descripción |
|----------|-------------|
| **Churn** | Indicador de abandono (0=Activo, 1=Abandonó) |

---

## 🤖 Modelos Implementados

Se entrenaron y evaluaron **3 modelos de clasificación**:

### 1. Regresión Logística (Baseline)
- **Accuracy**: 87.5%
- **ROC-AUC**: 0.88
- Modelo simple y interpretable

### 2. Árbol de Decisión
- **Accuracy**: 92.9%
- **ROC-AUC**: 0.87
- Buena interpretabilidad

### 3. Random Forest ⭐ **MODELO SELECCIONADO**
- **Accuracy**: 93.4%
- **Precision**: 88.8%
- **Recall**: 70.4%
- **ROC-AUC**: 0.97

**¿Por qué Random Forest?**
- ✅ Mayor precisión (93.4%)
- ✅ Excelente ROC-AUC (0.97) - mejor discriminación entre clases
- ✅ Robusto ante overfitting
- ✅ Proporciona importancia de features para interpretación de negocio

---

## 📈 Top 5 Features Más Importantes

1. **Tenure** (25.9%) - Antigüedad del cliente
2. **CashbackAmount** (16.8%) - Monto de cashback
3. **WarehouseToHome** (10.3%) - Distancia de entrega
4. **NumberOfAddress** (8.6%) - Número de direcciones
5. **DaySinceLastOrder** (8.1%) - Días desde última compra

---

## 🛠️ Instalación y Configuración

### Requisitos Previos
```bash
Python 3.8+
pip
```

### Dependencias
```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

---

## 🚀 Cómo Ejecutar el Proyecto

### 1. Análisis Exploratorio de Datos (EDA)
```bash
# Ejecutar script de EDA
python EDA/eda_script.py

# O abrir el notebook interactivo
jupyter notebook EDA/eda_analysis.ipynb
```

**Output**: 
- `datos/dataset_ecommerce_cleaned.csv` (datos limpios)
- Estadísticas descriptivas y correlaciones

### 2. Análisis de Definición de Churn
```bash
python Churn_Definition/churn_analysis.py
```

**Output**: 
- `Churn_Definition/days_since_last_order_boxplot.png`

### 3. Entrenamiento de Modelos
```bash
python Modeling/modeling_pipeline.py
```

**Output**: 
- Métricas de evaluación de los 3 modelos
- `Modeling/feature_importance_rf.png`
- `Modeling/cm_*.png` (matrices de confusión)

### 4. Segmentación de Clientes
```bash
python Segmentation/segmentation_analysis.py
```

**Output**: 
- `datos/dataset_ecommerce_segmented.csv` (con columnas `Churn_Probability` y `Risk_Segment`)
- `Segmentation/risk_segment_distribution.png`

### 5. Generar Dashboard Interactivo (Streamlit) ⭐

**Opción Recomendada: Dashboard Interactivo con Streamlit**
```bash
streamlit run Dashboard/app.py
```

El dashboard se abrirá automáticamente en `http://localhost:8501`

**Características del Dashboard Streamlit:**
- 🎯 Filtros interactivos en tiempo real (Risk Segment, Churn Status)
- 📊 Gráficos dinámicos con Plotly (zoom, pan, hover)
- 📈 7 visualizaciones interactivas
- 📋 Explorador de datos con descarga CSV
- 📱 Diseño responsive

**Alternativa: Dashboard HTML Estático**
```bash
python Dashboard/dashboard_generator.py
# Luego abrir: Dashboard/dashboard.html
```

### 6. Ver Reporte de Insights
```bash
# Abrir en cualquier editor Markdown
cat Insights/insights_report.md
```

---

## 📁 Estructura del Proyecto

```
Equipo-70-DataScience/
├── datos/
│   ├── data_ecommerce_customer_churn.csv    # Dataset original
│   ├── dataset_ecommerce_cleaned.csv         # Datos limpios
│   └── dataset_ecommerce_segmented.csv       # Datos con segmentación
├── EDA/
│   ├── eda_script.py                         # Script de análisis exploratorio
│   └── eda_analysis.ipynb                    # Notebook interactivo
├── Churn_Definition/
│   ├── churn_analysis.py                     # Análisis de definición de churn
│   └── days_since_last_order_boxplot.png     # Visualización
├── Modeling/
│   ├── modeling_pipeline.py                  # Pipeline de entrenamiento
│   ├── feature_importance_rf.png             # Importancia de features
│   └── cm_*.png                              # Matrices de confusión
├── Segmentation/
│   ├── segmentation_analysis.py              # Script de segmentación
│   └── risk_segment_distribution.png         # Distribución de riesgos
├── Dashboard/
│   ├── dashboard_generator.py                # Generador de dashboard
│   └── dashboard.html                        # Dashboard interactivo
└── Insights/
    └── insights_report.md                    # Reporte de insights de negocio
```

---

## 📊 Resultados Clave

- **Tasa de Churn**: 17.1% (674 de 3,941 clientes)
- **Modelo Final**: Random Forest con 93.4% de precisión
- **Segmentos de Riesgo**:
  - Alto Riesgo: Clientes con >70% probabilidad de churn
  - Riesgo Medio: 30-70% probabilidad
  - Bajo Riesgo: <30% probabilidad

---

## 💡 Recomendaciones de Negocio

1. **Onboarding Mejorado**: Enfocarse en los primeros 1-3 meses del cliente
2. **Resolución de Quejas**: Implementar protocolo "White Glove" para clientes con quejas
3. **Optimización de Recompensas**: Revisar programa de cashback
4. **Campañas Segmentadas**: Ofertas personalizadas para clientes de Alto Riesgo

---

## 👥 Equipo

**Equipo 70 - Data Science**  
No Country - Simulación S11-25

---

## 📄 Licencia

Este proyecto es parte de una simulación educativa de No Country.
