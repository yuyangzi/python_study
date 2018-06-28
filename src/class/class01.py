class Student():
    name = '王宜明'
    age = 23

    def print_info(self):
        self.a()
        print('我的名字是' + self.name)
        print('我的年龄是' + str(self.age))

    def a(self):
        print('a')


student = Student()

student.print_info()