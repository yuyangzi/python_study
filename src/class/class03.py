class Student():
    sum = 0

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.___sex = sex

    def print_info(self):
        print(self.name)

    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)

    @staticmethod
    def print_message():
        print('信息')
    
    def __print_info(self):
        print('_message')


student = Student('李白', 20, '男')

Student.plus_sum()
student.__class__.plus_sum()
student.__class__.print_message()


print(student.__dict__)


