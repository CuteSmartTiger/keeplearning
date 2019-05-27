#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/26 11:40
# @Author  : liuhu
# @Site    : 
# @File    : super查找属性.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Base(object):
    def __init__(self):
        self.read = 'read'


class Test(Base):
    def __init__(self):
        super().__init__()
        self.write = 'write'
        self.open = 'open'


t = Test()

print(t.read)
# print(t.write)

# print(t.open)
