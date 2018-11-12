import threading
import time


def func():
    print("I'm running...")
    time.sleep(10)
    print("I'm done...")


if __name__ == "__main__":
    t = threading.Timer(6, func)
    t.start()

    threading.Timer(3, func).start()

    i = 0
    while True:
        print("{0} ************ ".format(i))
        time.sleep(1)
        i += 1
        if i == 20:
            break
