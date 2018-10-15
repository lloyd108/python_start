class Animal:
    def __init__(self):
        self.name = self.__class__.__name__

    def run(self):
        print("I'm {} and I'm running now.".format(self.name))

class Bird(Animal):
    def run(self):
        Animal.run(self)
        print("But bird runs slow.")


class Dog(Animal):
    def run(self):
        Animal.run(self)
        print("Dog runs fast")


def func(obj):
    obj.run()


puppy = Dog()
poly = Bird()

func(puppy)
func(poly)
