"""

Author:ChinShall
Time:2023.11.25
Encoding:UTF-8

"""
import os
import random
import re
import sys
import time

import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/99.0.9999.999 Safari/537.36 '
}

url = input("请输入小说的第一章网址，e.g.https://m.jisuxs.cc/read/117406/19262726.html\n")

r = requests.get(url, headers=headers)
r.encoding = 'gbk'
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')
path = sys.path[0] + '/小说'
name = input("输入小说名字：")
fpath = path + '/' + name + '.txt'

text = soup.find('div', class_='nr_nr').text.replace(
    "=>>(本章未完,请点击下一页继续阅读)", ""
).replace(
    "    ", '\n'
).replace(
    "</p>", ""
)

with open(fpath, 'a', encoding='utf-8') as file:
    file.write(text)
print(text)

while True:
    # 生成随机时间
    second = random.randint(3, 10)
    # time.sleep(second)

    # 翻页
    next_page = soup.find('div', class_='nr_page').find(class_='next').find('a').get('href')
    r = requests.get(next_page, headers=headers)
    r.encoding = 'gbk'
    demo = r.text
    soup = BeautifulSoup(demo, 'html.parser')

    # 获取文本
    if soup.find(class_='cover'):
        print("结束！")
        break

    text = soup.find('div', class_='nr_nr').text.replace(
        "=>>(本章未完,请点击下一页继续阅读)", ""
    ).replace(
        '    ', '\n'
    ).replace(
        "</p>", ""
    )
    with open(fpath, 'a', encoding='utf-8') as file:
        file.write(text)
    print(text)
