import threading
import time


lock_1 = threading.Lock()
lock_2 = threading.Lock()



def my_func_1():
    print("func_1 starting...")
    print("func_1 acquiring lock1")
    lock_1.acquire()
    print("func_1 acquired lock1")
    print("func_1 waiting for lock2")
    time.sleep(10)
    print("func_1 acquiring lock2")
    lock_2.acquire()
    print("func_1 acquired lock2")
    time.sleep(10)
    lock_2.release()
    print("func_1 released lock2")
    lock_1.release()
    print("func_1 released lock1")
    print("func_1 done...")


def my_func_2():
    print("func_2 starting...")
    print("func_2 acquiring lock2")
    lock_2.acquire()
    print("func_2 acquired lock2")
    print("func_2 waiting for lock1")
    time.sleep(10)
    print("func_2 acquiring lock1")
    lock_1.acquire()
    print("func_2 acquired lock1")
    time.sleep(10)
    lock_1.release()
    print("func_2 released lock1")
    lock_2.release()
    print("func_2 released lock2")
    print("func_2 done...")


if __name__ == "__main__":
    print("main process starting...")

    t1 = threading.Thread(target=my_func_1, args=())
    t2 = threading.Thread(target=my_func_2, args=())

    t1.start()
    t2.start()

    t1.join(30)
    t2.join(30)

    print("main process done...")