import netCDF4
import numpy as np
import xarray as xr
f = netCDF4.Dataset('precip.2022.nc')
#print(f)

print(f.variables.keys()) # get all variable names
#print(f.variables.get("apcp")) # get all variable names
rain = f.variables['apcp']
time = f.variables['time']
#print(rain)
print(time)
# need to clean so only lat lon values of california remain


Lat, Lon = f.variables['lat'], f.variables['lon']
#print(Lat)
#print(Lon)
#print(Lat[:])


# extract lat/lon values (in degrees) to numpy arrays
latvals = Lat[:]; lonvals = Lon[:]

# a function to find the index of the point closest pt
# (in squared distance) to give lat/lon value.
def getclosest_ij(lats,lons,latpt,lonpt):
  # find squared distance of every point on grid
  dist_sq = (lats-latpt)**2 + (lons-lonpt)**2
  # 1D index of minimum dist_sq element
  minindex_flattened = dist_sq.argmin()
  # Get 2D index for latvals and lonvals arrays from 1D index
  return np.unravel_index(minindex_flattened, lats.shape)




iy_min, ix_min = getclosest_ij(latvals, lonvals, 20, -120)# get indexing closest to lat lon vals
precip = f.variables['apcp']
#print('%7.4f %s' % (precip[364,iy_min,ix_min], precip.units))
#time variable is 0-364 daily vaulue 
Time =f.variables['time']
timevals = Time[:]
precipval = precip[:]

#277 lat vals & lon vals 
#365 time vals
#365 precip vals
#print(lonvals)


#create a helper function so that only lat and lon values exist for california 

#print(f)



# script for cleaning and processing .nc files
# will convert data to readable/processable .csv file
# sorts out all data not in relevant latitude and longitude for sierra region
# LAT/LON:
# range from W to E: 119 44'46" W --> 120 33'07" W
# range from S to N:  38 26'12" N -->  39 39'51" N
# run with filename for NC file and desired CSV name

# import netCDF4 as nc
# import numpy as np
# import xarray as xr


# def nc_processor(filename, csvname,var):
#     ds = nc.Dataset(filename)
#     print(ds.variables.keys())

#     data = xr.open_dataset(filename)
#     df = data[['time',var]].to_dataframe()
#     index_drop = df[ (df['lat'] < 38.436667) | (df['lat'] > 39.664167) ].index
#     df.drop(index_drop, inplace=True)

#     index_drop = df[ (df['lon'] < -120.551944) | (df['lon'] > -119.746111)].index
#     df.drop(index_drop, inplace=True)
#     df.shape
#     df.to_csv(csvname, index=False)

# def last_var(filename):
#     ds = nc.Dataset(filename)
#     # get last element in ds.variables.keys()
#     # return element
#     list_of_vars = list(ds.variables.keys())
#     return list_of_vars[-1]

# run above function with NC file names and desired CSV file name
# need to figure out last variable in keys

# nc_processor('albedoDaily2019-2020.nc', 'albedoDaily2019-2020.csv'
        # , last_var('albedoDaily2019-2020.nc'))

###### Will show how to use python to iterate through filenames #####


#ds = netCDF4.Dataset('precip.2022.nc')
#data = xr.open_dataset('precip.2022.nc')
#df = data[['time','apcp']].to_dataframe()
#index_drop = df[ (df['lat'] < 32.5350) | (df['lat'] >  42.0056) ].index
#df.drop(index_drop, inplace=True)

#index_drop = df[ (df['lon'] < -124.2126) | (df['lon'] > -114.1312)].index
#df.drop(index_drop, inplace=True)
#df.shape
#df.to_csv('test', index=False)
