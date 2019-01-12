#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 16:18
# @Author  : liuhu
# @Site    :
# @File    : 02服务端宕机后消息durable之rabbitmq_produce.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

import pika


connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='192.168.37.134'))
channel = connection.channel()

# make message persistent
channel.queue_declare(queue='durable_queue_name', durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    import time
    time.sleep(4)
    print('ok')
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(callback,
                      queue='durable_queue_name',
                      no_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
