#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 17:27
# @Author  : liuhu
# @File    : dict方法测试.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
class Son(object):
    def son(self):
        print 'son'


class Parent(Son):
    name = 'liuhu'
    age = '18'
    sex = 'man'
    eat = 'cow'
    def __init__(self,*args):
        self.args = [i for i in args]

    def son(self, *args):
        print tuple([i for i in args])

    def keys(self):
        return tuple(self.args)

    def __getitem__(self, item):
        return getattr(self, item)


c = Parent('name','age')
print dict(c)

b = Parent('name')
print dict(b)

# class D:
#     name = 'zhangsan'
#     age = 18
#
#     def __init__(self):
#         self.sex = '男'
#
#     def keys(self):
#         return ('name', 'sex')
#
#     def __getitem__(self, item):
#         return getattr(self, item)
#
#
# d = D()
# print(d.__dict__)  # {'sex': '男'}
# print(dict(d))
