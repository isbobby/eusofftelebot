#dependencies
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import datetime as dt

#local imports
from bot_replies import bot_replies
from menu import get_today_breakfast, get_tmr_breakfast, get_tmr_dinner, get_today_dinner
from markup import menu_markup

#configuration
TOKEN = '676612820:AAHmVMr1Qkd0Cah7u1i7I-ByFBwb_pnGoO0'
bot = telebot.TeleBot(TOKEN)

# Handle '/start - also prompts users to use other features'
@bot.message_handler(commands=["help", "start"])
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
    if message.text == "mealbot" or message.text =="/mealbot":
        bot.send_message(message.chat.id, bot_replies['mealbot_landing'], reply_markup=menu_markup())
    else: 
        bot.send_message(
        chat_id, "There is no such function. Please try again"
    )

#Handles the subsequent queries from /mealbot
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    date = dt.datetime.fromtimestamp(call.message.date)

    #this entry shows the call back properties in terminal, useful for testing
    entry = {
        'date': date,
        'button': call.data,
        'username': call.message.chat.username,
        'type': 'callbackquery'
    }
    print(entry)

    #get breakfast menu for today and tomorrow
    if call.data == "cb_tdy_bf":
        bot.send_message(call.message.chat.id, get_today_breakfast())
    if call.data == "cb_tmr_bf":
        bot.send_message(call.message.chat.id, get_tmr_breakfast())
    if call.data == "cb_tdy_dn":
        bot.send_message(call.message.chat.id, text=get_today_dinner(), parse_mode="MARKDOWN")
    if call.data == "cb_tmr_dn":
        bot.send_message(call.message.chat.id, get_tmr_dinner())

bot.polling()