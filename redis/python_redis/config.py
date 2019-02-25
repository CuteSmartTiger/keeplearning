#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 11:40
# @Author  : liuhu
# @File    : config.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
import redis

redisClient = redis.StrictRedis(host='192.168.6.92', port=6379, db=0)