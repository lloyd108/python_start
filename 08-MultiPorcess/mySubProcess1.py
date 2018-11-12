import multiprocessing as mp
from time import sleep, ctime


class MyClock(mp.Process):
    def __init__(self, interval, name):
        super().__init__()
        self.interval = interval
        self.name = name

    def run(self):
        while True:
            print("Current time is {0} and cur process name is {1}.".format(ctime(), self.name))
            sleep(self.interval)


if __name__ == "__main__":
    for i in range(5):
        process_name = "process-" + str(i + 1)
        p = MyClock(i + 1, process_name)
        # p.run(process_name)
        p.start()

    while True:
        sleep(1)
        print()