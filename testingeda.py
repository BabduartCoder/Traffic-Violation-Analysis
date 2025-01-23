import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df_long = pd.read_csv(r'C:\Users\duart\Desktop\Traffic Violations Project\Traffic-Violation-Analysis\Databases\cleaned_data.csv')

print(df_long.head())

# Get summary statistics
print(df_long.describe())

# Check for missing values
print(df_long.isnull().sum())