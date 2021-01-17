# -*- coding: utf-8 -*-
from find_page import *
from find_info import *
from multiprocessing import Process
import random


class RunTycCrawler(Process):
    def __init__(self, start_industry):
        self.start_industry = start_industry
        print('天眼查爬虫 起始位置：%s 启动' % str(start_industry))
        super().__init__()

    def run(self):
        refresh_proxy_ip()
        # todo_company_list = get_todo_company()
        # for todo_company_url in todo_company_list:
        #     print("开始爬取这个之前没有写的公司：", todo_company_url['id'])
        #     get_info(todo_company_url['id'], 1)
        #     time.sleep(2)

        todo_industry_list = get_todo_industry(self.start_industry)
        for todo_industry_url in todo_industry_list:
            print("开始爬取此页下的公司：", todo_industry_url['href'])
            company_url_list = get_company(todo_industry_url['href'])
            time.sleep(random.uniform(0, 2))
            for company_url in company_url_list:
                print("开始爬取此公司：", company_url)
                get_info(company_url, 1)
                time.sleep(random.uniform(0, 2))

# 只爬取 96个行业的TOP 100 企业基本信息
if __name__ == '__main__':
    jobs = []
    for i in range(0, 400, 50):
        p = RunTycCrawler(i)
        p.daemon = True  # 一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
        jobs.append(p)
        p.start()
        time.sleep(10)
    days = 7
    time.sleep(60 * 60 * 24 * days)
    print('天眼查爬虫全部启动！,预计爬%d天' % days)
