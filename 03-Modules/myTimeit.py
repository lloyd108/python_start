import timeit
import time
import sys
import dis
# help(timeit)

sys.setrecursionlimit(99999)


def factorial(a):
    if a <= 1:
        return 1
    else:
        return a * factorial(a - 1)


t1 = time.time()
factorial(2000)
time.sleep(3)
print(time.time() - t1)


code1 = """
sum = []
for i in range(1000):
    sum.append(i)
"""

code2 = """
def factorial(a):
    if a <= 1:
        return 1
    else:
        return a * factorial(a - 1)

factorial(2000)
"""

t1 = timeit.timeit(stmt="[i for i in range(1000)]", number=100000)
t2 = timeit.timeit(stmt=code1, number=100000)
t3 = timeit.timeit(stmt=code2, number=1000)
t4 = timeit.timeit(stmt="time.sleep(2)", number=10)
print(t1, t2, t3, t4, sep="/////")

# dis(factorial(3))
