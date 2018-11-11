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
    html='\n'.join(all_lines)
    return html




if __name__ == "__main__":
    import time
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = []
    for url in range(20):
        url = 'http://www.baidu.com'
        # tasks.append(get_url(url))
        # 使用future获取执行结果
        tasks.append(asyncio.ensure_future(get_url(url)))
    loop.run_until_complete(asyncio.wait(tasks))
    # 将直接的结果循环打印出来
    for task in tasks:

        print('任务结果为：{0}'.format(task.result()))
    print(time.time() - start_time)
