#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 9:21
# @Author  : liuhu
# @File    : 数据结构之栈.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Stack():
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.top = -1

    def push(self, ele):  # 入栈之前检查栈是否已满
        if self.isfull():
            raise Exception("out of range")
        else:
            self.stack.append(ele)
            self.top = self.top + 1

    def pop(self):  # 出栈之前检查栈是否为空
        if self.isempty():
            raise Exception("stack is empty")
        else:
            self.top = self.top - 1
            return self.stack.pop()

    def isfull(self):
        return self.top + 1 == self.size

    def isempty(self):
        return self.top == -1


s=Stack(5)
for i in range(6):
    s.push(i)
s.pop()
print s.isempty()
