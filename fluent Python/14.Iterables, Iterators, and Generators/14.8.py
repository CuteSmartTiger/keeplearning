import itertools
# 有理数，可以约分
from fractions import Fraction

print(Fraction(1, 7))

print('---------------------------')


class ArithmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end  # None -> 无穷数列

    def __iter__(self):
        # 强制转换成前面的加法算式得到的类型
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


print(list(ArithmeticProgression(1, 0.5, 3)))
# print(next(ArithmeticProgression(1,0.5,3)))
# print(next(ArithmeticProgression(1,0.5,3)))   #'ArithmeticProgression' object is not an iterator
for i in ArithmeticProgression(1, 0.5, 3):
    print(i)

print('---------------定义aritprog_gen生成器函数-------------')


def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        # 使用初始值加上阶数乘以指数，不用累加，可以减少精度累加的不准确效应
        result = begin + step * index


# next只能读取一个数，无法迭代
print(next(aritprog_gen(1, 1, 4)))
print(next(aritprog_gen(1, 1, 4)))

print(list(aritprog_gen(1, 1, 4)))

print('-------------等差数列---------------------')

# itertools.count 函数返回的生成器能生成多个数。如果不传
# 入参数，itertools.count 函数会生成从零开始的整数数列
seq = itertools.count(1, 1)
print(next(seq))
print(next(seq))
print(next(seq))
# list(seq) 可以无限生成


gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))

print(list(gen))

print('-----------------')


# aritprog_gen是生成器工厂函数，因为定义体中
# 没有 yield 关键字，不是生成器函数
def aritprog_gen2(begin, step, end=None):
    # 判断类型,若一个为整数一个浮点数，则统一为浮点数
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    return ap_gen


# print(aritprog_gen(1,0.5,3))

# 这里使用next方法无法迭代，注意与上面直接定义的gen对比
print(next(aritprog_gen2(1, 1)))
print(next(aritprog_gen2(1, 1)))
# print(list(aritprog_gen(1,0.5,3)))
