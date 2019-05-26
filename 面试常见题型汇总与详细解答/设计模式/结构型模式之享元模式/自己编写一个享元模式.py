#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 16:07
# @Author  : liuhu
# @File    : 自己编写一个享元模式.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
# 学生类  老师类  工人类  每一类共享元

from enum import Enum

HumanType = Enum('HumanType', 'student_type teacher_type worker_type')


class Human(object):
    human_type_pool = dict()

    def __new__(cls, human_type):
        obj = cls.human_type_pool.get(human_type, None)
        if not obj:
            obj = super(Human, cls).__new__(cls)
            cls.human_type_pool[human_type] = obj
            obj.human_type = human_type
        return obj

    def render(self, age, color):
        print('render {} ,age is {},color is {}'.format(self.human_type, age, color))


s1 = Human(HumanType.student_type)
s1.render(18,'red')
s1.render(28,'white')
s2 = Human(HumanType.student_type)
print(id(s1)==id(s2))
print(s1 is s2)