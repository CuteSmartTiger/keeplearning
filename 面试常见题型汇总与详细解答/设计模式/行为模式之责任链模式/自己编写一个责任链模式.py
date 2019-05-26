#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 16:22
# @Author  : liuhu
# @File    : 自己编写一个责任链模式.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# job_list = ['lopen', 'read', 'close']
job_list = [ 'read']
# job_list = ['lopen']


class Base(object):
    def __init__(self, next_node=None):
        self.next = next_node
        print(self.next)

    def deal(self, key):
        if hasattr(self, key):
            method = getattr(self, key)
            method(key)
        else:
            print('{0}'.format(key))
            if hasattr(self.next, 'deal'):
                print('{0}点有deal 方法'.format(self.next))
                self.next.deal(key)
            else:
                print('{0} has no {1}'.format(self.next, key))

    # def __call__(self, *args, **kwargs):
    #     return self


class FileOpen(Base):

    def open(self, key):
        print('{0} has done'.format(key))


class FileRead(Base):

    def read(self, key):
        print('{0} has done'.format(key))


class FileClose(Base):

    def close(self, key):
        print('{0} has done'.format(key))


clo = FileClose()
re = FileRead(clo)
op = FileOpen(re)
for job in job_list:
    op.deal(job)
