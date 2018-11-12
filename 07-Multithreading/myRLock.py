import threading
import time


num = 0
# mutex = threading.Lock()
mutex = threading.RLock()


class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if mutex.acquire(3):
            num += 1
            msg = self.name + " set num to " + str(num)
            print(msg)
            mutex.acquire()
            mutex.release()
            mutex.release()


def my_func():
    for i in range(5):
        time.sleep(1)
        t = MyThread()
        t.start()


if __name__ == "__main__":
    my_func()
