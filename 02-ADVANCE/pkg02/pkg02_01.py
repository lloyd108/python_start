class Bird:
    def __init__(self, name="Bird", gender="None"):
        self.name = name
        self.gender = gender

    def fly(self):
        print("Name of bird is {0}, gender is {1} and is flying...".format(\
            self.name, self.gender))