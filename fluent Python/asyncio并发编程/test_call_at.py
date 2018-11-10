import asyncio


def callback(sleep_times,loop):
    print('sleep {0} suceess {1}'.format(sleep_times,loop.time()))


def stoploop(loop):
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    now =loop.time()
    # 消息队列中立即执行
    loop.call_at(now+2, callback, 2,loop)
    loop.call_at(now+1, callback, 1,loop)
    loop.call_at(now+3, callback, 3,loop)
    loop.call_soon(callback, 4,loop)
    # 这里使用run_forever而不是until_completed,因为调用的是函数而不是协程
    loop.run_forever()
