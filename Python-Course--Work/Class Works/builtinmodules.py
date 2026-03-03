
from datetime import date,time
today= date.today()

print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday)
print(today.isoweekday)

from datetime import date,time,datetime
now = datetime.now()

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Weekday (0=Monday):", now.weekday())
print("ISO Weekday (1=Monday):", now.isoweekday())

from datetime import date,time,datetime
now =datetime.now()
print("year:",now.year)
print("month:",now.month)
print("day:",now.day)
print("hour:",now.hour)
print("minute:",now.minute)
print("second:",now.second)
print("microsecond:",now.microsecond)

# Formmatting date and times :
from datetime import date,time,datetime
now =datetime.now()
print(now)
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%H:%M:%S"))
print(now.strftime("%I:%M:%S"))
print(now.strftime("%A, %d %b %Y %I:%M:%S %p"))

from datetime import date,time,datetime,timedelta
today = datetime.now()
now=datetime.now()
n=today-timedelta(days=5)
print(n)
h=now-timedelta(days=5)
print(n)
h=now-timedelta(hours=15)
print(h)













