from collections import Iterable, Iterator


l1 = [i for i in range(10)]

print(isinstance(l1, Iterator))
print(isinstance(l1, Iterable))

s1 = "This a simple string."
print(isinstance(s1, Iterator))
print(isinstance(s1, Iterable))

s1_iter = iter(s1)
print(isinstance(s1_iter, Iterator))
print(isinstance(s1_iter, Iterable))

print(s1_iter.__next__())
print(next(s1_iter), next(s1_iter))


def my_func():
    print("step1")
    yield 1
    print("step2")
    yield 2
    print("step3")
    yield 3
    return None


a = my_func()
a1 = next(a)
a2 = next(a)
a3 = next(a)
# a4 = next(a)
print(a1, a2, a3)
