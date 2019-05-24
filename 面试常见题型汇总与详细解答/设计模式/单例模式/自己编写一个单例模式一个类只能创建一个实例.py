#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 16:07
# @Author  : liuhu
# @File    : 自己编写一个单例模式一个类只能创建一个实例.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class Singleton(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.instance
