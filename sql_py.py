import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Liquidez": [1.4, 1.6, 1.8],
    "Endeudamiento": [0.6, 0.55, 0.5],
    "Rentabilidad": [0.08, 0.09, 0.1]
}

df = pd.DataFrame(data, index=["2023", "2024", "2025"])

sns.heatmap(df, annot=True, cmap="YlGnBu")
plt.show()

