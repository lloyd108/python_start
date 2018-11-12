import time

print(time.timezone)
print(time.altzone)
print(time.daylight)

print(time.time())

print("*" * 10)

t = time.localtime()
print(type(t))
print(t)
print(isinstance(t, tuple))

print("^" * 10)

tt = time.asctime(t)
print(type(tt))
print(tt)

print("&" * 10)

ts = time.mktime(t)
print(type(ts))
print(ts)

print(type(time.sleep(10)))

time.sleep(6)
print("$" * 100)

t = time.localtime()
ft = time.strftime("%Y%m%d %H:%M:%S", t)
print(ft)