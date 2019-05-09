#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 23:50
# @Author  : liuhu
# @Site    : 
# @File    : 基数排序.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def radix_sort(lst):
    """基数排序"""
    if not lst:
        return lst

    RADIX = 10
    placement = 1

    # 获取最大值，最为循环退出出口
    max_digit = max(lst)
    while placement < max_digit:
        # 0到9的柱状桶，使用列表表示，用于存放基数相同的数据
        buckets = [list() for _ in range(RADIX)]
        # 遍历列表，按基数分类放入桶中
        for i in lst:
            tmp = (i // placement) % RADIX
            buckets[tmp].append(i)

        # 从低到高，将桶中数据依次放入到列表中
        a = 0
        # 相同的数据，在原列表中靠前，分配到桶中时也靠前，取出时也先取出，所以是稳定性排序
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                lst[a] = i
                a += 1

        # 进入下一个循环
        placement *= RADIX
    return lst


print radix_sort([12, 13, 5, 234])
print radix_sort([])
print radix_sort([12, -13, 5, -234])
