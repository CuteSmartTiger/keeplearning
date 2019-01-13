#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 16:34
# @Author  : liuhu
# @Site    : 
# @File    : 03多个消费者按顺序取消息之rabbitmq_consume.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

__author__ = 'liuhu'
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.37.134'))
channel = connection.channel()

# make message persistent
channel.queue_declare(queue='mutil_consume')


def callback(ch, method, properties, body):
    print(" [x1] Received %r" % body)
    import time
    time.sleep(5)
    print('ok')
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback,
                      queue='mutil_consume',
                      no_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
