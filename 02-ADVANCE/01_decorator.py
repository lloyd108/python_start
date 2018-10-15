def deco(func):
    def say():
        print("First line to add somthing.")
        func()
        print("OK...")
    return say


@deco
def hello():
    print("Hello World!")


hello()
