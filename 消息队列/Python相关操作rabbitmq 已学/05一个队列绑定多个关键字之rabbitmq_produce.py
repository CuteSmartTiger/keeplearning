#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 19:12
# @Author  : liuhu
# @Site    :
# @File    : 05一个队列绑定多个关键字之rabbitmq_produce.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = ''

import pika
import sys

'''
同时运行消费者1，消费者2，然后修改生产者的关键字，运行生产者。
当生产者：severity = 'info'，则消费者1收到消息，消费者2没收到消息
当生产者：severity = 'error'，则消费者1、消费者2 都收到消息
'''

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.37.134'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

# severity = 'info'
severity = 'error'
message = 'Hello World!'
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()
