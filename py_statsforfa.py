### curso de coursera , usaremos pandas , numpy , matplotlib , statsmodels
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf # Para usar fórmulas

# hice pip install en el powershell de windows 

df = pd.read_csv('stock_5_years.csv')
df.head()

df["short_name"] = df["Country"].str[:3] # Crear una nueva columna con las primeras 3 letras del país

df.head(3)