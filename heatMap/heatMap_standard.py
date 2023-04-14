import pandas as pd

# Read in the CSV file as a pandas DataFrame
df = pd.read_csv('heatMap.csv')

# Multiply the safety grade column by 100
df['safety grade'] = df['safety grade'] * 100

# Save the updated DataFrame to a new CSV file
df.to_csv('heatMap_standardization.csv', index=False)
