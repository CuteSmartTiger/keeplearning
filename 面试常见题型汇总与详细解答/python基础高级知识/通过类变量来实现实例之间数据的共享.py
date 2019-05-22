#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 22:53
# @Author  : liuhu
# @Site    : 
# @File    : 通过类变量来实现实例之间数据的共享.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

class Human:
    love_color = []

    def add(self, color):
        self.love_color.append(color)

a =Human()
a.add('red')
b = Human()
b.add('blue')
print(a.love_color)
print(b.love_color)