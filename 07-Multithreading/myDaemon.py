import time
import threading


def func():
    print("start func...")
    time.sleep(10)
    print("end func...")


print("Main thread start...")

t1 = threading.Thread(target=func, args=())

t1.setDaemon(True)
# t1.daemon = True

t1.start()

# t1.join()

time.sleep(3)
print("Main thread end...")