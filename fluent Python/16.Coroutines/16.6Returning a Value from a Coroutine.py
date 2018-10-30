from collections import namedtuple

Result = namedtuple('Result', 'count average')


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


cor_avg = averager()
next(cor_avg)
print(cor_avg.send(10))
print(cor_avg.send(15))
print(cor_avg.send(20))

try:
    cor_avg.send(None)
except StopIteration as exc:
    result = exc.value
    print(result)
# Result(count=3, average=15.0)