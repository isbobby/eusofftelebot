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
    elif (message.text == "Events this week 📆"):
        response = eventBot.getCalendarResponse()

    elif (message.text == "Monday"):
        response = eventBot.getEventByDay(day="Monday")

    elif (message.text == "Tuesday"):
        response = eventBot.getEventByDay(day="Tuesday")

    elif (message.text == "Wednesday"):
        response = eventBot.getEventByDay(day="Wednesday")

    elif (message.text == "Thursday"):
        response = eventBot.getEventByDay(day="Thursday")

    elif (message.text == "Friday"):
        response = eventBot.getEventByDay(day="Friday")

    elif (message.text == "Saturday"):
        response = eventBot.getEventByDay(day="Saturday")
        
    elif (message.text == "Sunday"):
        response = eventBot.getEventByDay(day="Sunday")

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

    # Emergency annoucment 2020
    elif (message.text == "Announcement❗️"):
        response = publicationBot.getNCOVAnnonucement()

    else:
        response = getErrorResponse()

    return response


def getHomeResponse():
    CustomReplyArray = [
        [KeyboardButton("Announcement❗️")],
        [KeyboardButton("Meal Plan 🍞")],
        [KeyboardButton("Events this week 📆"), KeyboardButton("Eusoff Publications 📩")],
        [KeyboardButton("Home")]
    ]
    CustomReply = ReplyKeyboardMarkup(keyboard=CustomReplyArray)
    response = Response(text="Bringing you home",
                        has_markup=True, reply_markup=CustomReply)
    return response


def getErrorResponse():
    return Response(text="Sorry, I don't recognize this command, try /start", has_markup=True, reply_markup=None)
