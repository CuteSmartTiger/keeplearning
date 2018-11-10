# wait与gather用法的区别
import time
import asyncio


async def get_html(url):
    print('start get url')
    await asyncio.sleep(2)
    print('end get url')


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # tasks为所要提交的所有任务
    # tasks = [get_html('www.baidu.com') for i in range(10)]
    # tasks中所有的任务执行完毕后才会执行下一步
    # gather是相比wait更高级抽象的方法，tasks前需要加*号，才可以解析
    # loop.run_until_complete(asyncio.gather(*tasks))
    # print(time.time() - start_time)

    #gather更加高级，灵活
    group1 = [get_html('www.baidu.com') for i in range(10)]
    group2 = [get_html('www.google.com') for i in range(10)]
    loop.run_until_complete(asyncio.gather(*group1,*group2))
    print(time.time() - start_time)

    # 或者：
    # group1 = [get_html('www.baidu.com') for i in range(10)]
    # group2 = [get_html('www.google.com') for i in range(10)]
    # group1=asyncio.gather(*group1)
    # group2=asyncio.gather(*group2)
    # group2.cancel()
    # loop.run_until_complete(asyncio.gather(group1, group2))
    # print(time.time() - start_time)