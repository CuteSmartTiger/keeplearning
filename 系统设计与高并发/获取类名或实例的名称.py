#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 23:04
# @Author  : liuhu
# @Site    : 
# @File    : 获取类名或实例的名称.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

class AquireName:
    def aquire_name(self):
        print('{}'.format(type(self).__name__))
        print('{}'.format(self.__doc__))
        print('{}'.format(self.__dir__()))
        pass
        return


s = AquireName()
print(s.aquire_name())
