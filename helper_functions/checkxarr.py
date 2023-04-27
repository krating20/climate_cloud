import xarray as xr
# single file
dataDIR = 'precip.2022.nc'
data = xr.open_dataset(dataDIR)
df = data.to_dataframe()
df = df.drop('Lambert_Conformal', axis=1)
df = df.drop('time_bnds', axis=1)
df = df.reset_index(level='y', drop=True)
df = df.reset_index(level='x', drop=True)
df = df.reset_index(level='nbnds', drop=True)
index_drop = df[ (df['lat'] < 37) | (df['lat'] > 38) ].index
df.drop(index_drop, inplace=True)
index_drop = df[ (df['lon'] < -122) | (df['lon'] > -121)].index 
df.drop(index_drop, inplace=True)
print(df)
df.to_csv('test.csv', index=True)
#df = df.drop('Lambert_Conformal', axis=1)