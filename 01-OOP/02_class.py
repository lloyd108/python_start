"""
class related
"""

class Student():
    name = "A"
    age = 18


class A():
    name = "yz"
    age = 30

    def say(self):
        self.name = "zfb"
        self.age = 27


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


if __name__ == "__main__":
    # class02_01()
    class02_02()
