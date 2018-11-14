class School(object):
    def __init__(self, student_list):
        self.students = student_list

    def __getattr__(self, item):
        print('没有这个属性')
        return None


if __name__ == '__main__':
    school = School(['A', 'B', 'C'])
    print(school.age)

# __getattr__ 属于处理属性的特殊方法，仅当获取指定的属性失败，搜索过 obj、Class 和超类之后调用。
#  表达式 obj.no_such_attr、getattr(obj, 'no_such_attr') 和hasattr(obj, 'no_such_attr') 可能会触发
#  Class.__getattr__(obj, 'no_such_attr') 方法，但是，仅当在obj、Class 和超类中找不到指定的属性时才会触发。
#  在查找不到属性时调用
