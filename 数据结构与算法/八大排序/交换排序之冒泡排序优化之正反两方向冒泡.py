#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 12:13
# @Author  : liuhu
# @File    : 交换排序之冒泡排序.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def bubble_sort(collection):
    """冒泡排序优化之正反两方向冒泡"""
    # 标记反向
    low =0
    # 标记正向比较结束位置
    high = len(collection)-1
    while low < high:
        # 正向找最大
        for j in range(low,high):
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        high -= 1

        # 反向找最小
        for j in range(high,low,-1):
            if collection[j] > collection[j - 1]:
                collection[j], collection[j - 1] = collection[j - 1], collection[j]
        low += 1
    return collection


print bubble_sort([3, 1, 5, 7, 2, 4, 9, -6, 10, 8])
print bubble_sort([])