"""
nothing special
just a simple package of student
"""


class Student:
    def __init__(self, name="initName", age=0):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0} and {1} years old now.".format(self.name, self.age))


def say_hello(place = "Python"):
    print("Welcome to {0}!!".format(place))


if __name__ == "__main__":
    # print("This is {0}.".format(__name__))
    print("lolololo")
    print("This is {0}.".format(__name__))
