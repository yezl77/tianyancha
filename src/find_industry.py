# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from mysql import *

# 先把要爬数据
# 清空行业表
clear_industry()
with open("../html/industry_list.html", encoding="UTF-8", mode='r') as f, \
        open("industry2.py", encoding="UTF-8", mode='a+') as f1:
    html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    # print(html)

    # 行业搜索
    div = soup.find('div', class_="right -scroll js-industry-container hidden search-industry")
    ins_a_list = div.find_all('a', class_="link-sub-hover-click item -right")
    for ins_a in ins_a_list:
        href = ins_a.get('href')
        ins_name = ins_a.get_text()
        for p in ["", "/p2", "/p3", "/p4", "/p5"]:
            data = (ins_name, href + p, False)
            insert_industry(data)
        # f1.write(href+"\n")



