import xarray as xr
# single file
dataDIR = 'precip.2022.nc'
data = xr.open_dataset(dataDIR)
df = data[['time','apcp']].to_dataframe()
index_drop = df[ (df['lat'] < 32.5350) | (df['lat'] > 42.0056) ].index
df.drop(index_drop, inplace=True)

index_drop = df[ (df['lon'] < -124.2126) | (df['lon'] > -114.1312)].index 
df.drop(index_drop, inplace=True)
df.shape
df.to_csv('test.csv', index=False)


#this code generate 935 data points 