#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 10:55
# @Author  : liuhu
# @File    : 使用链的结构实现栈.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class StackNode(object):
    """node"""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack(object):
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def pop(self):
        assert not self.is_empty()
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def push(self, value):
        self.top = StackNode(data=value, next=self.top)
        self.size += 1

    def peek(self):
        assert not self.is_empty()
        return self.top.data


s = Stack()
# s.pop()
for i in range(200):
    s.push(i)
print(s.size)
print(s.peek())
print(s.pop())
print(s.is_empty())
