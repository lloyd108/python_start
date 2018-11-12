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
print(s1_iter.__next__())