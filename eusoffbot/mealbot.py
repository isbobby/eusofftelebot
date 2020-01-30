from eusoffweb.models import Breakfast, Dinner
from eusoffbot.response import Response
from eusoffbot.timebot import TimeBot

from datetime import datetime, timedelta
from telegram import KeyboardButton, ReplyKeyboardMarkup

import pytz


class MealBot():
    def __init__(self):
        self.tb = TimeBot()

    def getMealplanResponse(self):
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


    def getTodayBreakfast(self):
        """
        This method queries the DB for breakfast with today's date
        """
        date = self.tb.getTodayDate()
        todayBreakfast = Breakfast.query.filter(Breakfast.date == date).first()

        try: 
            print(date)
        except:
            print("Date error")

        if todayBreakfast:
            return Response(text=todayBreakfast.toString(), has_markup=True, reply_markup=None)

        return Response(text="Breakfast is not provided today, or the menu is not yet updated)", has_markup=True, reply_markup=None)


    def getTodayDinner(self):
        """
        This method queries the DB for dinner with today's date
        """
        date = self.tb.getTodayDate()
        try: 
            print(date)
        except:
            print("Date error")

        todayDinner = Dinner.query.filter(Dinner.date == date).first()
        if todayDinner:
            return Response(text=todayDinner.toString(), has_markup=True, reply_markup=None)

        return Response(text="Dinner is not provided today, or the menu is not yet updated)", has_markup=True, reply_markup=None)


    def getTomorrowBreakfast(self):
        """
        This method queries the DB for breakfast with tomorrow's date
        """
        date = self.tb.getTomorrowDate()
        try: 
            print(date)
        except:
            print("Date error")

        tomorrowBreakfast = Breakfast.query.filter(
            Breakfast.date == date).first()
        if tomorrowBreakfast:
            return Response(text=tomorrowBreakfast.toString(), has_markup=True, reply_markup=None)

        return Response(text="Breakfast is not provided tomorrow, or the menu is not yet updated)", has_markup=True, reply_markup=None)


    def getTomorrowDinner(self):
        """
        This method queries the DB for dinner with tomorrow's date
        """
        date = self.tb.getTomorrowDate()
        try: 
            print(date)
        except:
            print("Date error")
            
        tomorrowDinner = Dinner.query.filter(Dinner.date == date).first()
        if tomorrowDinner:
            return Response(text=tomorrowDinner.toString(), has_markup=True, reply_markup=None)

        return Response(text="Dinner is not provided tomorrow, or the menu is not yet updated)", has_markup=True, reply_markup=None)
