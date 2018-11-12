def say_hello(name):
    print("I want to say hello to you {0}".format(name.capitalize()))
    print("Hello, {0}".format(name.capitalize()))
    print("Done...............")


if __name__ == "__main__":
    print('***' * 10)
    name = input("Please input your name: ")
    print(say_hello(name=name))
    print('@@@' * 10)