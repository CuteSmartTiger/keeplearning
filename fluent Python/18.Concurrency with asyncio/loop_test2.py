# task与future用法的区别

import time
import asyncio


async def get_html(url):
    print('start get url')
    # 协程或者异步中不可以使用time.sleep阻塞方法
    # 前面需要加await，await后面需要使用awaitable对象
    await asyncio.sleep(2)
    return 'liuhu'


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # get_future=asyncio.ensure_future(get_html('wwww.baidu.com'))
    task=loop.create_task(get_html('wwww.baidu.com'))
    # tasks中所有的任务执行完毕后才会执行下一步
    #可以接受协程类型或者future类型
    # loop.run_until_complete(get_future)
    loop.run_until_complete(task)
    # print(get_future.result())
    print(task.result())


