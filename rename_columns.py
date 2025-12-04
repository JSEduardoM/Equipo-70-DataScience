import pandas as pd

# Load original data
df = pd.read_csv('datos/data_ecommerce_customer_churn.csv')

print("Original columns:", df.columns.tolist())

# Rename columns to Spanish
df.rename(columns={
    'Tenure': 'Antiguedad',
    'WarehouseToHome': 'Distancia_Almacen',
    'NumberOfDeviceRegistered': 'Numero_Dispositivos',
    'PreferedOrderCat': 'Categoria_Preferida',
    'SatisfactionScore': 'Nivel_Satisfaccion',
    'MaritalStatus': 'Estado_Civil',
    'NumberOfAddress': 'Numero_Direcciones',
    'Complain': 'Queja',
    'DaySinceLastOrder': 'Dias_Ultima_Compra',
    'CashbackAmount': 'Monto_Cashback',
    'Churn': 'Target'
}, inplace=True)

print("\nRenamed columns:", df.columns.tolist())

# Save renamed dataset
df.to_csv('datos/data_ecommerce_customer_churn_es.csv', index=False)
print("\n✅ Dataset saved to 'datos/data_ecommerce_customer_churn_es.csv'")

# Also create a mapping file for reference
mapping = {
    'Tenure': 'Antiguedad',
    'WarehouseToHome': 'Distancia_Almacen',
    'NumberOfDeviceRegistered': 'Numero_Dispositivos',
    'PreferedOrderCat': 'Categoria_Preferida',
    'SatisfactionScore': 'Nivel_Satisfaccion',
    'MaritalStatus': 'Estado_Civil',
    'NumberOfAddress': 'Numero_Direcciones',
    'Complain': 'Queja',
    'DaySinceLastOrder': 'Dias_Ultima_Compra',
    'CashbackAmount': 'Monto_Cashback',
    'Churn': 'Target'
}

mapping_df = pd.DataFrame(list(mapping.items()), columns=['English', 'Spanish'])
mapping_df.to_csv('datos/column_mapping.csv', index=False)
print("✅ Column mapping saved to 'datos/column_mapping.csv'")
