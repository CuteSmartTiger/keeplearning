#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 16:07
# @Author  : liuhu
# @File    : 面试题2-自己编写一个单例模式一个类只能创建一个实例.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
import time
import threading


# 此方案适合单线程
class Singleton(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            time.sleep(2)
            cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.instance


def test1():
    t1 = Singleton()
    t2 = Singleton()
    print(id(t1))
    print(id(t2))
    print(id(t1) == id(t2))


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
