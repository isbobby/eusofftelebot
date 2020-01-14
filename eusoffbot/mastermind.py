from telegram import KeyboardButton, ReplyKeyboardMarkup

from eusoffbot.response import Response

from eusoffbot.mealbot import MealBot
from eusoffbot.eventbot import EventBot
from eusoffbot.publicationbot import PublicationBot

eventBot = EventBot()
publicationBot = PublicationBot()
mealBot = MealBot()

def getResponse(message):
    """
    Calls the corresponding methods for responses users enter
    """
    # Meal plan related
    if (message.text == "/start" or message.text == "Home"):
        response = getHomeResponse()

    elif (message.text == "Meal Plan 🍞"):
        response = mealBot.getMealplanResponse()

    elif (message.text == "Today's Breakfast"):
        response = mealBot.getTodayBreakfast()

    elif (message.text == "Today's Dinner"):
        response = mealBot.getTodayDinner()

    elif (message.text == "Tomorrow's Breakfast"):
        response = mealBot.getTomorrowBreakfast()

    elif (message.text == "Tomorrow's Dinner"):
        response = mealBot.getTomorrowDinner()

    # Event related
    elif (message.text == "Calendar and Fixture 📆"):
        response = eventBot.getCalendarResponse()

    elif (message.text == "What's up today"):
        response = eventBot.getTodayEvent()

    elif (message.text == "What's up tomorrow"):
        response = eventBot.getTomorrowEvent()

    # Publication related
    elif (message.text == "Eusoff Publications 📩"):
        response = publicationBot.getPubsResponse()

    elif (message.text == "Eusoff Wordpress"):
        response = publicationBot.getEusoffWordpress()

    elif (message.text == "Eusoffworks Facebook"):
        response = publicationBot.getEusoffWorksFB()

    else:
        response = getErrorResponse()

    return response

def getHomeResponse():
    CustomReplyArray = [
        [KeyboardButton("Meal Plan 🍞")],
        [KeyboardButton("Calendar and Fixture 📆")],
        [KeyboardButton("Eusoff Publications 📩")],
        [KeyboardButton("Home")]
    ]
    CustomReply = ReplyKeyboardMarkup(keyboard=CustomReplyArray)
    response = Response(text="Bringing you home",
                        has_markup=True, reply_markup=CustomReply)
    return response

def getErrorResponse():
    return Response(text="Sorry, I don't recognize this command, try /start", has_markup=True, reply_markup=None)
