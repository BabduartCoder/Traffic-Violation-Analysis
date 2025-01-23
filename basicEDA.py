import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df_long = pd.read_csv(r'C:\Users\duart\Desktop\Traffic Violations Project\Traffic-Violation-Analysis\Databases\cleaned_data.csv')

print(df_long.head())

# Get summary statistics and missing values
print(df_long.describe())
print(df_long.isnull().sum())

#visualizations start here
sns.set_style("whitegrid")

# Plot the total counts per year
plt.figure(figsize=(12, 6))
sns.barplot(x='Year', y='Value', data=df_long, estimator=sum, ci=None)
plt.title('Total Counts per Year')
plt.xlabel('Year')
plt.ylabel('Total Counts')
plt.xticks(rotation=45)
plt.show()

# Plot the counts by Violation Group
plt.figure(figsize=(14, 8))
sns.barplot(x='Violation_Group', y='Value', data=df_long, estimator=sum, ci=None)
plt.title('Total Counts by Violation Group')
plt.xlabel('Violation Group')
plt.ylabel('Total Counts')
plt.xticks(rotation=90)
plt.show()

# Plot the counts by Department
plt.figure(figsize=(14, 8))
sns.barplot(x='Category', y='Value', data=df_long, estimator=sum, ci=None)
plt.title('Total Counts by Department')
plt.xlabel('Category')
plt.ylabel('Total Counts')
plt.xticks(rotation=90)
plt.show()

# Heatmap of counts by Year and Violation Group
pivot_table = df_long.pivot_table(values='Value', index='Violation_Group', columns='Year', aggfunc='sum')
plt.figure(figsize=(14, 10))
sns.heatmap(pivot_table, annot=True, fmt="g", cmap='viridis')
plt.title('Heatmap of Counts by Year and Violation Group')
plt.xlabel('Year')
plt.ylabel('Violation Group')
plt.show()

# Line plot of counts over time for each Violation Group
plt.figure(figsize=(14, 8))
sns.lineplot(x='Year', y='Value', hue='Violation_Group', data=df_long, estimator=sum)
plt.title('Counts Over Time for Each Violation Group')
plt.xlabel('Year')
plt.ylabel('Total Counts')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()