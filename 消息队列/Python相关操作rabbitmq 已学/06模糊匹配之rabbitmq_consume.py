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

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_keys = "#.baidu.#"
# binding_keys = "*.baidu.*"


for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_log',
                       queue=queue_name,
                       routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()