#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 22:24
# @Author  : liuhu
# @Site    : 
# @File    : 插入排序之折半插入排序.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


def binary_insert_sort(nums):
    """折半插入排序
    :param nums:
    :return:
    """
    # 遍历数组中的所有元素，其中0号索引元素默认已排序，因此从1开始
    # 当nums元素数量为空或者1时，不会进入for循环
    for i in range(1, len(nums)):
        #  二分查找在已排序中寻找待插入位置确定待插入点
        left = 0
        right = i - 1
        target = nums[i]
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        print(left,right)
        for j in range(i, right+1, -1):
            # 交换,并由此处可见折半插入排序为稳定性排序
            nums[j]= nums[j - 1]
            # nums[j], nums[j - 1] = nums[j - 1], nums[j]

        nums[right+1] = target
        print(nums)

    return nums


if __name__ == '__main__':
    binary_insert_sort([5, 3, 2, 2, 0])
    # print(binary_insert_sort([1]))
