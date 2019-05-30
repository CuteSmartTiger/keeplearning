#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 11:56
# @Author  : liuhu
# @File    : python2.7_redis.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
import redis

redisClient = redis.StrictRedis(host='192.168.6.93', port=6379, db=0)
# res = redisClient.set('test_redis', 'Hello Python')
res1 = redisClient.set('count', 0)
# print res1

# value = redisClient.get('test_redis')
value1 = redisClient.get('counter')
if value1:
    print type(value1)
    print type(int(value1))
    value1 = int(value1)
    value1 +=1
    # d=redisClient.set('count', value1)
    # print d
# print value
print value1
