# 1. epoll并不代表一定比select好
# 在并发高的情况下，连接活跃度不是很高， epoll比select
# 并发性不高，同时连接很活跃， select比epoll好

# 通过非阻塞io实现http请求
# 本节需要理解高并发的设计模式：select + 回调 + 事件循环
#  并发性高
# 使用单线程，减少了线程切换带来的损耗

import socket
from urllib.parse import urlparse
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

# import select
# select.select()与selector不一样

# 使用DefaultSelector()这样可以可以自己解析运行的操作系统
selector = DefaultSelector()
# 使用select完成http请求
urls = []
stop = False


# 使用类而不是函数，方便调用内部变量
class Fetcher:
    def connected(self, key):
        # 注销监听的key
        selector.unregister(key.fd)
        # 此处不用try 捕获
        self.client.send(
            "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        # 此处调用了readable，为什么不需要传递参数key了
        # 此处注册读的事件
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    # 当socket可读时，处理的方式
    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            # 每获取一次加一次数据
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                # 这里必须定义为全局变量
                global stop
                stop = True

    def get_url(self, url):
        self.spider_url = url
        # 解析url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/"

        # 建立socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置非阻塞模式
        self.client.setblocking(False)

        # 使用非阻塞方式，尝试连接
        try:
            self.client.connect((self.host, 80))
        except BlockingIOError as e:
            pass

        # 注册，注册文件描述符，写入事件，调用连接
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


# 回调是需要自己去调用的
def loop():
    # 事件循环，不停的请求socket的状态并调用对应的回调函数
    # 1. select本身是不支持register模式
    # 2. socket状态变化以后的回调是由程序员完成的
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            # 获取事件注册中的函数
            call_back = key.data
            call_back(key)
    # 回调+事件循环+select(poll\epoll)


if __name__ == "__main__":
    fetcher = Fetcher()
    import time

    start_time = time.time()
    for url in range(30):
        # url = "http://shop.projectsedu.com/goods/{}/".format(url)
        url = "http://www.baidu.com/"
        urls.append(url)
        fetcher = Fetcher()
        fetcher.get_url(url)

    # gevent tando 协程都是按照：回调+事件循环+select(poll\epoll)
    loop()
    print(time.time() - start_time)

# def get_url(url):
#     #通过socket请求html
#     url = urlparse(url)
#     host = url.netloc
#     path = url.path
#     if path == "":
#         path = "/"
#
#     #建立socket连接
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client.setblocking(False)
#     try:
#         client.connect((host, 80)) #阻塞不会消耗cpu
#     except BlockingIOError as e:
#         pass
#
#     #不停的询问连接是否建立好， 需要while循环不停的去检查状态
#     #做计算任务或者再次发起其他的连接请求
#
#     while True:
#         try:
#             client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
#             break
#         except OSError as e:
#             pass
#
#
#     data = b""
#     while True:
#         try:
#             d = client.recv(1024)
#         except BlockingIOError as e:
#             continue
#         if d:
#             data += d
#         else:
#             break
#
#     data = data.decode("utf8")
#     html_data = data.split("\r\n\r\n")[1]
#     print(html_data)
#     client.close()
