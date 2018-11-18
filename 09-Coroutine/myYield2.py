def simple_coroutine(a):
    print('-> start')

    b = yield a
    print('-> recived', a, b)

    c = yield a + b
    print('-> recived', a, b, c)

    # yield
    # exit()

# runc
def my_start():
    sc = simple_coroutine(5)

    aa = next(sc)
    print(aa)
    bb = sc.send(6) # 5, 6
    print(bb)
    cc = sc.send(7) # 5, 6, 7
    print(cc)


try:
    my_start()
except StopIteration as e:
    print("StopIteration Error...", e.value)
else:
    print("NOt done...")
finally:
    print("All done here.")

# print(list(my_start()))
