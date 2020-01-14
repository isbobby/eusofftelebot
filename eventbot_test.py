from datetime import datetime, timedelta

import pytz

singaporeTimezone = pytz.timezone("Asia/Singapore")
todayTime = datetime.now(singaporeTimezone)

day_difference = datetime.now().weekday()
print("Day difference is " + str(day_difference))

tomorrowTime = datetime.now(singaporeTimezone) + timedelta(days=1)
print("tomorrow date time - " + str(tomorrowTime))

MonDatetime = datetime.now(singaporeTimezone) - timedelta(days=day_difference)
MonDate = MonDatetime.strftime("%Y-%m-%d")
print("Monday - " + str(MonDate))

TuesDatetime = MonDatetime + timedelta(days=1)
TuesDate = TuesDatetime.strftime("%Y-%m-%d")
# TuesDate = TuesDate.strftime("%Y-%m-%d 00:00:00")
print("Tuesday - " + str(TuesDate))

WedDatetime = MonDatetime + timedelta(days=2)
WedDate = WedDatetime.strftime("%Y-%m-%d")
print("Wednesday - " + str(WedDate))

ThursDatetime = MonDatetime + timedelta(days=3)
ThursDate = ThursDatetime.strftime("%Y-%m-%d")
print("Thursday - " + str(ThursDate))

FriDatetime = MonDatetime + timedelta(days=4)
FriDate = FriDatetime.strftime("%Y-%m-%d")
print("Friday - " + str(FriDate))

SatDatetime = MonDatetime + timedelta(days=5)
SatDate = SatDatetime.strftime("%Y-%m-%d")
print("Saturday - " + str(SatDate))

SunDatetime = MonDatetime + timedelta(days=6)
SunDate = SunDatetime.strftime("%Y-%m-%d")
print("Sunday - " + str(SunDate))

