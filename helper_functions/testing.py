#shape file stuff
import json
from shapely.geometry import shape, Point

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
        
catchecker(-121.1892, 37.01344,'usdm.json')