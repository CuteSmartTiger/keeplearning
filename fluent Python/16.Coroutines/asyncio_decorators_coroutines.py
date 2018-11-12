import threading
import asyncio
import types


# 二选一，两个装饰器都可以用
@asyncio.coroutine
# @types.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(0.5)
    print('Hello again! (%s)' % threading.currentThread())


if __name__ == '__main__':
    import time

    tasks = []
    start_time = time.time()
    loop = asyncio.get_event_loop()
    for i in range(20):
        tasks.append(hello())
    print(tasks)
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    print(time.time() - start_time)
