import asyncio


def callback(sleep_times):
    print('sleep {} suceess'.format(sleep_times))


def stoploop(loop):
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # 消息队列中立即执行
    loop.call_later(2, callback, 2)
    loop.call_later(1, callback, 1)
    loop.call_later(3, callback, 3)
    loop.call_soon(callback, 4)
    # 这里使用run_forever而不是until_completed,因为调用的是函数而不是协程
    loop.run_forever()
