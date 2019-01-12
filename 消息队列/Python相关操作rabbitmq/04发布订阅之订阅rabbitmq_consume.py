#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 18:55
# @Author  : liuhu
# @Site    : 
# @File    : 04发布订阅之订阅rabbitmq_consume.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'liu hu'

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.37.134'))
channel = connection.channel()
'''
多次执行这个文件，就会随机生成多个队列。并且exchange都绑定这些队列。
然后发布者只需要给exchange发送消息，然后exchange绑定的多个队列都有
这个消息了。订阅者就收到这个消息了。
'''
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')
# 随机创建队列
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
# 绑定
channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
