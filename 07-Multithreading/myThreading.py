import time
# import _thread as thread
import threading as thread


def loop1():
    loop1_time = time.time()

    time.sleep(30)

    print("Loop1 runs {0} seconds.".format(time.time() - loop1_time))


def loop2():
    loop2_time = time.time()

    time.sleep(2)

    print(thread.current_thread())
    # print(thread.enumerate())
    # print(thread.active_count())
    # print(thread.activeCount())

    print("Loop2 runs {0} seconds.".format(time.time() - loop2_time))


def main():
    print("Main starts at: ", time.strftime("%Y-%m-%d %H:%M:%S"))
    main_time = time.time()
    # thread.start_new_thread(loop1, ())
    # thread.start_new_thread(loop2, ())
    t1 = thread.Thread(target=loop1, args=())
    t2 = thread.Thread(target=loop2, args=())
    t2.setName("so_funny")
    t1.start()
    t2.start()

    for thr in thread.enumerate():
        print(thr)
    print("Done")

    t1.join()
    print("#" * 10)
    t2.join()
    print("*" * 10)
    print("Main ends at: ", time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Main runs {0} seconds.".format(time.time() - main_time))


if __name__ == '__main__':
    main()
