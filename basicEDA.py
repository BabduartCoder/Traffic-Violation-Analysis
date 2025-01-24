# Benedicto Amaty
# Date: 2025-01-23
# Description: This script performs basic exploratory data analysis (EDA) on the cleaned dataset.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df_long = pd.read_csv(r'C:\Users\duart\Desktop\Traffic Violations Project\Traffic-Violation-Analysis\Databases\cleaned_data.csv')
print(df_long.head())

# Get summary statistics and missing values
print(df_long.describe())
print(df_long.isnull().sum())

# Summary Statistics for each Category_Group
category_group_stats = df_long.groupby('Category_Group')['Value'].agg(['mean', 'median', 'sum', 'std', 'min', 'max']).reset_index()
print("\nSummary Statistics by Category Group:")
print(category_group_stats)

# Summary Statistics for each Violation Group
violation_group_stats = df_long.groupby('Violation_Group')['Value'].agg(['mean', 'median', 'sum', 'std', 'min', 'max']).reset_index()
print("\nSummary Statistics by Violation Group:")
print(violation_group_stats)

# Summary Statistics for each Year
yearly_stats = df_long.groupby('Year')['Value'].agg(['mean', 'median', 'sum', 'std', 'min', 'max']).reset_index()
print("\nSummary Statistics by Year:")
print(yearly_stats)

# Save these statistics to CSV files if needed
category_group_stats.to_csv(r'C:\Users\duart\Desktop\Traffic Violations Project\Traffic-Violation-Analysis\Databases\category_group_stats.csv', index=False)
violation_group_stats.to_csv(r'C:\Users\duart\Desktop\Traffic Violations Project\Traffic-Violation-Analysis\Databases\violation_group_stats.csv', index=False)
yearly_stats.to_csv(r'C:\Users\duart\Desktop\Traffic Violations Project\Traffic-Violation-Analysis\Databases\yearly_stats.csv', index=False)
print("\nSummary statistics saved as CSV files.")

# Visualizations start here
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

# Plot the counts by Category (split by Category Group)
plt.figure(figsize=(14, 8))
sns.barplot(x='Category', y='Value', hue='Category_Group', data=df_long, estimator=sum, ci=None)
plt.title('Total Counts by Category (Split by Category Group)')
plt.xlabel('Category')
plt.ylabel('Total Counts')
plt.xticks(rotation=90)
plt.legend(title='Category Group')
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

print("All visualizations have been generated successfully.")