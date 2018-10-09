import math as m
import random as r

print(m.ceil(5.25))

print(m.pi)

print(m.e)

for i in range(0,10):
    print(r.random())

for i in range(10):
    print(r.randint(1,10))

help(r.randint)


a = 1000000
b = a

print(b is a)