import abc


class Person(metaclass=abc.ABCMeta):
    name = "PERSON"

    def say(self):
        print("hehe")

    @abc.abstractmethod
    def talk(self):
        pass

    @abc.abstractclassmethod
    def eat(cls):
        pass

    @abc.abstractstaticmethod
    def drink():
        pass



class Human(Person):
    pass


xiaoming = Human()
xiaoming.say()




