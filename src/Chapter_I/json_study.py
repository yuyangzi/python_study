"""
学习:\
    json转Python字典方法
    Python字典dict to json
    读取json文件转换成Python dict
"""

import json


def python_dict_to_json(python_dict):
    """
    Python字典dict to json
    :param python_dict: dict
    :return:
    """
    json_data = json.dumps(python_dict)
    print(json_data)


def json_to_python_dict(json_data):
    """
    json转Python字典方法
    :param json_data: json str
    :return:
    """

    request = json.loads(json_data, encoding='utf-8')
    print(request['name'])


def read_json_file_to_dict():
    f = open('./static/book.json')
    s = f.read()
    request = json.loads(s, encoding='utf-8')
    print(request['name'])
    f.close()


if __name__ == '__main__':
    python_dict_to_json({'name': '区块链-技术驱动金融'})

    json_data_1 = '''
    {
  "name": "Python书籍",
  "origin_price": 66,
  "pub_date": "2018-4-14 17:00:00",
  "store": [
    "京东",
    "淘宝"
  ],
  "author": [
    "张三",
    "李四",
    "王五"
  ],
  "is_valid": true,
  "is_sale": false,
  "meta": {
    "isbn": "abc-123",
    "pages": 300
  },
  "desc": null
}
    '''

    json_to_python_dict(json_data_1)

    read_json_file_to_dict()
