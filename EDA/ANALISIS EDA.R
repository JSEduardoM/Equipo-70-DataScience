# ==========================================
# ANÁLISIS DE COMPORTAMIENTO DE CLIENTES (CHURN) EN R
# ==========================================

# Cargar librerías necesarias
library(dplyr)
library(ggplot2)
library(readr)
library(corrplot)

# 1️⃣ Carga de datos
datos <- read.csv("~/No-Country-Ciencia-Datos/S11-25-Equipo-70-DataScience/datos/online_retail_customer_churn.csv")


# Vista previa de los datos
head(datos)
tail(datos)
str(datos)
summary(datos)

# Conteo de categorías
table(datos$Gender)
table(datos$Promotion_Response)

# 2️⃣ Limpieza y renombrado de variables (en español)
datos <- datos %>%
  rename(
    Edad = Age,
    Genero = Gender,
    Ingreso_Anual = Annual_Income,
    Total_Gastado = Total_Spend,
    Anios_como_cliente = Years_as_Customer,
    Numeros_Compras = Num_of_Purchases,
    Importe_Promedio_Transaccion = Average_Transaction_Amount,
    Numero_de_Devoluciones = Num_of_Returns,
    Cantidad_de_Contactos_Soporte = Num_of_Support_Contacts,
    Nivel_Satisfaccion = Satisfaction_Score,
    Ultimo_dia_compra = Last_Purchase_Days_Ago,
    Esta_Suscripto_via_Email = Email_Opt_In,
    Respuesta_a_Promocion = Promotion_Response,
    Target = Target_Churn
  )

# Convertir variables a tipos adecuados
datos$Genero <- tolower(as.character(datos$Genero))
datos$Respuesta_a_Promocion <- tolower(as.character(datos$Respuesta_a_Promocion))
datos$Esta_Suscripto_via_Email <- as.integer(datos$Esta_Suscripto_via_Email)
datos$Target <- as.integer(datos$Target)
datos$Ingreso_Anual <- datos$Ingreso_Anual * 1000

# 3️⃣ Selección de variables de comportamiento incluyendo interacción con campañas
variables_comportamiento <- c(
  "Numeros_Compras",
  "Importe_Promedio_Transaccion",
  "Ultimo_dia_compra",
  "Cantidad_de_Contactos_Soporte",
  "Numero_de_Devoluciones",
  "Total_Gastado",
  "Anios_como_cliente",
  "Esta_Suscripto_via_Email",
  "Respuesta_a_Promocion",
  "Target"
)

datos_comportamiento <- datos[, variables_comportamiento]

# 4️⃣ Separar variables numéricas y categóricas
numericas <- datos_comportamiento %>% select_if(is.numeric)
categoricas <- datos_comportamiento %>% select_if(Negate(is.numeric))

cat("Variables numéricas de comportamiento:\n")
print(names(numericas))
cat("Variables categóricas de comportamiento:\n")
print(names(categoricas))

# 5️⃣ Histogramas para variables numéricas
for(col in names(numericas)){
  ggplot(datos_comportamiento, aes_string(x=col)) +
    geom_histogram(binwidth=30, fill="steelblue", color="black", alpha=0.7) +
    geom_density(aes(y=30*..count..), color="red") + 
    labs(title=paste("Distribución de", col), x=col, y="Frecuencia") +
    theme_minimal() -> p
  print(p)
}

# 6️⃣ Boxplots para variables numéricas
for(col in names(numericas)){
  ggplot(datos_comportamiento, aes_string(x=col)) +
    geom_boxplot(fill="lightblue") +
    labs(title=paste("Boxplot de", col), x=col) +
    theme_minimal() -> p
  print(p)
}

# 7️⃣ Gráficos de barras para variables categóricas (incluye Respuesta_a_Promocion y Target)
for(col in names(categoricas)){
  ggplot(datos_comportamiento, aes_string(x=col)) +
    geom_bar(fill="orange") +
    labs(title=paste("Distribución de", col), x=col, y="Cantidad") +
    theme_minimal() +
    theme(axis.text.x = element_text(angle=45, hjust=1)) -> p
  print(p)
}

# 8️⃣ Matriz de correlación para variables numéricas
corr <- cor(numericas)
corrplot(corr, method="color", type="upper", addCoef.col = "black", tl.cex=0.8, number.cex=0.7)
title("Matriz de Correlaciones – Variables de Comportamiento")

# 9️⃣ Identificación de correlaciones fuertes (>0.5 o <-0.5)
correlaciones_fuertes <- corr
correlaciones_fuertes[abs(correlaciones_fuertes) < 0.5] <- NA
cat("Correlaciones fuertes (>0.5 o <-0.5):\n")
print(correlaciones_fuertes)
