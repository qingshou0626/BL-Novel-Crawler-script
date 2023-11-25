"""

Author:ChinShall
Time:2023.11.25
Encoding:UTF-8

"""
import random
import time
import requests
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/99.0.9999.999 Safari/537.36 '
}
url = 'https://www.shlwx.com/xs/47365/1.html'

r = requests.get(url, headers=headers)
r.encoding = r.apparent_encoding
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')

text = soup.find(class_='Readarea ReadAjax_content').text.replace(
    "　　请收藏本站：https://www.shlwx.com。书荒啦文学网手机版：https://m.shlwx.com", ""
).replace(
    "『点此报错』『加入书签』", ""
).replace(
    "　　", '\n'
).replace(
    "如果你喜欢“就要耽美网”一定要介绍给你的朋友哦！", ""
)
with open('saved_text.txt', 'a', encoding='utf-8') as file:
    file.write(text)
print(text)

while True:
    # 生成随机时间
    second = random.randint(3, 10)
    # time.sleep(second)

    # 翻页
    next_page = soup.find(class_='Readpage_down js_page_down').get('href')
    next_url = 'https://www.shlwx.com' + next_page
    r = requests.get(next_url, headers=headers)
    r.encoding = r.apparent_encoding
    demo = r.text
    soup = BeautifulSoup(demo, 'html.parser')

    # 获取文本
    if soup.find(class_='listmain'):
        print("结束！")
        break

    text = soup.find(class_='Readarea ReadAjax_content').text.replace(
        "　　请收藏本站：https://www.shlwx.com。书荒啦文学网手机版：https://m.shlwx.com", ""
    ).replace(
        "『点此报错』『加入书签』", ""
    ).replace(
        "　　", '\n'
    ).replace(
        "如果你喜欢“就要耽美网”一定要介绍给你的朋友哦！", ""
    )
    with open('saved_text.txt', 'a', encoding='utf-8') as file:
        file.write(text)
    print(text)
