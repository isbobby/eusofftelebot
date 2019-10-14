# This file first imports both breakfast and dinner menus
# Taking formatted date as the parameter, it will query for the column of given date
# This column is formatted, returned at the end of the function and sent to user accordingly

import pandas as pd
import datetime

#read both csv files
pd.set_option('display.max_colwidth',1000)
bf = pd.read_csv('src/bf.csv')
dn = pd.read_csv('src/dn.csv')

#format base files

#format date: new version takes date from user directly, hence these are no longer in use
""" today = datetime.datetime.today().date().strftime("%d/%m/%Y")
tomorrow_raw = datetime.date.today() + datetime.timedelta(days=1)
tomorrow = tomorrow_raw.strftime("%d/%m/%Y") """

#these functions query and format menu data
def get_today_breakfast(day):
    #converting pandas column object to a python dictionary
    raw_dict = []
    try:
        raw_dict = bf[day].dropna().to_dict()
    except KeyError as e:
        print ('I got a KeyError - reason "%s"' % str(e))
    except IndexError as e:
        print ('I got an IndexError - reason "%s"' % str(e))

    #if the menu is empty, return a string to notify there is no breakfast
    if bool(raw_dict) == False:
        return "There is no breakfast today." 
    
    #else put all the items into string forms and pass to telegram
    raw_list = [ item for item in raw_dict.values()]
    string = ''
    for item in raw_list:
        if item == 'STAPLES:' or item == 'SPECIALS:' or item == 'SANDWICHES:' or item == 'DRINKS:':
            string += '\n'
        string += item + '\n'
    return string

#same as above, with different date 
def get_tmr_breakfast(day):
    raw_dict = []
    try:
        raw_dict = bf[day].dropna().to_dict()
    except KeyError as e:
        print ('I got a KeyError - reason "%s"' % str(e))
    except IndexError as e:
        print ('I got an IndexError - reason "%s"' % str(e))
    if bool(raw_dict) == False:
        return "There is no breakfast tomorrow." 

    raw_list = [ item for item in raw_dict.values()]
    string = ''
    for item in raw_list:
        if item == 'STAPLES:' or item == 'SPECIALS:' or item == 'SANDWICHES:' or item == 'DRINKS:':
            string += '\n'
        string += item + '\n'
    return string

def get_tmr_dinner(day):
    raw_dict = []
    try:
        raw_dict = dn[day].dropna().to_dict()
    except KeyError as e:
        print ('I got a KeyError - reason "%s"' % str(e))
    except IndexError as e:
        print ('I got an IndexError - reason "%s"' % str(e))

    if bool(raw_dict) == False:
        return "There is no dinner tomorrow." 

    raw_list = [ item for item in raw_dict.values()]
    string = ''
    for item in raw_list:
        if item == 'MEATS:' or item == 'SIDE DISHES:' or item == 'SPECIAL:' or item == 'DESSERT:' or item == 'DRINK:' or item == 'SOUP:':
            string += '\n'
        string += item + '\n'
    
    #to do: bold these headers
    #words_to_bold=['Meat', 'Side Dish', 'Special', 'Dessert']

    return string

def get_today_dinner(day):
    raw_dict = []
    try:
        raw_dict = dn[day].dropna().to_dict()
    except KeyError as e:
        print ('I got a KeyError - reason "%s"' % str(e))
    except IndexError as e:
        print ('I got an IndexError - reason "%s"' % str(e))

    if bool(raw_dict) == False:
        return "There is no dinner today." 
    
    raw_list = [ item for item in raw_dict.values()]
    string = ''
    for item in raw_list:
        if item == 'MEATS:' or item == 'SIDE DISHES:' or item == 'SPECIAL:' or item == 'DESSERT:' or item == 'DRINK:' or item == 'SOUP:':
            string += '\n'  #if the string is a header, execute a line break first.
        string += item + '\n'
    
    #to do: bold these headers
    #words_to_bold=['Meat', 'Side Dish', 'Special', 'Dessert']

    return string


def test():
    raw_dict = []
    try:
        raw_dict = dn['02/09/2019'].dropna().to_dict()
    except KeyError as e:
        print ('I got a KeyError - reason "%s"' % str(e))
    except IndexError as e:
            print ('I got an IndexError - reason "%s"' % str(e))
    return raw_dict