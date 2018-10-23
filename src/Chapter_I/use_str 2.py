"""
学习string的格式化操作
"""


def format_str():
    """
    使用format函数格式化
    """

    # 格式化字符串-位置格式化
    print('我的名字叫{0}, 我今年{1}岁, 我来到这个世界已经{1}年了'.format('李白', 19))

    # 名称格式化1
    print('我的名字是{user_name}, 我今年{age}岁了'.format(user_name='白居易', age=1000))

    # 名称格式化2
    user_info = {
        'user_name': '张良',
        'age': 2000,
    }
    print('我的名字是{user_name}, 年龄是{age}'.format(**user_info))

    # 格式化元组
    point = (1, 2)
    print('坐标位置为{0[0]}, {0[1]}'.format(point))

    # 格式化类
    class User:

        def __init__(self, user_name, user_age):
            self.user_name = user_name
            self.user_age = user_age

        def show(self):
            return '我的名字是{self.user_name}, 年龄为{self.user_age}'.format(self=self)

        def __str__(self):
            return self.show()

    user = User('王羲之', 1700)
    print(user)


if __name__ == '__main__':
    format_str()
