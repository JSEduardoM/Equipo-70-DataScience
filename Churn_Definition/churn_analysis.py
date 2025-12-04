import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load data
try:
    df = pd.read_csv('datos/dataset_ecommerce_limpio_es.csv')
    print("Data loaded successfully.")
except FileNotFoundError:
    print("Error: File not found. Please run EDA first.")
    exit()

# Analysis of Dias_Ultima_Compra vs Target
print("\n--- Estadísticas de Dias_Ultima_Compra por Target ---")
print(df.groupby('Target')['Dias_Ultima_Compra'].describe())

# Visualizing
plt.figure(figsize=(10, 6))
sns.boxplot(x='Target', y='Dias_Ultima_Compra', data=df)
plt.title('Días Desde Última Compra por Estado de Churn')
plt.xlabel('Target (0=Activo, 1=Churn)')
plt.ylabel('Días Desde Última Compra')
plt.savefig('Churn_Definition/dias_ultima_compra_boxplot.png')
print("\nBoxplot guardado en 'Churn_Definition/dias_ultima_compra_boxplot.png'")

# Check for a potential threshold
print("\n--- Análisis de Umbral ---")
for days in [30, 45, 60, 90]:
    churn_rate_above = df[df['Dias_Ultima_Compra'] > days]['Target'].mean()
    count_above = df[df['Dias_Ultima_Compra'] > days].shape[0]
    print(f"Días > {days}: Count={count_above}, Tasa de Churn={churn_rate_above:.2f}")

# Check overlap
min_churn_days = df[df['Target'] == 1]['Dias_Ultima_Compra'].min()
max_active_days = df[df['Target'] == 0]['Dias_Ultima_Compra'].max()
print(f"\nMín Dias_Ultima_Compra para Target=1: {min_churn_days}")
print(f"Máx Dias_Ultima_Compra para Target=0: {max_active_days}")
