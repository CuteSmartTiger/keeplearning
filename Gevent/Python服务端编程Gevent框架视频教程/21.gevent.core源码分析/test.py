from gevent import core
import gevent.hub

loop = gevent.hub.get_hub().loop

print loop

def hello_world():
    print 'hi!'

def lazy_hello_world():
    print 'lazy!'

loop.run_callback(hello_world)
timer = loop.timer(3)
timer.start(lazy_hello_world)
print loop

loop.run()