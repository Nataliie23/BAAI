#
# Natalia, 2025/10/22
# Short description of the task
# Apply correlation analysis to business problems

# 1. Input
# Data manipulation and analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv('Correlataion_Analysis_Data.csv')

df.info()

correlation_matrix = df.iloc[:,1:6].corr()

print(correlation_matrix.round(3))
#print(f'Correlation: {correlation:.2f}')
#print(f'P value:{pvalue:.4e}')

#if p_value < 0.05:
   # print("The correlation is statistically significant")
#print(df.isnull().sum())
#print ("Data loaded succesfully!")
#print (f"Dataset shape: {df.shape}")

# 2. Process

sns.heatmap(correlation_matrix)
plt.title('Natalia is the most intelligent person in the world')
plt.tight_layout()
plt.show()