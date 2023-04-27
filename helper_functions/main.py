import os

#shape file stuff
import json
from shapely.geometry import shape, Point
# depending on your version, use: from shapely.geometry import shape, Point

####REDO####
#IF











directory = 'data/2022drought_json'
list = sorted(os.listdir(directory))
for filename in list:
    print(filename)
    with open(filename) as f:
        js = json.load(f)
    #for X(7*number of coords for  date) rows in the csv
        point = Point(-121.1892, 37.01344)#lon/lat from csv row
        for feature in js['features']:
            polygon = shape(feature['geometry'])
            if polygon.contains(point):
                print ("found")
                print(feature.get("id"))




# load GeoJSON file containing sectors


# construct point based on lon/lat returned by geocoder
point = Point(-121.1892, 37.01344)#SCU coord

# check each polygon to see if it contains the point
for feature in js['features']:
    polygon = shape(feature['geometry'])
    if polygon.contains(point):
        print ("found")
        print(feature.get("id"))
        #assign to column 
       


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