import pandas as pd

# Read the original CSV file
df = pd.read_csv('2022.csv')

# Read the second CSV file with the "air" column
df_air = pd.read_csv('bgrun.2022.csv')

# Add the "air" column to the original dataframe
df.insert(loc=4, column='bgrun', value=df_air['bgrun'])

# Save the updated dataframe to a new CSV file
df.to_csv('updated_bgrun_2022.csv', index=False)