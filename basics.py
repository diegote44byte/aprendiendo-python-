import pandas as pd 
import numpy as np 
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("US_Regional_Sales_Data.csv")
print(df.head()) 
print(df.dtypes)

#arreglos porque unit price es string , tambien arreglamos unit cost
df['Unit Price'] = df['Unit Price'].replace('[\$,]', '', regex=True).astype(float)
df['Unit Cost'] = df['Unit Cost'].replace('[\$,]', '', regex=True).astype(float)

# 4. VERIFICAMOS
print("\n--- DESPUÉS DE LA CONVERSIÓN ---")
print("Tipos de datos:")
print(df[['Unit Price', 'Unit Cost']].dtypes)
print("\nPrimeros valores de Unit Price (ahora números):")
print(df['Unit Price'].head())


# Descriptive statistics
print("Basics Statistics:")

df.shape
print(df.shape) # muestra muchas filas y 16 columnas

print(f"Count: {df['Unit Price'].count()}") # muestra el conteo de valores no nulos en la columna "Amount"
print(f"Mean: {df['Unit Price'].mean():.2f}") # muestra el promedio de la columna "Amount"
print(f"Median: {df['Unit Price'].median():.2f}") # muestra la mediana de la columna "Amount"
print(f"Mode: {df['Unit Price'].mode()[0]:.2f}") # muestra la moda de la columna "Amount"
print(f"Standard Deviation: {df['Unit Price'].std():.2f}") # muestra la desviación estándar de la columna "Amount"
print(f"Variance: {df['Unit Price'].var():.2f}") # muestra la varianza de la columna "Amount"
print(f"Minimum: {df['Unit Price'].min():.2f}") # muestra el valor mínimo de la columna "Amount"
print(f"Maximum: {df['Unit Price'].max():.2f}") # muestra el valor máximo de la columna "Amount"
print(f"Range: {df['Unit Price'].max() - df['Unit Price'].min():.2f}") # muestra el rango de la columna "Amount"

## percentiles y quartiles (graficar con boxplot)
print(f"25th Percentile: {df['Unit Price'].quantile(0.25):.2f}")
print(f"50th Percentile (Median): {df['Unit Price'].quantile(0.50):.2f}")
print(f"75th Percentile: {df['Unit Price'].quantile(0.75):.2f}")
print(f"90th Percentile: {df['Unit Price'].quantile(0.90):.2f}")

# Boxplot (horizontal) 
plt.figure(figsize=(8, 6))
sns.boxplot(x=df['Unit Price'])
plt.title("Boxplot of Unit Price")
plt.xlabel("Unit Price")
plt.show()

#figura en vertical
df['Unit Price'].plot(kind='box',figsize=(8,6))
plt.title("Boxplot of Unit Price")
plt.xlabel("Unit Price")
plt.show()

#outlier detection (IQR Method) 

