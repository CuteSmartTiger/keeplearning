#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 11:03
# @Author  : liuhu
# @File    : 插入排序之insert_sort简单明白版本.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def insert_sort(collections):
    '''插入排序'''
    length = len(collections)
    for i in range(1, length):
        sort_value = collections[i]
        # 在已排序序列中查找待插入的位置i
        # TODO 使用二分查找待插入位置
        while i > 0:
            # 大于才会进行交换，相等则未发生交换，所以为稳定性排序
            if collections[i - 1] > sort_value:
                collections[i] = collections[i - 1]
                i -= 1
            else:
                break
        collections[i] = sort_value

    return collections


print insert_sort([5, 3, 2, 2, 0])
print insert_sort([0, 5, 3, 2, 2])
print insert_sort([1, 0])
print insert_sort([-2, -5, -45])
