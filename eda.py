import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
data = pd.read_csv(r'C:\Users\duart\Desktop\Traffic Violations Project\Palm Beach County - 2020-2023 CLEAN.csv')

# Example: Summary statistics
print(data.describe())

# Example: Visualization
sns.lineplot(data=data, x='YEAR', y='Guilty Count')
plt.show()
