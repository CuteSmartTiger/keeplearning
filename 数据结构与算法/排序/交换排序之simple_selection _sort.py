#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 19:42
# @Author  : liuhu
# @File    : 交换排序之simple_selection_sort.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

from __future__ import print_function


# 此方法应该为简单排序，而不是插入排序
def simple_selection_sort(collection):
    """Pure implementation of the simple selection  sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> simple_selection_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> simple_selection_sort([])
    []
    >>> simple_selection_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    for index in range(1, len(collection)):
        while index > 0 and collection[index - 1] > collection[index]:
            collection[index], collection[index - 1] = collection[index - 1], collection[index]
            index -= 1

    return collection


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(simple_selection_sort(unsorted))