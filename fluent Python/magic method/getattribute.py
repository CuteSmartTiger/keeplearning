class School(object):
    def __init__(self, student_list):
        self.students = student_list

    def __getattr__(self, item):
        print('没有这个属性')
        return None

    def __getattribute__(self, item):
        raise AttributeError
        # return '无条件调用属性接口'


if __name__ == '__main__':
    school = School(['A', 'B', 'C'])
    print(school.age)
    print(school.students)

# __getattribute__(self, name)尝试获取指定的属性时总会调用这个方法，不过，寻找的属性是特
#    殊属性或特殊方法时除外。点号与 getattr 和 hasattr 内置函数会触发这个方法。调用 __getattribute__
#    方法且抛出 AttributeError异常时，才会调用 __getattr__ 方法。为了在获取 obj 实例的属性时不导致无
#    限递归，__getattribute__ 方法的实现要使用super().__getattribute__(obj, name)。
