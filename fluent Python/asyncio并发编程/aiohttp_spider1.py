# asyncio 爬虫 去重 入库
import asyncio
import re

import aiohttp
import aiomysql
from pyquery import PyQuery

stopping = False

start_url = 'http://www.baidu.com'
waitting_urls = []
# 去重，条数不多的情况下可以使用set去重，如果
# 数据上亿条，则此方法非常消耗内存，可以使用过滤器
seen_urls = set()

# 设置并发的数量,完成对并发的控制
sem = asyncio.Semaphore(3)


async def fetch(url, session):
    async with sem:
        await asyncio.sleep(1)
        try:
            # get(url)是一个耗时操作，所以前面使用async with
            async with session.get(url) as resp:
                # 获取请求的状态
                print('url status:{0}'.format(resp.status))
                if resp.status in [200, 201]:
                    data = await resp.text()
                    print(data)
                    return data
        except Exception as e:
            print(e)


def extract_urls(html):
    urls = []
    # 可以查找PyQuery官方文档了解用法
    pq = PyQuery(html)
    for link in pq.items('a'):
        url = link.attr('href')
        if url and url.startwith('http') and url not in seen_urls:
            urls.append(url)
            waitting_urls.append(url)
    return urls


async def init_urls(url, session):
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)


async def article_handler(url, session, pool):
    # 获取文章详情并解析入库
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)
    pq = PyQuery(html)
    title = pq("title").text()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT 42;")
            insert_sql = "insert into article_test(title) values('{}')".format(title)
            await cur.execute(insert_sql)


async def consumer(pool):
    async with aiohttp.ClientSession() as session:
        while not stopping:
            if len(waitting_urls) == 0:
                await asyncio.sleep(0.5)
                continue
            url = waitting_urls.pop()
            print('start get utl :{}'.format(url))
            if re.match('http://.*?jobbole.com/\d+/', url):
                if url not in seen_urls:
                    asyncio.ensure_future(article_handler(url, session))
            else:
                if url not in seen_urls:
                    asyncio.ensure_future(init_urls(url,session))


async def main(loop):
    # 等待MySQL连接建立好，创建连接池时需要指定charset与autocommit
    # await 必须要在协程中使用
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='',
                                      db='mysql', loop=loop,
                                      charset='utf-8', autocommit=True)

    async with aiohttp.ClientSession() as session:
        html = await fetch(start_url, session)
        seen_urls.add(start_url)
        extract_urls(html)
        # asyncio.ensure_future(init_urls(start_url))
        # asyncio.ensure_future(consumer(pool))

    asyncio.ensure_future(consumer(pool))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(loop))
    loop.run_forever()
