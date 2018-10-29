[参考手册地址](https://jimmysong.io/kubernetes-handbook/concepts/cni.html)


```

from functools import wraps
def coroutine(func):
    @wraps(func)
    def primer(*args,**kwargs):
        gen = func(*args,**kwargs)
        next(gen)
        return gen
    return primer


# @coroutine
def caculate_ave():
    total = 0.0
    count = 0
    average = None
    print '初始化参数'
    while True:
        print '内循环'
        term = yield average
        total += term
        count += 1
        average = total/count


c = caculate_ave()

# 调用 next 函数，预激协程
print next(c)
# 打印结果：
# 初始化参数
# 内循环
# None

# send 将信息发送给term
print c.send(4)
print c.send(5)
print c.send(7)
print c.send(12)
```
