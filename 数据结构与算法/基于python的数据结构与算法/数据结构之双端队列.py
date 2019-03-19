#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 17:21
# @Author  : liuhu
# @File    : 数据结构之双端队列.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用内建类型list
class Deque:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.insert(0, item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)


# 使用标准库collections.deque
from collections import deque


class Deque:
    def __init__(self):
        self.items = deque()

    def addFront(self, item):
        self.items.appendleft(item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.popleft()

    def removeRear(self):
        return self.items.pop()

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)


# 判断是否回文
def palchecker(aString):
    chardeque = Deque()
    for ch in aString:
        chardeque.addRear(ch)
    while chardeque.size() > 1:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            return False
    return True


if __name__ == '__main__':
    str1 = 'able was i ere i saw elba'
    print('"%s" is%s palindrome' % (str1, '' if palchecker(str1) else ' not'))
    str2 = u'人人为我、我为人人'
    print(u'"%s"%s是回文' % (str2, u'' if palchecker(str2) else u'不'))
    str3 = u"What's wrong 怎么啦"
    print(u'"%s"%s是回文' % (str3, u'' if palchecker(str3) else u'不'))
