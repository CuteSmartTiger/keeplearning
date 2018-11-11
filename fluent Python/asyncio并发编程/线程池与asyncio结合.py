# 使用多线程：在协程中集成阻塞IO
# asyncio异步IO可以完成 多线程 多进程 协程的任务
# ThreadPoolExector + asyncio
import asyncio
from concurrent.futures import ThreadPoolExecutor
import socket
from urllib.parse import urlparse


# 此为阻塞接口
def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client.setblocking(False)
    client.connect((host, 80))  # 阻塞不会消耗cpu

    # 不停的询问连接是否建立好， 需要while循环不停的去检查状态
    # 做计算任务或者再次发起其他的连接请求

    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))

    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break

    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()


if __name__ == '__main__':
    import time

    start_time = time.time()
    loop = asyncio.get_event_loop()
    # 申请一个线程池，让阻塞代码在线程池中运行
    executor = ThreadPoolExecutor()
    tasks = []
    for url in range(20):
        url = 'http://www.baidu.com'
        task = loop.run_in_executor(executor, get_url, url)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start_time)
