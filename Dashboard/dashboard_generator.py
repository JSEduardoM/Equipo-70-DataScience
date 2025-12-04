import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

# Set style
sns.set_palette("husl")

# Load data
try:
    df = pd.read_csv('datos/dataset_ecommerce_segmented.csv')
    print("Data loaded successfully.")
except FileNotFoundError:
    print("Error: Segmented data not found.")
    exit()

# Function to convert plot to base64
def plot_to_base64(fig):
    buffer = BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight', dpi=100)
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode()
    buffer.close()
    plt.close(fig)
    return image_base64

# Calculate metrics
total_customers = len(df)
churn_rate = df['Churn'].mean() * 100
active_customers = df[df['Churn'] == 0].shape[0]
churned_customers = df[df['Churn'] == 1].shape[0]
high_risk_count = df[df['Risk_Segment'] == 'High Risk'].shape[0]
medium_risk_count = df[df['Risk_Segment'] == 'Medium Risk'].shape[0]
low_risk_count = df[df['Risk_Segment'] == 'Low Risk'].shape[0]

# Generate visualizations
charts = {}

# 1. Churn Distribution Pie Chart
fig, ax = plt.subplots(figsize=(6, 6))
colors = ['#2ecc71', '#e74c3c']
sizes = [active_customers, churned_customers]
labels = [f'Active\n({active_customers})', f'Churned\n({churned_customers})']
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 12, 'weight': 'bold'})
ax.set_title('Customer Churn Distribution', fontsize=14, weight='bold', pad=20)
charts['churn_pie'] = plot_to_base64(fig)

# 2. Risk Segment Distribution
fig, ax = plt.subplots(figsize=(8, 5))
risk_counts = df['Risk_Segment'].value_counts()
colors_risk = ['#27ae60', '#f39c12', '#e74c3c']
bars = ax.bar(['Low Risk', 'Medium Risk', 'High Risk'], 
              [risk_counts.get('Low Risk', 0), risk_counts.get('Medium Risk', 0), risk_counts.get('High Risk', 0)],
              color=colors_risk, edgecolor='black', linewidth=1.5)
ax.set_ylabel('Number of Customers', fontsize=12, weight='bold')
ax.set_title('Customer Distribution by Risk Segment', fontsize=14, weight='bold', pad=20)
ax.grid(axis='y', alpha=0.3)
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height)}',
            ha='center', va='bottom', fontsize=11, weight='bold')
charts['risk_bar'] = plot_to_base64(fig)

# 3. Feature Importance (Top 8)
feature_importance = {
    'Tenure': 0.259,
    'CashbackAmount': 0.168,
    'WarehouseToHome': 0.103,
    'NumberOfAddress': 0.086,
    'DaySinceLastOrder': 0.081,
    'Complain': 0.069,
    'SatisfactionScore': 0.066,
    'NumberOfDeviceRegistered': 0.052
}
fig, ax = plt.subplots(figsize=(10, 6))
features = list(feature_importance.keys())
importances = list(feature_importance.values())
colors_gradient = plt.cm.viridis([i/len(features) for i in range(len(features))])
bars = ax.barh(features, importances, color=colors_gradient, edgecolor='black', linewidth=1.2)
ax.set_xlabel('Importance Score', fontsize=12, weight='bold')
ax.set_title('Top 8 Feature Importances (Random Forest)', fontsize=14, weight='bold', pad=20)
ax.grid(axis='x', alpha=0.3)
for i, bar in enumerate(bars):
    width = bar.get_width()
    ax.text(width, bar.get_y() + bar.get_height()/2.,
            f'{importances[i]:.3f}',
            ha='left', va='center', fontsize=10, weight='bold', color='black')
charts['feature_importance'] = plot_to_base64(fig)

# 4. Tenure vs Churn
fig, ax = plt.subplots(figsize=(8, 5))
tenure_churn = df.groupby('Churn')['Tenure'].mean()
colors_tenure = ['#2ecc71', '#e74c3c']
bars = ax.bar(['Active (0)', 'Churned (1)'], tenure_churn.values, color=colors_tenure, edgecolor='black', linewidth=1.5)
ax.set_ylabel('Average Tenure (months)', fontsize=12, weight='bold')
ax.set_title('Average Tenure by Churn Status', fontsize=14, weight='bold', pad=20)
ax.grid(axis='y', alpha=0.3)
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.1f}',
            ha='center', va='bottom', fontsize=11, weight='bold')
charts['tenure_churn'] = plot_to_base64(fig)

