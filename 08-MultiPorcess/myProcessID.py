import multiprocessing
import time
import os


def my_clock(interval, name):
    while True:
        print("Current time is {0}, cur process name is {1}, pid is {2} and ppid is {3}.".\
              format(time.ctime(), name, os.getpid(), os.getppid()))
        time.sleep(interval)


if __name__ == "__main__":
    for i in range(5):
        process_name = "process-" + str(i + 1)
        p = multiprocessing.Process(target=my_clock, args=(5, process_name))
        p.start()
        # p.join()

    while True:
        print("Main process id is {0} and parent process id is {1}.".format(os.getpid(), os.getppid()))
        time.sleep(5)

    print("Main process done........")
