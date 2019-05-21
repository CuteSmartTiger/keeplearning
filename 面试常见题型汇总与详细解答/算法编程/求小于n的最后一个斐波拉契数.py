#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 14:03
# @Author  : liuhu
# @File    : 求小于n的最后一个斐波拉契数.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def last_fb(n):
    assert n > 1, "n must bigger than 1"
    a, b = 1, 0
    while a < n:
        a, b = a + b, a
    return b


print last_fb(14)
