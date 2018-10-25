from random import randint


def d6():
    return randint(1, 6)


# 传入两个参数，使用常规
# 的函数或任何可调用的对象创建迭代器。这样使用时，第一个参数必须
# 是可调用的对象，用于不断调用（没有参数），产出各个值；第二个值
# 是哨符，这是个标记值，当可调用的对象返回这个值时，触发迭代器抛
# 出 StopIteration 异常，而不产出哨符。
d6_iter = iter(d6, 2)
# d6_iter 对象一旦耗尽就没
# 用了。如果想重新开始，必须再次调用 iter(...)，重新构建迭代器

for roll in d6_iter:
    print(roll)


# 此函数一致处于循环中，未实验成功
# 这段代码逐行读取文件，直到遇到空行或者到达文件末尾为止
# with open(r'C:\project\keeplearning\fluent Python\Iterables, Iterators, and Generators\itertest.txt') as fp:
#     for line in iter(fp.readline, '\n'):
#         print(line)