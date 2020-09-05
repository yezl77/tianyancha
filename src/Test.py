# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 18:09:44 2018
@author: 白马非马
"""

# !/usr/bin/env python
# -*- coding:utf-8 -*-
# 需要事先安装selenium和plantom.js，不适合大量爬虫，速度太慢，这里只爬取所有行业的第一页20个公司
# 注意需要少量人工值守，当代理IP意外在4个行业以内超时崩掉时。需要手动关闭，可能不关闭代理IP会自动好转，但基本不可能
from selenium import webdriver
import time
from bs4 import BeautifulSoup  # 网页代码解析器
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
import json
import urllib.request

ipurl = "http://piping.mogumiao.com/proxy/api/get_ip_al?appKey=6d22aed70f7d0479cbce55dff726a8d8a&count=1&expiryDate=5&format=1"
# 代理IP获取API


# mysql数据库驱动信息
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='1234',
    db='user',
    charset='utf8'
)


# 获取代理IP
def getip_port():
    req = urllib.request.Request(ipurl)
    data = urllib.request.urlopen(req).read()
    # loads:把json转换为dict
    s1 = json.loads(data)
    # print (s1["msg"][0]["ip"] )
    # print (s1["msg"][0]["port"] )
    ipstrs = s1["msg"][0]["ip"] + ":" + s1["msg"][0]["port"]
    print("代理IP:" + ipstrs)
    return ipstrs


# 创建浏览器驱动
def driver_open():
    # dcap = dict(DesiredCapabilities.PHANTOMJS)
    # dcap["phantomjs.page.settings.userAgent"] = (
    # "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
    # )
    # driver = webdriver.PhantomJS(executable_path='phantomjs.exe', desired_capabilities=dcap)

    proxy = Proxy(
        {
            'proxyType': ProxyType.MANUAL,
            'httpProxy': getip_port()  # 代理ip和端口
        }
    )
    desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
    desired_capabilities = dict(DesiredCapabilities.PHANTOMJS)
    desired_capabilities["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
    )
    # 把代理ip加入到技能中
    proxy.add_to_capabilities(desired_capabilities)
    driver = webdriver.PhantomJS(
        executable_path='phantomjs.exe',
        desired_capabilities=desired_capabilities
    )
    return driver


# 获取网页内容
def get_content(driver, url):
    driver.get(url)
    # 等待5秒，更据动态网页加载耗时自定义
    # sleeptime=random.randint(2,3)
    time.sleep(1)
    content = driver.page_source.encode('utf-8')
    # driver.close()
    soup = BeautifulSoup(content, 'lxml')
    # print(soup)
    return soup


# 解析网页内容，爬虫筛选不完善，不匹配所有网页，
# 天眼查4分之三的网页可正常解析，时间为2018-2-27
# 有爬虫大神可对此进行改进，期待谢谢
def get_basic_info(soup, instr):
    # com=soup.find_all("span")
    # print(com[6])

    company = soup.find(attrs={'class': 'f18 in-block vertival-middle sec-c2'}).text
    fddbr = soup.find(attrs={'class': 'f18 overflow-width sec-c3'}).text
    # fddbr=soup.find_all("a")
    baseinfo = soup.find_all(attrs={'class': 'baseinfo-module-content-value'})
    zczb = baseinfo[0].text
    zt = baseinfo[2].text
    zcrq = baseinfo[1].text

    foundAllTd = soup.find_all("td");
    # print len(basics)

    # jyfw = soup.find(attrs={'class':'js-full-container hidden'}).text
    print(u'公司名称：' + company)
    print(u'法定代表人：' + fddbr)
    print(u'注册资本：' + zczb)

    print(u'公司状态：' + zt)
    print(u'注册日期：' + zcrq)

    # 根据网页td标签粗略识别网页类型，
    # 有两种，一种大公司，报表内容较为多，td标签数大致为800到1000
    # 小公司基本在500以下
    # 少量公司td标签数在中间，无法很好识别，数量不多，影响不大，时间：2018-2-26
    if len(foundAllTd) > 600:
        """

        print (u'员工人数：'+foundAllTd[50].text)
        print (u'行业：'+foundAllTd[527].text)
        print (u'企业类型：'+foundAllTd[523].text)

        #print (u'工商注册号：'+foundAllTd[517].text)
        print( u'组织机构代码：'+foundAllTd[519].text)
        print (u'营业期限：'+foundAllTd[529].text)
        print( u'登记机构：'+foundAllTd[533].text)
        print (u'核准日期：'+foundAllTd[531].text)
        print( u'统一社会信用代码：'+foundAllTd[521].text)
        print (u'注册地址：'+foundAllTd[537].text)
        print (u'经营范围：'+foundAllTd[539].text)
        """
        sql = "INSERT INTO company (instr,company_name,industry,business_scope,type_enterprise,regist_capital,legal_represent,regist_date,company_status,operat_period,registrat_body,approval_date,address,people_num) VALUES ( '%s','%s','%s', '%s', '%s', '%s', '%s',  '%s', '%s', '%s', '%s', '%s', '%s', '%s' )"
        data = (instr, company, foundAllTd[527].text, foundAllTd[539].text, foundAllTd[523].text, zczb, fddbr, zcrq, zt,
                foundAllTd[529].text, foundAllTd[533].text, foundAllTd[531].text, foundAllTd[537].text,
                foundAllTd[49].text)

    else:
        """
        print (u'行业：'+foundAllTd[18].text)
        #print (u'工商注册号：'+foundAllTd[8].text)
        print (u'企业类型：'+foundAllTd[14].text)
        print( u'组织机构代码：'+foundAllTd[10].text)
        print (u'营业期限：'+foundAllTd[20].text)
        print( u'登记机构：'+foundAllTd[24].text)
        print (u'核准日期：'+foundAllTd[22].text)
        print( u'统一社会信用代码：'+foundAllTd[16].text)
        print (u'注册地址：'+foundAllTd[28].text)
        print (u'经营范围：'+foundAllTd[30].text)
        """
        sql = "INSERT INTO company (instr,company_name,industry,business_scope,type_enterprise,regist_capital,legal_represent,regist_date,company_status,operat_period,registrat_body,approval_date,address) VALUES ( '%s','%s', '%s', '%s', '%s', '%s',  '%s', '%s', '%s', '%s', '%s', '%s', '%s' )"
        data = (instr, company, foundAllTd[18].text, foundAllTd[30].text, foundAllTd[14].text, zczb, fddbr, zcrq, zt,
                foundAllTd[20].text, foundAllTd[24].text, foundAllTd[22].text, foundAllTd[28].text)

    # 插入数据

    cursor.execute(sql % data)
    connect.commit()
    # print('成功插入', cursor.rowcount, '条数据')


# 获取高管信息，已失效，对代码运行没有影响
def get_gg_info(soup):
    ggpersons = soup.find_all(attrs={"event-name": "company-detail-staff"})
    ggnames = soup.select('table.staff-table > tbody > tr > td.ng-scope > span.ng-binding')
    # print(len(gg))
    for i in range(len(ggpersons)):
        ggperson = ggpersons[i].text
        ggname = ggnames[i].text
        print(ggperson + " " + ggname)


# 获取信息，已失效，对代码运行没有影响
def get_gd_info(soup):
    tzfs = soup.find_all(attrs={"event-name": "company-detail-investment"})
    for i in range(len(tzfs)):
        tzf_split = tzfs[i].text.replace("\n", "").split()
        tzf = ' '.join(tzf_split)
        print(tzf)


# 获取信息，已失效，对代码运行没有影响
def get_tz_info(soup):
    btzs = soup.select('a.query_name')
    for i in range(len(btzs)):
        btz_name = btzs[i].select('span')[0].text
        print(btz_name)


# 在首页获取行业链接
def get_industry(soup):
    # print(soup.find(attrs={'class':'industry_container js-industry-container'}))
    # hangye = soup.find(attrs={'class':'industry_container js-industry-container'}).find_all("a")
    x = []
    buyao = 70  # 开始爬数据时删掉
    hangye = soup.find_all('a')
    for item in hangye:
        if 'https://www.tianyancha.com/search/oc' in str(item.get("href")):
            print(item.get("href"))
            if buyao > 0:
                buyao -= 1
            else:
                x.append(str(item.get("href")))
    print("行业数")
    print(len(x))
    return x;


# 获取行业下公司链接
def get_industry_company(soup):
    y = []
    companylist = soup.find_all('a')
    for item in companylist:
        if 'https://www.tianyancha.com/company/' in str(item.get("href")):
            print(item.get("href"))
            y.append(str(item.get("href")))
    return y


if __name__ == '__main__':
    # cursor = connect.cursor()  # 连接数据库

    companycount = 0  # 爬取的公司数
    instrcount = 0  # 爬取的行业数，每4个行业换一个代理IP,每个行业爬取第一页20个
    theinscount = 0  # 需要爬取的行业标签数，每4个行业换一个代理IP,每个行业爬取第一页20个

    driver = driver_open()
    url = "https://www.tianyancha.com/"
    soup = get_content(driver, url)
    instrlist = get_industry(soup)
    theinscount = len(instrlist)
    print

    for instr in instrlist:  # 遍历行业链接
        instrcount += 1
        print(instrcount)
        print(instr)
        compsoup = get_content(driver, instr)
        complist = get_industry_company(compsoup)
        for comp in complist:  # 遍历行业下公司链接
            print(comp)
            companycount += 1
            # print(num)
            print("行业数爬了" + str(instrcount))

            try:
                infosoup = get_content(driver, comp)
                print('----获取基础信息----')
                get_basic_info(infosoup, instr)
            except:
                print('异常跳过', end=' ')

        if instrcount % 4 == 0:  # 每3个行业链接换一个代理IP,防止网页封禁代理IP,
            # 有时会出问题，代理IP超时之类，遇到此类情况关掉程序，或者关掉plantomjs
            print("换IP")
            # driver.close()#关闭驱动 ,可能会有多个plantomjs窗口，需要常关
            driver = driver_open()
            # try:
            #    get_basic_info(soup,instr)
            # except:
            #    print('异常跳过', end=' ')
        # print()

    cursor.close()
    connect.close()  # 关闭数据库链接