# 5. Cashback vs Churn
fig, ax = plt.subplots(figsize=(8, 5))
cashback_churn = df.groupby('Churn')['CashbackAmount'].mean()
bars = ax.bar(['Active (0)', 'Churned (1)'], cashback_churn.values, color=colors_tenure, edgecolor='black', linewidth=1.5)
ax.set_ylabel('Average Cashback Amount', fontsize=12, weight='bold')
ax.set_title('Average Cashback by Churn Status', fontsize=14, weight='bold', pad=20)
ax.grid(axis='y', alpha=0.3)
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'${height:.2f}',
            ha='center', va='bottom', fontsize=11, weight='bold')
charts['cashback_churn'] = plot_to_base64(fig)

# 6. Satisfaction Score Distribution
fig, ax = plt.subplots(figsize=(8, 5))
df_active = df[df['Churn'] == 0]['SatisfactionScore']
df_churned = df[df['Churn'] == 1]['SatisfactionScore']
ax.hist([df_active, df_churned], bins=5, label=['Active', 'Churned'], color=['#2ecc71', '#e74c3c'], edgecolor='black', alpha=0.7)
ax.set_xlabel('Satisfaction Score', fontsize=12, weight='bold')
ax.set_ylabel('Number of Customers', fontsize=12, weight='bold')
ax.set_title('Satisfaction Score Distribution by Churn Status', fontsize=14, weight='bold', pad=20)
ax.legend(fontsize=11)
ax.grid(axis='y', alpha=0.3)
charts['satisfaction_dist'] = plot_to_base64(fig)

