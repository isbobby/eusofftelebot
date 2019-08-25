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

#format date: new version takes date from user directly, hence these are no longer in use
""" today = datetime.datetime.today().date().strftime("%d/%m/%Y")
tomorrow_raw = datetime.date.today() + datetime.timedelta(days=1)
tomorrow = tomorrow_raw.strftime("%d/%m/%Y") """

#these functions query and format menu data
def get_today_breakfast(day):
    #converting pandas column object to a python dictionary
    raw_dict = bf[day].dropna().to_dict()

    #if the menu is empty, return a string to notify there is no breakfast
    if bool(raw_dict) == False:
        return "There is no breakfast today." 
    
    #special condition!
    elif day == '25/08/2019' or day == '26/08/2019':
        return "Special Menu is served due to pipe burst in catering kitchen, normal menue resumes on Tuesday 27/08/2019"

    #else put all the items into string forms and pass to telegram
    raw_list = [ item for item in raw_dict.values()]
    string = ''
    for item in raw_list:
        string += item + '\n'
    return string

#same as above, with different date 
def get_tmr_breakfast(day):
    raw_dict = bf[day].dropna().to_dict()
    if bool(raw_dict) == False:
        return "There is no breakfast tomorrow." 

    #special condition
    elif day == '25/08/2019' or day == '26/08/2019':
        return "Special Menu is served due to pipe burst in catering kitchen, normal menue resumes on Tuesday 27/08/2019"

    raw_list = [ item for item in raw_dict.values()]
    string = ''
    for item in raw_list:
        string += item + '\n'
    return string

def get_tmr_dinner(day):
    raw_dict = dn[day].dropna().to_dict()
    if bool(raw_dict) == False:
        return "There is no dinner today." 

    #special condition
    elif day == '25/08/2019' or day == '26/08/2019':
        return "Special Menu is served due to pipe burst in catering kitchen, normal menue resumes on Tuesday 27/08/2019."

    raw_list = [ item for item in raw_dict.values()]
    string = ''
    for item in raw_list:
        string += item + '\n'
    
    #to do: bold these headers
    words_to_bold=['Meat', 'Side Dish', 'Special', 'Dessert']

    return string

def get_today_dinner(day):
    raw_dict = dn[day].dropna().to_dict()
    if bool(raw_dict) == False:
        return "There is no dinner tomorrow." 
    
    #special situation 
    elif day == '25/08/2019' or day == '26/08/2019':
        return "Special Menu is served due to pipe burst in catering kitchen, normal menue resumes on Tuesday 27/08/2019"
    
    raw_list = [ item for item in raw_dict.values()]
    string = ''
    for item in raw_list:
        string += item + '\n'
    
    #to do: bold these headers
    words_to_bold=['Meat', 'Side Dish', 'Special', 'Dessert']

    return string
