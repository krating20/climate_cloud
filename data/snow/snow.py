import xarray as xr
# single file
dataDIR = 'bgrun.2010.nc'
data = xr.open_dataset(dataDIR)
df = data.to_dataframe()

#df = df.reset_index(level='y', drop=True)
#df = df.reset_index(level='x', drop=True)
#df = df.reset_index(level='nbnds', drop=True)
print(df)



#df = df.drop('Lambert_Conformal', axis=1)

#df.to_csv('air.2019.csv', index=False, columns=['air'])