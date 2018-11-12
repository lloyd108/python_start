import os
import sys

print("current directory")
my_dir = os.getcwd()
print(my_dir)

print("upper directory")
os.chdir("../")
print(os.getcwd())
print(os.listdir(my_dir))
print(os.listdir(os.getcwd()))

print("upper...")
# os.chdir("aaaa")
os.chdir("../")
print(os.getcwd())
print(os.listdir(my_dir))
print(os.listdir(os.getcwd()))

ab_path = r"E:\python_start\03-MODULES"
# os_directory = os.mkdir(ab_path + r"\test")

rst = os.system("dir")
print(type(rst))
print(rst)


print(os.getenv("PATH"))

# os.system("taskmgr")
print(my_dir)
os.chdir(my_dir)
print(os.sep)
print(os.linesep)
print(os.curdir)
print(os.pardir)
print(os.name, sys.platform, sep="///")

print(os.path.abspath(os.curdir))

my_file_name = "test_file"