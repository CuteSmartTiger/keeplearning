#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 11:54
# @Author  : liuhu
# @File    : 使用list实现字典.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class _ArrayIterator:
    def __init__(self, items):
        self._items = items
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idex < len(self._items):
            val = self._items[self._idx]
            self._idex += 1
            return val
        else:
            raise StopIteration


class Map(object):
    """ Map ADT list implemention
    Map()
    length()
    contains(key)
    add(key, value)
    remove(key)
    valudOf(key)
    iterator()
    """

    def __init__(self):
        self._entryList = list()

    def __len__(self):
        return len(self._entryList)

    def __contains__(self, key):
        ndx = self._findPosition(key)
        return ndx is not None

    def add(self, key, value):
        ndx = self._findPosition(key)
        if ndx is not None:
            self._entryList[ndx].value = value
            return False
        else:
            entry = _MapEntry(key, value)
            self._entryList.append(entry)
            return True

    def valueOf(self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, 'Invalid map key'
        return self._entryList[ndx].value

    def remove(self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, 'Invalid map key'
        self._entryList.pop(ndx)

    def __iter__(self):
        return _MapIterator(self._entryList)

    def _findPosition(self, key):
        for i in range(len(self)):
            if self._entryList[i].key == key:
                return i
        return None


class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


c = Map()
c.add('name', 'liuhu')
c.add('age', 18)
for key, value in c:
    print key, value
