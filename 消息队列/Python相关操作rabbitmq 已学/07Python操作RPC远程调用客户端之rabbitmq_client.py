#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 21:10
# @Author  : liuhu
# @Site    :
# @File    : 07Python操作RPC远程调用客户端之rabbitmq_produce.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# !/usr/bin/env python
import pika
import uuid


class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='192.168.37.134'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)

        self.callback_queue = result.method.queue

        # 接受信息
        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)


    def on_response(self,ch, method, props, body):
        print('self.corr_id:{0}'.format(self.corr_id))
        if self.corr_id == props.correlation_id:
            self.response = body
            print(self.response)

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,
                                   ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)


fibonacci_rpc = FibonacciRpcClient()

import time
print(" 客户端 请求 fib() 操作")
x = 0
while True:
    response = fibonacci_rpc.call(x)
    int(response)
    x +=1
    print("客户端显示: 远程操作后的结果是 %r" % response)
    time.sleep(0.2)