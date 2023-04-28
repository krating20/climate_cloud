import netCDF4
import numpy as np
f = netCDF4.Dataset('subset.nc')


print(f.variables.keys()) # get all variable names