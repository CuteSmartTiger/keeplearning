# task与future用法的区别
import time
import asyncio
from functools import partial


# 如何获取协程的返回值，添加一个callback方法
async def get_html(url):
    print('start get url')
    # 协程或者异步中不可以使用time.sleep阻塞方法
    # 前面需要加await，await后面需要使用awaitable对象
    await asyncio.sleep(2)
    return 'liuhu'


def callback(url, future):
    print(url)
    print('send kiss to me')


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # get_future=asyncio.ensure_future(get_html('wwww.baidu.com'))
    task = loop.create_task(get_html('wwww.baidu.com'))
    # 使用偏函数实现可以往callback中传参数
    task.add_done_callback(partial(callback, 'wwww.baidu.com'))
    loop.run_until_complete(task)
    # 执行完callback函数后再返回值，task.result()获取函数的返回值
    print(task.result())
