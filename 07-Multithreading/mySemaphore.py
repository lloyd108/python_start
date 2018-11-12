import threading
import time
import random


my_semaphore = threading.Semaphore(3)


def my_semaphore_func():
    if my_semaphore.acquire():
        sleep_time = random.randint(1,99)
        for i in range(2):
            print(threading.current_thread().getName() + " get semaphore and sleeped " + str(sleep_time))
        time.sleep(sleep_time)
        my_semaphore.release()
        print(threading.current_thread().getName() + " released semaphore.")


for i in range(10):
    t = threading.Thread(target=my_semaphore_func, args=())
    t.start()
    # t.join()

