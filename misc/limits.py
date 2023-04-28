# script for cleaning and processing .nc files
# will convert data to readable/processable .csv file
# sorts out all data not in relevant latitude and longitude for sierra region
# LAT/LON:
# range from W to E: 119 44'46" W --> 120 33'07" W
# range from S to N:  38 26'12" N -->  39 39'51" N
# run with filename for NC file and desired CSV name

import netCDF4 as nc
import numpy as np
import xarray as xr


def nc_processor(filename, csvname,var):
     ds = nc.Dataset(filename) #ds = noaaa data
     print(ds.variables.keys())

     data = xr.open_dataset(filename)
     df = data[['time',var]].to_dataframe()
     index_drop = df[ (df['lat'] < 38.436667) | (df['lat'] > 39.664167) ].index
     df.drop(index_drop, inplace=True)

     index_drop = df[ (df['lon'] < -120.551944) | (df['lon'] > -119.746111)].index
     df.drop(index_drop, inplace=True)
     df.shape
     df.to_csv(csvname, index=False)

def last_var(filename):
     ds = nc.Dataset(filename)
#     # get last element in ds.variables.keys()
#     # return element
#     list_of_vars = list(ds.variables.keys())
#     return list_of_vars[-1]

# run above function with NC file names and desired CSV file name
# need to figure out last variable in keys

nc_processor('albedo.2022.nc', 'albedoDaily2022.csv'
         ,'albedo')

###### Will show how to use python to iterate through filenames #####
#ds = nc.Dataset('albedo.2022.nc') #ds = noaaa data
#print(ds.variables.keys())