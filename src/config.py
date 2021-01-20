# -*- coding: utf-8 -*-
# 蘑菇代理 API appkey 为空代表不用代理直接爬
# appkey = ""
api_tyle="get_ip_al"
appkey="a9d22f04b55e42d2a94afe2dfb1e431b"

# mysql 数据库  配置
#建表见具体表结构: sql/tianyancha.sql
#另外，在这里提出一个倡议，就是避免大家重复爬取，我建了一个云数据库，这样大家只要连接这个数据库，就可以一起爬取信息，分享信息。
host = 'rm-bp1y79633ms121d2j4o.mysql.rds.aliyuncs.com'
port = 3306
user = 'crawer'
passwd = 'crawer123'
db = 'db_tyc'
charset = 'utf8mb4'

# host = 'localhost'
# port = 3306
# user = 'root'
# passwd = '123456'
# db = 'dev'
# charset = 'utf8'


# 爬虫 错误处理配置
# 爬取一个页面被反爬 的换代理IP重试次数
retries = 3
# 爬取一个页面请求异常 的换代理IP重试次数
html_retries = 5
# 爬取一个页面超时时间 （秒）
request_timeout = 10
