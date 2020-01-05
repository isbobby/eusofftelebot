#this file contains all markup 
from packages.telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

def MenuMarkup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Tdy's Bf 🍞", callback_data="cb_tdy_bf"),
               InlineKeyboardButton("Tdy's Dinz 🍱", callback_data="cb_tdy_dn"),
               InlineKeyboardButton("Tmr's Bf 🍞", callback_data="cb_tmr_bf"),
               InlineKeyboardButton("Tmr's Dinz 🍱", callback_data="cb_tmr_dn"),
               InlineKeyboardButton("Dabao Dinz 🥪", callback_data="cb_take_away"),
               InlineKeyboardButton("Home 🏠", callback_data="cb_home"))

    return markup

def ResponseMarkup():
    markup = ReplyKeyboardMarkup()
    meal_plan_btn = KeyboardButton('Meal Plan')
    markup.row(meal_plan_btn)
    cal_btn = KeyboardButton('Calendar/Fixture')
    markup.row(cal_btn)
    pub_btn = KeyboardButton('Publications ')
    markup.row(pub_btn)
    help_btn = KeyboardButton('Help')
    markup.row(help_btn)
    return markup
    
def FAQMarkup():
    markup=1
    return markup

def CalendarMarkup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Home 🏠", callback_data="cb_home"))
    return markup