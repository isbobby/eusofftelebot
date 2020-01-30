from eusoffweb.models import Event
from eusoffbot.response import Response
from eusoffbot.timebot import TimeBot
from eusoffweb import db

from datetime import datetime, timedelta
from telegram import KeyboardButton, ReplyKeyboardMarkup
from sqlalchemy import between, select

import pytz

class EventBot():
    def __init__(self):
        """
        Initialize timebot
        """
        self.tb = TimeBot()
    
    def getEventDescription(self, event):
        """
        Returns a descriptive string for an event object
        """
        descriptiveString = (
                event.description +"\n"
                "Time: " + event.datetime.strftime("%H:%M") + "\n" +
                "Venue: " + event.venue + "\n\n"
            )
        return descriptiveString

    def getEventByDay(self, day):
        """
        Takes in a day argument and queries for the events happening on this day.
        Then return these events as a string to the users.
        """
        datetime_of_given_day = self.tb.getThisWeekDatetimeByDay(day)

        start_of_given_day = self.tb.formatStartOfDay(datetime_of_given_day)
        end_of_given_day = self.tb.formatEndOfDay(datetime_of_given_day)

        events_on_this_day = db.engine.execute( 
            "SELECT * FROM event WHERE datetime BETWEEN '{}' AND '{}';".format(start_of_given_day, end_of_given_day)
        )

        event_description = "Event(s) on " + day + "\n\n"
        has_event = False 

        for event in events_on_this_day:
            event_description += (self.getEventDescription(event))
            has_event = True
        
        if has_event:
            return Response(text=event_description, has_markup=True, reply_markup=None)

        return Response(text="Seems like nothing is happening this day", has_markup=True, reply_markup=None)

    def getCalendarResponse(self):
        CustomReplyArray = [
            # [KeyboardButton("Calendar (PDF)")],
            [KeyboardButton("Monday"), KeyboardButton("Tuesday")],
            [KeyboardButton("Wednesday"), KeyboardButton("Thursday")],
            [KeyboardButton("Friday"), KeyboardButton("Saturday")],
            [KeyboardButton("Sunday"), KeyboardButton("Home")],
        ]
        CustomReply = ReplyKeyboardMarkup(keyboard=CustomReplyArray)
        response = Response(text="See what's happening this week",
                            has_markup=True, reply_markup=CustomReply)
        return response

    def submitEvent(self, event_detail):
        """
        This method allows users to submit a event, which will be forwarded to Bobby for database logging
        """ 
        return 1


        




