#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 22:46
# @Author  : liuhu
# @Site    : 
# @File    : 全局变量作用域.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


a = 3


def test_a():
    a = 10

    def test1():
        a = 20
        print(a)

    print(a)
    test1()
    print(a)


test_a()
print(a)
