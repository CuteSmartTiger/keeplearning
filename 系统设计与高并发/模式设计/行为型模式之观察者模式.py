#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 22:11
# @Author  : liuhu
# @Site    : 
# @File    : 行为型模式之观察者模式.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Publisher:
    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('Failed to add: {}'.format(observer))

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('Failed to remove: {}'.format(observer))

    def notify(self):
        print('notify')
        [o.notify(self) for o in self.observers]


class DefaultFormatter(Publisher):
    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name
        self._data = 0

    def __str__(self):
        return "{}: '{}' has data = {}".format(type(self).__name__, self.name, self._data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        try:
            self._data = int(new_value)
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            self.notify()


class HexFormatter:
    def notify(self, publisher):
        print("{}: '{}' has now hex data = {}".format(type(self).__name__, publisher.name, hex(publisher.data)))


class BinaryFormatter:
    def notify(self, publisher):
        print("{}: '{}' has now bin data = {}".format(type(self).__name__, publisher.name, bin(publisher.data)))


def main():
    df = DefaultFormatter('test1')
    print(df)
    print('==========================')
    hf = HexFormatter()
    df.add(hf)
    hf2 = HexFormatter()
    df.add(hf2)
    df.data = 3


    # df.data = 5
    # print(df.observers)
    # print('==========================')
    # bf = BinaryFormatter()
    # df.add(bf)
    # df.data = 21
    # print(df)
    # print('==========================')
    # df.remove(hf)
    # df.data = 40
    # print(df)
    # print('==========================')
    # df.remove(hf)
    # df.add(bf)
    # df.data = 'hello'
    # print(df)
    # print('==========================')
    # df.data = 15.8
    # print(df)


if __name__ == '__main__':
    main()
