from eusoffweb.models import Breakfast, Dinner
from eusoffbot.response import Response

from datetime import datetime, timedelta
from telegram import KeyboardButton, ReplyKeyboardMarkup

"""
Define date variables
"""
todayTime = datetime.now()
tomorrowTime = datetime.now() + timedelta(days=1)

DateToday = todayTime.strftime("%Y-%m-%d")
DateTomorrow = tomorrowTime.strftime("%Y-%m-%d")


def getMealplanResponse():
    CustomReplyArray = [
        [KeyboardButton("Today's Breakfast"),
         KeyboardButton("Today's Dinner")],
        [KeyboardButton("Tomorrow's Breakfast"),
         KeyboardButton("Tomorrow's Dinner")],
        [KeyboardButton("Home")]
    ]
    CustomReply = ReplyKeyboardMarkup(keyboard=CustomReplyArray)
    response = Response(text="Bringing you the menu",
                        has_markup=True, reply_markup=CustomReply)
    return response


def getTodayBreakfast():
    """
    This method queries the DB for breakfast with today's date
    """
    todayBreakfast = Breakfast.query.filter(
        Breakfast.date == DateToday).first()
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
    tomorrowBreakfast = Breakfast.query.filter(
        Breakfast.date == DateTomorrow).first()
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
