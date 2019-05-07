#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 22:25
# @Author  : liuhu
# @Site    : 
# @File    : 插入排序之shell_sort.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def insert_shell_sort(nums):
    # 初始化gap值，此处利用序列长度的一半为其赋值
    gap = len(nums) // 2
    # 第一层循环：依次改变gap值对列表进行分组,当gap等于1时进行最后一遍循环
    while gap >= 1:
        # 下面：利用直接插入排序的思想对分组数据进行排序
        # range(gap, len(L)):由于数组下标从0开始，所以从gap开始依次比较
        for i in range(gap, len(nums)):
            # range(i, 0, -gap):从i开始与选定元素开始倒序比较
            # 每个比较元素之间间隔gap
            for j in range(i, 0, -gap):
                # 如果该组当中两个元素满足交换条件，则进行交换
                if nums[j] < nums[j-gap]:
                    # temp = nums[j-gap]
                    # nums[j-gap] = nums[j]
                    # nums[j] = temp
                    nums[j],nums[j-gap] = nums[j-gap],nums[j]
                else:
                    break
        gap = gap // 2
    return nums


def shell_sort(nums):
    # 初始化gap值，此处利用序列长度的一半为其赋值
    gap = len(nums) // 2
    # 第一层循环：依次改变gap值对列表进行分组,当gap等于1时进行最后一遍循环
    while gap >= 1:
        # 下面：利用直接插入排序的思想对分组数据进行排序
        # range(gap, len(L)):由于数组下标从0开始，所以从gap开始依次比较
        # gap分组比较，同等的数值可能分部不同组而导致后一组比较后交换，而前一组比较后不交换
        # 故而破坏稳定性，成为不稳定性排序
        for i in range(gap, len(nums)):
            # range(i, 0, -gap):从i开始与选定元素开始倒序比较
            # 每个比较元素之间间隔gap
            for j in range(i, 0, -gap):
                # 如果该组当中两个元素满足交换条件，则进行交换
                if nums[j] < nums[j-gap]:
                    nums[j],nums[j-gap] = nums[j-gap],nums[j]
                else:
                    break
        gap = gap // 2
    return nums



print shell_sort([0, 5, -4,-4,3, 2, 2])
