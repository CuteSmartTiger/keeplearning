def gen_fnuc():
    try:
        yield 1
    except Exception as e:
        pass
    yield 2
    yield 3
    return 'liuhu'


if __name__ == '__main__':
    # 生成生成器对象gen
    gen = gen_fnuc()
    ge = gen.send(None)
    print(ge)
    # 当前yield抛出异常
    gen.throw(Exception,'hi')

