#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 9:59
# @Author  : liuhu
# @File    : 数据结构之堆(优先队列).py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# coding=utf-8
from heapq import heappush, heappop


class PriorityQueue:
    def __init__(self):
        self._queue = []

    def put(self, item, priority):
        heappush(self._queue, (-priority, item))

    def get(self):
        if self.isempty():
            raise ValueError('no element')
        else:
            return heappop(self._queue)[-1]

    def isempty(self):
        return len(self._queue) == 0


q = PriorityQueue()
q.put('world', 1)
q.put('hello', 2)
print q.get()
print q.get()
print q.get()

# 优化
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]
