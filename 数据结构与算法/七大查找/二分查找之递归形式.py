#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 15:20
# @Author  : liuhu
# @File    : 二分查找之递归形式.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def binary_search(nums, key, start=0, end=None):
    """递归实现二分查找"""
    # 初始化时end的值
    end = len(nums) - 1 if end is None else end
    # 递归出口
    if end < start:
        return False
    # 防止溢出
    mid = (end - start) // 2 + start
    if key > nums[mid]:
        return binary_search(nums, key, start=mid + 1, end=end)
    elif key < nums[mid]:
        return binary_search(nums, key, start=start, end=mid - 1)
    elif key == nums[mid]:
        return mid


if __name__ == '__main__':
    LIST = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    result = binary_search(LIST, 99)
    # print(result)
    print binary_search([2], 1)
    # print binary_search(LIST, 100)
