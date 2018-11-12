# Python为了语义更加明确，以便区分协程与生成器，引入
# async与await关键词用于定于原生的协程


async def download(url):
    return 'nice'


from collections import Awaitable


async def download_url(url):
    # await表示将主导权交给download字生成器(实现了await方法)，并等待返回值赋给res
    # 此处的await可以理解为yield from ，async与await结合使用，
    # async中不可以使用yield 或者yield from
    print('test')
    res = await download(url)
    # res = await customed_await(url)
    return res


# 自定义一个waitable对象
import types


@types.coroutine
def customed_await(url):
    yield 'liuhu'


if __name__ == '__main__':
    corou = download_url('http://www.baidu.com')
    # 此处不可以使用next(None)方法
    # send方法预激函数，可以通过print函数判断，不发送send则函数不会运行
    corou.send(None)
