#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 18:26
# @Author  : liuhu
# @Site    : 
# @File    : hasattr.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

class Parent(object):
    def test(self):
        print('parent test')


class Son(Parent):
    def test_hasattr(self):
        if hasattr(self, 'test'):
            print('当前实例存在test方法')
        else:
            print('当前实例不存在test方法')


s = Son()
s.test_hasattr()
# s.test()
