import threading
import timeit


loop_sum = 0
loop_count = 1000000


def my_sum():
    global loop_sum
    global loop_count
    for i in range(loop_count):
        loop_sum += 1


def my_minus():
    global loop_sum
    global loop_count
    for i in range(loop_count):
        loop_sum -= 1


def multi_main():
    t1 = threading.Thread(target=my_sum, args=())
    t2 = threading.Thread(target=my_minus(), args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()


def single_main():
    my_sum()
    my_minus()


if __name__ == "__main__":
    t1 = timeit.timeit(stmt=multi_main, number=10)
    t2 = timeit.timeit(stmt=single_main, number=10)
    print(t1, t2, sep="///")

    print("starting...", loop_sum)
    t3 = threading.Thread(target=my_sum, args=())
    t4 = threading.Thread(target=my_minus, args=())

    t3.start()
    t4.start()

    t3.join()
    t4.join()

    print("ending...", loop_sum)