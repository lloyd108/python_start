def func_A():
    print("Func a")
    return None


def func_B():
    print("Func B")

    def func_C():
        print("Func C")
        return "c"
    return func_C


fb = func_B()
print(type(fb))
print(fb)
print(fb())

print("#" * 30)


def tired(func):
    def say_tired(*args, **kwargs):
        print("I'm tired...")
        return func(*args, **kwargs)
    return say_tired


@tired
def say(content="something"):
    print("I'm so glad...{0}".format(content))


say("haha")

# b = tired(say)
# b()
