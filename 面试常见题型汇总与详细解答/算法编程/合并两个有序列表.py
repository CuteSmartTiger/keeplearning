#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 13:54
# @Author  : liuhu
# @File    : 合并两个有序列表.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
a = [1, 2, 3, 7]
b = [3, 4, 5]


# 学习这个算法时，把二路归并排序算法梳理一遍
def merge_list(list1, list2):
    if not list2:
        return list1
    if not list1:
        return list2
    result = []
    k = i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
        k += 1

    while i < len(list1):
        result.append(list1[i])
        i += 1
        k += 1

    while j < len(list2):
        result.append(list2[j])
        j += 1
        k += 1
    return result


print(merge_list(a, b))