# Generate HTML
html_content = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-commerce Churn Analysis Dashboard</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 36px;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }}
        
        .header p {{
            font-size: 16px;
            opacity: 0.9;
        }}
        
        .metrics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8f9fa;
        }}
        
        .metric-card {{
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border-left: 5px solid;
        }}
        
        .metric-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }}
        
        .metric-card.primary {{ border-left-color: #667eea; }}
        .metric-card.success {{ border-left-color: #2ecc71; }}
        .metric-card.danger {{ border-left-color: #e74c3c; }}
        .metric-card.warning {{ border-left-color: #f39c12; }}
        
        .metric-label {{
            font-size: 14px;
            color: #7f8c8d;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 10px;
            font-weight: 600;
        }}
        
        .metric-value {{
            font-size: 36px;
            font-weight: bold;
            color: #2c3e50;
        }}
        
        .metric-subtitle {{
            font-size: 12px;
            color: #95a5a6;
            margin-top: 5px;
        }}
        
        .content {{
            padding: 30px;
        }}
        
        .section {{
            margin-bottom: 50px;
        }}
        
        .section-title {{
            font-size: 24px;
            color: #2c3e50;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
            display: inline-block;
        }}
        
        .chart-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
            gap: 30px;
            margin-top: 20px;
        }}
        
        .chart-container {{
            background: white;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }}
        
        .chart-container:hover {{
            transform: scale(1.02);
        }}
        
        .chart-container img {{
            width: 100%;
            height: auto;
            border-radius: 10px;
        }}
        
        .insights-box {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 15px;
            padding: 30px;
            margin-top: 30px;
        }}
        
        .insights-box h3 {{
            font-size: 22px;
            margin-bottom: 15px;
        }}
        
        .insights-box ul {{
            list-style: none;
            padding-left: 0;
        }}
        
        .insights-box li {{
            padding: 10px 0;
            padding-left: 30px;
            position: relative;
        }}
        
        .insights-box li:before {{
            content: "✓";
            position: absolute;
            left: 0;
            font-weight: bold;
            font-size: 18px;
        }}
        
        .model-performance {{
            background: #ecf0f1;
            border-radius: 15px;
            padding: 25px;
            margin-top: 20px;
        }}
        
        .model-performance h4 {{
            color: #2c3e50;
            margin-bottom: 15px;
            font-size: 18px;
        }}
        
        .performance-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
        }}
        
        .performance-item {{
            background: white;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
        }}
        
        .performance-item .label {{
            font-size: 12px;
            color: #7f8c8d;
            margin-bottom: 5px;
        }}
        
        .performance-item .value {{
            font-size: 24px;
            font-weight: bold;
            color: #667eea;
        }}
        
        .footer {{
            background: #2c3e50;
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 14px;
        }}
        
        @media (max-width: 768px) {{
            .chart-grid {{
                grid-template-columns: 1fr;
            }}
            
            .metrics-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 E-commerce Churn Analysis Dashboard</h1>
            <p>Análisis Predictivo de Abandono de Clientes | Random Forest Model</p>
        </div>
        
        <div class="metrics-grid">
            <div class="metric-card primary">
                <div class="metric-label">Total Customers</div>
                <div class="metric-value">{total_customers:,}</div>
                <div class="metric-subtitle">Base de clientes</div>
            </div>
            
            <div class="metric-card success">
                <div class="metric-label">Active Customers</div>
                <div class="metric-value">{active_customers:,}</div>
                <div class="metric-subtitle">{(active_customers/total_customers*100):.1f}% del total</div>
            </div>
            
            <div class="metric-card danger">
                <div class="metric-label">Churned Customers</div>
                <div class="metric-value">{churned_customers:,}</div>
                <div class="metric-subtitle">{churn_rate:.1f}% tasa de churn</div>
            </div>
            
            <div class="metric-card warning">
                <div class="metric-label">High Risk</div>
                <div class="metric-value">{high_risk_count:,}</div>
                <div class="metric-subtitle">Requieren atención inmediata</div>
            </div>
        </div>
        
        <div class="content">
            <div class="model-performance">
                <h4>🤖 Random Forest Model Performance</h4>
                <div class="performance-grid">
                    <div class="performance-item">
                        <div class="label">Accuracy</div>
                        <div class="value">93.4%</div>
                    </div>
                    <div class="performance-item">
                        <div class="label">Precision</div>
                        <div class="value">88.8%</div>
                    </div>
                    <div class="performance-item">
                        <div class="label">Recall</div>
                        <div class="value">70.4%</div>
                    </div>
                    <div class="performance-item">
                        <div class="label">ROC-AUC</div>
                        <div class="value">0.97</div>
                    </div>
                </div>
            </div>
            
            <div class="section">
                <h2 class="section-title">📈 Churn Overview</h2>
                <div class="chart-grid">
                    <div class="chart-container">
                        <img src="data:image/png;base64,{charts['churn_pie']}" alt="Churn Distribution">
                    </div>
                    <div class="chart-container">
                        <img src="data:image/png;base64,{charts['risk_bar']}" alt="Risk Segments">
                    </div>
                </div>
            </div>
            
            <div class="section">
                <h2 class="section-title">🎯 Feature Importance Analysis</h2>
                <div class="chart-container">
                    <img src="data:image/png;base64,{charts['feature_importance']}" alt="Feature Importance">
                </div>
            </div>
            
            <div class="section">
                <h2 class="section-title">🔍 Key Drivers Analysis</h2>
                <div class="chart-grid">
                    <div class="chart-container">
                        <img src="data:image/png;base64,{charts['tenure_churn']}" alt="Tenure vs Churn">
                    </div>
                    <div class="chart-container">
                        <img src="data:image/png;base64,{charts['cashback_churn']}" alt="Cashback vs Churn">
                    </div>
                </div>
                <div class="chart-container" style="margin-top: 30px;">
                    <img src="data:image/png;base64,{charts['satisfaction_dist']}" alt="Satisfaction Distribution">
                </div>
            </div>
            
            <div class="insights-box">
                <h3>💡 Key Insights & Recommendations</h3>
                <ul>
                    <li><strong>Tenure is Critical:</strong> Clientes con menor antigüedad tienen 3x más probabilidad de abandonar. Mejorar onboarding en primeros 3 meses.</li>
                    <li><strong>Cashback Works:</strong> Clientes activos reciben 20% más cashback en promedio. Optimizar programa de recompensas.</li>
                    <li><strong>Complaints Matter:</strong> Quejas aumentan churn en 26%. Implementar protocolo de resolución rápida.</li>
                    <li><strong>High Risk Segment:</strong> {high_risk_count} clientes requieren intervención inmediata con ofertas personalizadas.</li>
                    <li><strong>Satisfaction Score:</strong> Clientes con score <3 tienen alta probabilidad de churn. Monitorear y actuar proactivamente.</li>
                </ul>
            </div>
        </div>
        
        <div class="footer">
            <p>Equipo 70 - Data Science | No Country S11-25 | Powered by Random Forest ML Model</p>
        </div>
    </div>
</body>
</html>
"""

with open('Dashboard/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Enhanced dashboard generated successfully at 'Dashboard/dashboard.html'")
print(f"📊 Total charts embedded: {len(charts)}")
print("🚀 Open the file in your browser to view the interactive dashboard!")
