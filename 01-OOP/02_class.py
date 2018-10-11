"""
class related
"""

class Student():
    name = "A"
    age = 18


class A():
    name = "yz"
    age = 30

    """
    def __init__(self):
        self.name = "init"
        self.age = "init"
    """

    def say(self):
        self.name = "zfb"
        self.age = 27

class Teacher():
    name = "teacher"
    age = "100"

    def say(self):
        self.name = "teacherName"
        self.age = 33
        print("My name is {0} and {1} now.".format(self.name, self.age))

    def sayagain(self, name, age):
        self.name = name
        self.age = age
        print("My name is {0} and {1} now.".format(__class__.name, age))

    def saythird():
        print("I don't have any name.")


def class02_01():
    for k, v in Student.__dict__.items():
        print(k, v, sep="&&&&&&")
    print(Student.__dict__)

    print(__name__)

    print("*" * 50)

    zfb = Student()
    print(zfb.__dict__)
    print(zfb.name)


def class02_02():
    print(A.name)
    print(A.age)
    print(id(A.name))
    print(id(A.age))

    print("*" * 30)

    a = A()
    print(a.name)
    print(a.age)
    print(id(a.name))
    print(id(a.age))

    print(a.__dict__)

    print("*" * 30)

    a.say()
    print(A.name)
    print(A.age)
    print(id(A.name))
    print(id(A.age))

    print("*" * 30)

    print(a.name)
    print(a.age)
    print(id(a.name))
    print(id(a.age))

    print(a.__dict__)


def class02_03():
    wangLaoShi = Teacher()
    wangLaoShi.say()

    # __class__
    wangLaoShi.sayagain("Wangwangwang", 36)
    
    # wangLaoShi.saythird()
    # Teacher().saythird()
    Teacher.saythird()
    print(Teacher.name, Teacher().age, sep="//////")

if __name__ == "__main__":
    # class02_01()
    # class02_02()
    class02_03()

