from functools import reduce


def my_add(x, y):
    return x + y


l1 = [i for i in range(10)]

rst = reduce(my_add, l1)
print(rst)