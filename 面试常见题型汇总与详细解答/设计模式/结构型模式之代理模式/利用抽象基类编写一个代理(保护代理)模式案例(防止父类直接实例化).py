#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 20:59
# @Author  : liuhu
# @File    : 利用抽象基类编写一个代理(保护代理)模式案例(防止父类直接实例化).py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

import abc


class SensitiveInfo(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    @abc.abstractmethod
    def read(self):
        print('There are {} users: {}'.format(len(self.users), ' '.join(self.users)))

    @abc.abstractmethod
    def add(self, user):
        self.users.append(user)
        print('Added user {}'.format(user))
        print(self.users)


class Info(SensitiveInfo):
    """SensitiveInfo的保护代理"""

    def __init__(self):
        SensitiveInfo.__init__(self)
        # super().__init__()
        # super(Info, self).__init__()
        print(self.users)
        self.secret = '123123'

    def read(self):
        super(Info, self).read()

    def add(self, user):
        sec = input('what is the secret? ')
        super(Info, self).add(user) if sec == self.secret else print("That's wrong!")
        # self.protected.add(user) if sec == self.secret else print("That's wrong!")


c = Info()
c.read()
c.add('liuhu')
