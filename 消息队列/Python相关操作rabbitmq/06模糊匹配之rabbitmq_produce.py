#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 19:20
# @Author  : liuhu
# @Site    : 
# @File    : 06模糊匹配之rabbitmq_consume.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


"""
exchange type = topic
在topic类型下，可以让队列绑定几个模糊的关键字

# 表示可以匹配 0 个 或 多个 字符
*  表示只能匹配 一个 任意字符
"""

import pika
import sys



connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.37.134'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_log',
                         exchange_type='topic')


# routing_key = 'c.baidu.o'
routing_key = 'newbaidueold'

message = 'Hello World!'
channel.basic_publish(exchange='topic_log',
                      routing_key=routing_key,
                      body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()

'''
#.orange.#  匹配：new.orange.old  neworangeold
*.orange.*  匹配：neworangeold，不匹配：new.orange.old
'''