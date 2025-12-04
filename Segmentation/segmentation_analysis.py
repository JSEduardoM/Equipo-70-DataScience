import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

# Load data
try:
    df = pd.read_csv('datos/dataset_ecommerce_limpio_es.csv')
    print("Data loaded successfully.")
except FileNotFoundError:
    print("Error: File not found. Please run EDA first.")
    exit()

# Preprocessing
X = df.drop('Target', axis=1)
y = df['Target']

categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
numerical_cols = X.select_dtypes(include=[np.number]).columns.tolist()

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ])

# Train Random Forest (Full dataset for segmentation)
rf_model = RandomForestClassifier(random_state=42)
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('classifier', rf_model)])

print("Entrenando modelo Random Forest en dataset completo...")
pipeline.fit(X, y)

# Predict Probabilities
churn_probs = pipeline.predict_proba(X)[:, 1]
df['Probabilidad_Churn'] = churn_probs

# Define Segments
def define_segment(prob):
    if prob > 0.7:
        return 'Alto Riesgo'
    elif prob > 0.3:
        return 'Riesgo Medio'
    else:
        return 'Bajo Riesgo'

df['Segmento_Riesgo'] = df['Probabilidad_Churn'].apply(define_segment)

# Segment Distribution
print("\n--- Distribución de Segmentos ---")
print(df['Segmento_Riesgo'].value_counts(normalize=True))

# Segment Profiles
print("\n--- Perfiles de Segmentos (Valores Promedio) ---")
numeric_cols_for_profile = ['Antiguedad', 'Monto_Cashback', 'Nivel_Satisfaccion', 'Dias_Ultima_Compra', 'Probabilidad_Churn']
profile = df.groupby('Segmento_Riesgo')[numeric_cols_for_profile].mean()
print(profile)

# Save Segmented Data
df.to_csv('datos/dataset_ecommerce_segmentado_es.csv', index=False)
print("\nDataset segmentado guardado en 'datos/dataset_ecommerce_segmentado_es.csv'")

# Visualize Segments
plt.figure(figsize=(8, 5))
sns.countplot(x='Segmento_Riesgo', data=df, order=['Bajo Riesgo', 'Riesgo Medio', 'Alto Riesgo'], palette='viridis')
plt.title('Distribución de Clientes por Riesgo de Churn')
plt.savefig('Segmentation/distribucion_segmentos_riesgo.png')
print("Gráfico de distribución guardado en 'Segmentation/distribucion_segmentos_riesgo.png'")
