from telegram import KeyboardButton, ReplyKeyboardMarkup
from datetime import datetime, timedelta

from eusoffbot.response import Response
from eusoffbot import replies

from eusoffweb.models import Breakfast, Dinner

"""
Define date variables
"""
todayTime = datetime.now()
tomorrowTime = datetime.now() + timedelta(days=1)

DateToday = todayTime.strftime("%Y-%m-%d")
DateTomorrow = tomorrowTime.strftime("%Y-%m-%d")


def getResponse(message):
    """
    Calls the corresponding methods for responses users enter
    """
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
    """
    This method queries the DB for breakfast with today's date
    """
    todayBreakfast = Breakfast.query.filter(Breakfast.date == DateToday).first()
    if todayBreakfast:
        return Response(text=todayBreakfast.toString(), has_markup=True, reply_markup=None)

    return Response(text="Breakfast is not provided today, or the menu is not yet updated)", has_markup=True, reply_markup=None)


def getTodayDinner():
    """
    This method queries the DB for dinner with today's date
    """
    todayDinner = Dinner.query.filter(Dinner.date == DateToday).first()
    if todayDinner:
        return Response(text=todayDinner.toString(), has_markup=True, reply_markup=None)

    return Response(text="Dinner is not provided today, or the menu is not yet updated)", has_markup=True, reply_markup=None)


def getTomorrowBreakfast():
    """
    This method queries the DB for breakfast with tomorrow's date
    """
    tomorrowBreakfast = Breakfast.query.filter(Breakfast.date == DateTomorrow).first()
    if tomorrowBreakfast:
        return Response(text=tomorrowBreakfast.toString(), has_markup=True, reply_markup=None)

    return Response(text="Breakfast is not provided tomorrow, or the menu is not yet updated)", has_markup=True, reply_markup=None)


def getTomorrowDinner():
    """
    This method queries the DB for dinner with tomorrow's date
    """
    tomorrowDinner = Dinner.query.filter(Dinner.date == DateTomorrow).first()
    if tomorrowDinner:
        return Response(text=tomorrowDinner.toString(), has_markup=True, reply_markup=None)

    return Response(text="Dinner is not provided tomorrow, or the menu is not yet updated)", has_markup=True, reply_markup=None)


def getCalendarPDF():
    return Response(text="Some error has occured", has_markup=True, reply_markup=None)


def getUpcomingMatches():
    return Response(text="Some error has occured", has_markup=True, reply_markup=None)


def getUpcomingPerformances():
    return Response(text="Some error has occured", has_markup=True, reply_markup=None)


def getSMCNewsletterPDF():
    return Response(text="Some error has occured", has_markup=True, reply_markup=None)
