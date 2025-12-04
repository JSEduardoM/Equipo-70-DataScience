# 📊 Análisis Exploratorio de Datos (EDA)

## 🎯 Objetivo

Realizar un análisis exploratorio completo del dataset de clientes de e-commerce para comprender las características de los datos, identificar patrones, detectar valores faltantes y preparar los datos para el modelado predictivo.

---

## 📁 Archivos en esta Carpeta

| Archivo | Descripción |
|---------|-------------|
| `eda_script.py` | Script automatizado para limpieza y análisis de datos |
| `eda_analysis.ipynb` | Notebook interactivo con análisis exploratorio |
| `EDA_E_Commerce.ipynb` | Notebook completo con visualizaciones detalladas |
| `etapa_EDA.ipynb` | Notebook de la etapa de EDA |
| `generate_notebook.py` | Script para generar notebooks automáticamente |

---

## 🚀 Cómo Ejecutar

### Opción 1: Script Automatizado
```bash
python EDA/eda_script.py
```

### Opción 2: Notebook Interactivo
```bash
jupyter notebook EDA/eda_analysis.ipynb
```

---

## 📈 Resultados Obtenidos

### 1. **Dataset Original**
- **Total de registros**: 3,941 clientes
- **Total de variables**: 12 variables (10 numéricas/categóricas + 1 variable objetivo)
- **Periodo de datos**: Datos históricos de comportamiento de clientes

### 2. **Limpieza de Datos**

#### Valores Faltantes Detectados:
| Variable | Valores Faltantes | % del Total |
|----------|-------------------|-------------|
| `Antiguedad` | 264 | 6.7% |
| `Distancia_Almacen` | 251 | 6.4% |
| `Nivel_Satisfaccion` | 73 | 1.9% |
| `Numero_Direcciones` | 136 | 3.5% |
| `Dias_Ultima_Compra` | 307 | 7.8% |

#### Estrategia de Imputación:
- **Variables numéricas**: Imputación con la **mediana** (más robusta ante outliers)
- **Variables categóricas**: Imputación con la **moda** (valor más frecuente)

### 3. **Estadísticas Descriptivas**

#### Variables Numéricas Clave:
| Variable | Media | Mediana | Desv. Std | Min | Max |
|----------|-------|---------|-----------|-----|-----|
| `Antiguedad` | 10.2 meses | 10 meses | 6.9 | 0 | 61 |
| `Distancia_Almacen` | 15.6 km | 14 km | 10.8 | 5 | 127 |
| `Numero_Dispositivos` | 3.8 | 4 | 1.0 | 1 | 6 |
| `Nivel_Satisfaccion` | 3.0 | 3 | 1.4 | 1 | 5 |
| `Dias_Ultima_Compra` | 4.6 días | 3 días | 3.7 | 0 | 46 |
| `Monto_Cashback` | 177.6 | 159.5 | 81.6 | 0 | 324.9 |

### 4. **Análisis de Correlaciones**

#### Correlaciones Más Fuertes con `Target` (Churn):
1. **`Antiguedad`**: -0.35 (correlación negativa fuerte)
   - ✅ Clientes con mayor antigüedad tienen **menor probabilidad de abandonar**
   
2. **`Queja`**: +0.25 (correlación positiva)
   - ⚠️ Clientes con quejas tienen **mayor probabilidad de churn**
   
3. **`Dias_Ultima_Compra`**: +0.18 (correlación positiva)
   - ⚠️ Más días sin comprar aumenta el riesgo de abandono
   
4. **`Monto_Cashback`**: -0.15 (correlación negativa)
   - ✅ Mayor cashback reduce la probabilidad de churn

### 5. **Distribución de la Variable Objetivo**

| Estado | Cantidad | Porcentaje |
|--------|----------|------------|
| **Activos** (Target=0) | 3,267 | 82.9% |
| **Churn** (Target=1) | 674 | 17.1% |

> ⚠️ **Desbalance de clases**: El dataset está desbalanceado (17.1% churn vs 82.9% activos). Esto se considerará en el modelado.

### 6. **Insights de Variables Categóricas**

#### Categoría Preferida (`Categoria_Preferida`):
- **Laptop & Accessory**: Categoría más popular
- **Mobile Phone**: Segunda categoría más frecuente
- **Fashion**: Tercera categoría

#### Estado Civil (`Estado_Civil`):
- **Married**: 40% de los clientes
- **Single**: 35% de los clientes
- **Divorced**: 25% de los clientes

---

## 📊 Outputs Generados

### Archivos de Datos:
1. **`datos/dataset_ecommerce_limpio_es.csv`**
   - Dataset limpio con valores faltantes imputados
   - Listo para modelado
   - 3,941 registros × 12 columnas

### Visualizaciones Generadas:
- Histogramas de distribución de variables numéricas
- Boxplots para detección de outliers
- Matriz de correlación (heatmap)
- Gráficos de barras para variables categóricas
- Análisis de la distribución de churn

---

## 🔍 Hallazgos Clave

### ✅ Insights Positivos:
1. **Antigüedad es protectora**: Clientes con más tiempo en la plataforma son más leales
2. **Cashback funciona**: El programa de recompensas reduce el churn
3. **Datos de calidad**: Solo 6-8% de valores faltantes en variables críticas

### ⚠️ Señales de Alerta:
1. **Quejas predicen churn**: Clientes con quejas tienen 25% más probabilidad de abandonar
2. **Inactividad es riesgosa**: Días sin comprar correlaciona con abandono
3. **Desbalance de clases**: Necesitaremos técnicas de balanceo en el modelado

### 🎯 Recomendaciones para Modelado:
1. **Features importantes**: Priorizar `Antiguedad`, `Queja`, `Dias_Ultima_Compra`, `Monto_Cashback`
2. **Normalización**: Aplicar escalado a variables numéricas
3. **Encoding**: Convertir variables categóricas a formato numérico
4. **Balanceo**: Considerar SMOTE o ajuste de pesos de clase

---

## 📝 Próximos Pasos

✅ **Completado**: Limpieza y análisis exploratorio  
➡️ **Siguiente**: Análisis de definición de churn (`Churn_Definition/`)

---

## 🛠️ Dependencias

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

---

## 👤 Autor

**Equipo 70 - Data Science**  
No Country - Simulación S11-25
