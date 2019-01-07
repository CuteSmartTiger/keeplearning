import gevent

class MyGreenlet(gevent.Greenlet):
    def __init__(self, message, n, timeout):
        gevent.Greenlet.__init__(self)
        self.message = message
        self.n = n
        self.timeout = gevent.Timeout(timeout)

    def _run(self):
        self.timeout.start()
        print self.message
        gevent.sleep(self.n)

gr1 = MyGreenlet('hello greenlet', 2, 1)
gr1.start()
gr1.join()
