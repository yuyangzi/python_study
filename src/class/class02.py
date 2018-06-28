class Student():

    sex = '女'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def print_info(self):
        print(self.name)

student = Student('李白', 20, '男')
print(student.name, Student.sex)
print(student.age, Student.sex)


