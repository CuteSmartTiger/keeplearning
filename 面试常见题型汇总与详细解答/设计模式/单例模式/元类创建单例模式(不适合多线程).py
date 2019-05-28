#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 11:34
# @Author  : liuhu
# @File    : 元类创建单例模式(不适合多线程).py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
import threading


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(object):
    __metaclass__ = Singleton




def test1():
    t1 = MyClass()
    t2 = MyClass()
    print('t1 id :{}'.format(id(t1)))
    print('t2 id :{}'.format(id(t2)))
    print(id(t1))
    print(id(t2))
    print(id(t1) == id(t2))


def test2():
    s1 = MyClass()
    s2 = MyClass()
    print('s1 id :{}'.format(id(s1)))
    print('s2 id :{}'.format(id(s2)))
    print(id(s1) == id(s2))


f1 = threading.Thread(target=test1, args=())
f2 = threading.Thread(target=test2, args=())
f1.start()
f2.start()