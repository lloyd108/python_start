class Person:
    name = "Person"
    __age = 25
    _gender = "Male"


p = Person()
print(p.name)
#print(p.__age)
print(p._gender)
print(Person.__dict__)
print(p._Person__age)