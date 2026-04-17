import pandas as pd

df = pd.read_csv('C:/Users/sande/Desktop/DATA_ANALYST_PORTFOLIO/P9_HEALTHCARE_ANALYSIS/data/insurance.csv')

print(df.head())
print(df.info())
print(df.describe())

print("Average Medical Cost:", df['charges'].mean())

print(df.groupby('smoker')['charges'].mean())

print(df.groupby('region')['charges'].mean())

print(df.groupby('sex')['charges'].mean())

import matplotlib.pyplot as plt
import seaborn as sns

sns.boxplot(x='smoker', y='charges', data=df)
plt.savefig('C:/Users/sande/Desktop/DATA_ANALYST_PORTFOLIO/P9_HEALTHCARE_ANALYSIS/images/smoker_cost.png')
plt.show()

sns.barplot(x='region', y='charges', data=df)
plt.savefig('C:/Users/sande/Desktop/DATA_ANALYST_PORTFOLIO/P9_HEALTHCARE_ANALYSIS/images/region_cost.png')
plt.show()

sns.scatterplot(x='bmi', y='charges', hue='smoker', data=df)
plt.savefig('C:/Users/sande/Desktop/DATA_ANALYST_PORTFOLIO/P9_HEALTHCARE_ANALYSIS/images/bmi_cost.png')
plt.show()
