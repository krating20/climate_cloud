import xarray as xr

# Load the NOAA data
data = xr.open_dataset('precip.2022.nc')

# Extract the latitude and longitude coordinates
lat = data['latitude']
lon = data['longitude']

lat_ca = lat[(lat >= california_lat_min) & (lat <= california_lat_max)]
lon_ca = lon[(lon >= california_lon_min) & (lon <= california_lon_max)]

# Subset the NOAA data to cover only California
data_ca = data.sel(latitude=lat_ca, longitude=lon_ca)
# Save the subsetted data as a new netCDF file
data_ca.to_netcdf('path/to/new_file.nc')