import multiprocessing
import time


def my_clock(interval, name):
    while True:
        print("Current time is {0} and cur process name is {1}.".format(time.ctime(), name))
        time.sleep(interval)


if __name__ == "__main__":
    for i in range(5):
        process_name = "process-" + str(i + 1)
        p = multiprocessing.Process(target=my_clock, args=(5, process_name))
        p.start()
        # p.join()

    print("Main process done........")
    exit()