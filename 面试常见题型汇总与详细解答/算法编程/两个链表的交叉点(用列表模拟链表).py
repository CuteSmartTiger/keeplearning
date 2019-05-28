#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 15:30
# @Author  : liuhu
# @File    : 两个链表的交叉点(用列表模拟链表).py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

a = [1, 2, 3, 7, 9, 1, 5]
b = [4, 5, 7, 9, 1, 5]


def same_point(a, b):
    length = min(len(a), len(b)) - 1
    i=1
    while length >= 0:
        print(a[-i],b[-i])
        if a[-i] == b[-i]:
            length -= 1
            i +=1
        else:
            return a[-i + 1]
    print(length)
    return False


print(same_point(a,b))