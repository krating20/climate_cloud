import pandas as pd

# Read the original CSV file
df = pd.read_csv('2010.csv')

# Read the second CSV file with the "air" column
df_air = pd.read_csv('air.2010.csv')

# Add the "air" column to the original dataframe
df.insert(loc=4, column='air', value=df_air['air'])

# Save the updated dataframe to a new CSV file
df.to_csv('updated_air_2010.csv', index=False)