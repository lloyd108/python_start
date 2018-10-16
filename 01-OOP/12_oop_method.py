class Person:
    def eat(self):
        print("{} is instance method.".format(self))
        print("I'm eating...")

    @classmethod
    def play(cls):
        print("{} is classmethod.".format(cls))
        print("I'm playing...")

    @staticmethod
    def say():
        print("I'm saying...")


p = Person()
p.eat()
p.play()
p.say()

print("&" * 30)

Person.eat(Person)
Person.play()
Person.say()