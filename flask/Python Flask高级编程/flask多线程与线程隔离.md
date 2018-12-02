flask webserver

flask自带的是单线程 单进程响应请求，是webserver开启多线程满足同时发来的多个请求



Python主要依赖的数据结构是字典
多线程 线程id作为唯一标识
request = {thread_key1:Request1,thread_key2:Request2,....}



#### Local
线程隔离使用Werkzeug的包中的Local()
```PYTHON
pipenv install Werkzeug
from werkzeug.local import Local
```



#### LocalStack线程隔离对象
- 同时可以了解push top pop 方法

```Python
from werkzeug.local import LocalStack
import threading, time

test_localstack = LocalStack()
test_localstack.push(1)


def worker():
    print('before push, test local stack value {}'.format(test_localstack.top))
    test_localstack.push(2)
    print('after push,test local stack value {}'.format(test_localstack.top))


new_test = threading.Thread(target=worker, name='xiancheng')
new_test.start()

time.sleep(1)
print('main thread value is {0}'.format(test_localstack.top))

```



#### 其他线程隔离对象
```PYTHON
# context locals
_request_ctx_stack = LocalStack()
_app_ctx_stack = LocalStack()
current_app = LocalProxy(_find_app)
request = LocalProxy(partial(_lookup_req_object, 'request'))
session = LocalProxy(partial(_lookup_req_object, 'session'))
g = LocalProxy(partial(_lookup_app_object, 'g'))
```


#### 名词概念理解
- 使用线程隔离对象创建被线程隔离的对象，请区别线程隔离对象与被线程隔离的对象
- 线程隔离与线程安全



#### 通过这种设计我们可以学到的设计思路
