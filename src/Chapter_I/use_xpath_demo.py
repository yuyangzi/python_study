"""
使用xPath 模块爬取网页数据
"""

from lxml import html


def pares_html():
    # 打开文本
    html_file = open('./static/index.html', 'r', encoding='utf-8')

    # 读取文本
    html_str = html_file.read()

    # 获取选择器
    selector = html.fromstring(html_str)

    # 读取h3标签文本
    h3_text = selector.xpath('/html/body/h3/text()')
    print(h3_text[0])

    # 获取li标签
    li_element = selector.xpath('//ul/li')

    for li in li_element:
        print(li.xpath('text()')[0])

    # 读取class属性为important的标签内容
    li_important = selector.xpath('/html/body/ul/li[@class="important"]/text()')
    print(li_important[0])

    # 读取a标签的href属性和文本
    a_link = selector.xpath('/html/body/div[@id="container"]/a/@href')
    print(a_link)

    # 读取a标签的文本文本内容
    a_text = selector.xpath('//a/text()')
    print(a_text)

    # 打印最后一个p标签的文本内容
    p_last_text = selector.xpath('/html/body/p[last()]/text()')
    print(p_last_text[0])

    # 关闭文本
    html_file.close()


if __name__ == '__main__':
    pares_html()
