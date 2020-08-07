#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 21:23
# @Author  : liuhu
# @Site    : 
# @File    : 快速排序.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

import random


def partition(nums, left, right):
    random_index = random.randint(left, right)
    pivot = nums[random_index]
    nums[random_index], nums[right] = nums[right], nums[random_index]
    j = left
    for i in range(left, right):
        if nums[i] <= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    nums[j], nums[right] = nums[right], nums[j]
    return j


def quick_sort(nums, l=None, r=None):
    if l is None and r is None:
        l = 0
        r = len(nums) - 1
    elif l is not None and r is not None:
        pass
    else:
        raise ValueError('l or r not valid')
    if l < r:
        partition_index = partition(nums, l, r)
        quick_sort(nums, l, partition_index - 1)
        quick_sort(nums, partition_index + 1, r)


if __name__ == '__main__':
    li = [4, 3, 3, 1, 4, 6, 9]
    quick_sort(li)
    print(li)

    li = [3, 2]
    quick_sort(li)
    print(li)
