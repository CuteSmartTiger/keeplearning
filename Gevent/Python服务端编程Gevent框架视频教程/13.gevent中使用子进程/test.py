import gevent
from multiprocessing import Process, Pipe
from gevent.socket import wait_read, wait_write

a,b= Pipe()
c,d= Pipe()

def relay():
    for i in range(10):
        msg = b.recv()
        c.send(msg+' in '+str(i))

def put_msg():
    for i in range(10):
        wait_write(a.fileno())
        a.send('hi')
def get_msg():
    for i in range(10):
        wait_read(d.fileno())
        print d.recv()

proc = Process(target=relay)
proc.start()

g1 = gevent.spawn(put_msg)
g2 = gevent.spawn(get_msg)
gevent.joinall([g1, g2], timeout=1)

