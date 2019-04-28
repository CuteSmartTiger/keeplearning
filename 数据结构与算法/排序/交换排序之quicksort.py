#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 16:17
# @Author  : liuhu
# @File    : 交换排序之quicksort.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def quick_sort_3partition(sorting, left, right):
    """
    :param sorting: list
    :param left: int
    :param right: int
    :return:
    """
    if right <= left:
        return
    a = i = left
    b = right
    pivot = sorting[left]
    while i <= b:
        if sorting[i] < pivot:
            sorting[a], sorting[i] = sorting[i], sorting[a]
            a += 1
            i += 1
        elif sorting[i] > pivot:
            sorting[b], sorting[i] = sorting[i], sorting[b]
            b -= 1
        else:
            i += 1
    quick_sort_3partition(sorting, left, a - 1)
    quick_sort_3partition(sorting, b + 1, right)


unsort_list = [3, 1, 5, 7, 2, 4, 9, 6, 10, 8]
quick_sort_3partition(unsort_list, 0, len(unsort_list) - 1)
print(unsort_list)
