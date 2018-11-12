class School(object):
    def __init__(self, student_list):
        self.students = student_list

    def __getattr__(self, item):
        print('没有这个属性')
        return None

    def __getattribute__(self, item):
        return '无条件调用属性接口'


if __name__ == '__main__':
    school = School(['A', 'B', 'C'])
    print(school.age)
    print(school.students)
