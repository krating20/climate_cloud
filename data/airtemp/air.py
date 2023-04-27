import pandas as pd

# Read the CSV file and include only the 'air' column
df = pd.read_csv('air.2019.csv', usecols=['air'])

# Write the resulting dataframe to a new CSV file
df.to_csv('air.2019.csv', index=False, columns=['air'])