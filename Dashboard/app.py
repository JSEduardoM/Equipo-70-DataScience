import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Page configuration
st.set_page_config(
    page_title="Análisis de Churn E-commerce",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better visualization
st.markdown("""
<style>
    /* Main styling */
    .main {
        padding: 0rem 1rem;
    }
    
    /* Metric cards */
    [data-testid="stMetricValue"] {
        font-size: 32px;
        font-weight: bold;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 16px;
        font-weight: 600;
        color: #555;
    }
    
    /* Headers */
    h1 {
        color: #1f77b4;
        text-align: center;
        padding: 20px 0;
        font-size: 42px !important;
        font-weight: 700 !important;
    }
    
    h2 {
        color: #2c3e50;
        border-bottom: 3px solid #1f77b4;
        padding-bottom: 10px;
        margin-top: 30px;
        font-size: 28px !important;
    }
    
    h3 {
        color: #34495e;
        font-size: 22px !important;
        margin-top: 20px;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
        color: white;
        font-weight: 500;
    }
    
    /* Info boxes */
    .insight-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        margin: 20px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .insight-box h3 {
        color: white !important;
        margin-top: 0;
    }
    
    .insight-box ul {
        margin-top: 15px;
    }
    
    .insight-box li {
        margin: 10px 0;
        line-height: 1.6;
    }
    
    /* Success/Warning/Danger boxes */
    .success-box {
        background-color: #d4edda;
        border-left: 5px solid #28a745;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    
    .warning-box {
        background-color: #fff3cd;
        border-left: 5px solid #ffc107;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    
    .danger-box {
        background-color: #f8d7da;
        border-left: 5px solid #dc3545;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #f0f2f6;
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #1f77b4;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('datos/dataset_ecommerce_segmentado_es.csv')
        return df
    except FileNotFoundError:
        st.error("❌ Error: Dataset no encontrado. Por favor ejecuta el script de segmentación primero.")
        st.stop()

df = load_data()

# Sidebar with improved styling
with st.sidebar:
    st.markdown("# 🎯 Controles del Dashboard")
    st.markdown("---")
    
    st.markdown("### 📊 Filtros")
    
    # Risk Segment Filter
    risk_filter = st.multiselect(
        "🎚️ Segmento de Riesgo",
        options=df['Segmento_Riesgo'].unique(),
        default=df['Segmento_Riesgo'].unique(),
        help="Filtrar clientes por nivel de riesgo"
    )
    
    # Churn Status Filter
    churn_filter = st.multiselect(
        "👥 Estado de Churn",
        options=['Activo', 'Churn'],
        default=['Activo', 'Churn'],
        help="Filtrar por estado del cliente"
    )
    
    st.markdown("---")
    
    # Apply filters
    churn_map = {'Activo': 0, 'Churn': 1}
    churn_numeric = [churn_map[x] for x in churn_filter]
    
    df_filtered = df[
        (df['Segmento_Riesgo'].isin(risk_filter)) &
        (df['Target'].isin(churn_numeric))
    ]
    
    # Filter summary
    st.markdown("### 📈 Resumen de Filtros")
    st.info(f"**Mostrando:** {len(df_filtered):,} / {len(df):,} clientes")
    st.success(f"**Filtrado:** {((len(df_filtered)/len(df))*100):.1f}% del total")
    
    st.markdown("---")
    st.markdown("### ℹ️ Acerca de")
    st.markdown("""
    **Modelo:** Random Forest  
    **Accuracy:** 93.4%  
    **ROC-AUC:** 0.97
    """)

# Main title with icon
st.markdown("# 📊 Dashboard de Análisis de Churn E-commerce")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 18px; margin-bottom: 30px;'>
    <strong>Análisis Predictivo de Abandono de Clientes</strong> | Powered by Random Forest ML Model
</div>
""", unsafe_allow_html=True)

# Calculate metrics
total_customers = len(df_filtered)
active_customers = df_filtered[df_filtered['Target'] == 0].shape[0]
churned_customers = df_filtered[df_filtered['Target'] == 1].shape[0]
churn_rate = (churned_customers / total_customers * 100) if total_customers > 0 else 0
high_risk_count = df_filtered[df_filtered['Segmento_Riesgo'] == 'Alto Riesgo'].shape[0]
avg_churn_prob = df_filtered['Probabilidad_Churn'].mean() * 100

# Key Metrics with improved layout
st.markdown("## 📈 Indicadores Clave de Rendimiento")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        label="👥 Total Clientes",
        value=f"{total_customers:,}",
        help="Número total de clientes en vista filtrada"
    )

with col2:
    st.metric(
        label="✅ Activos",
        value=f"{active_customers:,}",
        delta=f"{(active_customers/total_customers*100):.1f}%" if total_customers > 0 else "0%",
        delta_color="normal"
    )

