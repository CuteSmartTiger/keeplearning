import socket

# 网络类型  协议
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定
server.bind(('0.0.0.0', 8000))
# 一直监听
server.listen()
# 有新生成的数据，则生成信息的sock
sock, addr = server.accept()

# 获取从客户端获取的数据
# 一次获取1K的数据
# 一直监听
while True:
    data = sock.recv(1024)
    print(data.decode("utf8"))
    re_data = input()
    sock.send(re_data.encode("utf8"))
    # server.close()
    # sock.close()
