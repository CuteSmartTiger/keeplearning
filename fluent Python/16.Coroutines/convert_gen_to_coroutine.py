# 生成器是可以暂停的函数
import inspect


# 生成器主要指使用yield往外产出数据，
# 而协程则是指可以产出与消费数据
def gen_func():
    # 生成器可以接受一个值
    # 作用一：返回一个值给调用方
    # 作用二：调用方通过send()方法返回值给生成器
    res = yield 1
    return 'liuhu'


if __name__ == '__main__':
    gen = gen_func()
    print(inspect.getgeneratorstate(gen))
    next(gen)
    print(inspect.getgeneratorstate(gen))
    try:
        next(gen)
    except StopIteration:
        pass
    print(inspect.getgeneratorstate(gen))

# 1.使用同步的方式编写异步的代码
# 2.在适当的时候可以暂停函数并在适当时候启动函数
