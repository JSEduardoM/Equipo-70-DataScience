import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set plot style
sns.set(style="whitegrid")

# Load data with Spanish columns
try:
    df = pd.read_csv('datos/data_ecommerce_customer_churn_es.csv')
    print("Data loaded successfully.")
except FileNotFoundError:
    print("Error: File not found.")
    exit()

# 1. Data Inspection
print("\n--- Información del Dataset ---")
print(df.info())

print("\n--- Primeras 5 filas ---")
print(df.head())

print("\n--- Valores Faltantes ---")
print(df.isnull().sum())

print("\n--- Duplicados ---")
print(f"Duplicados: {df.duplicated().sum()}")

# 2. Data Cleaning
print("\n--- Manejando Valores Faltantes ---")
missing_cols = df.columns[df.isnull().any()].tolist()
print(f"Columnas con valores faltantes: {missing_cols}")

for col in missing_cols:
    if df[col].dtype == 'object':
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].median())

print("Valores faltantes después de imputación:")
print(df.isnull().sum())

# 3. Univariate Analysis
print("\n--- Distribución de la Variable Objetivo (Target) ---")
print(df['Target'].value_counts(normalize=True))

print("\n--- Resumen Numérico ---")
print(df.describe())

# 4. Bivariate Analysis
print("\n--- Matriz de Correlación ---")
numeric_df = df.select_dtypes(include=[np.number])
corr_matrix = numeric_df.corr()
print(corr_matrix['Target'].sort_values(ascending=False))

# Save cleaned data for next steps
df.to_csv('datos/dataset_ecommerce_limpio_es.csv', index=False)
print("\nDataset limpio guardado en 'datos/dataset_ecommerce_limpio_es.csv'")
