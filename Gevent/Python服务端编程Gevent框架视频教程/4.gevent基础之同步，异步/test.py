import redis
import Queue
import time
from threading import Thread

def handle_callback(res):
    print 'get redis res: ', res

class SetData:
    def __init__(self, key, value, handle):
        self.key = key
        self.value = value
        self.handle = handle

class RedisAsyncHandle(Thread):
    queue = Queue.Queue(maxsize=1024)
    r = redis.Redis(host='localhost', port=6379, db=0)

    def send_set_cmd(self, key, value):
        set_data = SetData(key, value, handle_callback)
        self.queue.put(set_data)

    def run(self):
        while True:
            while not self.queue.empty():
                item = self.queue.get()
                print 'get item'
                res = self.r.set(item.key, item.value)
                item.handle(res)
            time.sleep(0.1)


handle = RedisAsyncHandle()
handle.start()
handle.send_set_cmd('name1', 'allen1')
handle.join()




