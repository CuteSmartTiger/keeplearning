#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 15:57
# @Author  : liuhu
# @Site    : 
# @File    : 01消费者连接断消息不丢失.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.37.134'))
channel = connection.channel()

channel.queue_declare(queue='queue_name')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    import time
    time.sleep(2)
    print('ok')
    ch.basic_ack(delivery_tag = method.delivery_tag)
    print('返回值')

channel.basic_consume(callback,
                      queue='queue_name',
                      no_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()