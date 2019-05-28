#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 11:06
# @Author  : liuhu
# @File    : 面试题2-加锁的单例模式-适合多线程.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

import time
import threading
from functools import wraps

lock = threading.Lock()

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        return r

    return wrapper

# 此方案适合多线程，但是效率不高
class Singleton(object):

    instance = None

    def __new__(cls, *args, **kwargs):
        lock.acquire()
        if not cls.instance:
            time.sleep(2)
            cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        lock.release()
        return cls.instance

@timethis
def test1():
    t1 = Singleton()
    t2 = Singleton()
    print(id(t1))
    print('====')
    print(id(t2))
    print(id(t1) == id(t2))

@timethis
def test2():
    s1 = Singleton()
    s2 = Singleton()
    print(id(s1))
    print(id(s2))
    print(id(s1) == id(s2))


f1 = threading.Thread(target=test1, args=())
f2 = threading.Thread(target=test2, args=())
f1.start()
f2.start()
