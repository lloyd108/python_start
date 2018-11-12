from pkg01 import pkg01_01 as pk1
import pkg02.pkg02_01


cat = pk1.Animal("Cat", "Male")
eagle = pkg02.pkg02_01.Bird("Eagle", "Female")

cat.eat()
eagle.fly()

