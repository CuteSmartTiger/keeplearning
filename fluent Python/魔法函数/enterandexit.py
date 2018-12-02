# 上下文管理器定义：
# 1.定义一个类，类中实现enter与exit两个方法
# 2.enter打开获取资源，并将对象返回
# 3.exit 退出资源关闭，返回True或者False，不返
# 回值则默认为空，即False，False表示管理器不处理异常
# 4.定义处理资料的方法，也可不定义

class test:
    def __enter__(self):
        print('huo qu')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exc_type:{0}, exc_val:{1}, exc_tb:{2}'.format(exc_type, exc_val, exc_tb))
        print('tui chu')
        return True

    def deal(self):
        print('自定义处理方法')


# test实例化后才可以打开
with test() as f:
    print(f)
    print('go')
