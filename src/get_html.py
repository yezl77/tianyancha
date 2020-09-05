# -*- coding: utf-8 -*-
import requests
import time

cursor = 0
get_proxy_url = "代理IP获取写自己的"
proxy_id = ""


# 请求url的html内容
def get_html(url):
    time.sleep(3)
    print(proxy_id)
    # 代理 IP ,具体刷新获取代理IP需要自己实现下面的refresh_proxy_ip() 函数
    proxy = {
        'http': 'http://'+proxy_id,
        'https': 'https://'+proxy_id
    }
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Host": "www.tianyancha.com",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }
    try:
        # response = requests.get(url, headers=headers, proxies=proxy)
        response = requests.get(url,headers=headers, proxies=proxy, timeout=10)
    except BaseException:
        print("异常发生")
        # 这里没有对异常情况作具体处理，只是直接换代理IP 重新请求 就完事昂
        refresh_proxy_ip()
        return get_html(url)

    if response.status_code is not 200:
        print("不正常")
        refresh_proxy_ip()
        return get_html(url)
    else:
        return response.text


def refresh_proxy_ip():
    global proxy_id
    time.sleep(1)
    proxy_id = requests.get(get_proxy_url).text.replace(" ", "")
    print('代理ip请求异常，更换代理IP:http://' + proxy_id + "/")





# # print(response.text)
# with open("z_company4.html", encoding="UTF-8", mode='w') as f:
#     response =get_html('https://www.tianyancha.com/company/1744525522')
#     f.write(response)
# list = get_todo_industry()
# get_html('https://www.tianyancha.com/company/2321098091')