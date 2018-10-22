from types import MethodType


class A:
    pass


def say(self):
        print("I'm saying...")

say(1)

A.say = say
A.say(1)

a = A()
a.say()

print("*" * 10)


class B:
    pass


def talk(s):
    print("I'm talking...")


b = B()
b.talk = MethodType(talk, B)
b.talk()

print(type(b))

print("*" * 10)


def eat(self):
    print("I'm eating...")


def drink(self):
    print("I'm drinking...")


X = type("NewClass", (object, ), {"new_eat": eat, "new_drink": drink})

x = X()
x.new_eat()
x.new_drink()