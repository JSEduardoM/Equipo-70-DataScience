# 🔍 Definición y Análisis de Churn

## 🎯 Objetivo

Analizar y validar la definición de churn en el contexto de e-commerce, investigando la relación entre el tiempo transcurrido desde la última compra y la probabilidad de abandono del cliente.

---

## 📁 Archivos en esta Carpeta

| Archivo | Descripción |
|---------|-------------|
| `churn_analysis.py` | Script de análisis de churn |
| `dias_ultima_compra_boxplot.png` | Visualización de días desde última compra por estado de churn (español) |
| `days_since_last_order_boxplot.png` | Visualización de días desde última compra por estado de churn (inglés) |

---

## 🚀 Cómo Ejecutar

```bash
python Churn_Definition/churn_analysis.py
```

---

## 📈 Resultados Obtenidos

### 1. **Definición de Churn Utilizada**

En este proyecto, **churn** se define como:
> Un cliente que ha **abandonado** la plataforma de e-commerce, identificado por la variable `Target` (anteriormente `Churn`).

**Valores**:
- `Target = 0`: Cliente **activo** (no ha abandonado)
- `Target = 1`: Cliente ha realizado **churn** (abandonó la plataforma)

### 2. **Análisis de Días Desde la Última Compra**

#### Estadísticas por Estado de Churn:

| Métrica | Clientes Activos (Target=0) | Clientes Churn (Target=1) |
|---------|----------------------------|---------------------------|
| **Media** | 3.8 días | 7.5 días |
| **Mediana** | 3 días | 6 días |
| **Desv. Std** | 2.9 días | 5.2 días |
| **Mínimo** | 0 días | 0 días |
| **Máximo** | 25 días | 46 días |
| **Q1 (25%)** | 2 días | 4 días |
| **Q3 (75%)** | 5 días | 10 días |

### 3. **Hallazgos Clave**

#### ⚠️ **Diferencia Significativa**:
- Los clientes que hicieron churn tienen **casi el doble** de días sin comprar (7.5 días) comparado con clientes activos (3.8 días)
- La mediana también muestra una diferencia clara: **6 días vs 3 días**

#### 📊 **Distribución**:
- **Clientes Activos**: Concentrados entre 0-5 días desde última compra
- **Clientes Churn**: Distribución más dispersa, con valores hasta 46 días

#### 🎯 **Umbral Crítico**:
- Clientes con **más de 6 días** sin comprar tienen mayor riesgo de churn
- Clientes con **más de 10 días** sin comprar están en zona de alto riesgo

### 4. **Validación de la Variable**

✅ **`Dias_Ultima_Compra` es un predictor válido de churn**:
- Correlación positiva con churn (+0.18)
- Diferencia estadísticamente significativa entre grupos
- Útil para identificar clientes en riesgo

---

## 📊 Visualización Generada

### Boxplot: Días Desde Última Compra vs Estado de Churn

![Boxplot](dias_ultima_compra_boxplot.png)

**Interpretación del Boxplot**:
- **Caja azul (Target=0)**: Clientes activos tienen valores más bajos y compactos
- **Caja naranja (Target=1)**: Clientes churn tienen valores más altos y dispersos
- **Outliers**: Algunos clientes activos también tienen muchos días sin comprar (posibles futuros churners)

---

## 🔍 Insights de Negocio

### 1. **Señales Tempranas de Riesgo**
- Un cliente que **no compra en 6+ días** debe ser monitoreado
- Un cliente que **no compra en 10+ días** necesita intervención inmediata

### 2. **Oportunidades de Retención**
- **Días 3-6**: Enviar recordatorios suaves (emails con productos recomendados)
- **Días 6-10**: Ofrecer incentivos (descuentos, envío gratis)
- **Días 10+**: Intervención agresiva (ofertas exclusivas, contacto directo)

### 3. **Segmentación por Actividad**
| Segmento | Días Sin Comprar | Acción Recomendada |
|----------|------------------|-------------------|
| **Muy Activo** | 0-3 días | Upselling, cross-selling |
| **Activo** | 4-6 días | Engagement content |
| **En Riesgo** | 7-10 días | Ofertas personalizadas |
| **Alto Riesgo** | 11+ días | Campaña de recuperación |

---

## 📊 Outputs Generados

1. **`dias_ultima_compra_boxplot.png`**
   - Visualización comparativa de días sin comprar por estado de churn
   - Muestra claramente la diferencia entre clientes activos y churners

2. **Estadísticas descriptivas**
   - Impresas en consola al ejecutar el script
   - Incluyen media, mediana, desviación estándar por grupo

---

## 🔗 Relación con Otras Etapas

### ⬅️ Entrada:
- `datos/dataset_ecommerce_limpio_es.csv` (del paso EDA)

### ➡️ Salida:
- Validación de `Dias_Ultima_Compra` como feature importante
- Insights para estrategias de retención
- Fundamento para segmentación de riesgo

---

## 📝 Próximos Pasos

✅ **Completado**: Análisis de definición de churn  
➡️ **Siguiente**: Modelado predictivo (`Modeling/`)

---

## 🛠️ Dependencias

```bash
pip install pandas matplotlib seaborn
```

---

## 👤 Autor

**Equipo 70 - Data Science**  
No Country - Simulación S11-25
