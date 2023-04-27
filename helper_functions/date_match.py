import re
import os

search_string = "20220104"


directory_path = "data/2022drought_json"



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


date_match("data/2022drought_json","20220101","20220104","20221227")


