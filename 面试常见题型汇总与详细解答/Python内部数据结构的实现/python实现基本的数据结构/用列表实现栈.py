#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 10:10
# @Author  : liuhu
# @File    : 用列表实现栈.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Stack:
    """ Stack ADT, using a python list
    pop(): assert not empty
    peek(): assert not empty, return top of non-empty stack without removing it
    push(value)
    """

    def __init__(self):
        self.items = list()

    def __len__(self):
        return len(self.items)

    def is_empty(self):
        return len(self) == 0

    def pop(self):
        assert not self.is_empty(), "stack is empty"
        return self.items.pop()

    def push(self, value):
        self.items.append(value)

    def peek(self):
        assert not self.is_empty(), "stack is empty"
        return self.items[-1]


s = Stack()
# s.pop()
print(s.push(2))
print(s.peek())
print(s.pop())
print(s.is_empty())
