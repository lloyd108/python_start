import os


def simple_coroutine():
    print(os.name)
    l1 = ["The current system is:", os.name]
    os_name = " ".join(l1)


    x = yield os_name

    print("Continued value is x: ", x)


if __name__ == "__main__":
    try:
        s = simple_coroutine()
        print(next(s))
        s.send("continue...")
    except StopIteration as e:
        print("well then...")
