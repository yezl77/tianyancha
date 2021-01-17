# tianyancha
天眼查爬取企业信息-企业信用信息查询系统-天眼查爬虫

运行main.py即可爬取90%的天眼查公司

运行test_main.py只爬取96个行业的前100家公司

代理IP请自费或自力更生建免费IP池

正式爬取前请自行搭建好mysql 数据库 和 表
配置信息在 config.py里 修改为你的数据库和蘑菇代理appkey即可

跑test.main ， main 之前需要跑一次 find_industry.py这个脚本：把96个行业*5页的行业记录初始化好。

