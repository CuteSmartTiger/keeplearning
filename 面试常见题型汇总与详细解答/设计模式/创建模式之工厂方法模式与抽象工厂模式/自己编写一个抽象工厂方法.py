#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/26 1:04
# @Author  : liuhu
# @Site    : 
# @File    : 自己编写一个抽象工厂方法.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# 抽象工厂设计模式的实现是同属于单个类的许多个工厂方法用于创建一系列种类的相关对象


class Teacher(object):
    def __init__(self, name):
        self.name = name

    def make_role(self):
        return 'teacher'

    def make_weapon(self):
        return 'book'

    def make_action(self):
        return 'teach'


class Soldier(object):
    def __init__(self, name):
        self.name = name

    def make_role(self):
        return 'soldier'

    def make_weapon(self):
        return 'hammer'

    def make_action(self):
        return 'defend home'


class Game(object):
    def __init__(self, factory):
        self.name = factory.name
        self.role = factory.make_role()
        self.weapon = factory.make_weapon()
        self.action = factory.make_action()

    def start_play(self):
        print('{} named {} use {} to {}'.format(self.role, self.name, self.weapon, self.action))


t = Teacher('lao shi')
g = Game(t)
g.start_play()

s = Soldier('knight')
g2 = Game(s)
g2.start_play()