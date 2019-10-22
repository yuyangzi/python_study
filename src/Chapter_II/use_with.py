def read_file():
    f = None
    try:
        f = open('./static/test.json', 'r', encoding='utf-8')
        data = f.read()
        print(data)
    except IOError as error:
        print(error)
        print('文件读取错误')
    finally:
        f.close()


def read_file_with():
    with open('./static/test1.json', 'r', encoding='utf-8') as f:
        data = f.read()
        print(data)


if __name__ == '__main__':
    read_file()
