#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 11:21
# @Author  : liuhu
# @File    : 数据结构之单向链表测试.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# 每个Node分为两部分。一部分含有链表的元素，可以称为数据域；另一部分为一指针，指向下一个Node
class Node(object):

    __slots__ = ['_item', '_next']

    def __init__(self, item):
        self._item = item
        self._next = None

    def getItem(self):
        return self._item

    def getNext(self):
        return self._next

    def setItem(self, newitem):
        self._item = newitem

    def setNext(self, newnext):
        self._next = newnext


class SingleLinkedList():
    def __init__(self):
        self._head = None  # 初始化为空链表

    def isEmpty(self):
        return self._head == None

    def size(self):
        current = self._head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def travel(self):
        current = self._head
        while current != None:
            print current.getItem()
            current = current.getNext()

    def add(self, item):
        temp = Node(item)
        temp.setNext(self._head)
        self._head = temp

    def append(self, item):
        temp = Node(item)
        if self.isEmpty():
            self._head = temp  # 若为空表，将添加的元素设为第一个元素
        else:
            current = self._head
            while current.getNext() != None:
                current = current.getNext()  # 遍历链表
            current.setNext(temp)  # 此时current为链表最后的元素

    def search(self, item):
        current = self._head
        founditem = False
        while current != None and not founditem:
            if current.getItem() == item:
                founditem = True
            else:
                current = current.getNext()
        return founditem

    def index(self, item):
        current = self._head
        count = 0
        found = None
        while current != None and not found:
            count += 1
            if current.getItem() == item:
                found = True
            else:
                current = current.getNext()
        if found:
            return count
        else:
            raise ValueError, '%s is not in linkedlist' % item

    def remove(self, item):
        current = self._head
        pre = None
        while current != None:
            if current.getItem() == item:
                if not pre:
                    self._head = current.getNext()
                else:
                    pre.setNext(current.getNext())
                break
            else:
                pre = current
                current = current.getNext()

    def insert(self, pos, item):
        if pos <= 1:
            self.add(item)
        elif pos > self.size():
            self.append(item)
        else:
            temp = Node(item)
            count = 1
            pre = None
            current = self._head
            while count < pos:
                count += 1
                pre = current
                current = current.getNext()
            pre.setNext(temp)
            temp.setNext(current)


if __name__ == '__main__':
    a = SingleLinkedList()
    for i in range(1, 10):
        a.append(i)
    print a.size()
    a.travel()
    print a.search(6)
    print a.index(5)
    a.remove(4)
    a.travel()
    a.insert(4, 100)
    a.travel()
    print type(a)
