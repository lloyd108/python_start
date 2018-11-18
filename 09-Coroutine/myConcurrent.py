from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import Executor
import time


def some_message(msg):
    time.sleep(5)
    return "--**--" + msg + "--**--"


# create a thread pool
pool = ThreadPoolExecutor(max_workers=100)

# add tasks into pool
f1 = pool.submit(some_message, "1")
f2 = pool.submit(some_message, "2")
f3 = pool.submit(some_message, "3")

# for v in range(4, 10):
    # a = pool.submit(some_message, str(v))
    # print(a.result())

l1 = [str(i) for i in range(1000)]

for v in pool.map(some_message, l1):
    print(v)

# print(f1.done())
# time.sleep(10)
# print(f1.done())

# print(f1.result())
# print(f2.result())