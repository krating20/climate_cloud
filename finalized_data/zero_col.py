import pandas as pd

# Read in the CSV file
df = pd.read_csv('2022_final.csv')

# Replace empty cells in the fourth column with '0'
df['drought catagory'] = df['drought catagory'].fillna(0)

# Write the updated data to a new CSV file
df.to_csv('updated_2022.csv', index=False)