# -*- coding: utf-8 -*-
from find_page import *
from find_info import *
from multiprocessing import Process
import random


# 正常爬取主进程
class RunTycCrawler(Process):
    def __init__(self, start_industry, limit_step):
        self.start_industry = start_industry
        self.limit_step = limit_step
        print('天眼查爬虫 起始位置：%s 启动' % str(start_industry))
        super().__init__()

    def run(self):
        refresh_proxy_ip()
        todo_industry_list = get_todo_industry(self.start_industry, self.limit_step)
        for todo_industry_url in todo_industry_list:
            print("开始爬取此页下的公司：", todo_industry_url['href'])
            company_url_list = get_company(todo_industry_url['href'])
            time.sleep(random.uniform(0, 2))
            for company_url in company_url_list:
                print("开始爬取此公司：", company_url)
                get_info(company_url, 1)
                time.sleep(random.uniform(0, 2))


# 对爬取异常失败进行补救
class RunTycCrawler_Undo(Process):
    def __init__(self, start_industry, limit_step):
        self.start_industry = start_industry
        self.limit_step = limit_step
        print('天眼查爬虫 爬取异常失败进行补救 启动%d：' % self.start_industry)
        super().__init__()
        pass

    def run(self):
        refresh_proxy_ip()

        todo_company_list = get_todo_company(self.start_industry, self.limit_step)
        for todo_company_url in todo_company_list:
            print("开始补救爬取异常失败公司%d：" % self.start_industry, todo_company_url['id'])
            get_info(todo_company_url['id'], 1)
            time.sleep(random.uniform(1, 2))


# 只爬取 96个行业的TOP 100 企业基本信息
if __name__ == '__main__':
    jobs = []
    step = 10
    step_1 = 100

    # for i in range(0, 800, step_1):
    #     p = RunTycCrawler_Undo(i,step_1)
    #     p.daemon = True  # 一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
    #     jobs.append(p)
    #
    # for i in range(0, 30, step):
    #     p = RunTycCrawler(i,step)
    #     p.daemon = True  # 一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
    #     jobs.append(p)

    p = RunTycCrawler_Undo(0, 100)
    p.daemon = True  # 一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
    jobs.append(p)
    #
    # p = RunTycCrawler(0,100)
    # p.daemon = True  # 一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
    # jobs.append(p)

    for p in jobs:
        p.start()
        time.sleep(10)

    days = 7
    time.sleep(60 * 60 * 24 * days)
    print('天眼查爬虫全部启动！,预计爬%d天' % days)
