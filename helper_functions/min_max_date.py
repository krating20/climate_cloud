import os
from datetime import datetime
directory = 'data/2022drought_json'



    #for X(7*number of coords for  date) rows in the csv
        #use the function to check coord and poly shape


def min_max_date(flag,directory):

    list = sorted(os.listdir(directory))
    startdate =str()
    enddate = str()
    if(flag == "min"):
        print("min_date")
        print(list[0])
    elif(flag == "max"):
        print("max_date")
        print(list[-1])
    else:
        print("error flag must be min/max")


min_max_date("max",'data/2022drought_json')