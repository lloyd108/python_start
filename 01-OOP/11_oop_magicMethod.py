class A:
    def __new__(cls, *args, **kwargs):
        print("I'm new...")
        return super().__new__(cls)

    def __init__(self):
        self.name = self.__class__.__name__
        print("I'm {} and I'm initializing..".format(self.name))

    def __call__(self, *args, **kwargs):
        print("I've been called.")

    def __str__(self):
        return "I'm {} and I'm a string".format(self.name)

    def __repr__(self):
        pass

    def __getattr__(self, item):
        if item == "gender":
            return "Male"
        else:
            print("No attr")

    def __setattr__(self, key, value):
        print("Set {0} values {1}...".format(key, value))
        # self.key = value
        super().__setattr__(key, value)




a = A()
print("*" * 30)
a()
print(a)
a.age
print(a.gender)
a.date = "today"
print(a.date)