#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 18:52
# @Author  : liuhu
# @Site    : 
# @File    : 04发布订阅之发布rabbitmq_produce.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'liu hu'

import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.37.134'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()