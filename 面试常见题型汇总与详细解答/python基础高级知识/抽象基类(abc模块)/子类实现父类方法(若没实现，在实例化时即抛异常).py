#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 20:47
# @Author  : liuhu
# @File    : 子类实现父类方法(若没实现，在实例化时即抛异常).py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


import abc
from collections.abc import *


# 通过元类继承保证子类必须实现父类方法
class Cache(metaclass=abc.ABCMeta):
    """通过abc模块限定子类必须实现父类方法"""

    @abc.abstractmethod
    def get(self, key):
        print('abc get  {0}'.format(key))

    @abc.abstractmethod
    def set(self, key, value):
        print('abc set method')


class Redis(Cache):
    def get(self, key):
        # super(Redis, self).get(key)
        super().get(key)

    def set(self, key, value):
        pass


redis_cache = Redis()
redis_cache.get('name')
