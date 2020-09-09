# -*- coding: utf-8 -*-
import requests
import time

cursor = 0
get_proxy_url = "http://piping.mogumiao.com/proxy/api/get_ip_al?appKey=a35eb4a35d654c09a7a75ca397715c7e&count=10&expiryDate=0&format=2&newLine=1"
proxy_id_list = []
proxy_id = ""

free_ip = "https://ip.jiangxianli.com/api/proxy_ip"


# 请求url的html内容
def get_html(url, count):
    if count > 5:
        print("重试超过5次：建议停机检查：", url)
        return ""
        # exit(1)
    # time.sleep(1)
    print("爬取此网页：", url, "次数：", count, " 代理IP：", proxy_id)
    # 代理 IP ,具体刷新获取代理IP需要自己实现下面的refresh_proxy_ip() 函数
    proxy = {
        'http': 'http://' + proxy_id,
        'https': 'https://' + proxy_id
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
        response = requests.get(url, headers=headers, proxies=proxy, timeout=5)
    except BaseException:
        print("异常发生")
        # 这里没有对异常情况作具体处理，只是直接换代理IP 重新请求 就完事昂
        refresh_proxy_ip()
        return get_html(url, count + 1)

    if response.status_code is not 200:
        print("不正常")
        refresh_proxy_ip()
        return get_html(url, count + 1)
    else:
        return response.text


# def refresh_proxy_ip():
#     global proxy_id
#     global proxy_id_list
#     if len(proxy_id_list) < 5:
#         for p_id in requests.get(get_proxy_url).text.split(" "):
#             proxy_id_list.append(p_id)
#         time.sleep(1)
#     proxy_id = proxy_id_list.pop(0)
#     # proxy_id = requests.get(get_proxy_url).text.replace(" ", "")
#     print('代理ip请求异常，更换代理IP:http://' + proxy_id + "/")


def refresh_proxy_ip():
    global proxy_id
    global proxy_id_list
    time.sleep(1)
    requests.get(free_ip)
    proxy_id = proxy_id_list.pop(0)
    # proxy_id = requests.get(get_proxy_url).text.replace(" ", "")
    print('代理ip请求异常，更换代理IP:http://' + proxy_id + "/")


def get_html2(url):
    appKey = "ZzhrWkg3cmFKQ1lrZTlJQjpBckJwTmw0N2R3c2FaQWc4"

    # 蘑菇隧道代理服务器地址
    ip_port = 'secondtransfer.moguproxy.com:9001'

    proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
    headers = {
        "Proxy-Authorization": 'Basic ' + appKey,
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4"}
    r = requests.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
    print(r.status_code)
    print(r.content)
    if r.status_code == 302 or r.status_code == 301:
        loc = r.headers['Location']
        print(loc)
        url_f = loc
        r = requests.get(url_f, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
        print(r.status_code)
        print(r.text)

# # print(response.text)
# with open("z_company4.html", encoding="UTF-8", mode='w') as f:
#     response =get_html('https://www.tianyancha.com/company/1744525522', 0 )
#     f.write(response)
# list = get_todo_industry()
# get_html('https://www.tianyancha.com/company/2321098091')
