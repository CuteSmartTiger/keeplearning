# 了解yield from用法


# 自定义一个生成器


def chain1(*iterables):
    for it in iterables:
        for i in it:
            yield i


s = 'ABC'
# t = tuple(range(3))
t = range(3)
print(list(chain1(s, t)))

print('-----------------------------')


# 引入新句法yield from
def chain2(*iterables):
    for it in iterables:
        # yield from 代替了最内层的for循环
        yield from it


s = 'ABC'
# t = tuple(range(3))
t = range(3)
print(list(chain2(s, t)))
