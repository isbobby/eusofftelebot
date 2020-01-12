from telegram import KeyboardButton, ReplyKeyboardMarkup

from eusoffbot.response import Response
from eusoffbot.mealbot import (getTodayBreakfast, getTodayDinner,
                               getTomorrowBreakfast, getTomorrowDinner, getMealplanResponse)
from eusoffbot.eventbot import getCalendarPDF, getCalendarResponse, getTomorrowEvent, getTodayEvent

def getResponse(message):
    """
    Calls the corresponding methods for responses users enter
    """
    # Meal plan related
    if (message.text == "/start" or message.text == "Home"):
        response = getHomeResponse()

    elif (message.text == "Meal Plan 🍞"):
        response = getMealplanResponse()

    elif (message.text == "Today's Breakfast"):
        response = getTodayBreakfast()

    elif (message.text == "Today's Dinner"):
        response = getTodayDinner()

    elif (message.text == "Tomorrow's Breakfast"):
        response = getTomorrowBreakfast()

    elif (message.text == "Tomorrow's Dinner"):
        response = getTomorrowDinner()

    # Event related
    elif (message.text == "Calendar and Fixture 📆"):
        response = getCalendarResponse()

    elif (message.text == "What's up today"):
        response = getTodayEvent()

    elif (message.text == "What's up tomorrow"):
        response = getTomorrowEvent()

    elif (message.text == "Eusoff Publications 📩"):
        response = getPubsResponse()

    else:
        response = getErrorResponse()

    return response


def getHomeResponse():
    CustomReplyArray = [
        [KeyboardButton("Meal Plan 🍞")],
        [KeyboardButton("Calendar and Fixture 📆")],
        # [KeyboardButton("Eusoff Publications 📩")],
        [KeyboardButton("Home")]
    ]
    CustomReply = ReplyKeyboardMarkup(keyboard=CustomReplyArray)
    response = Response(text="Bringing you home",
                        has_markup=True, reply_markup=CustomReply)
    return response


def getPubsResponse():
    CustomReplyArray = [
        [KeyboardButton("SMC Newsletter")],
        [KeyboardButton("Home")]
    ]
    CustomReply = ReplyKeyboardMarkup(keyboard=CustomReplyArray)
    response = Response(text="Checking this month's publication",
                        has_markup=True, reply_markup=CustomReply)
    return response


def getErrorResponse():
    return Response(text="Sorry, I don't recognize this command, try /start", has_markup=True, reply_markup=None)


def getSMCNewsletterPDF():
    return Response(text="Some error has occured", has_markup=True, reply_markup=None)
