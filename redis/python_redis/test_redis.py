#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 15:45
# @Author  : liuhu
# @File    : test_redis.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

import redis
import pickle
redisClient = redis.StrictRedis(host='192.168.6.96', port=6379, db=2)
# res = redisClient.set('test_redis', 'Hello Python')
res1 = redisClient.keys()
print res1
# for i in res1:
#     redisClient.delete(i)
for i in res1:
    print pickle.loads(redisClient.get(i))
# res2 = redisClient.keys()
# print res2
