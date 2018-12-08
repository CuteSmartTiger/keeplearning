class School(object):
    # 用于定义创建类的过程
    # 第一个参数传递的是类
    # new方法主要用于元高级编程
    def __new__(cls, *args, **kwargs):
        print('in new')
        # return作为连接new方法与init方法的桥梁
        return super().__new__(cls)

    def __init__(self, name):
        print('in init')
        self.students = name

    # def __call__(self, *args, **kwargs):
    #     return self.students


# new是用来控制对象的生成过程，在对象生成之前
# init是用来完善对象的
# 如果new方法不反悔对象，则不会调用init函数
if __name__ == '__main__':
    # 类实例化传入的参数需要与init中的参数名称相同，否则会报错
    school = School(name='liuhu')

