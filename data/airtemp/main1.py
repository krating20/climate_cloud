import xarray as xr
# single file

files = ['air.sfc.2010.nc','air.sfc.2011.nc','air.sfc.2012.nc','air.sfc.2013.nc','air.sfc.2014.nc']
files_CSV = ['air.2010.csv','air.2011.csv','air.2012.csv','air.2013.csv','air.2014.csv']
for i in range(len(files)):
    dataDIR = files[i]
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
    df = df['air']
    print(df)
    df.to_csv(files_CSV[i], index=True)
#df = df.drop('Lambert_Conformal', axis=1)

#df.to_csv('air.2019.csv', index=False, columns=['air'])