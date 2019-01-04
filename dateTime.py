from datetime import datetime
from datetime import date
import calendar

now = datetime.now()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
minute = str(now.minute)
second = str(now.second)
mydate = date.today()
weekday = calendar.day_name[mydate.weekday()]

def getTime():
    now = datetime.now()
    mm = str(now.month)
    dd = str(now.day)
    yyyy = str(now.year)
    hour = str(now.hour)
    minute = str(now.minute)
    second = str(now.second)
    mydate = date.today()
    if now.hour >= 12:
        ampm = ' PM'
    else:
        ampm = ' AM'
    if now.hour > 12:
        hour = str(now.hour - 12)
    weekday = calendar.day_name[mydate.weekday()]
    return "The time is now " + hour + ":" + minute + ampm

def getDate():
    now = datetime.now()
    mm = str(now.month)
    dd = str(now.day)
    yyyy = str(now.year)
    hour = str(now.hour)
    minute = str(now.minute)
    second = str(now.second)
    mydate = date.today()
    weekday = calendar.day_name[mydate.weekday()]
    return "Today is " + weekday + ", " + mm + "/" + dd + "/" + yyyy

print("Hello there!")
print(getTime())
print(getDate())
