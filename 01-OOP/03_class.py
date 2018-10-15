class A:
    name = "aaaa"
    age = 17

    def __init__(self):
        self.name = "initA"
        self.age = 66

    def say(self):
        print("My name is {0} and I'm {1} years old.".format(self.name, self.age))

    def sayagain(self):
        print("My name is {0} and I'm {1} years old.".format(__class__.name, __class__.age))


class B:
    name = "bbbb"
    age = 15


a = A()

a.say()
A.say(a)
A.say(A)
A().say()
a.sayagain()
A().sayagain()

A.say(B)

dir(a)
