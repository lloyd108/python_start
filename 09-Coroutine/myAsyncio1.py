import threading
#import time
import asyncio


@asyncio.coroutine
def say():
    print("my thread is ", threading.currentThread())
    yield from asyncio.sleep(10)
    print("my thread is ", threading.currentThread())


loop = asyncio.get_event_loop()
tasks = [say(), say(), say()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()