#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 12:12
# @Author  : liuhu
# @File    : 交换排序之冒泡排序优化之记录每趟最后一次交换的位置.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def bubble_sort(collection):
    """冒泡排序优化之记录每一趟最后交换的位置"""
    length = len(collection)
    i = length-1
    while i > 0:
        pos = 0
        for j in range(i):
            if collection[j] > collection[j + 1]:
                pos = j
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        i = pos
    return collection


print bubble_sort([3, 1, 5, 7, 2, 4,4, 9, -6, 10, 8])
print bubble_sort([])