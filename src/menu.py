# This file first imports both breakfast and dinner menus
# Taking formatted date as the parameter, it will query for the column of given date
# This column is formatted, returned at the end of the function and sent to user accordingly

import pandas as pd
import datetime

#read both csv files
pd.set_option('display.max_colwidth',1000)
bf = pd.read_csv('bf.csv')
dn = pd.read_csv('dn.csv')

#format base files

#format date
today = datetime.datetime.today().date().strftime("%d/%m/%Y")
tomorrow_raw = datetime.date.today() + datetime.timedelta(days=1)
tomorrow = tomorrow_raw.strftime("%d/%m/%Y")

#these functions query and format menu data
def get_today_breakfast():
    #converting pandas column object to a python dictionary
    raw_dict = bf[today].dropna().to_dict()

    #if the menu is empty, return a string to notify there is no breakfast
    if bool(raw_dict) == False:
        return "There is no hall breakfast this day\n" 
    
    #else put all the items into string forms and pass to telegram
    raw_list = [ item for item in raw_dict.values()]
    string = ''
    for item in raw_list:
        string += item + '\n'
    return string

#same as above, with different date 
def get_tmr_breakfast():
    raw_dict = bf[tomorrow].dropna().to_dict()
    if bool(raw_dict) == False:
        return "There is no hall breakfast this day\n" 
    raw_list = [ item for item in raw_dict.values()]
    string = ''
    for item in raw_list:
        string += item + '\n'
    return string

def get_tmr_dinner():
    raw_dict = dn[tomorrow].dropna().to_dict()
    if bool(raw_dict) == False:
        return "There is no hall dinner this day\n" 
    raw_list = [ item for item in raw_dict.values()]
    string = ''
    for item in raw_list:
        string += item + '\n'
    
    #to do: bold these headers
    words_to_bold=['Meat', 'Side Dish', 'Special', 'Desert']

    return string

def get_today_dinner():
    raw_dict = dn[today].dropna().to_dict()
    if bool(raw_dict) == False:
        return "There is no hall dinner this day\n" 
    raw_list = [ item for item in raw_dict.values()]
    string = ''
    for item in raw_list:
        string += item + '\n'
    
    #to do: bold these headers
    words_to_bold=['Meat', 'Side Dish', 'Special', 'Desert']

    return string
