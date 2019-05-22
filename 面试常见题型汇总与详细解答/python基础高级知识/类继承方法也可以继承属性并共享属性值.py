#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 22:46
# @Author  : liuhu
# @Site    : 
# @File    : 类继承方法也可以继承属性.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Human:
    love_color = []

    def add(self, color):
        self.love_color.append(color)


class Man(Human):
    pass


class Woman(Human):
    pass


a = Man()
a.add('red')
b = Woman()
b.add('blue')
print(a.love_color)
print(b.love_color)
