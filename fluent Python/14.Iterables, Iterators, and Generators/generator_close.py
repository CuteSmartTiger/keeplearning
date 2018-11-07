def gen_fnuc():
    # 生成器中尽量不用捕获异常
    try:
        yield 1
    except GeneratorExit:
        print('pass')
        pass
    # 后面有yield则报错，后面没有则不会报错
    yield 2
    # yield 3
    return 'liuhu'


if __name__ == '__main__':
    # 生成生成器对象gen
    gen = gen_fnuc()
    ge = gen.send(None)
    print(ge)
    # 如果生成器中没有捕捉异常，则close后面的print会继续执行
    # 下一个yield抛出异常
    gen.close()
    # next(gen)
    # print('ji')