with col3:
    st.metric(
        label="❌ Churn",
        value=f"{churned_customers:,}",
        delta=f"-{churn_rate:.1f}%",
        delta_color="inverse"
    )

with col4:
    st.metric(
        label="⚠️ Alto Riesgo",
        value=f"{high_risk_count:,}",
        help="Clientes que requieren atención inmediata"
    )

with col5:
    st.metric(
        label="📊 Prob. Churn Prom.",
        value=f"{avg_churn_prob:.1f}%",
        help="Probabilidad promedio de churn"
    )

# Model Performance Section
st.markdown("---")
st.markdown("## 🤖 Rendimiento del Modelo Random Forest")

col1, col2, col3, col4 = st.columns(4)

metrics_data = [
    ("Accuracy", "93.4%", "Precisión general de predicción"),
    ("Precision", "88.8%", "Precisión para predicción de churn"),
    ("Recall", "70.4%", "Recall para predicción de churn"),
    ("ROC-AUC", "0.97", "Área bajo la curva ROC")
]

for col, (label, value, help_text) in zip([col1, col2, col3, col4], metrics_data):
    with col:
        st.metric(label=f"🎯 {label}", value=value, help=help_text)

# Tabs for better organization
st.markdown("---")
tab1, tab2, tab3, tab4 = st.tabs(["📊 Resumen", "🎯 Análisis de Features", "🔍 Análisis Profundo", "📋 Explorador de Datos"])

