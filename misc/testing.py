#https://www.earthinversion.com/utilities/reading-NetCDF4-data-in-python/

import netCDF4
import numpy as np
f = netCDF4.Dataset('airtemp_surface_daily2022.nc')
#print(f) # get all variable names

print(f.variables.keys()) # get all variable names
#sst = f.variables['sst'] # sst variable
#time = f.variables['time']
airtemp = f.variables['air']
print(airtemp)
#for d in f.dimensions.items():
  #print(d)
#print(airtemp.shape)
#apcp = f.variables['apcp'] # temperature variable
#print(f)


time = f.variables['time']
#nbnds = f.variables['nbnds']
x,y = f.variables['x'], f.variables['y']
#print(time)
#print(x)
#print(y)

vtime = time[:]
#print(vtime)




lat, lon = f.variables['lat'],f.variables['lon']
#print(lat)
#print(lon)
#print(lat[:])


latvals = lat[:]; lonvals = lon[:]
def getclosest_ij(lats,lons,latpt,lonpt):

    dist_sq = (lats-latpt)**2+(lons-lonpt)**2

    miniindex_flattened = dist_sq.argmin()

    return np.unravel_index(miniindex_flattened,lats.shape)
iy_min,ix_min = getclosest_ij(latvals,lonvals,50.,-140)
#print(iy_min)
#print(ix_min)

#print('%7.4f %s' % (airtemp[0,0,iy_min,ix_min], airtemp.units))



#deauture selection quarters