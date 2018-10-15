"""
nothing special
"""


class Fish:
    def __init__(self, name):
        self.name = name

    def swim(self):
        print("I'm swimming...")


class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print("I'm flying...")


class Person:
    def __init__(self, name):
        self.name = name

    def work(self):
        print("I'm working...")


class SuperMan(Person, Bird, Fish):
    pass


class Student(Person):
    pass


if __name__ == "__main__":
    s = SuperMan("Ken Clark")
    s.work()
    s.fly()
    s.swim()
    print(s.name)

    stu = Student("ZFB")
    stu.work()
    print(stu.name)