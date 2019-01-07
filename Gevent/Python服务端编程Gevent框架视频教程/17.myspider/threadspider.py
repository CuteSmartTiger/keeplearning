import requests
from threading import Timer, Lock, Thread
from utils import  HtmlAnalyzer
from Queue import Queue
import time

class Strategy(object):
    def __init__(self, max_depth, max_count, concurrency=5):
        self.max_depth = max_depth
        self.max_count = max_count
        self.concurrency = concurrency
        self.timeout = 60
        self.time = 12*60

class UrlObject(object):
    def __init__(self, url, depth):
        self.url = url.strip('/')
        self.depth = depth

class ThreadSpider(object):
    def __init__(self, max_depth, max_count, root_url):
        self.strategy = Strategy(max_depth, max_count)
        self.queue = Queue()
        self.url_set = set()
        self.handler_num = 0
        self.lock = Lock()
        self.thread_lock = Lock()
        self.thread_pool = {}
        self.thread_id = 0
        self.is_stop = False
        self.thread_num = 0
        self.currency_limit = False
        self.last_data = None
        obj = UrlObject(root_url, 0)
        self.put(obj)

    def put(self, obj):
        hash_val = hash(obj.url)
        self.lock.acquire()
        res = hash_val in self.url_set
        self.lock.release()
        if res:
            return
        self.url_set.add(hash_val)
        self.queue.put(obj)

    def _run_loop(self):
        while True:
            if self.is_stop:
                time.sleep(1)
                continue
            if self.currency_limit:
                time.sleep(1)
                self.thread_lock.acquire()
                self.thread_num = len(self.thread_pool)
                if self.thread_num == self.strategy.concurrency:
                    self.thread_lock.release()
                    continue
                else:
                    self.currency_limit = False
                self.thread_lock.release()
            else:
                try:
                    url = self.queue.get()
                except:
                    continue
            self.thread_id = self.thread_id+1
            thd = Handler(url, self, self.thread_id)

            self.thread_lock.acquire()
            self.thread_pool[self.thread_id] = thd
            if len(self.thread_pool) == self.strategy.concurrency:
                self.currency_limit = True
            self.thread_lock.release()

            self.thread_num = self.thread_num+1
            print "add thread ", self.thread_id

            thd.start()
            self.handler_num = self.handler_num+1
            if self.strategy.max_count <= self.handler_num:
                print "handler num %d is full so stop " % self.handler_num
                self.is_stop = True

    def remove_thread(self, thd_id):
        self.thread_lock.acquire()
        if thd_id in self.thread_pool:
            del self.thread_pool[thd_id]
            print "del threadid ", thd_id
        self.thread_lock.release()

    def run(self):
        self._run_loop()

class Handler(Thread):
    def __init__(self, urlobj, spider, thd_id):
        Thread.__init__(self)
        print "begin thread %d with url %s" %(thd_id, urlobj.url)
        self.urlobj= urlobj
        self.spider = spider
        self.thread_id = thd_id
        self.charset = "utf-8"

    def run(self):
        try :
            html = self.open(self.urlobj.url)
        except Exception,why:
            return
        depth = self.urlobj.depth + 1
        if depth > self.spider.strategy.max_depth:
            return
        for link in self.feed(html):
            if hash(link) in self.spider.url_set:
                continue
            url = UrlObject(link, depth)
            self.spider.put(url)
        self.spider.remove_thread(self.thread_id)

    def open(self, url):
        strategy = self.spider.strategy
        try:
            resp = requests.get(url, timeout=strategy.timeout)
        except:
            return

        if resp.status_code != requests.codes.ok:
            return
        charset = HtmlAnalyzer.detectCharSet(resp.text)
        if charset is not None:
            self.charset = charset
            resp.encoding = charset
        return resp.text
    def feed(self, html):
        return HtmlAnalyzer.extractLinks(html, self.urlobj.url, self.charset)


class MySpider(object):
    def __init__(self, max_depth, max_count, root_url):
        self.spider = ThreadSpider(max_depth=max_depth,
                                   max_count=max_count,
                                   root_url=root_url)
    def run(self):
        self.spider.run()

test = MySpider(max_depth=5, max_count=100, root_url="http://www.maiziedu.com")
test.run()