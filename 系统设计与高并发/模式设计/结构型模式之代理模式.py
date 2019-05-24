#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 17:43
# @Author  : liuhu
# @File    : 结构型模式之代理模式.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class LazyProperty(object):
    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__
        # print('function overriden: {}'.format(self.fget))
        # print("function's name: {}".format(self.func_name))

    def __get__(self, obj, cls):
        if not obj:
            print('there is no object')
            return None
        value = self.method(obj)
        print('value {}'.format(value))
        setattr(obj, self.method_name, value)
        return value


class Test:
    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None

    @LazyProperty
    def resource(self):
        print('initializing self._resource which is: {}'.format(self._resource))
        self._resource = tuple(range(5))
        print(self._resource)
        print('after _source')
        return self._resource


def main():
    t = Test()
    print(t.x)
    print(t.y)
    print(t.resource)
    print(t.resource)
    print(t.resource)
    print(t.resource)

main()