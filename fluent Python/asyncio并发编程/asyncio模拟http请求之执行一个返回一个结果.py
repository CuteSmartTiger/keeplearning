# asyncio 没有提供http协议的接口,提供tcp udp底层的的协议，
# 可以使用aiohttp获取http协议接口
import asyncio
import socket
from urllib.parse import urlparse


async def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    # 建立socket连接
    # await 后面跟协程的方法
    reader, writer = await asyncio.open_connection(host, 80)
    # 封装过后的send方法
    writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
    all_lines = []
    async for raw_line in reader:
        data = raw_line.decode('utf8')
        all_lines.append(data)
    html = '\n'.join(all_lines)
    return html


async def main():
    tasks = []
    for url in range(20):
        url = 'http://www.baidu.com'
        tasks.append(asyncio.ensure_future(get_url(url)))
    for task in asyncio.as_completed(tasks):
        result = await task
        print('协程执行一个返回一个的结果为：{0}'.format(result))


if __name__ == "__main__":
    import time
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(time.time() - start_time)
