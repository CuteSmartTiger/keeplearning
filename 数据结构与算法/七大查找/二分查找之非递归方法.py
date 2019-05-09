#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 15:10
# @Author  : liuhu
# @File    : 二分查找之非递归方法.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


# def binary_search(lis, key):
#     low = 0
#     high = len(lis) - 1
#     time = 0
#     while low < high:
#         time += 1
#         mid = int((low + high) / 2)
#         if key < lis[mid]:
#             high = mid - 1
#         elif key > lis[mid]:
#             low = mid + 1
#         else:
#             # 打印折半的次数
#             print("times: %s" % time)
#             return mid
#     print("times: %s" % time)
#     return False

def binary_search(lis, key):
    """非递归形式二分查找"""
    low = 0
    high = len(lis) - 1
    while low < high:
        # mid = int((low + high) / 2)
        mid = (high - low)//2 + low
        if key < lis[mid]:
            high = mid - 1
        elif key > lis[mid]:
            low = mid + 1
        else:
            return mid
    return False


if __name__ == '__main__':
    LIST = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    result = binary_search(LIST, 99)
    print(result)
