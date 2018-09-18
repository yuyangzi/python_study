"""
爬去当当网的书籍信息
"""

import requests
from lxml import html


def spider_book(book_id):
    """
    爬去当当网书籍信息
    :param book_id:
    :return: void
    """

    # 当当网书籍搜索API
    url = 'http://search.dangdang.com/?key={sn}&act=input'.format(sn=book_id)

    # 返回的HTML数据
    result_html = requests.get(url=url).text

    # XPath对象
    selector = html.fromstring(result_html)

    # 找到书籍信息list数据
    ul_list_data = selector.xpath('//div[@id="search_nature_rg"]/ul/li')

    for li_element in ul_list_data:
        # 标题
        book_title = li_element.xpath('a[@class="pic"]/@title')
        print(book_title[0])

        # 购买链接
        book_link = li_element.xpath('a[@class="pic"]/@href')
        print(book_link[0])

        # 价格
        book_price = li_element.xpath('p[@class="price"]/span[@class="search_now_price"]/text()')
        print(book_price[0].replace('¥', ''))

        # 商家
        book_store = li_element.xpath('p[@class="search_shangjia"]/a/text()')
        book_store = '当当自营' if len(book_store) else book_store[0]
        print(book_store)


if __name__ == '__main__':
    spider_book('9787115428028')

