"""
encapsulation:
public/private/protected
super()
"""


class Person:
    name = "Person"
    __age = 25
    _gender = "Male"
    special = "Hahaha"
    age = 33
    gender = "666"

    def __init__(self):
        self.name = "Person_self"

    def sleepwell(self):
        print("{} is sleeping~".format(self.name))


class Teacher(Person):
    """
    def __init__(self):
        self.name = super().name + "Teacher"
        self.age = 13
        self.gender = "Unknown"
    """

    def __init__(self, name):
        self.name = name
        self.age = 22
        self.gender = "Unknown"

    def sleepwell(self):
        super().sleepwell()
        print("OKOKOK")


def encapsulation():
    p = Person()
    print(p.name)
    # print(p.__age)
    print(p._gender)
    print(Person.__dict__)
    print(p._Person__age)


def inherited():
    """
    mryan = Teacher()
    mryan.sleepwell()

    print("#" * 30)
    print(mryan.name, mryan.age, mryan.gender, sep="////")
    print(Teacher.name, Teacher.special, sep="****")
    print(type(Teacher.name), type(Teacher().name), sep="^^^^")
    print(type(Teacher), type(Teacher()), sep="%%%%")
    print(isinstance(Teacher(),type(Person())))
    """

    print("#" * 30)
    mrzhou = Teacher("Zhou")
    mrzhou.sleepwell()

    print("#" * 30)
    print(mrzhou.name, mrzhou.age, mrzhou.gender, sep="////")
    print(Teacher.name, Teacher.special, sep="****")
    # print(type(Teacher.name), type(Teacher().name), sep="^^^^")
    # print(type(Teacher), type(Teacher()), sep="%%%%")
    # print(isinstance(Teacher(), type(Person())))




if __name__ == "__main__":
    # encapsulation()
    inherited()


