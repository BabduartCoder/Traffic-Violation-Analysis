import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
data = pd.read_csv(r'C:\Users\duart\Desktop\Traffic Violations Project\Palm Beach County 2011-2023 CLEAN.csv')

# Example: Summary statistics
print(data.describe())
print(data.isnull().sum())

# Calculate specific statistics
print("Mean Values:")
print(data.mean())

print("Median Values:")
print(data.median())

print("Ranges:")
print(data.max() - data.min())

print(data['Guilty Count'].describe())
print(data['YEAR'].value_counts())


# Example: Visualization
sns.lineplot(data=data, x='YEAR', y='Guilty Count')
plt.show()

#example 2
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

#example 3
import plotly.express as px
fig = px.line(data, x='YEAR', y='Guilty Count', title="Interactive Traffic Trends")
fig.show()
