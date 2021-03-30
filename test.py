"""
对爬虫当时进行测试，选取丁香医生的网站进行爬虫
"""

import requests
import json
from bs4 import BeautifulSoup
import re


# Get方式获取网页数据
url_test = 'https://dxy.com/article/5665'
# 从<html>中进行判断，如果 <html style="overflow-y: auto;">
str_html = requests.get(url_test)
# str_html是一个URL对象，代表整个网站
# str_html.text 表示网页源码
soup = BeautifulSoup(str_html.text, 'lxml')
pattern = re.compile(r"<p>.*?</p>")
# data = soup.find("script", text=pattern)
data = soup.select('body > script')  # 返回的是一个列表，CSS选择器
# 第一个数据是需要的数据
# print(data[0])
# print(data[0].string)
data_list = pattern.findall(data[0].string)
content = ''
for item in data_list:
    item = re.sub("<.*?>", '', item)  # 将文本中关于<>中包含的字符串去掉
    content += re.sub(" ", '', item)  # 去掉空格

print(content)