# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

with open("test1.html", encoding="UTF-8", mode='r') as f, \
        open("industry.py", encoding="UTF-8", mode='a+') as f1:
    html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    # print(html)

    # 行业搜索
    div = soup.find('div', class_="right -scroll js-industry-container hidden search-industry")
    ins_a_list = div.find_all('a', class_="link-sub-hover-click item -right")
    for ins_a in ins_a_list:
        href = ins_a.get('href')
        ins_name = ins_a.get_text()
        f1.write(ins_name+'", "')



