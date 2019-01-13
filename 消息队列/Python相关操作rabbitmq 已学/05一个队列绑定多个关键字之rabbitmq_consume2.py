#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 19:05
# @Author  : liuhu
# @Site    : 
# @File    : 05一个队列绑定多个关键字之rabbitmq_consume1.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

result = channel.queue_declare(exclusive=True)    # 随机生成队列

queue_name = result.method.queue
print(queue_name)

severities = [ "error"]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
