#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 14:59
# @Author  : liuhu
# @File    : 顺序查找.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def sequential_search(lis, key):
    """顺序查找"""
    length = len(lis)
    for i in range(length):
        if lis[i] == key:
            return i
        else:
            continue
    return False


if __name__ == '__main__':
    LIST = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    result = sequential_search(LIST, 123)
    print result
    print sequential_search([1], 123)