def gen_fnuc():
    # yield 'www.baidu.com'
    url = yield 'www.baidu.com'
    print(url)
    yield 2
    yield 3

    return 'liuhu'


if __name__ == '__main__':
    # 生成生成器对象gen
    gen = gen_fnuc()
    # 在调用send发送非None值时，我们必须启动一次生成器，方法两种：
    # 一则：gen.send(None)
    # 二则：next(gen)
    # send方法可以传递值进入生成器内部，同时重启生成器执行到下一个yield位置
    ge = gen.send(None)  # yield出来的值赋给ge变量，send发送中的None传值给url
    print(ge)
    print(next(gen))  # next运行，但是不会打印yield抛出的值，需要使用print方法，也可以将结果赋予变量
