import csv
import json
import re
import os

from shapely.geometry import shape, Point
#given lat lon and the geo json file this function will return the drought catagory of the given coordinate 


directory = 'data/2022drought_json'
directory_path = 'data/2022drought_json'
#filelist = sorted(os.listdir(directory))

def date_change(date):
    date_str = date
    date_str_without_dashes = date_str.replace("-", "")
    return date_str_without_dashes

def catchecker(lon,lat,filename):
    with open('usdm.json') as f:
        js = json.load(f)
    point = Point(lon, lat)#SCU coord
    for feature in js['features']:
        polygon = shape(feature['geometry'])
        if polygon.contains(point):
            return feature.get("id")
        




def min_max_date(flag,directory):

    list = sorted(os.listdir(directory))
    if(flag == "min"):
        print("min_date")
        print(list[0])
    elif(flag == "max"):
        print("max_date")
        print(list[-1])
    else:
        print("error flag must be min/max")


def directory_search(directory_path,search_string):
    file_pattern = re.compile(f"{search_string}\.json$")
    for filename in os.listdir(directory_path):
        if file_pattern.match(filename):
            print(f"Found matching file: {filename}")
            return True

#directory_search("data/2022drought_json","20220104")

def date_match(directory_path,search_string,min_date,max_date):
    if(directory_search(directory_path,search_string)== True):
        #append
        print("correct geo json found ")
    elif(search_string<min_date):
        print("date less than min date")
        mod_date= int(search_string)
        while(directory_search(directory_path,mod_date) != True):
            mod_date+=1
        print(mod_date)
        converted_date=str(mod_date)
        json_file_name = converted_date + ".json"
        print(json_file_name)
        return json_file_name
    elif(search_string>max_date):
        print("date greater than max date")
        mod_date= int(search_string)
        while(directory_search(directory_path,mod_date) != True):
            mod_date-=1
        print(mod_date)
        converted_date=str(mod_date)
        json_file_name = converted_date + ".json"
        print(json_file_name)
        return json_file_name
    else:
        print("date is in between sets")
        #if in between we want to use the data of the week ahead 
        mod_date= int(search_string)
        while(directory_search(directory_path,mod_date) != True):
            mod_date+=1
        print(mod_date)
        converted_date=str(mod_date)
        json_file_name = converted_date + ".json"
        print(json_file_name)
        return json_file_name 


#STARTDATE
#ENDDATE    


Min_date = min_max_date("min",directory)
Max_date = min_max_date("max",directory)

# Open the CSV file for reading and writing
with open('2022_APCP_SCU.csv', 'r') as csv_file, open('append_test.csv', 'w') as new_csv_file:
    reader = csv.reader(csv_file)
    writer = csv.writer(new_csv_file)

    # Write the header row with the new column name
    header = next(reader)
    header.append('drought catagory')
    writer.writerow(header)

    # Iterate over each row in the CSV file and add the new column value
    for row in reader:
        # Assuming the first three columns contain integer values
        
        #new_value = row[0]
        date = row[0]
        new_date = date_change(date)
        #date is changed from 2022-01-04 to 2022-01-04
        
        json_file = date_match(directory_path,new_date,Min_date,Max_date)
        new_value = catchecker(row[2],row[1],json_file)
        row.append(new_value)
        print("appened new value")
        print(new_value)
        writer.writerow(row)

#date = row[0]
#new date = to_number(date)
#match and done
#else
#if newdate <date min
#else if newdate > date max
#else ++ until mod 7 = 2 
