import gevent
from gevent.queue import Queue, Empty, LifoQueue, PriorityQueue

class Job():
    def __init__(self, prority, des):
        self.protity = prority
        self.des = des

    def __cmp__(self, other):
        return cmp(self.protity, other.protity)

    def __str__(self):
        return "protity %d des %s" %(self.protity, self.des)


q = PriorityQueue()
q.put(Job(3, 'mid job'))
q.put(Job(10, 'low job'))
q.put(Job(1, 'important job'))

while not q.empty():
    job = q.get()
    print job