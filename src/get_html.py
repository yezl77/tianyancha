# -*- coding: utf-8 -*-
import requests
import time
import config

cursor = 0

get_proxy_url = "http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=%s&count=5&expiryDate=0&format=2&newLine=1"%config.appkey
proxy_id_list = []
proxy_id = ""
proxy_page = 0

free_ip = "https://ip.jiangxianli.com/api/proxy_ip"

free_ips = "https://ip.jiangxianli.com/api/proxy_ips?page="

appKey = "ZnltYmhhTFp6WEs5UEw1aDp3VUVwOW1BRmh0em56ejRu"

# 蘑菇隧道代理服务器地址
ip_port = 'secondtransfer.moguproxy.com:9001'

#蘑菇代理: API 方式请求url的html内容
def get_html(url, count):
    if count > config.html_retries:
        print("重试超过%d次：建议停机检查：" % config.html_retries, url)
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
        if len(config.appkey) is 0:
            response = requests.get(url, headers=headers)
        else:
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


# # 通过隧道代理 爬取
# def get_html(url, count):
#     if count > 5:
#         print("重试超过5次：建议停机检查：", url)
#         return ""
#     print("爬取此网页：", url, "次数：", count, " 代理IP：", proxy_id)
#
#     proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
#
#     headers = {
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
#         "Cache-Control": "max-age=0",
#         "Connection": "keep-alive",
#         "Host": "www.tianyancha.com",
#         "Sec-Fetch-Dest": "document",
#         "Sec-Fetch-Mode": "navigate",
#         "Sec-Fetch-Site": "none",
#         "Sec-Fetch-User": "?1",
#         "Upgrade-Insecure-Requests": "1",
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
#         "Proxy-Authorization": 'Basic ' + appKey,
#     }
#     try:
#         # response = requests.get(url, headers=headers)
#         requests.packages.urllib3.disable_warnings()
#         response = requests.get(url, headers=headers, proxies=proxy, timeout=5, verify=False, allow_redirects=False)
#     except BaseException:
#         print("异常发生")
#         return get_html(url, count + 1)
#
#     if response.status_code is not 200:
#         print("不正常")
#         return get_html(url, count + 1)
#     else:
#         print(response.text)
#         return response.text

def refresh_proxy_ip():
    print('代理ip请求异常，重新请求')
    global proxy_id
    global proxy_id_list
    if len(proxy_id_list) < 1:
        response_text = requests.get(get_proxy_url).text
        while "3001" in str(response_text):
            print("ip 池获取频率太快")
            time.sleep(3)
            response_text = requests.get(get_proxy_url).text
        for p_id in response_text.split(" "):
            proxy_id_list.append(p_id)

    proxy_id = proxy_id_list.pop(0)
    # proxy_id = requests.get(get_proxy_url).text.replace(" ", "")
    print('代理ip请求异常，更换代理IP:http://' + proxy_id + "/")




def refresh_proxy_ip_free():
    global proxy_id
    global proxy_id_list
    if len(proxy_id_list) < 15:
        for d in get_free_proxy():
            proxy_id_list.append(d["ip"]+":"+d["port"])
        time.sleep(1)
    proxy_id = proxy_id_list.pop(0)
    print('代理ip请求异常，更换代理IP:http://' + proxy_id + "/")


def get_free_proxy():
    global proxy_page
    proxy_page = proxy_page + 1
    if proxy_page > 8:
        proxy_page = 1
    response = requests.get(free_ips + str(proxy_page)).json()
    print('代理ip请求返回', response["msg"])
    if response["code"] is 0:
        data = response["data"]["data"]
        page = response["data"]["current_page"]
        print("当前代理页为", page)
        return data



# # print(response.text)
# with open("company_list.html", encoding="UTF-8", mode='w') as f:
#     response =get_html('https://www.tianyancha.com/search/oc01/p1', 0)
#     f.write(response)
# list = get_todo_industry()
# get_html('https://www.tianyancha.com/company/2321098091')
# refresh_proxy_ip()
# print(get_proxy_url)
# print(len(config.appkey) is 0)

# 调试代码：
# with open("company_list.html", encoding="UTF-8", mode='w') as f:
#     response =get_html('https://www.tianyancha.com/search/oc01/p1', 0)
#     f.write(response)