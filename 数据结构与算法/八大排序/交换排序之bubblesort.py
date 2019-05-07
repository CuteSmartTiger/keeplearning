#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 16:17
# @Author  : liuhu
# @File    : 交换排序之bubblesort.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def bubble_sort(collection):
    """冒泡排序"""
    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        # 当某趟遍历时未发生交换，则已排列完成，跳出循环
        if not swapped:
            break
    return collection
