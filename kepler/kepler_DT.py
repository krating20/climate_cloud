import pandas as pd

# Read in the CSV file
df = pd.read_csv('2022.csv')

# Convert the "time" column to datetime format with HH:MM set to 00:00
df['time'] = pd.to_datetime(df['time']).dt.strftime('%Y/%m/%d 00:00')

df.to_csv('2022DT.csv', index=False)