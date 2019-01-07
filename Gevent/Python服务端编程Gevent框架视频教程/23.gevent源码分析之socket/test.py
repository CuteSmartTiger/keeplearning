import gevent
from gevent import socket

sock = socket.create_connection(('localhost', 50000))
print sock
sock.send('hello')
