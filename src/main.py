#dependencies
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import datetime as dt
import logging as logger
import time

#local imports
from bot_replies import bot_replies
from menu import get_today_breakfast, get_tmr_breakfast, get_tmr_dinner, get_today_dinner
from markup import menu_markup, calendar_markup, faq_markup, menu_return
# from calendar import get_calendar

#configuration
TOKEN = '676612820:AAHmVMr1Qkd0Cah7u1i7I-ByFBwb_pnGoO0'
bot = telebot.TeleBot(TOKEN)

# Handle '/start - also prompts users to use other features'
@bot.message_handler(commands=["help", "start", "home"])
def send_welcome(message):
    chat_id = message.chat.id
    message = bot.send_message(
        chat_id,
        bot_replies['welcome']
    )
    bot.message_handler(message, main_requests)

#Handles the main requests: /mealbot, /faq or /events
@bot.message_handler(func=lambda message: message.text is not None)
def main_requests(message):
    chat_id = message.chat.id
    
    #this if statement brings users to mealbot commands
    if message.text == "Mealbot" or message.text =="/Mealbot":
        bot.send_message(message.chat.id, bot_replies['mealbot_landing'], reply_markup=menu_markup())
      
    #FAQ to be added
    elif message.text == "FAQ" or message.text =="/FAQ":
        bot.send_message(message.chat.id, bot_replies['faq_landing'])

    elif message.text == "Calendar" or message.text =="/Calendar":
        bot.send_photo(message.chat_id, photo=open('tests/test.png', 'rb'))
        bot.send_message(message.chat.id, bot_replies['calendar_landing'], reply_markup= calendar_markup())

    else: 
        bot.send_message(
        chat_id, "There is no such function. Please try again"
    )

#Handles the subsequent callback queries from /mealbot, view the markup callbacks in markup.py
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    date = dt.datetime.fromtimestamp(call.message.date)

    #this entry shows the call back properties in terminal, useful for testing
    #this entry also takes the date which the message is sent, and use it to get the corresponding menu
    entry = {
        'date': date,
        'button': call.data,
        'username': call.message.chat.username,
        'type': 'callbackquery'
    }
    print(entry)
    print(entry['date'].strftime("%d/%m/%Y"))
    tomorrow_raw = entry['date'] + dt.timedelta(days=1)

    today = entry['date'].strftime("%d/%m/%Y")
    tomorrow = tomorrow_raw.strftime("%d/%m/%Y")

    #get breakfast menu for today and tomorrow
    if call.data == "cb_tdy_bf":
        bot.send_message(call.message.chat.id, get_today_breakfast(day=today))
        bot.send_message(call.message.chat.id, bot_replies['mealbot_landing'], reply_markup=menu_markup())
    elif call.data == "cb_tmr_bf":
        bot.send_message(call.message.chat.id, get_tmr_breakfast(day=tomorrow))
        bot.send_message(call.message.chat.id, bot_replies['mealbot_landing'], reply_markup=menu_markup())
    elif call.data == "cb_tdy_dn":
        bot.send_message(call.message.chat.id, get_today_dinner(day=today), parse_mode="MARKDOWN")
        bot.send_message(call.message.chat.id, bot_replies['mealbot_landing'], reply_markup=menu_markup())
    elif call.data == "cb_tmr_dn":
        bot.send_message(call.message.chat.id, get_tmr_dinner(day=tomorrow))
        bot.send_message(call.message.chat.id, bot_replies['mealbot_landing'], reply_markup=menu_markup())
    elif call.data == "cb_home":
        send_welcome(call.message)
    elif call.data == "cb_mealbot":
        bot.send_message(call.message.chat.id, bot_replies['mealbot_landing'], reply_markup=menu_markup())
    #to do: implement a dabao FAQ for dabao service
    elif call.data == "cb_take_away":
        bot.send_message(call.message.chat.id, bot_replies['mealbot_dabao'])
        bot.send_message(call.message.chat.id, bot_replies['mealbot_return'])
    #to do: get calendar

        
while True:
    try:
        bot.polling()
    # ConnectionError and ReadTimeout because of possible timout of the requests library
    # TypeError for moviepy errors
    # maybe there are others, therefore Exception
    except Exception as e:
        logger.error(e)
        time.sleep(15)
