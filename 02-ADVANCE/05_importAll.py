from o01_stu import *
import importlib
import sys


STU = importlib.import_module("01_stu")

say_hello()
STU.say_hello()


print("*" * 50)

print(sys.path)

my_method_path = r"E:\python_start\01-OOP"
sys.path.append(my_method_path)
print(sys.path)