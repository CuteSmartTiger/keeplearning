# 1.检测是否属于生成器类型
import types

# enumerate为内建的生成器函数
e = enumerate('ABC')
print(isinstance(e, types.GeneratorType))


# False


# 2.1不使用 GeneratorType 实例实
# 现斐波纳契数列生成器
class FibonacciGenerator:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result


class Fibonacci:
    def __iter__(self):
        return FibonacciGenerator()


# 2.2 对2.1的优化：使用GeneratorType类实现
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# 备注：在Python社区中把迭代器与生成器作为同一个概念，解释比较模糊