# -*- coding: utf-8 -*-
from industry import *
from find_info import *


# 爬取 行业 -> 省份直辖市 链接
def get_page_province(industry_url):
    html = get_html(industry_url, 0)
    soup = BeautifulSoup(html, 'html.parser')

    # 行业 -> 省份直辖市
    div = soup.find('div', class_="scope-box scope-content-box")
    if div is None:
        print("此页查找不到省份内容 scope-box scope-content-box：", industry_url, "注意这个必须要查到哦哦哦哦哦哦哦！！！！！！！！！！！")
        refresh_proxy_ip()
        return get_page_province(industry_url)
    page_a_list = div.find_all('a')
    province = []
    for page_a in page_a_list:
        province_href = page_a.get('href')
        province.append(province_href[38:])
    print(province)


# 爬取 行业 -> 省份直辖市 -> 市 链接
def get_page_city(province_href):
    html = get_html(province_href, 0)
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', class_="scope-box")
    if div is None:
        print("此页查找不到市区内容 scope-box：", province_href, "注意这个必须要查到哦哦哦哦哦哦哦！！！！！！！！！！！")
        refresh_proxy_ip()
        return get_page_city(province_href)
    a_list = div.find_all('a')
    city_list = []
    for city_a in a_list:
        city_href = city_a.get('href')
        print(city_href)
        insert_industry_province_city(city_href)
        # qu_list.append(qu_href)


# 爬取 行业 -> 省份直辖市 -> 市 -> 区 链接
def get_page_qu(city_href):
    html = get_html(city_href, 0)
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', class_="scope-box")
    if div is None:
        print("此页查找不到县区内容 scope：", city_href, "注意这个必须要查到哦哦哦哦哦哦哦！！！！！！！！！！！")
        refresh_proxy_ip()
        return get_page_qu(city_href)
    a_list = div.find_all('a')
    for city_a in a_list:
        qu_href = city_a.get('href')
        # print("县区:",qu_href)
        insert_industry_province_city_qu(qu_href)
        # qu_list.append(qu_href)


# 爬取 行业 -> 省份直辖市 -> 市 -> 区 -> 分页链接
def get_page(qu_href,count):
    if count>config.retries:
        return True
    html = get_html(qu_href, 0)
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', class_=" search-pager")
    company_list_div = soup.find('div', class_="result-list sv-search-container")
    no_company_div = soup.find('div', class_="no-result-container deep-search-detail")
    # 此条件下确实没有分页信息或者公司
    if no_company_div is not None:
        return True
    # 如果没有上面的条件，说明被反爬挡住了
    if company_list_div is None:
        print("此页查找不到分页 ：", qu_href, "注意这个必须要查到哦哦哦哦哦哦哦！！！！！！！！！！！")
        refresh_proxy_ip()
        return get_page(qu_href,count+1)
    # 如果公司列表的不为空，而分页为空，说明只有这一页
    if div is None:
        insert_industry_province_city_qu_page(qu_href)
        return True
    a_list = div.find_all('a')
    page_list = []
    page_count = 0
    for page_a in a_list:
        if page_count > 4:
            break
        page_count += 1
        page_href = page_a.get('href')
        print("分页:",page_href)
        insert_industry_province_city_qu_page(page_href)
        # qu_list.append(qu_href)


def get_page_company(page_url,count):
    if count>config.retries:
        return True
    html = get_html(page_url, 0)
    soup = BeautifulSoup(html, 'html.parser')
    # print(html)

    # 页内公司href 链表
    company_href_list = []
    company_list_div = soup.find('div', class_="result-list sv-search-container")
    no_company_div = soup.find('div', class_="no-result-container deep-search-detail")
    # 此条件下确实没有分页信息或者公司
    if no_company_div is not None:
        return True
    # 如果没有上面的条件，说明被反爬挡住了
    if company_list_div is None:
        print("此页查找不到公司列表：", page_url, "注意这个必须要查到哦哦哦哦哦哦哦！！！！！！！！！！！")
        # return True
        refresh_proxy_ip()
        return get_page_company(page_url,count+1)
    a_list = company_list_div.find_all('a')

    if a_list is not None:
        for item in a_list:
            if 'https://www.tianyancha.com/company/' in str(item.get("href")):
                if len(str(item.get("href"))) > 36:
                    insert_company(str(item.get("href")))
                    company_href_list.append(str(item.get("href")))
    print("此页一共爬取公司数: ", len(company_href_list))


# 爬取 行业 + 省份直辖市 -> 市 所有的链接 存到mysql
def get_city_to_mysql():
    refresh_proxy_ip()
    # 行业
    for industry_href in industry_href_list:
        for province_str in province_list:
            # 行业 -> 省份直辖市
            province_href = industry_href + province_str
            # 行业 -> 省份直辖市 -> 市
            get_page_city(province_href)


# 爬取 行业 -> 省份直辖市 -> 区 所有的链接 存到mysql
def get_qu_to_mysql():
    todo_city_list = get_todo_industry_province_city()
    for todo_city_url in todo_city_list:
        print("开始爬取未爬的城市：", todo_city_url['href'])
        get_page_qu(todo_city_url['href'])
        do_industry_province_city(todo_city_url['href'])


# 爬取 行业 -> 省份/直辖市 -> 市 ->区县 -> 所有分页 所有的链接 存到mysql
def get_page_to_mysql():
    todo_url_list = get_todo_industry_province_city_qu()
    while len(todo_url_list) > 0:
        for todo_url in todo_url_list:
            print("开始爬取未爬的区县：", todo_url['href'])
            get_page(todo_url['href'],1)
            do_industry_province_city_qu(todo_url['href'])
        todo_url_list = get_todo_industry_province_city_qu()


# 爬取 行业 -> 省份直辖市 -> 市区 -> 所有分页 -> 公司下 所有的链接 存到mysql
def get_company_to_mysql():
    todo_page_list = get_todo_industry_province_city_qu_page()
    while len(todo_page_list) > 0:
        for todo_url in todo_page_list:
            print("开始爬取未爬的分页：", todo_url['href'])
            get_page_company(todo_url['href'],1)
            do_industry_province_city_qu_page(todo_url['href'])
        todo_page_list = get_todo_industry_province_city_qu_page()


# 爬取 行业 -> 省份直辖市 -> 市区 -> 所有分页 -> 公司 -> 公司背景等信息 存到mysql
def get_company_info_to_mysql():
    todo_company_list = get_todo_company_limit()
    while len(todo_company_list) > 0:
        for todo_url in todo_company_list:
            print("开始爬取未爬的公司：", todo_url['id'])
            get_info(todo_url['id'], 1)
        todo_company_list = get_todo_company_limit()


if __name__ == '__main__':
    # 一步 一步  爬取所有天眼查所有公司，极其变态
    # 把数据库表建好，然后跑这个程序，下面五个可以分五条线程 按先后顺序启动 即可
    # get_city_to_mysql()     # 爬取行业-》省份  url
    # get_qu_to_mysql()       # 爬取行业-》省份-》市  -》区  url

    # 以上已经完成并存云数据库，不必重复爬取

    # get_page_to_mysql()  # 爬取行业-》省份-》市 -》区-》分页  url
    # get_company_to_mysql()  # 爬取行业-》省份-》市 -》区-》分页->公司列表  url
    get_company_info_to_mysql()   # 爬取公司信息  url
