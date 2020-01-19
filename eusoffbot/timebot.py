from datetime import datetime, timedelta
import pytz

class TimeBot():
    def __init__(self):
        """
        Define date variables
        """
        self.singaporeTimezone = pytz.timezone("Asia/Singapore")

        self.todayTime = datetime.now(self.singaporeTimezone)
        self.tomorrowTime = datetime.now(
            self.singaporeTimezone) + timedelta(days=1)

        self.DateToday = self.todayTime.strftime("%Y-%m-%d")
        self.DateTomorrow = self.tomorrowTime.strftime("%Y-%m-%d")

        self.DatetimeToday = self.todayTime.strftime("%Y-%m-%d 00:00:00")
        self.DatetimeTodayMidnight = self.todayTime.strftime(
            "%Y-%m-%d 23:59:59")

        self.DatetimeTomorrow = self.tomorrowTime.strftime("%Y-%m-%d 00:00:00")
        self.DatetimeTomorrowMidnight = self.tomorrowTime.strftime(
            "%Y-%m-%d 23:59:59")

    def getThisWeekDatetimeByDay(self, day):
        """
            This method takes in a day ( Monday, Tuesday ...) string as an argument, 
            and returns the raw datetime object of this day in the current week
        """
        day_difference = todayTime.weekday()
        print("Day difference is " + str(day_difference))

        MonDatetime = datetime.now(self.singaporeTimezone) - timedelta(days=day_difference)
        TuesDatetime = MonDatetime + timedelta(days=1)
        WedDatetime = MonDatetime + timedelta(days=2)
        ThursDatetime = MonDatetime + timedelta(days=3)
        FriDatetime = MonDatetime + timedelta(days=4)
        SatDatetime = MonDatetime + timedelta(days=5)
        SunDatetime = MonDatetime + timedelta(days=6)

        if ( day == "Monday" or day == "monday" ):
            return MonDatetime
        
        elif ( day == "Tuesday" or day == "tuesday" ):
            return TuesDatetime

        elif ( day == "Wednesday" or day == "wednesday" ):
            return WedDatetime

        elif ( day == "Thursday" or day == "thursday" ):
            return ThursDatetime

        elif ( day == "Friday" or day == "friday" ):
            return FriDatetime

        elif ( day == "Saturday" or day == "Saturday" ):
            return SatDatetime

        elif ( day == "Sunday" or day == "sunday" ):
            return SunDatetime

        return "error"

    def formatStartOfDay(self, datetimeObject):
        """
        This method converts a datetime object to YYYY-MM-DD 00:00:00 and return it as a string
        """
        return datetimeObject.strftime("%Y-%m-%d 00:00:00")

    def formatEndOfDay(self, datetimeObject):
        """
        This method converts a datetime object to YYYY-MM-DD 23:59:59 and return it as a string
        """
        return datetimeObject.strftime("%Y-%m-%d 23:59:59")