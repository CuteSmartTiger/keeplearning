#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 16:08
# @Author  : liuhu
# @File    : linear_search.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def linear_search(sequence, target):
    for index, item in enumerate(sequence):
        if item == target:
            return index
    return False


if __name__ == '__main__':
    LIST = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    result = linear_search(LIST, 123)
    print result
    print linear_search([1], 123)
    print linear_search([], 123)