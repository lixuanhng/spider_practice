import requests
import json
from bs4 import BeautifulSoup
import re
import time
"""
如果报错信息如下：
data_list = pattern.findall(data[0].string)
IndexError: list index out of range
则说明代码有误
"""


def articleTypeEntrance(url_tmp, page_index):
    """
    确定需要爬取的页面
    :param url_tmp:
    :param page_index:
    :return:
    """
    time.sleep(5)
    url_tmp += page_index
    str_html = requests.get(url_tmp)
    soup = BeautifulSoup(str_html.text, 'lxml')
    # 将结果转为字符串
    data = soup.select('body > script')[0].string
    data = data.split('=')[1]
    data_dict = json.loads(data)
    # 收集所有文本
    contents = []
    for item in data_dict['feedList']['items']:
        contents.append(requireArticle(str(item['object_id'])))
    return contents


def requireArticle(object_id):
    """
    返回一篇文章的全文
    :param object_id:
    :return:
    """
    time.sleep(5)
    str_html = requests.get('https://dxy.com/article/' + object_id)
    soup = BeautifulSoup(str_html.text, 'lxml')
    pattern = re.compile(r"<p>.*?</p>")
    data = soup.select('body > script')  # 返回的是一个列表，CSS选择器
    data_list = pattern.findall(data[0].string)
    content = ''
    for item in data_list:
        item = re.sub("<.*?>", '', item)  # 将文本中关于<>中包含的字符串去掉
        content += re.sub(" ", '', item)  # 去掉空格
    print(content)
    return content


if __name__ == '__main__':
    articles = []
    url = "https://dxy.com/baike/category/24834?tag_id=25323&page_index="
    for idx in range(1, 9):
        print('开始第' + str(idx) + '页面')
        articles += articleTypeEntrance(url, str(idx))
    # 保存这些文章
    with open('../data_crawled/disease_and_dict', 'w', encoding=utf-8) as f:
        for each in articles:
            print(each)
            f.write(each + '\n')