with tab1:
    st.markdown("### 📊 Resumen de Churn")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Churn Distribution
        churn_counts = df_filtered['Target'].value_counts()
        fig = go.Figure(data=[go.Pie(
            labels=['Activo', 'Churn'],
            values=[churn_counts.get(0, 0), churn_counts.get(1, 0)],
            marker=dict(colors=['#2ecc71', '#e74c3c']),
            hole=0.5,
            textinfo='label+percent',
            textfont=dict(size=16, color='white'),
            hovertemplate='<b>%{label}</b><br>Cantidad: %{value}<br>Porcentaje: %{percent}<extra></extra>'
        )])
        fig.update_layout(
            title={
                'text': "Distribución de Churn de Clientes",
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 20, 'color': '#2c3e50'}
            },
            height=400,
            showlegend=True,
            legend=dict(font=dict(size=14))
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Risk Segment Distribution
        risk_counts = df_filtered['Segmento_Riesgo'].value_counts()
        fig = go.Figure(data=[go.Bar(
            x=['Bajo Riesgo', 'Riesgo Medio', 'Alto Riesgo'],
            y=[risk_counts.get('Bajo Riesgo', 0), risk_counts.get('Riesgo Medio', 0), risk_counts.get('Alto Riesgo', 0)],
            marker=dict(
                color=['#27ae60', '#f39c12', '#e74c3c'],
                line=dict(color='white', width=2)
            ),
            text=[risk_counts.get('Bajo Riesgo', 0), risk_counts.get('Riesgo Medio', 0), risk_counts.get('Alto Riesgo', 0)],
            textposition='outside',
            textfont=dict(size=14, color='black'),
            hovertemplate='<b>%{x}</b><br>Clientes: %{y}<extra></extra>'
        )])
        fig.update_layout(
            title={
                'text': "Distribución de Clientes por Segmento de Riesgo",
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 20, 'color': '#2c3e50'}
            },
            yaxis_title="Número de Clientes",
            height=400,
            showlegend=False,
            yaxis=dict(gridcolor='lightgray')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Risk Summary Boxes
    st.markdown("### 🎯 Resumen por Segmento de Riesgo")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        low_risk = risk_counts.get('Bajo Riesgo', 0)
        st.markdown(f"""
        <div class="success-box">
            <h4 style="margin:0; color:#155724;">✅ Bajo Riesgo</h4>
            <p style="font-size:24px; font-weight:bold; margin:10px 0; color:#155724;">{low_risk:,} clientes</p>
            <p style="margin:0; color:#155724;">Base de clientes leales - Enfoque en upselling</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        medium_risk = risk_counts.get('Riesgo Medio', 0)
        st.markdown(f"""
        <div class="warning-box">
            <h4 style="margin:0; color:#856404;">⚠️ Riesgo Medio</h4>
            <p style="font-size:24px; font-weight:bold; margin:10px 0; color:#856404;">{medium_risk:,} clientes</p>
            <p style="margin:0; color:#856404;">Lista de vigilancia - Medidas preventivas necesarias</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        high_risk = risk_counts.get('Alto Riesgo', 0)
        st.markdown(f"""
        <div class="danger-box">
            <h4 style="margin:0; color:#721c24;">🚨 Alto Riesgo</h4>
            <p style="font-size:24px; font-weight:bold; margin:10px 0; color:#721c24;">{high_risk:,} clientes</p>
            <p style="margin:0; color:#721c24;">¡Intervención inmediata requerida!</p>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("### 🎯 Análisis de Importancia de Features")
    
    # Feature Importance
    feature_importance = {
        'Antiguedad': 0.259,
        'Monto_Cashback': 0.168,
        'Distancia_Almacen': 0.103,
        'Numero_Direcciones': 0.086,
        'Dias_Ultima_Compra': 0.081,
        'Queja': 0.069,
        'Nivel_Satisfaccion': 0.066,
        'Numero_Dispositivos': 0.052
    }
    
    fig = go.Figure(data=[go.Bar(
        x=list(feature_importance.values()),
        y=list(feature_importance.keys()),
        orientation='h',
        marker=dict(
            color=list(feature_importance.values()),
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title="Importancia")
        ),
        text=[f'{v:.1%}' for v in feature_importance.values()],
        textposition='outside',
        textfont=dict(size=14),
        hovertemplate='<b>%{y}</b><br>Importancia: %{x:.3f}<extra></extra>'
    )])
    fig.update_layout(
        title={
            'text': "Top 8 Importancia de Features (Random Forest)",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 22, 'color': '#2c3e50'}
        },
        xaxis_title="Puntuación de Importancia",
        height=500,
        xaxis=dict(gridcolor='lightgray'),
        yaxis=dict(tickfont=dict(size=14))
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Feature Explanations
    st.markdown("### 📝 Explicación de Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🏆 Features Principales:**
        - **Antiguedad (25.9%)**: Duración de lealtad del cliente - factor más crítico
        - **Monto_Cashback (16.8%)**: Efectividad del programa de recompensas
        - **Distancia_Almacen (10.3%)**: Impacto de la distancia de entrega
        - **Numero_Direcciones (8.6%)**: Nivel de engagement del cliente
        """)
    
    with col2:
        st.markdown("""
        **💡 Insights Clave:**
        - Clientes nuevos tienen 3x más probabilidad de churn
        - Mayor cashback se correlaciona con retención
        - La distancia afecta satisfacción y churn
        - Múltiples direcciones indican engagement
        """)

with tab3:
    st.markdown("### 🔍 Análisis Profundo")
    
    # Tenure vs Churn
    st.markdown("#### 📅 Análisis de Antigüedad")
    col1, col2 = st.columns(2)
    
    with col1:
        tenure_churn = df_filtered.groupby('Target')['Antiguedad'].mean()
        fig = go.Figure(data=[go.Bar(
            x=['Activo (0)', 'Churn (1)'],
            y=tenure_churn.values,
            marker=dict(
                color=['#2ecc71', '#e74c3c'],
                line=dict(color='white', width=2)
            ),
            text=[f'{v:.1f} meses' for v in tenure_churn.values],
            textposition='outside',
            textfont=dict(size=14),
            hovertemplate='<b>%{x}</b><br>Antigüedad Prom: %{y:.1f} meses<extra></extra>'
        )])
        fig.update_layout(
            title="Antigüedad Promedio por Estado de Churn",
            yaxis_title="Antigüedad Promedio (meses)",
            height=400,
            yaxis=dict(gridcolor='lightgray')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        cashback_churn = df_filtered.groupby('Target')['Monto_Cashback'].mean()
        fig = go.Figure(data=[go.Bar(
            x=['Activo (0)', 'Churn (1)'],
            y=cashback_churn.values,
            marker=dict(
                color=['#2ecc71', '#e74c3c'],
                line=dict(color='white', width=2)
            ),
            text=[f'${v:.2f}' for v in cashback_churn.values],
            textposition='outside',
            textfont=dict(size=14),
            hovertemplate='<b>%{x}</b><br>Cashback Prom: $%{y:.2f}<extra></extra>'
        )])
        fig.update_layout(
            title="Cashback Promedio por Estado de Churn",
            yaxis_title="Monto de Cashback Promedio",
            height=400,
            yaxis=dict(gridcolor='lightgray')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Satisfaction Analysis
    st.markdown("#### 😊 Distribución de Nivel de Satisfacción")
    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=df_filtered[df_filtered['Target'] == 0]['Nivel_Satisfaccion'],
        name='Activo',
        marker=dict(color='#2ecc71', line=dict(color='white', width=1)),
        opacity=0.75,
        hovertemplate='<b>Activo</b><br>Puntuación: %{x}<br>Cantidad: %{y}<extra></extra>'
    ))
    fig.add_trace(go.Histogram(
        x=df_filtered[df_filtered['Target'] == 1]['Nivel_Satisfaccion'],
        name='Churn',
        marker=dict(color='#e74c3c', line=dict(color='white', width=1)),
        opacity=0.75,
        hovertemplate='<b>Churn</b><br>Puntuación: %{x}<br>Cantidad: %{y}<extra></extra>'
    ))
    fig.update_layout(
        title="Distribución de Nivel de Satisfacción por Estado de Churn",
        xaxis_title="Nivel de Satisfacción",
        yaxis_title="Número de Clientes",
        barmode='overlay',
        height=400,
        legend=dict(font=dict(size=14)),
        xaxis=dict(gridcolor='lightgray'),
        yaxis=dict(gridcolor='lightgray')
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Churn Probability Distribution
    st.markdown("#### 📊 Distribución de Probabilidad de Churn")
    fig = go.Figure()
    colors = {'Bajo Riesgo': '#27ae60', 'Riesgo Medio': '#f39c12', 'Alto Riesgo': '#e74c3c'}
    for segment in ['Bajo Riesgo', 'Riesgo Medio', 'Alto Riesgo']:
        segment_data = df_filtered[df_filtered['Segmento_Riesgo'] == segment]['Probabilidad_Churn']
        fig.add_trace(go.Box(
            y=segment_data,
            name=segment,
            marker=dict(color=colors[segment]),
            boxmean='sd',
            hovertemplate='<b>%{fullData.name}</b><br>Probabilidad: %{y:.2%}<extra></extra>'
        ))
    fig.update_layout(
        title="Distribución de Probabilidad de Churn por Segmento de Riesgo",
        yaxis_title="Probabilidad de Churn",
        height=450,
        yaxis=dict(gridcolor='lightgray', tickformat='.0%'),
        legend=dict(font=dict(size=14))
    )
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.markdown("### 📋 Explorador de Datos")
    
    # Summary statistics
    st.markdown("#### 📊 Estadísticas Resumidas")
    summary_cols = ['Antiguedad', 'Monto_Cashback', 'Nivel_Satisfaccion', 'Probabilidad_Churn']
    st.dataframe(
        df_filtered[summary_cols].describe().style.format("{:.2f}"),
        use_container_width=True
    )
    
    # Raw data viewer
    st.markdown("#### 🔍 Visor de Datos Crudos")
    show_data = st.checkbox("Mostrar datos filtrados (primeras 100 filas)", value=False)
    
    if show_data:
        display_cols = ['Antiguedad', 'Monto_Cashback', 'Nivel_Satisfaccion', 'Queja', 
                       'Target', 'Segmento_Riesgo', 'Probabilidad_Churn']
        st.dataframe(
            df_filtered[display_cols].head(100).style.format({
                'Probabilidad_Churn': '{:.2%}',
                'Monto_Cashback': '${:.2f}'
            }),
            use_container_width=True
        )
    
    # Download section
    st.markdown("#### 💾 Descargar Datos")
    csv = df_filtered.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Descargar Datos Filtrados como CSV",
        data=csv,
        file_name='analisis_churn_filtrado.csv',
        mime='text/csv',
        help="Descargar el dataset actualmente filtrado"
    )

# Insights Section
st.markdown("---")
st.markdown("## 💡 Insights Clave y Recomendaciones Accionables")

st.markdown("""
<div class="insight-box">
<h3>🎯 Recomendaciones Estratégicas</h3>
<ul style="font-size: 16px;">
<li><strong>🏆 Enfoque en Onboarding:</strong> Clientes con menos de 3 meses tienen 3x más probabilidad de abandonar. Implementar programa de bienvenida robusto.</li>
<li><strong>💰 Optimizar Programa de Cashback:</strong> Clientes activos reciben 20% más cashback. Revisar y mejorar el programa de recompensas para clientes de alto riesgo.</li>
<li><strong>📞 Resolución de Quejas:</strong> Las quejas aumentan el churn en 26%. Crear protocolo "White Glove" para resolución inmediata.</li>
<li><strong>🎯 Atacar Segmento de Alto Riesgo:</strong> {high_risk_count:,} clientes requieren atención inmediata con ofertas personalizadas y contacto proactivo.</li>
<li><strong>😊 Monitorear Satisfacción:</strong> Clientes con puntuación <3 tienen alta probabilidad de churn. Implementar sistema de alertas automáticas.</li>
</ul>
</div>
""".format(high_risk_count=high_risk_count), unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px; background-color: #f8f9fa; border-radius: 10px;'>
<p style='font-size: 16px; margin: 0;'><strong>Equipo 70 - Data Science</strong> | No Country S11-25</p>
<p style='font-size: 14px; margin: 5px 0 0 0;'>Powered by Random Forest ML Model | Dashboard v2.0 (Español)</p>
</div>
""", unsafe_allow_html=True)
