#shape file stuff

import fiona
import shapely

with fiona.open("path/to/shapefile.shp") as fiona_collection:

    # In this case, we'll assume the shapefile only has one record/layer (e.g., the shapefile
    # is just for the borders of a single country, etc.).
    shapefile_record = fiona_collection.next()

    # Use Shapely to create the polygon
    shape = shapely.geometry.asShape( shapefile_record['geometry'] )

    point = shapely.geometry.Point(32.398516, -39.754028) # longitude, latitude

    # Alternative: if point.within(shape)
    if shape.contains(point):
        print ("Found shape for point.")
        #add a catagory to csv


#my todo
#generate csv for scu area
#then run this function on the csv file for each point

#how many rows for each date??