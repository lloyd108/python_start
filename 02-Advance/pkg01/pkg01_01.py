class Animal:
    def __init__(self, name="Animal", gender="None"):
        self.name = name
        self.gender = gender

    def eat(self):
        print("name of animal is {0}, gender is {1} and eatting..."\
              .format(self.name, self.gender))
