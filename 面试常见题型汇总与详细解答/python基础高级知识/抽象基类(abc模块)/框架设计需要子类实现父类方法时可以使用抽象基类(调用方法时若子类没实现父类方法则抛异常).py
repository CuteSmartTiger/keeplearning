#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 20:40
# @Author  : liuhu
# @File    : 框架设计需要子类实现父类方法时可以使用抽象基类(调用方法时若子类没实现父类方法则抛异常).py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Cache(object):
    """在父类中的方法raise NotImplementedError，让子类在没有定义实现父类方法时抛异常"""
    def get(self, key):
        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError


class Redis(Cache):
    pass

redis_cache = Redis()
redis_cache.get('name')
