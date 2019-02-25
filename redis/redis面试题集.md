
```python
# 1. 如果redis中的某个列表中的数据量非常大，如果实现循环显示每一个值？
import redis

redisClient = redis.StrictRedis(host='192.168.6.92', port=6379, db=1)

for i in range(20):
    redisClient.lpush("1",i)


print redisClient.lrange('1',0,-1)


def list_iter(key, count=3):
    start = 0
    while True:
        result = redisClient.lrange(key, start, start + count - 1)
        print result
        start += count
        if not result:
            break
        for item in result:
            yield item


for val in list_iter('1'):
            print val

```
