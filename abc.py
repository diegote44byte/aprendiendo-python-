import pandas as pd 
import numpy as np 
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("US_Regional_Sales_Data.csv")
print(df.head()) 
print(df.dtypes)

df['Unit Price'] = df['Unit Price'].replace('[\$,]', '', regex=True).astype(float)
df['Unit Cost'] = df['Unit Cost'].replace('[\$,]', '', regex=True).astype(float)

# 4. VERIFICAMOS
print("\n--- DESPUÉS DE LA CONVERSIÓN ---")
print("Tipos de datos:")
print(df[['Unit Price', 'Unit Cost']].dtypes)
print("\nPrimeros valores de Unit Price (ahora números):")
print(df['Unit Price'].head())

print(f"Count: {df['Unit Price'].count()}") # muestra el conteo de valores no nulos en la columna "Amount"
print(f"Mean: {df['Unit Price'].mean():.2f}") 

df.filter(items=['Unit Price', 'Unit Cost'],axis=1) # describe muestra estadísticas descriptivas de las columnas seleccionadas #funciona mejor en jupyter notebooks 


