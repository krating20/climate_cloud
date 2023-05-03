import csv
import json
import re
import os

from shapely.geometry import shape, Point

#change based on year dealing with
directory = '2013drought_json'
directory_path = '2013drought_json'
csv_path ='cdf/apcp.2013.csv'
csv_out ='2013_final.csv'
#filelist = sorted(os.listdir(directory))

def date_change(date):
    date_str = date
    date_str_without_dashes = date_str.replace("-", "")
    return date_str_without_dashes

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
        
#
def min_max_date(flag,directory):

    list = sorted(os.listdir(directory))
    if(flag == "min"):
        #print("min_date")
        #print(list[0])
        return list[0]
    elif(flag == "max"):
       # print("max_date")
        #print(list[-1])
        return list[-1]
    else:
        print("error flag must be min/max")

def folder_toset(directory_path):
  files = os.listdir(directory_path)
  json_files = [f.replace(".json", "") for f in files]
  set(json_files)
  return json_files


#takes in directory ,the date,mindate & the max date to return the appropriate json file 
def date_match(dir_list,search_string,min_date,max_date):
  #print(dir_list)
  if search_string in dir_list:
        #append
    print("correct geo json found ")
    json_file_name = search_string + ".json"
    print(json_file_name)
    return json_file_name
  elif(search_string<min_date):
    print("date less than min date")
    mod_date= int(search_string)
    while(mod_date not in dir_list):
      int_mod_date = int(mod_date)
      int_mod_date+=1
      mod_date = str(int_mod_date)
    print(mod_date)
    converted_date=str(mod_date)
    json_file_name = converted_date + ".json"
    print(json_file_name)
    return json_file_name
  elif(search_string>max_date):
    print("date greater than max date")
    mod_date= int(search_string)
    while(mod_date not in dir_list):
      int_mod_date = int(mod_date)
      int_mod_date-=1
      mod_date = str(int_mod_date)
    print(mod_date)
    converted_date=str(mod_date)
    json_file_name = converted_date + ".json"
    print(json_file_name)
    return json_file_name
  else:
    print("date is in between sets")
    #if in between we want to use the data of the week ahead 
    mod_date= int(search_string)
    while(mod_date not in dir_list):
      int_mod_date = int(mod_date)
      int_mod_date+=1
      mod_date = str(int_mod_date)
    print(mod_date)
    converted_date=str(mod_date)
    json_file_name = converted_date + ".json"
    print(json_file_name)
    return json_file_name 


#above code but using pandas 
import pandas as pd

Min_date = min_max_date("min",directory)
Max_date = min_max_date("max",directory)
dir_list = folder_toset(directory_path)
df = pd.read_csv(csv_path)

# Use the apply method to apply the function to each row in the DataFrame
df['drought catagory'] = df.apply(lambda row: catchecker(row['lon'],row['lat'],date_match(dir_list,date_change(row['time']),Min_date,Max_date)), axis=1)
  #date is changed from 2022-01-04 to 2022-01-04     
# Save the updated DataFrame to a new CSV file
df.to_csv(csv_out, index=False)