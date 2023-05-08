import xarray as xr
# single file

files = ['tcdc.2010.nc','tcdc.2011.nc','tcdc.2012.nc','tcdc.2013.nc','tcdc.2014.nc','tcdc.2015.nc','tcdc.2016.nc','tcdc.2017.nc','tcdc.2018.nc','tcdc.2019.nc','tcdc.2022.nc']
files_CSV = ['tcdc.2010.csv','tcdc.2011.csv','tcdc.2012.csv','tcdc.2013.csv','tcdc.2014.csv','tcdc.2015.csv','tcdc.2016.csv','tcdc.2017.csv','tcdc.2018.csv','tcdc.2019.csv','tcdc.2022.csv']
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
    df = df['tcdc']
    print(df)
    df.to_csv(files_CSV[i], index=True)
#df = df.drop('Lambert_Conformal', axis=1)

#df.to_csv('air.2019.csv', index=False, columns=['air'])