远程过程调用（RPC）Remote procedure call

- 消息属性
   AMQP协议在一个消息中预先定义了一个包含14个属性的集合。大部分属性很少用到，以下几种除外：
  1. delivery_mode: 标记一个消息为持久的（值为2）或者 瞬时的（其它值）， 你需要记住这个属性（在第二课时用到过）
  2. content_type : 用来描述 MIME 类型的编码 ,比如我们经常使用的 JSON 编码，设置这个属性就非常好实现： application/json
  3. reply_to：reply_to没有特别的意义，只是一个普通的变量名，只是它通常用来命名一个 callback 队列
  4. correlation_id ： 用来关联RPC的请求与应答。关联id的作用：当在一个队列中接收了一个返回，我们并不清楚这个结果时属于哪个请求的，这样当correlation_id属性使用后，我们为每个请求设置一个唯一值，这个值就是关联id。这样，请求会有一个关联id，该请求的返回结果也有一个相同的关联id。然后当我们从callback队列中接收到一个消息后，我们查看一下这个关联，基于这个我们就能将请求和返回进行匹配。如果我们看到一个未知的correlation_id值，我们可以直接丢弃这个消息 -- 它是不属于我们的请求


- RPC执行过程

  1.  当客户端启动后，它创建一个匿名的唯一的回调队列
  2.  对一个RPC请求, 客户端发送一个消息包含两个属性： reply_to （用来设置回调队列）和 correlation_id（用来为每个请求设置一个唯一标识）
  3.  请求发送到 rpc_queue队列
  4. RPC worker( 服务端) 在那个队列中等待请求，当一个请求出现后，服务端就执行一个job并将结果消息发送给客户端，使用reply_to字段中的队列
  5.  客户端在callback 队列中等待数据, 当一个消息出现后，检查这个correlation_id属性,如果和请求中的值匹配将返回给应用


- 服务端代码
```Python
#rpc_server.py
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

```



- 客户端代码
```python
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

print(" 客户端 请求 fib() 操作")
response = fibonacci_rpc.call(7)
print("客户端显示: 远程操作后的结果是 %r" % response)
```


- [Python操作rabbitmq 实践笔记](https://www.cnblogs.com/wt11/p/5970297.html)(推荐理由：此篇文章有关系RPC远程过程调用)
