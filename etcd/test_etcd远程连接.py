#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 14:21
# @Author  : liuhu
# @File    : test_etcd远程连接.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
import etcd3
host ='192.168.6.95'
et = etcd3.client(host='192.168.6.95', port='2379')
print et