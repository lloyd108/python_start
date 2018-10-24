import calendar

help(calendar)
cal = calendar.calendar(2018, w=1, l=1, c=1)
print(type(cal))
print(cal)

print(calendar.isleap(2018))
print(calendar.leapdays(2000, 2020))

print(calendar.month(2018, 10))

print(calendar.monthrange(2018, 10))

print(calendar.monthcalendar(2018, 10))

calendar.prcal(2018)
calendar.prmonth(2018, 10)
print(calendar.weekday(2018, 10, 24))