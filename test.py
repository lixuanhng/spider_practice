"""
数据处理
"""

import requests
import json
# from bs4 import BeautifulSoup
import re
import os


def punctuation_transform_en_to_zh(refresh_text):
    """
    标点符号转化
    """
    # 处理英文句号
    targets_1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                 '一', '二', '三', '四', '五', '六', '七', '八', '九', '十',
                 ')', '）', '>', ']']
    p1 = re.compile('.(?=\\.)')  # 找到英文句号并取其前一位
    match_1 = re.findall(p1, refresh_text)
    if match_1:
        for item in match_1:
            if item not in targets_1:
                refresh_text = re.sub(item + '.', item + '。', refresh_text)  # 非特殊用途需要替换
    # 处理英文逗号
    targets_2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    p2 = re.compile('.(?=,)')  # 找到英文逗号并取其前一位
    match_2 = re.findall(p2, refresh_text)
    if match_2:
        for item in match_2:
            if item not in targets_2:
                refresh_text = re.sub(item + ',', item + '，', refresh_text)  # 非特殊用途需要替换
    # 处理英文问号
    refresh_text = re.sub('\\?', '？', refresh_text)
    # 处理英文小括号
    refresh_text = re.sub('\\(', '（', refresh_text)
    refresh_text = re.sub('\\)', '）', refresh_text)
    # 处理英文冒号
    refresh_text = re.sub(':', '：', refresh_text)
    # 处理英文分号
    refresh_text = re.sub(';', '；', refresh_text)
    return refresh_text


if __name__ == '__main__':
    all_sentences = []
    for root, dirs, files in os.walk("../data_crawled", topdown=False):
        for name in files:
            if '0406' in name:
                with open(os.path.join(root, name), 'r', encoding='utf-8') as f:
                    type_p = f.readlines()
                    for article in type_p:
                        article = article.strip('\n')
                        article = re.sub(r"\r", '', article)
                        article = re.sub(r"\n", '', article)
                        sign = r"。|！｜？"
                        sentences = re.split(sign, article)
                        for sen in sentences:
                            if '图片来源' not in sen and '公众号' not in sen and sen and len(sen)>20:
                                # sen = punctuation_transform_en_to_zh(sen)
                                all_sentences.append(sen)

    print("共有 {} 个句子".format(len(all_sentences)))

    with open('./sentence_inputs_0406.txt', 'w', encoding='utf-8') as sf:
        for sen in all_sentences:
            sf.write(sen + '\n')