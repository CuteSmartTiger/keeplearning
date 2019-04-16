#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 0:10
# @Author  : liuhu
# @Site    : 
# @File    : 闭包.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

def test1():
    a= 10
    def test2():
        a = 20
        print('test2:{0}'.format(a))
    test2()
    print('test1:{0}'.format(a))

test1()