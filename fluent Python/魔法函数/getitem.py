class School(object):
    def __init__(self, student_list):
        self.students = student_list

    def __getitem__(self, item):
        return self.students[item]


student_list = ['a', 's', 'f', 't']

students = School(student_list)
# 定义了getitem方法，可以实现index索引取值
print(students[2])

# for循环时，当找不到__iter__方法时，会查
# 找__getitem__方法，有就可以实现循环取值
for student in students:
    print(student)
