import xarray as xr
# single file
dataDIR = 'apcp.2016.nc'
data = xr.open_dataset(dataDIR)
df = data.to_dataframe()
df = df.drop('Lambert_Conformal', axis=1)
df = df.drop('time_bnds', axis=1)
#df = df.reset_index(level='y', drop=True)
#df = df.reset_index(level='x', drop=True)
#df = df.reset_index(level='nbnds', drop=True)
index_drop = df[ (df['lat'] < 32.5350) | (df['lat'] >42.0056) ].index
df.drop(index_drop, inplace=True)
index_drop = df[ (df['lon'] < -124.2126) | (df['lon'] > -114.1312)].index 
df.drop(index_drop, inplace=True)
print(df)
df.to_csv('apcp.2016.csv', index=True)
#df = df.drop('Lambert_Conformal', axis=1)