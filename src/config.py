# -*- coding: utf-8 -*-
# 蘑菇代理 API appkey 为空代表不用代理直接爬
# appkey = ""
appkey="b40c1df059834f6a94a5ec9d0d63e501"

# mysql 数据库  配置
#具体表结构: sql/tianyancha.sql
host = 'localhost'
port = 3306
user = 'root'
passwd = '123456'
db = 'dev'
charset = 'utf8'

# 爬虫 错误处理配置
retries = 5
html_retries = 10
#爬取全部公司或者96个行业Top100的公司
craw_style="all"
# craw_style="top100"