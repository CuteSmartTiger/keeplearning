#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 20:57
# @Author  : liuhu
# @Site    : 
# @File    : 自己编写一个老师与学生关系的观察者模式.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Teacher:
    def __init__(self, name):
        self.name = name
        self.observers = []
        self._work = 'no home work'

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            raise ValueError('Observer has been in observers list')

    def remove(self, observer):
        self.observers.remove(observer)

    def __repr__(self):
        return '{}:{} has homework {} '.format(type(self).__name__, self.name, self._work)

    @property
    def homework(self):
        return self._work

    @homework.setter
    def homework(self, work):
        try:
            self._work = work
        except ValueError as e:
            raise ValueError('homework name must be str')
        else:
            self.notify()

    def notify(self):
        [o.notify() for o in self.observers]


class Student:

    def __init__(self, name):
        self.name = name

    def notify(self):
        print('{0} has been notify to get homework '.format(self.name))


teacher = Teacher('Dvd')
student_one = Student('student one')
student_two = Student('student two')

teacher.add(student_one)
teacher.add(student_two)
teacher.homework = 'math'
print(teacher)
teacher.remove(student_one)
teacher.homework = 'CN'
print(teacher)