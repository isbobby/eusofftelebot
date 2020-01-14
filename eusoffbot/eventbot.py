from eusoffweb.models import Event
from eusoffbot.response import Response
from eusoffweb import db

from datetime import datetime, timedelta
from telegram import KeyboardButton, ReplyKeyboardMarkup
from sqlalchemy import between, select

import pytz

class EventBot():
    def __init__(self):
        """
        Define date variables
        """
        self.singaporeTimezone = pytz.timezone("Asia/Singapore")

        self.todayTime = datetime.now(self.singaporeTimezone)
        self.tomorrowTime = datetime.now(self.singaporeTimezone) + timedelta(days=1)

        self.DateToday = self.todayTime.strftime("%Y-%m-%d")
        self.DateTomorrow = self.tomorrowTime.strftime("%Y-%m-%d")

        self.DatetimeToday = self.todayTime.strftime("%Y-%m-%d 00:00:00")
        self.DatetimeTodayMidnight = self.todayTime.strftime("%Y-%m-%d 23:59:59")

        self.DatetimeTomorrow = self.tomorrowTime.strftime("%Y-%m-%d 00:00:00")
        self.DatetimeTomorrowMidnight = self.tomorrowTime.strftime("%Y-%m-%d 23:59:59")
    
    def getEventDescription(self, event):
        """
        Returns a descriptive string for an event object
        """
        descriptiveString = (
                "Event Date and Time: " + event.datetime.strftime("%d - %b, %H:%M") + "\n\n" +
                "Event Venue: " + event.venue + "\n\n" +
                event.description +"\n\n"
            )
        return descriptiveString

    def getCalendarResponse(self):
        CustomReplyArray = [
            # [KeyboardButton("Calendar (PDF)")],
            [KeyboardButton("What's up today")],
            [KeyboardButton("What's up tomorrow")],
            [KeyboardButton("Home")]
        ]
        CustomReply = ReplyKeyboardMarkup(keyboard=CustomReplyArray)
        response = Response(text="Check out what is happening today or tomorrow",
                            has_markup=True, reply_markup=CustomReply)
        return response
    
    def getTodayEvent(self):
        todayEvents = db.engine.execute( 
            "SELECT * FROM event WHERE datetime BETWEEN '{}' AND '{}';".format(self.DatetimeToday, self.DatetimeTodayMidnight)
        )

        todayEventsDescription = ""
        
        for event in todayEvents:
            todayEventsDescription += (self.getEventDescription(event))
        
        if todayEventsDescription:
            return Response(text=todayEventsDescription, has_markup=True, reply_markup=None)

        return Response(text="Seems like nothing is happening today", has_markup=True, reply_markup=None)

    def getTomorrowEvent(self):
        tomorrowEvents = db.engine.execute(
            "SELECT * FROM event WHERE datetime BETWEEN '{}' AND '{}';".format(self.DatetimeTomorrow, self.DatetimeTomorrowMidnight)
        )
        tomorrowEventsDescription = ""
        
        for event in tomorrowEvents:
            tomorrowEventsDescription += (self.getEventDescription(event))
        
        if tomorrowEventsDescription:
            return Response(text=tomorrowEventsDescription, has_markup=True, reply_markup=None)

        return Response(text="Seems like nothing is happening today", has_markup=True, reply_markup=None)



        




