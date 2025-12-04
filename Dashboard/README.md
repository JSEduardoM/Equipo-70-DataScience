# 🚀 Cómo Ejecutar el Dashboard de Streamlit

## Instalación de Dependencias

Primero, instala las dependencias necesarias:

```bash
pip install -r Dashboard/requirements.txt
```

O instala manualmente:

```bash
pip install streamlit plotly pandas numpy matplotlib seaborn scikit-learn
```

## Ejecutar el Dashboard

Desde la raíz del proyecto, ejecuta:

```bash
streamlit run Dashboard/app.py
```

El dashboard se abrirá automáticamente en tu navegador en `http://localhost:8501`

## Características del Dashboard

### 🎯 Filtros Interactivos (Sidebar)
- **Risk Segment**: Filtra por Alto, Medio o Bajo riesgo
- **Churn Status**: Filtra por clientes Activos o Abandonados
- Contador en tiempo real de clientes filtrados

### 📊 Métricas Clave
- Total de clientes
- Clientes activos (con porcentaje)
- Clientes abandonados (con tasa de churn)
- Clientes de alto riesgo

### 🤖 Rendimiento del Modelo
- Accuracy: 93.4%
- Precision: 88.8%
- Recall: 70.4%
- ROC-AUC: 0.97

### 📈 Visualizaciones Interactivas
1. **Churn Distribution** - Gráfico de dona interactivo
2. **Risk Segment Distribution** - Gráfico de barras con valores
3. **Feature Importance** - Gráfico horizontal con escala de colores
4. **Tenure vs Churn** - Comparación de antigüedad
5. **Cashback vs Churn** - Análisis de cashback
6. **Satisfaction Distribution** - Histograma superpuesto
7. **Churn Probability by Risk** - Box plots por segmento

### 💡 Insights de Negocio
- Recomendaciones accionables basadas en datos
- Estrategias de retención priorizadas

### 📋 Explorador de Datos
- Checkbox para mostrar/ocultar datos raw
- Visualización de las primeras 100 filas filtradas
- Botón de descarga para exportar datos filtrados a CSV

## Ventajas sobre HTML Estático

✅ **Interactividad**: Filtros en tiempo real  
✅ **Gráficos Dinámicos**: Plotly permite zoom, pan, hover  
✅ **Exploración de Datos**: Ver y descargar datos filtrados  
✅ **Responsive**: Se adapta a cualquier tamaño de pantalla  
✅ **Fácil de Compartir**: Puede desplegarse en Streamlit Cloud gratis  

## Despliegue en la Nube (Opcional)

Para compartir el dashboard públicamente:

1. Sube el proyecto a GitHub
2. Ve a [share.streamlit.io](https://share.streamlit.io)
3. Conecta tu repositorio
4. Selecciona `Dashboard/app.py` como archivo principal
5. ¡Listo! Tendrás una URL pública

## Troubleshooting

**Error: "No module named 'streamlit'"**
```bash
pip install streamlit
```

**Error: "FileNotFoundError: datos/dataset_ecommerce_segmented.csv"**
- Asegúrate de ejecutar primero: `python Segmentation/segmentation_analysis.py`

**El dashboard no se abre automáticamente**
- Abre manualmente: http://localhost:8501
