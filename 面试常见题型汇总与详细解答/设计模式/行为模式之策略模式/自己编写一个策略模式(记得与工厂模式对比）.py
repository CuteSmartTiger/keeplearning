#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 11:34
# @Author  : liuhu
# @File    : 自己编写一个策略模式(记得与工厂模式对比）.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
# 设计思路：由用户从已有的方案中选择解决问题的策略

import sys


# 由用户选择排序的策略，关注的是方法，而工厂模式，关注的是对象
# 策略需要对客户显示开发，由用户选择，将算法类与客户解耦


# 具体策略类,比如下方各种排序算法

# 冒泡排序
def bubble_sort(nums):
    print(sys._getframe().f_code.co_name)
    print(nums)
    pass


# shell排序
def shell_sort(nums):
    print(sys._getframe().f_code.co_name)
    print(nums)
    pass


# 直接插入排序
def insert_sort(nums):
    print(sys._getframe().f_code.co_name)
    print(nums)
    pass


# 简单选择排序

# 基数排序

# 快速排序

# 二路并归排序


# 抽象策略类，接口返回客户选择的策略
def all_strategy(s, strategy):
    return strategy(s)


def user(unsorted_nums, number):
    strategys = {'1': bubble_sort, '2': shell_sort, '3': insert_sort}
    num = str(number)
    if num in strategys.keys():
        strategy = strategys[num]
        all_strategy(unsorted_nums, strategy)
    else:
        raise ValueError('there is no such strategy')


print(user([2, 1], 2))
