#shape file stuff

import fiona
import shapely

with fiona.open("USDM_20220104_M/USDM_20220104.shp") as fiona_collection:

    # In this case, we'll assume the shapefile only has one record/layer (e.g., the shapefile
    # is just for the borders of a single country, etc.).
    shapefile_record = fiona_collection.next()

    # Use Shapely to create the polygon
    shape = shapely.geometry.asShape( shapefile_record['geometry'] )

    point = shapely.geometry.Point(37.01344,-121.1892) # longitude, latitude

    # Alternative: if point.within(shape)
    if shape.contains(point):
        print("test")
        #add a catagory to csv
#37.01344	-121.1892
#37.18275	-121.9598
#37.23877	-121.6087
#37.29348	-121.2568
#37.51871	-121.6785
#37.57373	-121.3251
#37.79888	-121.749
#37.85422	-121.394
