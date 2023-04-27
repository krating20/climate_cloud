import re
import os

search_string = "20220104"
file_pattern = re.compile(f"{search_string}\.json$")

directory_path = "data/2022drought_json"

for filename in os.listdir(directory_path):
    if file_pattern.match(filename):
        print(f"Found matching file: {filename}")
#if date matches file then run function
#else use value from previous row
    #if previous row doesn't exist put in N/A


# set limits for first date and last date for that year as const values 
#if starting date is less than current we use first for those dates
#if end date is before 12/31/36 the nwe use previous values 