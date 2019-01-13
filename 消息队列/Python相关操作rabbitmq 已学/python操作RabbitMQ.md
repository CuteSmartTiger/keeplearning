pip install pika



##### no-ack＝False：rabbitmq消费者连接断了 消息不丢失
channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(callback, queue='hello', no_ack=False)

#####  durable：rabbitmq服务端宕机 消息不丢失
多次生产后，停掉服务器，重启后，消费者可以一次将数据全部打印出来，注意创建的queue名称bu 不能与现有的冲突，否则会发生消息队列的属性矛盾



##### 多个消费者，按消息的顺序取

channel.basic_qos(prefetch_count=1)


##### 发布订阅之发布给所有绑定队列
发布订阅原理：

1）发布订阅和简单的消息队列区别在于，发布订阅会将消息发送给所有的订阅者，而消息队列中的数据被消费一次便消失。

2）所以，RabbitMQ实现发布和订阅时，会为每一个订阅者创建一个队列，而发布者发布消息时，会将消息放置在所有相关队列中。

3）exchange 可以帮你发消息到多个队列！type设为什么值，就把消息发给哪些队列。


##### 一个队列还可以绑定多个关键字





##### 模糊匹配(python3.6实验模糊匹配失败)
```
exchange_type = topic

在topic类型下，可以让队列绑定几个模糊的关键字，之后发送者将数据发送到exchange，exchange将传入”路由值“和 ”关键字“进行匹配，匹配成功，则将数据发送到指定队列。

# 表示可以匹配 0 个 或 多个 字符
*  表示只能匹配 一个 任意字符
```









##### 参考文章
- [Introduction to Pika](https://pika.readthedocs.io/en/latest/intro.html#tcp-backpressure)(推荐)

- [python操作RabbitMQ](https://www.cnblogs.com/wangqiaomei/p/5715331.html)(推荐理由：有详细的代码实例，不过有些过时，需要自己调整，也有saltstack相关的实例使用)


- [RabbitMQ基础概念详细介绍](https://www.cnblogs.com/diegodu/p/4971586.html)(推荐理由：基础概念讲的不错)


- [Python操作rabbitmq 实践笔记](https://www.cnblogs.com/wt11/p/5970297.html)(推荐理由：此篇文章有关系RPC远程过程调用)
