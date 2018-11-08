import queue
import threading
import time


queue = queue.Queue()


class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 1000:
                for i in range(100):
                    count += 1
                    msg = self.name + " produced a product " + str(count)
                    queue.put(msg)
            time.sleep(1)


class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(100):
                    msg = self.name + " consumed a product " + queue.get()
                    print(msg)
            time.sleep(1)


if __name__ == '__main__':
    # queue = queue.Queue()

    for i in range(500):
        queue.put("init product " + str(i))
    for i in range(10):
        p = Producer()
        p.start()
        print("start a new producer instance: ", p.name)
    time.sleep(10)
    for i in range(1):
        c = Consumer()
        c.start()