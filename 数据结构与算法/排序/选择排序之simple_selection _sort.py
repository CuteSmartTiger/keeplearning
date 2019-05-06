#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 19:42
# @Author  : liuhu
# @File    : 选择排序之simple_selection_sort.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def simple_select_sort(unsorted_list):
    """
    :param unsorted_list: list
    :return:
    """
    length = len(unsorted_list)
    for i in range(length - 1):
        index_of_min_value = i
        for j in range(i + 1, length):
            if unsorted_list[j] < unsorted_list[index_of_min_value]:
                index_of_min_value = j
        unsorted_list[index_of_min_value], unsorted_list[i] = unsorted_list[i], unsorted_list[index_of_min_value]
    print(unsorted_list)
    return unsorted_list


simple_select_sort([0, 5, 3, 2, 2])
