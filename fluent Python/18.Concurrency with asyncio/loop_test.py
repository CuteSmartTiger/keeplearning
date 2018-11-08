# 事件循环+回调（驱动生成器）+epoll（IO多路复用）
# asyncio是Python用于解决异步IO编程的一整套解决方案

import time
import asyncio


async def get_html(url):
    print('start get url')
    # 协程或者异步中不可以使用time.sleep阻塞方法
    # 前面需要加await，await后面需要使用awaitable对象
    await asyncio.sleep(2)
    print('end get url')


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # tasks为所要提交的所有任务
    tasks = [get_html('www.baidu.com') for i in range(10)]
    # tasks中所有的任务执行完毕后才会执行下一步
    # asyncio.wait生成协程池
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start_time)
