from urllib import request
import re
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


class Spider():
    url = 'http://www.panda.tv/cate/lol'
    root_pattern = r'<div class="video-info">([\s\S]*?)</div>'
    name_pattern = r'</i>([\s\S]*?)</span>'
    number_pattern = r'<span class="video-number">([\s\S]*?)</span>'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __fromat_data(self, html_string):
        data_list = re.findall(self.root_pattern, html_string)
        return data_list

    def __distill_data(self, anchors):
        _anchors = []
        for anchor in anchors:
            name = self.__get_name(anchor)
            number = self.__get_people_number(anchor)
            _anchor = {'name': name, 'number': number}
            _anchors.append(_anchor)
        return _anchors

    def __get_name(self, anchor_str):
        return re.findall(self.name_pattern, anchor_str)

    def __get_people_number(self, anchor_str):
        return re.findall(self.number_pattern, anchor_str)

    def __refine(self, anchors):
        l = lambda anchor: {'name': anchor['name'][0].strip(), 'number': anchor['number'][0]}
        return map(l, anchors)


    def __sort_data(self, anchors):
        anchors = sorted(anchors, key=self.__sort_seed)
        return anchors

    def __sort_seed(self, anchor):
        number = anchor['number']
        number = re.findall(r'\d*', number)
        number = float(number[0])
        if '万' in anchor['number']:
            number *= 10000
        return number


    def __show(self, anchors):
        """
        显示函数
        """
        for rank in range(0, len(anchors)):
            print(str(rank) + ':' + anchors[rank]['name'] + '---------------' + anchors[rank]['number'])

    def go(self):
        htmls = self.__fetch_content()
        data_list = self.__fromat_data(htmls)
        anchors = self.__distill_data(data_list)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort_data(anchors)
        self.__show(anchors)

spider = Spider()
spider.go()
