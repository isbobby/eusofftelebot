from eusoffbot.response import Response
from eusoffbot import replies

from telegram import KeyboardButton, ReplyKeyboardMarkup


def get_response(message):
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

    elif (message.text == "Calendar and Fixture 📆"):
        response = getCalendarResponse()

    elif (message.text == "Eusoff Publications 📩"):
        response = getPubsResponse()

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


def getMealplanResponse():
    CustomReplyArray = [
        [KeyboardButton("Today's Breakfast"),
         KeyboardButton("Today's Dinner")],
        [KeyboardButton("Tomorrow's Breakfast"),
         KeyboardButton("Tomorrow's Dinner")],
        [KeyboardButton("Home")]
    ]
    CustomReply = ReplyKeyboardMarkup(keyboard=CustomReplyArray)
    response = Response(text="Bringing you home",
                        has_markup=True, reply_markup=CustomReply)
    return response


def getCalendarResponse():
    CustomReplyArray = [
        [KeyboardButton("Calendar (PDF)")],
        [KeyboardButton("Upcoming Matches")],
        [KeyboardButton("Upcoming Performances")],
        [KeyboardButton("Home")]
    ]
    CustomReply = ReplyKeyboardMarkup(keyboard=CustomReplyArray)
    response = Response(text="Happenings this month",
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
    return Response(text="Some error has occured", has_markup=True, reply_markup=None)


def getTodayBreakfast():
    return Response(text="Some error has occured", has_markup=True, reply_markup=None)


def getTodayDinner():
    return Response(text="Some error has occured", has_markup=True, reply_markup=None)


def getTomorrowBreakfast():
    return Response(text="Some error has occured", has_markup=True, reply_markup=None)


def getTomorrowDinner():
    return Response(text="Some error has occured", has_markup=True, reply_markup=None)


def getCalendarPDF():
    return Response(text="Some error has occured", has_markup=True, reply_markup=None)


def getUpcomingMatches():
    return Response(text="Some error has occured", has_markup=True, reply_markup=None)


def getUpcomingPerformances():
    return Response(text="Some error has occured", has_markup=True, reply_markup=None)


def getSMCNewsletterPDF():
    return Response(text="Some error has occured", has_markup=True, reply_markup=None)
