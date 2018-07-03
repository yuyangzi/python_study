class Student():
    sum = 0

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def print_info(self):
        print(self.name)

    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)


student = Student('李白', 20, '男')

Student.plus_sum()
student.__class__.plus_sum()
# print(student.age, Student.sex)


