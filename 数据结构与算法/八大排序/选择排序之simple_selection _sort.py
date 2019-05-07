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


# # 简单选择排序
# def select_sort(L):
#     # 依次遍历序列中的每一个元素，n个记录的直接选择排序可经过n-1趟直接选择排序得到有序结果
#     for x in range(0, len(L)-1):
#         # 将当前位置的元素定义此轮循环当中的最小值
#         minimum = L[x]
#         # 将该元素与剩下的元素依次比较寻找最小元素
#         for i in range(x + 1, len(L)):
#             if L[i] < minimum:
#                 temp = L[i]
#                 L[i] = minimum
#                 minimum = temp
#         # 将比较后得到的真正的最小值赋值给当前位置
#         L[x] = minimum

# 简单选择排序
def select_sort(L):
    '''简单选择排序'''
    # 依次遍历序列中的每一个元素，n个记录的直接选择排序可经过n-1趟直接选择排序得到有序结果
    for x in range(0, len(L) - 1):
        # 将当前位置的元素定义此轮循环当中的最小值
        minimum = L[x]
        # 将该元素与剩下的元素依次比较寻找最小元素
        for i in range(x + 1, len(L)):
            # 当小时才交换，则是稳定排序
            if L[i] < minimum:
                L[i], minimum = minimum, L[i]
        # 将比较后得到的真正的最小值赋值给当前位置
        L[x] = minimum
    return L


print select_sort([0, 5, 3,-3, 2, 2])
