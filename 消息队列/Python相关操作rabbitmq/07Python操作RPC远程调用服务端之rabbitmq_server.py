#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 21:05
# @Author  : liuhu
# @Site    : 
# @File    : 07Python操作RPC远程调用服务端.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# !/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.37.134'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 接受客户端指定的channel中队列的请求参数，执行后发布到消息队列中
def on_request(channel_node, method, props, body):
    n = int(body)

    print(" 等待的请求操作的函数是： fib(%s)" % n)
    response = fib(n)

    #  reply_to 和 correlation_id 属性要求服务端将处理完返回对应的消息
    channel_node.basic_publish(exchange='',
                               routing_key=props.reply_to,
                               properties=pika.BasicProperties(correlation_id=props.correlation_id),
                               body=str(response))

    channel_node.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)

# 接受客户的请求
channel.basic_consume(on_request, queue='rpc_queue')

print(" 等待 RPC 的 requests")
# 循环
channel.start_consuming()
