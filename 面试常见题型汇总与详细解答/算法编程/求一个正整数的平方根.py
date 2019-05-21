#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 13:09
# @Author  : liuhu
# @File    : 求一个正整数的平方根.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

def sqt(n):
    return n ** 0.5


print sqt(4)
print sqt(10)
print sqt(6)


def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    assert x >= 1
    low = 0
    mid = x // 2
    high = x
    while low <= high:  # 注意判断条件
        if mid * mid > x:
            high = mid - 1
        elif mid * mid < x:
            low = mid + 1
        else:
            return mid
        mid = (low + high) // 2
    return mid  # 向


print mySqrt(10)


# 针对小数位数进行求解  最多9位有效数字

def float_sqt(n, target):
    RADIX = 0.1
    place = 1
    count = 0
    base = n
    while True:
        place *= RADIX
        count += 1
        if count == 11:
            break
        while True:
            if base * base == target:
                return base
            elif base * base < target:
                base += place
            else:
                base -= place * 10
                break
        print place
    return base


print float_sqt(3, 10)

import math

print math.sqrt(10)

def self_sqr(target):
     n= mySqrt(target)
     return float_sqt(n,target)


print self_sqr(10)