# 1. epoll并不代表一定比select好
# 在并发高的情况下，连接活跃度不是很高， epoll比select
# 并发性不高，同时连接很活跃， select比epoll好

# 通过非阻塞io实现http请求

import socket
from urllib.parse import urlparse

# 本节内容为了说明;
# 使用非阻塞io完成http请求
# 虽然使用了非阻塞IO，但是内部的循环
# 依然占用很多时间，并没有提高并发

def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 非阻塞
    client.setblocking(False)
    try:
        client.connect((host, 80))  # 阻塞不会消耗cpu
    except BlockingIOError as e:
        pass

    # 不停的询问连接是否建立好， 需要while循环不停的去检查状态
    # 做计算任务或者再次发起其他的连接请求

    while True:
        try:
            # 尝试发送数据，一旦connect连接成功则才能发送成功
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
            # 若成功发送数据则跳出循环
            break
        except OSError as e:
            pass

    data = b""
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue
        if d:
            data += d
        else:
            # 持续获取数据直到获取不到为止
            break

    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()


if __name__ == "__main__":
    get_url("http://www.baidu.com")
