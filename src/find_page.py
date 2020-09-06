# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from get_html import *
from mysql import *


def get_company(page_url):
    html = get_html(page_url, 0)
    soup = BeautifulSoup(html, 'html.parser')
    # print(html)

    # 页内公司href 链表
    company_href_list = []
    a_list = soup.find_all('a')
    if a_list is None or len(a_list) is 0:
        print("此页查找不到链接：", page_url)
        # print(html)
        refresh_proxy_ip()
        return get_company(page_url)
    for item in a_list:
        if 'https://www.tianyancha.com/company/' in str(item.get("href")):
            if len(str(item.get("href"))) > 36:
                insert_company(str(item.get("href")))
                company_href_list.append(str(item.get("href")))
    do_industry(page_url)
    if len(company_href_list) is 0:
        print("此页查找不到公司链接：", page_url)
        # print(html)
        refresh_proxy_ip()
        return get_company(page_url)
    print("此页一共爬取公司数: ", len(company_href_list) )
    return company_href_list



