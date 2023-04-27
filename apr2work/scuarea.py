import xarray as xr
# single file
dataDIR = 'precip.2022.nc'
data = xr.open_dataset(dataDIR)
df = data[['apcp']].to_dataframe()

index_drop = df[ (df['lat'] < 37) | (df['lat'] > 38) ].index
df.drop(index_drop, inplace=True)
index_drop = df[ (df['lon'] < -122) | (df['lon'] > -121)].index 

df.drop(index_drop, inplace=True)
df.shape
df.to_csv('test.csv', index=False)

#9 coordinates in a day
#match shape file with day

#do it for 7 days starting from file date