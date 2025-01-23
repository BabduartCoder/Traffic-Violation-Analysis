import pandas as pd

file_path = r'C:\Users\duart\Desktop\Traffic Violations Project\Palm Beach County 2011-2023 CLEAN.csv' 
df = pd.read_csv(file_path)

df.columns = [
    'Year', 'Violation_Group', 'FHP_Count', 'City_Police_Count', 'Sheriff_Count', 
    'Other_Count', 'Guilty_Count', 'Civil_Penalties_Count', 
    'Adjudication_Withheld_Clerk_Count', 'Adjudication_Withheld_Judge_Count', 
    'Not_Guilty_Count', 'Charge_Dismissed_Count', 'Nolle_Pros_Count'
]

# Convert to long format
df_long = pd.melt(df, id_vars=['Year', 'Violation_Group'], 
                  var_name='Category', value_name='Value')

df_long.to_csv('cleaned_data.csv', index=False)
print("Data has been cleaned and saved to 'cleaned_data.csv'.")