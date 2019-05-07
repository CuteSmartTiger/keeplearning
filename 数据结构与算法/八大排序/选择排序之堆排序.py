#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 23:48
# @Author  : liuhu
# @Site    : 
# @File    : 选择排序之堆排序.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def heapify(unsorted, index, heap_size):
    '''调整大根堆'''
    # 定义保存当前系列最大值的下标largest
    largest = index
    # 获取当前节点下标(index)的左右子节点下标
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    # 在不超过堆容量时，进行左节点与父节点的比较，若比父节点大则更新最大值的下标
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index

    # 在不超过堆容量时，进行右节点与父节点的比较，若比父节点大则更新最大值的下标
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index

    # 若当前节点并不是最大值，则进行交换调整
    if largest != index:
        # 将当前节点的值与最大值进行互换
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


def heap_sort(unsorted):
    '''堆排序'''
    n = len(unsorted)
    # 从n // 2 - 1节点处依次构建堆
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)

    # 执行循环：
    # 1. 每次取出堆顶元素置于序列的最后(len - 1, len - 2, len - 3...)
    # 2. 调整堆，使其继续满足大顶堆的性质，注意实时修改堆中序列的长度
    for i in range(n - 1, 0, -1):
        # i为序列下标从后往前移动，所以最大值为于列表的最后
        # 将抽象数据结构堆的最大值即索引0位置的数值移动i位置
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted


print heap_sort([-8,5,-20,5,4,76])