#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 16:14
# @Author  : liuhu
# @File    : 哈希查找.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


# class HashTable:
#     def __init__(self, size):
#         assert size > 0, 'array size must be > 0'
#         self.elem = [None for _ in range(size)]  # 使用list数据结构作为哈希表元素保存方法
#         self.count = size  # 最大表长
#         self.time = 0  # 记录成功插入数据的个数
#
#     def hash(self, key):
#         if key < 0:
#             print '{0} is {1}'.format(key,key % self.count)
#         return key % self.count  # 散列函数采用除留余数法
#
#     def insert_hash(self, key):
#         """插入关键字到哈希表内"""
#         if self.time == self.count:  # 当空间已满，无法继续插入时报错
#             raise ValueError('no space')
#         address = self.hash(key)  # 求散列地址
#         while self.elem[address]:  # 当前位置已经有数据了，发生冲突。
#             address = (address + 1) % self.count  # 线性探测下一地址是否可用
#         self.elem[address] = key  # 没有冲突则直接保存。
#         self.time += 1
#
#     def search_hash(self, key):
#         """查找关键字，返回布尔值"""
#         star = address = self.hash(key)
#         while self.elem[address] != key:
#             address = (address + 1) % self.count
#             if not self.elem[address] or address == star:  # 说明没找到或者循环到了开始的位置
#                 return False
#         return True

class HashTable:
    def __init__(self, size):
        assert size > 0, 'array size must be > 0'
        self.elem = [None for _ in range(size)]  # 使用list数据结构作为哈希表元素保存方法
        self.count = size  # 最大表长
        self.time = 0  # 记录成功插入数据的个数

    def hash(self, key):
        return key % self.count  # 散列函数采用除留余数法

    def insert_hash(self, key):
        """插入关键字到哈希表内"""
        if self.time == self.count:  # 当空间已满，无法继续插入时报错
            raise ValueError('no space')
        address = self.hash(key)  # 求散列地址
        while self.elem[address]:  # 当前位置已经有数据了，发生冲突。
            address = (address + 1) % self.count  # 线性探测下一地址是否可用
        self.elem[address] = key  # 没有冲突则直接保存。
        self.time += 1

    def search_hash(self, key):
        """查找关键字，返回布尔值"""
        star = address = self.hash(key)
        while self.elem[address] != key:
            address = (address + 1) % self.count
            if not self.elem[address] or address == star:  # 说明没找到或者循环到了开始的位置
                return False
        return True


if __name__ == '__main__':
    list_a = [12, 67, 56, 16, 25, -37, 22, 29, -15, -47, 48, 34]
    hash_table = HashTable(12)
    # hash_table = HashTable(10)
    # hash_table = HashTable(-4)
    for i in list_a:
        hash_table.insert_hash(i)

    print hash_table.elem
    print len(hash_table.elem)
    # for i in hash_table.elem:
    #     if i:
    #         print((i, hash_table.elem.index(i)))
    # print("\n")

    print(hash_table.search_hash(-15))
    print(hash_table.search_hash(-37))