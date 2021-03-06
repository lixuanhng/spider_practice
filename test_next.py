import requests
import json
from bs4 import BeautifulSoup
import re
import time
"""
如果报错信息如下：
data_list = pattern.findall(data[0].string)
IndexError: list index out of range
则说明爬虫
"""


def articleTypeEntrance(url_tmp, cnt, save_path):
    """
    确定需要爬取的页面
    :param url_tmp:
    :param cnt:
    :return:
    """
    time.sleep(20)  # 添加时间间隔
    str_html = requests.get(url_tmp)
    soup = BeautifulSoup(str_html.text, 'lxml')
    # 将结果转为字符串
    try:
        data = soup.select('body > script')[0].string
    except Exception as e:
        print('请求结果为：')
        print(sin_html)
    data = data.split('data=')[1]
    data_dict = json.loads(data)
    # 收集所有文本
    for item in data_dict['feedList']['items']:
        if 'video' not in item.keys():  # 如果文章的组织形式是视频，那么忽略
            requireArticle(str(item['object_id']), save_path)
            cnt += 1
            print("  完成第 {} 篇文章抓取".format(str(cnt)))
        else:
            continue
    return cnt


def requireArticle(object_id, save_path):
    """
    返回一篇文章的全文
    :param object_id:
    :return:
    """
    time.sleep(20)
    url_comb = 'https://dxy.com/article/' + object_id
    sin_html = requests.get(url_comb)
    soup = BeautifulSoup(sin_html.text, 'lxml')
    pattern = re.compile(r"<p>.*?</p>")
    data = soup.select('body > script')  # 返回的是一个列表，CSS选择器
    try:
        data_list = pattern.findall(data[0].string)
        content = ''
        for item in data_list:
            item = re.sub("<.*?>", '', item)  # 将文本中关于<>中包含的字符串去掉
            item = re.sub(r"\r", '', item)
            item = re.sub(r"\n", '', item)
            content += re.sub(" ", '', item)  # 去掉空格
        # 前提是content是存在的
        if content:
            split_key = ['丁香园', '该文章', '原创']
            for item in split_key:
                if item in content:
                    content = content.split(item)[0]
                    break
            print('\t\t' + content)

            with open(save_path, 'a', encoding='utf-8') as f:
                f.write(content + '\n')
    except Exception as e:
        print('请求结果为：')
        print(sin_html)
        print(data)


if __name__ == '__main__':
    articles = []
    article_num = 0

    """
    4/1
    # 膳食指南-疾病饮食-9页-35文章-art_diet_diseaseDiet.txt
    url = "https://dxy.com/baike/category/24834?tag_id=25323" 
    
    # 膳食指南-豆及豆制品-2页-10文章-art_diet_toufu.txt
    url = "https://dxy.com/baike/category/24834?tag_id=25326"
    
    # 膳食指南-坚果零食-3页-18文章-art_diet_nut.txt
    url = "https://dxy.com/baike/category/24834?tag_id=24911"
    
    # 膳食指南-孕期饮食-6页-30文章-art_diet_pregnancy.txt
    url = "https://dxy.com/baike/category/24834?tag_id=23192"
    
    # 膳食指南-宝宝辅食-5页-10文章-art_diet_baby.txt
    url = "https://dxy.com/baike/category/24834?tag_id=25322"
    
    # 膳食指南-吃得好-9页-30文章-art_diet_health.txt
    url = "https://dxy.com/baike/category/24834?tag_id=25339"
    
    # 膳食指南-主食粗粮-8页-35文章-art_diet_mainFood.txt
    url = "https://dxy.com/baike/category/24834?tag_id=25325"
    
    # 膳食指南-奶及奶制品-5页-10文章-art_diet_milk.txt
    url = "https://dxy.com/baike/category/24834?tag_id=25327"
    
    # 膳食指南-蛋及蛋制品-3页-10文章-art_diet_egg.txt
    url = "https://dxy.com/baike/category/24834?tag_id=25328"
    
    
    # 膳食指南-微量/常量元素-7页-10文章-art_diet_nutrient.txt
    url = "https://dxy.com/baike/category/24834?tag_id=25331"
    
    4/6
    # 膳食指南-食品安全-4页-27文章-art_diet_food_safety_0406.txt
    url = https://dxy.com/baike/category/24834?tag_id=25332
    
    # 膳食指南-海鲜-5页-15文章-art_diet_seafood_0406.txt
    url = https://dxy.com/baike/category/24834?tag_id=24199
    
    # 膳食指南-外卖夜宵-2页-14文章-art_diet_takeout_0406.txt
    url = https://dxy.com/baike/category/24834?tag_id=25335
    
    # 膳食指南-甜品-3页-15文章-art_diet_dessert_0406.txt
    url = https://dxy.com/baike/category/24834?tag_id=22395
    
    # 膳食指南-养生饮食-2页-19文章-art_diet_liveLong_0406.txt
    url = https://dxy.com/baike/category/24834?tag_id=25334
    
    # 膳食指南-肉类-5页-26文章-art_diet_meat_0406.txt
    url = https://dxy.com/baike/category/24834?tag_id=25337
    
    # 膳食指南-蔬菜-8页-45文章-art_diet_vegatable_0406.txt
    url = https://dxy.com/baike/category/24834?tag_id=22511
    
    # 膳食指南-调味品-8页-14文章-art_diet_condiment_0406.txt
    url = https://dxy.com/baike/category/24834?tag_id=22940
    
    # 膳食指南-饮品-8页-10文章-art_diet_drink_0406.txt
    url = https://dxy.com/baike/category/24834?tag_id=25330
    
    # 膳食指南-水果-9页-10文章-art_diet_fruit_0406.txt
    url = https://dxy.com/baike/category/24834?tag_id=22259
    
    # 保健品-所有类型-art_health_care_0406.txt
    url = https://dxy.com/baike/category/24839?tag_id=25204--燕窝-4
    url = https://dxy.com/baike/category/24839?tag_id=23917--人参-2
    url = https://dxy.com/baike/category/24839?tag_id=25197--阿胶-1
    url = https://dxy.com/baike/category/24839?tag_id=25207--酵素-2
    url = https://dxy.com/baike/category/24839?tag_id=25201--蛋白粉-1
    url = https://dxy.com/baike/category/24839?tag_id=25205--灵芝-1
    url = https://dxy.com/baike/category/24839?tag_id=23213--虫草-2
    url = https://dxy.com/baike/category/24839?tag_id=24629--铁皮石斛-1
    url = https://dxy.com/baike/category/24839?tag_id=25198--纳豆-1
    url = https://dxy.com/baike/category/24839?tag_id=25199--玛卡-1
    url = https://dxy.com/baike/category/24839?tag_id=25200--松花粉-1
    url = https://dxy.com/baike/category/24839?tag_id=25203--松茸-1
    """

    # 建立新的爬虫，需要修改如下3个变量
    url = "https://dxy.com/baike/category/24839?tag_id=25203"
    max_page = 1
    path = '../data_crawled/art_health_care_0406.txt'

    for idx in range(1, max_page+1):
        print('开始第 {} 页面抓取'.format(str(idx)))
        count = 0
        if idx == 1:
            url_index = url
        else:
            url_index = url + "&page_index=" + str(idx)
        article_num += articleTypeEntrance(url_index, count, path)

    print('\n' + "共获取 {} 篇文章".format(str(article_num)))