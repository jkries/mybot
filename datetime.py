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

print("Hello there!")
print("Today is " + weekday + ", " + mm + "/" + dd + "/" + yyyy)
print("The time is " + hour + ":" + minute)
