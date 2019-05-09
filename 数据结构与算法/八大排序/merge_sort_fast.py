#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 10:22
# @Author  : liuhu
# @File    : merge_sort_fast.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def merge_sort_fast(nums):
    start = []
    end = []
    while len(nums) > 1:
        a = min(nums)
        b = max(nums)
        start.append(a)
        end.append(b)
        nums.remove(a)
        nums.remove(b)
    if nums:
        start.append(nums[0])
    end.reverse()
    return start + end
