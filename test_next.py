import requests
import json
from bs4 import BeautifulSoup
import re

url_test = 'https://dxy.com/baike/category/24834?tag_id=25323'
str_html = requests.get(url_test)
# print(str_html.text)
pattern = re.compile(r"<p>.*?</p>")


soup = BeautifulSoup(str_html.text, 'lxml')
# print(soup)
print('-' * 100)

data = soup.select('body > script')[0]  # 返回的是一个列表，CSS选择器
print(data)
print(type(data))
print('-' * 100)


# data_0 = soup.select('#container > div > div.layout-content.baike-category > div.base-content.left-content > div.baike-category-feed')
# data_1 = soup.select('#container > div > div.layout-content.baike-category > div.base-content.left-content > div.baike-category-feed > div:nth-child(1) > div > div.article-card-body > a')
# data_2 = soup.select('#container > div > div.layout-content.baike-category > div.base-content.left-content > div.baike-category-feed > div:nth-child(2) > div > div.article-card-body > a')
# data_3 = soup.select('#container > div > div.layout-content.baike-category > div.base-content.left-content > div.baike-category-feed > div:nth-child(3) > div > div.article-card-body > a')

# print(data_0)
# test_str = "<div class="baike-category-feed-item">"
# print(re.findall("\[test_str\].*?", data_0))
# print(data_1)
# print(data_2)
# print(data_3)