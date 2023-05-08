import xarray as xr
# single file

files = ['bgrun.2010.nc','bgrun.2011.nc','bgrun.2012.nc','bgrun.2013.nc','bgrun.2014.nc','bgrun.2015.nc','bgrun.2016.nc','bgrun.2017.nc','bgrun.2018.nc','bgrun.2019.nc','bgrun.2022.nc']
files_CSV = ['bgrun.2010.csv','bgrun.2011.csv','bgrun.2012.csv','bgrun.2013.csv','bgrun.2014.csv','bgrun.2015.csv','bgrun.2016.csv','bgrun.2017.csv','bgrun.2018.csv','bgrun.2019.csv','bgrun.2022.csv']
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
    df = df['bgrun']
    print(df)
    df.to_csv(files_CSV[i], index=True)
#df = df.drop('Lambert_Conformal', axis=1)

#df.to_csv('air.2019.csv', index=False, columns=['air'])