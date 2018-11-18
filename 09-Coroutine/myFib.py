def fib(cnt):
    n, a, b = 0, 0, 1
    while n < cnt:
        print(b)
        a, b = b, a + b
        n += 1


def y_fib(cnt):
    n, a, b = 0, 0, 1
    while n < cnt:
        yield b
        a, b = b, a + b
        n += 1


fib(10)
print("#" * 10)

rst = y_fib(10)
for i in range(11):
    try:
        print(next(rst))
    except StopIteration as e:
        print(e.args, e.value, e.__traceback__, sep="///")

rst = y_fib(10)
for v in rst:
    print(v)