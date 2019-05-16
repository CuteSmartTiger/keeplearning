#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 19:10
# @Author  : liuhu
# @File    : 工厂方法之自己编写.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


class ZipOperate(object):
    def __init__(self, filepath):
        self.path = filepath

    def upzip(self):
        print '解压 {} 文件'.format(self.path)


class PdfOperate(object):
    def __init__(self, filepath):
        self.path = filepath

    def read_pdf(self):
        print '读取 {} 文件'.format(self.path)


class ExcelOperate(object):
    def __init__(self, filepath):
        self.path = filepath

    def upzip(self):
        print '导入 {} 文件'.format(self.path)


def connect_factory(filepath):
    if filepath.endswith('.zip'):
        connector = ZipOperate
    elif filepath.endswith('.pdf'):
        connector = PdfOperate
    elif filepath.endswith('.xlxs'):
        connector = ExcelOperate
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)