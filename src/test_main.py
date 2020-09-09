# -*- coding: utf-8 -*-
from find_page import *
from find_info import *


if __name__ == '__main__':
    refresh_proxy_ip()
    # todo_company_list = get_todo_company()
    # for todo_company_url in todo_company_list:
    #     print("开始爬取这个之前没有写的公司：", todo_company_url['id'])
    #     get_info(todo_company_url['id'], 1)
    todo_industry_list = get_todo_industry()
    for todo_industry_url in todo_industry_list:
        print("开始爬取此页下的公司：", todo_industry_url['href'])
        company_url_list = get_company(todo_industry_url['href'])
        for company_url in company_url_list:
            print("开始爬取此公司：", company_url)
            get_info(company_url, 1)
