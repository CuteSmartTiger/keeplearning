# 第一步：了解两者直接的返回值的不同
def test1(gen):
    yield gen


def test2(gen):
    yield from gen


for value in test1(range(1, 10)):
    print(value)
# 输出结果：range(1, 10)

print('-------------------------')
for value in test2(range(1, 10)):
    print(value, end=' ')


# 输出结果：1 2 3 4 5 6 7 8 9


# 2.了解yield from的另一种用法：
def tes1(gen):
    yield from gen


def main_func():
    tes = tes1()
    tes.send(None)

# 以上解释：
# 1.main_func为调用方
# 2.tes1为委托生成器
# 3.gen为自生成器
# yield from 会在调用方与生成器之间建立一个双向通道
