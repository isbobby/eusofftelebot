from eusoffweb.models import Event
from eusoffbot.response import Response
from eusoffweb import db

from datetime import datetime, timedelta
from telegram import KeyboardButton, ReplyKeyboardMarkup
from sqlalchemy import between, select

import pytz

"""
Define date variables
"""
singaporeTimezone = pytz.timezone("Asia/Singapore")

todayTime = datetime.now(singaporeTimezone)
tomorrowTime = datetime.now(singaporeTimezone) + timedelta(days=1)

DateToday = todayTime.strftime("%Y-%m-%d")
DateTomorrow = tomorrowTime.strftime("%Y-%m-%d")

DatetimeToday = todayTime.strftime("%Y-%m-%d 00:00:00")
DatetimeTodayMidnight = todayTime.strftime("%Y-%m-%d 23:59:59")

DatetimeTomorrow = tomorrowTime.strftime("%Y-%m-%d 00:00:00")
DatetimeTomorrowMidnight = tomorrowTime.strftime("%Y-%m-%d 23:59:59")

def getCalendarResponse():
    CustomReplyArray = [
        # [KeyboardButton("Calendar (PDF)")],
        [KeyboardButton("What's up today")],
        [KeyboardButton("What's up tomorrow")],
        [KeyboardButton("Home")]
    ]
    CustomReply = ReplyKeyboardMarkup(keyboard=CustomReplyArray)
    response = Response(text="What's happenin",
                        has_markup=True, reply_markup=CustomReply)
    return response


def getCalendarPDF():
    return Response(text="Some error has occured, or this feature has not yet been implemented", has_markup=True, reply_markup=None)


def getTodayEvent():
    todayEvents = db.engine.execute(
        "SELECT * FROM event WHERE datetime BETWEEN '{}' AND '{}';".format(DatetimeToday, DatetimeTodayMidnight)
    )

    todayEventsDescription = ""
    
    for event in todayEvents:
        todayEventsDescription += (getEventDescription(event))
    
    if todayEventsDescription:
        return Response(text=todayEventsDescription, has_markup=True, reply_markup=None)

    return Response(text="Seems like nothing is happening today", has_markup=True, reply_markup=None)


def getTomorrowEvent():
    tomorrowEvents = db.engine.execute(
        "SELECT * FROM event WHERE datetime BETWEEN '{}' AND '{}';".format(DatetimeTomorrow, DatetimeTomorrowMidnight)
    )

    tomorrowEventsDescription = ""
    
    for event in tomorrowEvents:
        tomorrowEventsDescription += (getEventDescription(event))
    
    if tomorrowEventsDescription:
        return Response(text=tomorrowEventsDescription, has_markup=True, reply_markup=None)

    return Response(text="Seems like nothing is happening today", has_markup=True, reply_markup=None)


def getEventDescription(event):
    """
    Returns a descriptive string for an event object
    """
    descriptiveString = (
            "Event Date and Time: " + event.datetime.strftime("%d - %b, %H:%M") + "\n\n" +
            "Event Venue: " + event.venue + "\n\n" +
            event.description +"\n\n"
        )
    return descriptiveString