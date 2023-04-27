#shape file stuff
import json
from shapely.geometry import shape, Point
#given lat lon and the geo json file this function will return the drought catagory of the given coordinate 
def catchecker(lon,lat,filename):
    with open('usdm.json') as f:
        js = json.load(f)
    point = Point(lon, lat)#SCU coord
    for feature in js['features']:
        polygon = shape(feature['geometry'])
        if polygon.contains(point):
            print ("found")
            print(feature.get("id"))
            return feature.get("id")
        
    

#37.01344	-121.1892
#37.18275	-121.9598
#37.23877	-121.6087
#37.29348	-121.2568
#37.51871	-121.6785
#37.57373	-121.3251
#37.79888	-121.749
#37.85422	-121.394

#example
#scu has 8 coords for a day
#i=1
#for 8*7 rows
    #check coord with dataset i



#for each row 
    #check if the date has a corresponding goejson file
        #if found assign the USDM catagory for that date
    #else use the value from the previous date of the same geo coordinate / FILE?


# for (number of dates with each set * 7)
    #check with geo json