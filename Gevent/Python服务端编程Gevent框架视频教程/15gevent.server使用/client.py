from gevent import monkey
monkey.patch_all()
import gevent
import socket

def do_connect(addr, index):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(addr)
    gevent.sleep(0.5)
    sock.send("hello world")
    sock.close()

addr = ('localhost', 5000)

greenlets = []
num = 1
for i in xrange(num):
    g = gevent.spawn(do_connect, addr, i)
    greenlets.append(g)
gevent.joinall(greenlets)
