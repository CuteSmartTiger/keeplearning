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
    host='192.168.37.134'
))
channel = connection.channel()
channel.queue_declare(queue='queue_name')  # 如果队列没有创建，就创建这个队列
channel.basic_publish(exchange='',
                      routing_key='queue_name',   # 指定队列的关键字为，这里是队列的名字
                      body='Hello World!')  # 往队列里发的消息内容

print(" [x] Sent 'Hello World!'")
connection.close()