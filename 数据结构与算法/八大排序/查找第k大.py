#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 23:01
# @Author  : liuhu
# @Site    : 
# @File    : 查找第k大.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
import random


class FindKth(object):

    def find_Kth(self, nums, k):
        if not nums:
            return
        n = len(nums)
        if n < k:
            raise ValueError('k can not larger than {}'.format(n))
        k_max = len(nums) - k
        l = 0
        r = n - 1
        while True:
            ip_index = self.partition(nums, l, r)
            if ip_index == k_max:
                return nums[k_max]
            elif ip_index < k_max:
                l = ip_index + 1
            else:
                r = ip_index - 1

    @staticmethod
    def partition(nums, left, right):
        random_index = random.randint(left, right)
        pivot = nums[random_index]
        nums[random_index], nums[right] = nums[right], nums[random_index]
        j = left
        for i in range(left, right):
            if nums[i] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        nums[j], nums[right] = nums[right], nums[j]
        return j


if __name__ == '__main__':
    li = [4, 3, 3, 1, 4, 6, 9]
    s = FindKth()
    k = s.find_Kth(li, 3)
    print(k)
