#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 23:50
# @Author  : liuhu
# @Site    : 
# @File    : 归并排序.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def merge_array(L, first, mid, last, temp):
    """
    合并的函数，合并数组
    # 将序列L[first...mid]与序列L[mid+1...last]进行合并
    """
    # 对i,j,k分别进行赋值
    i, j, k = first, mid + 1, 0
    # 当左右两边都有数时进行比较，取较小的数
    while i <= mid and j <= last:
        if L[i] <= L[j]:
            temp[k] = L[i]
            i += 1
        else:
            temp[k] = L[j]
            j += 1
        k += 1

    # 以下两个while只会执行两个
    # 如果左边序列还有数
    while i <= mid:
        temp[k] = L[i]
        i += 1
        k += 1

    # 如果右边序列还有数
    while j <= last:
        temp[k] = L[j]
        j += 1
        k += 1

    # 将temp当中该段有序元素赋值给L待排序列使之部分有序
    for x in range(0, k):
        L[first + x] = temp[x]


def divide_array(L, first, last, temp):
    """分组"""
    if first < last:
        mid = (int)((first + last) / 2)
        # 使左边序列有序
        divide_array(L, first, mid, temp)
        # 使右边序列有序
        divide_array(L, mid + 1, last, temp)
        # 将两个有序序列合并
        merge_array(L, first, mid, last, temp)


# 归并排序的函数
def merge_sort(L):
    # 声明一个长度为len(L)的空列表
    temp = len(L) * [None]
    # 调用归并排序
    divide_array(L, 0, len(L) - 1, temp)
    return L


print merge_sort([0, 5, 3, 2, 2])
print merge_sort([])
print merge_sort([-2, -5, -45])