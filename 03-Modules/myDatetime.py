import datetime
from datetime import datetime as ddt
import time

dt = datetime.date(2018, 10, 24)

print(type(dt))
print(dt)
print(dt.day)
print(dt.month)
print(dt.year)

print("*" * 20)

my_dt = ddt(2018, 10, 24)
print(my_dt.today())
print(my_dt.now())
print(ddt.today())
print(ddt.now())
print(ddt.fromtimestamp(time.time()))

print("&" * 20)

t1 = ddt.now()
print(t1)
print(t1.strftime("%Y%m%d %H%M%S"))

td = datetime.timedelta(seconds=60)

t2 = t1 + td
print(t2.strftime("%Y%m%d %H%M%S"))