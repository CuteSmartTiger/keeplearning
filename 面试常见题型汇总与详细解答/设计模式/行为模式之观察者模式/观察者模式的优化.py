#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 23:26
# @Author  : liuhu
# @Site    : 
# @File    : 观察者模式的优化.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# 1. 订阅者学生，注册自己感兴趣的事件，事件列表中有则关注，没有则添加，也可以取消自己感兴趣的事件


class Share(object):
    event_dict = {}


class Student(Share):
    def __init__(self, name):
        self.name = name

    def register(self, event):
        if event not in self.event_dict:
            self.event_dict[event] = [self]
        else:
            self.event_dict[event].append(self)

    def unregister(self, event):
        if event in self.event_dict:
            self.event_dict[event].remove(self)
        else:
            raise ValueError('there is no {0}'.format(event))

    def notify(self, event):
        print('{0}:there is information about {1}'.format(self.name, event))


class Teacher(Share):
    def __init__(self, name):
        self.name = name

    def event(self, incident):
        if incident in self.event_dict:
            self.notify(incident)
        else:
            raise ValueError('there is no one focus on {}'.format(incident))

    def notify(self, incident):
        [o.notify(incident) for o in self.event_dict[incident]]


teacher = Teacher('laoshi')

student1 = Student('xiaoming')
student2 = Student('lilei')
student3 = Student('xiaofen')

student1.register('math')
student2.register('math')
student3.register('yuwen')

print(student1.event_dict)
print(teacher.event_dict)

print(teacher.name)
teacher.event('math')
