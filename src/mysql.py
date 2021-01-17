# -*- coding: utf-8 -*-
import pymysql
import config

connect = pymysql.Connect(
    host=config.host,
    port=config.port,
    user=config.user,
    passwd=config.passwd,
    db=config.db,
    charset=config.charset,
    cursorclass=pymysql.cursors.DictCursor
)
cursor = connect.cursor()


def insert(sql, data):
    cursor.execute(sql % data)
    connect.commit()


def excute(sql, data):
    data_list = list(data)
    for i in range(len(data_list)):
        data_list[i] = data_list[i].replace('\'', "\\'")
    data = tuple(data_list)
    sqldata = sql % data
    # print(sqldata)
    # print(sqldata)
    # escape_string_sql = pymysql.escape_string(sqldata)
    # print(escape_string_sql)
    # cursor.execute(escape_string_sql % data)
    cursor.execute(sqldata)

    connect.commit()


def update_company(data):
    sql = "update t_company set img= '%s', compCh= '%s', compEn= '%s', sscym= '%s', gsdj= '%s', zczb= '%s', " \
          "sshy= '%s', dsz= '%s', dm= '%s', fddbr= '%s', zjl= '%s', ygrs= '%s', glryrs= '%s', kggd= '%s', sjkzr= '%s', " \
          "zzkzr= '%s', zyyw= '%s', agdm= '%s', agjc= '%s', bgdm= '%s', bgjc= '%s', hgdm= '%s', hgjc= '%s', zqlb= '%s', " \
          "lxdh= '%s', dzyx= '%s', cz= '%s', gswz= '%s', qy= '%s', yzbm= '%s', bgdz= '%s', zcdz= '%s', flag='%d' " \
          "where id= '%s' "
    excute(sql, data)


def update_company_qybj(data):
    sql = "update t_company set compCh= '%s', fddbrr = '%s', zczb1 = '%s', sjzb1 = '%s', clrq1 = '%s', jyzt1 = '%s', " \
          "tyshxxdm1 = '%s', gszc1 = '%s', nsrsbh1 = '%s', zzjgdm1 = '%s', gslx1 = '%s', hy1 = '%s', " \
          "hzrq1 = '%s', djjg1 = '%s', yyqx1 = '%s', nsrzz1 = '%s', rygm1 = '%s', cbrs1 = '%s', cym1 = '%s', " \
          "ywmc1 = '%s', zcdz1 = '%s', jyfw1 = '%s', flag= true  " \
          "where id= '%s' "
    excute(sql, data)


def update_company_qyjj(data):
    sql = "update t_company set compCh= '%s', compEn= '%s', sscym= '%s', gsdj= '%s', zczb= '%s', " \
          "sshy= '%s', dsz= '%s', dm= '%s', fddbr= '%s', zjl= '%s', ygrs= '%s', glryrs= '%s', kggd= '%s', sjkzr= '%s', " \
          "zzkzr= '%s', zyyw= '%s', flag = true " \
          "where id= '%s' "
    excute(sql, data)


def update_company_zqxx(data):
    sql = "update t_company set agdm= '%s', agjc= '%s', bgdm= '%s', bgjc= '%s', hgdm= '%s', hgjc= '%s', zqlb= '%s', flag = true " \
          "where id= '%s' "
    excute(sql, data)


def update_company_lxxx(data):
    sql = "update t_company set lxdh= '%s', dzyx= '%s', cz= '%s', gswz= '%s', qy= '%s', yzbm= '%s', bgdz= '%s', zcdz= '%s', flag = true " \
          "where id= '%s' "
    excute(sql, data)


def insert_company(id):
    sql = "INSERT IGNORE INTO `t_company`(`id`, `flag`) VALUES ('%s', '%d')"
    cursor.execute(sql % (id, False))
    connect.commit()


def do_industry(href):
    sql = 'update t_industry  set flag= "%d" where href = "%s"'
    cursor.execute(sql % (True, href))
    connect.commit()


def clear_industry():
    sql = "truncate table t_industry_copy1"
    cursor.execute(sql)
    connect.commit()

def insert_industry(data):
    sql = "insert  t_industry (`industry`,`href`,`flag`)  VALUES ('%s', '%s', '%d')"
    cursor.execute(sql % data)
    connect.commit()


def get_todo_industry(start):
    sql = 'select href from t_industry where flag = false limit '+str(start)+',50'
    cursor.execute(sql)
    todo_href_list = cursor.fetchall()
    return todo_href_list


def get_todo_company():
    sql = 'select id from t_company where flag = false limit 0,100'
    cursor.execute(sql)
    todo_href_list = cursor.fetchall()
    return todo_href_list


def get_todo_company_limit():
    sql = 'select id from t_company where flag = false limit 300,100'
    cursor.execute(sql)
    todo_href_list = cursor.fetchall()
    return todo_href_list


def insert_industry_province(href):
    sql = "INSERT IGNORE INTO `t_industry_province`(`href`, `flag`) VALUES ('%s', '%d')"
    cursor.execute(sql % (href, False))
    connect.commit()


def insert_industry_province_city(href):
    sql = "INSERT IGNORE INTO `t_industry_province_city`(`href`, `flag`) VALUES ('%s', '%d')"
    cursor.execute(sql % (href, False))
    connect.commit()


def insert_industry_province_city_qu(href):
    sql = "INSERT IGNORE INTO `t_industry_province_city_qu`(`href`, `flag`) VALUES ('%s', '%d')"
    cursor.execute(sql % (href, False))
    connect.commit()


def insert_industry_province_city_qu_page(href):
    sql = "INSERT IGNORE INTO `t_industry_province_city_qu_page`(`href`, `flag`) VALUES ('%s', '%d')"
    cursor.execute(sql % (href, False))
    connect.commit()


def get_todo_industry_province_city():
    sql = 'select href from t_industry_province_city where flag = false limit 100'
    cursor.execute(sql)
    todo_href_list = cursor.fetchall()
    return todo_href_list


def do_industry_province_city(href):
    sql = 'update t_industry_province_city  set flag= true where href = "%s"' % href
    cursor.execute(sql)
    connect.commit()


def get_todo_industry_province_city_qu():
    sql = 'select href from t_industry_province_city_qu where flag = false limit 100'
    cursor.execute(sql)
    todo_href_list = cursor.fetchall()
    return todo_href_list


def do_industry_province_city_qu(href):
    sql = 'update t_industry_province_city_qu  set flag= true where href = "%s"' % href
    cursor.execute(sql)
    connect.commit()


def get_todo_industry_province_city_qu_page():
    sql = 'select href from t_industry_province_city_qu_page where flag = false limit 100'
    cursor.execute(sql)
    todo_href_list = cursor.fetchall()
    return todo_href_list


def do_industry_province_city_qu_page(href):
    sql = 'update t_industry_province_city_qu_page  set flag= true where href = "%s"' % href
    cursor.execute(sql)
    connect.commit()
