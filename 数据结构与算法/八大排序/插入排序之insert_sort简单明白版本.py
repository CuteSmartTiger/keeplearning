#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 11:03
# @Author  : liuhu
# @File    : 插入排序之insert_sort简单明白版本.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


# def insert_sort(collections):
#     '''插入排序'''
#     length = len(collections)
#     for i in range(1, length):
#         sort_value = collections[i]
#         # 在已排序序列中查找待插入的位置i
#         # TODO 使用二分查找待插入位置
#         while i > 0:
#             # 大于才会进行交换，相等则未发生交换，所以为稳定性排序
#             if collections[i - 1] > sort_value:
#                 collections[i] = collections[i - 1]
#                 i -= 1
#             else:
#                 break
#         collections[i] = sort_value
#
#     return collections


# 直接插入排序
# def insert_sort(nums):
#     '''直接插入排序'''
#     # 遍历数组中的所有元素，其中0号索引元素默认已排序，因此从1开始
#     # 当nums元素数量为空或者1时，不会进入for循环
#     for i in range(1, len(nums)):
#     # 将该元素与已排序好的前序数组依次比较，如果该元素小，则交换
#     # range(x,0,-1):从x倒序循环到0，依次比较，
#     # 每次比较如果小于会交换位置，正好按递减的顺序
#         for j in range(i, 0, -1):
#
#             # 判断：如果符合条件则交换
#             if nums[j] < nums[j-1]:
#                 nums[j] ,nums[j-1] = nums[j-1],nums[j]
#                 # temp = nums[j]
#                 # nums[j] = nums[j-1]
#                 # nums[j-1] = temp
#             else:
#                 break
#     return nums

# 直接插入排序
def insert_sort(nums):
    '''直接插入排序'''
    # 遍历数组中的所有元素，其中0号索引元素默认已排序，因此从1开始
    # 当nums元素数量为空或者1时，不会进入for循环
    for i in range(1, len(nums)):
        # 将该元素与已排序好的前序数组依次比较，如果该元素小，则交换
        # range(x,0,-1):从x倒序循环到0，依次比较，
        # 每次比较如果小于会交换位置，正好按递减的顺序
        for j in range(i, 0, -1):
            # 判断：如果符合条件则交换,并由此处可见直接插入排序为稳定性排序
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            else:
                break
    return nums


# print insert_sort([5, 3, 2, 2, 0])
# print insert_sort([0, 5, 3, 2, 2])
# print insert_sort([1, 0])
# print insert_sort([-2, -5, -45])
print insert_sort([1])
