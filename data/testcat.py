import csv
import json
import re
import os

from shapely.geometry import shape, Point

#change based on year dealing with
directory = '2017drought_json'
directory_path = '2017drought_json'
csv_path ='cdf/apcp.2017.csv'
csv_out ='2017_final.csv'
#filelist = sorted(os.listdir(directory))

def catchecker(lon,lat,filename):
    path = os.path.join(directory, filename)
    with open(path) as f:
        js = json.load(f)
    point = Point(lon, lat)#SCU coord
    for feature in js['features']:
        polygon = shape(feature['geometry'])
        if polygon.contains(point):
            return feature.get("id")
        else:
            return 0

print(catchecker(32.54809,-115.8204,'20170103.json'))