#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 16:19
# @Author  : liuhu
# @File    : save_and_get_raw_data.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

import redis
import pickle


class redisOperation(object):
    def __init__(self, host='192.168.6.92', port=6379, db=2):
        self.database = redis.StrictRedis(
            host=host, port=port, db=db)
        print("Successfully connect to Redis Server.")

    def setData(self, key, value, expire):
        self.database.set(key, pickle.dumps(value), expire)

    def getData(self, key):
        data = self.database.get(key)
        if data is None:
            return None
        else:
            return pickle.loads(data)

    def getKeys(self):
        byteKeys = self.database.keys()
        rawKeys = []
        for key in byteKeys:
            rawKeys.append(key.decode())
        return rawKeys


r = redisOperation(host='192.168.6.96', port=6379, db=2)

# r.setData('username', [10,20,90,(30,10,29)],10)
# r.setData('username', [10,20,90,(30,10,29)],10)
print r.getData('username')
