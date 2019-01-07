from gevent import Greenlet
import gevent
import time
def run_in_greenlet1():
    print 'run_in_greenlet1.0'
    gevent.sleep(0)
    print 'run_in_greenlet1.1'
    gevent.sleep(0)

def run_in_greenlet2():
    print 'run_in_greenlet2'
    gevent.sleep(0)
    print 'run_in_greenlet2.1'

gevent.joinall([gevent.spawn(run_in_greenlet1)
                , gevent.spawn(run_in_greenlet2)])