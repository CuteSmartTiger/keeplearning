import socket
import threading

# 网络类型  协议
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定
server.bind(('0.0.0.0', 8000))
# 一直监听
server.listen()


# 有新生成的数据，则生成信息的sock
def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024)
        print(data.decode("utf8"))
        re_data = input()
        sock.send(re_data.encode("utf8"))


# 一直监听
while True:
    sock, addr = server.accept()
    # 用线程处理接受新接受的连接用户
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()
