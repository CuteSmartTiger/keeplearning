#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 14:30
# @Author  : liuhu
# @Site    : 
# @File    : rabbitmq_produce.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='192.168.37.134'))

channel = connection.channel()

channel.queue_declare(queue='queue_name')  # 如果队列没有创建，就创建这个队列

def callback(ch, method, propertities,body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='queue_name',  # 队列名
                      no_ack=True)  # 不通知已经收到，如果连接中断可能消息丢失

print(' [*] Waiting for message. To exit press CTRL+C')
channel.start_consuming()