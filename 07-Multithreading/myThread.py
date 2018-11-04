import time
import _thread as thread


def loop1():
    loop1_time = time.time()

    time.sleep(4)

    print("Loop1 runs {0} seconds.".format(time.time() - loop1_time))


def loop2():
    loop2_time = time.time()

    time.sleep(2)

    print("Loop2 runs {0} seconds.".format(time.time() - loop2_time))


def main():
    print("Main starts at: ", time.strftime("%Y-%m-%d %H:%M:%S"))
    main_time = time.time()
    thread.start_new_thread(loop1, ())
    thread.start_new_thread(loop2, ())
    print("Main ends at: ", time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Main runs {0} seconds.".format(time.time() - main_time))


if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)
