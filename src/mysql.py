# -*- coding: utf-8 -*-
import pymysql
import config
import time

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


def get_todo_industry(start,limit_step):
    sql = 'select href from t_industry where flag = false limit '+str(start)+','+str(limit_step)
    cursor.execute(sql)
    todo_href_list = cursor.fetchall()
    return todo_href_list


def get_todo_company():
    sql = 'select id from t_company where flag = false limit 0,100'
    cursor.execute(sql)
    todo_href_list = cursor.fetchall()
    return todo_href_list


def get_todo_company(start,num):
    sql = 'select id from t_company where flag = false limit '+str(start)+','+str(num)
    cursor.execute(sql)
    todo_href_list = cursor.fetchall()
    return todo_href_list

def get_todo_company_limit():
    sql = 'select id from t_company where flag = false limit 100'
    cursor.execute(sql)
    todo_href_list = cursor.fetchall()
    return todo_href_list

def get_company_task():
    sql1 = 'SET @hrefs := 0;  '
    sql2 = 'UPDATE t_company SET flag = 1, id = (SELECT @hrefs := id)WHERE flag  = 0  LIMIT 1;'
    sql3= 'SELECT @hrefs;'
    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)
    todo_href_list = cursor.fetchall()
    connect.commit()
    return todo_href_list
    # todo_href_list = cursor.fetchall()


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

def get_qu():
    sql = "select * FROM t_industry_province_city where href like '%oc01%areaCode%'"
    # sql = "SELECT * FROM t_industry_province_city_qu_copy where href like  '%oc01?%'"
    cursor.execute(sql)
    todo_href_list = cursor.fetchall()
    return todo_href_list


def timer(func):
    def decor(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        d_time = end_time - start_time
        print("the running time is : ", d_time)

    return decor


@timer
def save_to_mysql():
    qu_list = get_qu()
    print(len(qu_list))
    for ii in range(1, 96):
        i = str(ii)
        if ii<10:
            i='0'+i
        print("#####################################################"+i)
        data = []
        sql = "INSERT IGNORE INTO `t_industry_province_city_qu`(`href`) VALUES ('%s')"
        for qu in qu_list:
            href =qu['href'].replace("oc01","oc"+i)
            data.append((href))

            sql = "INSERT IGNORE INTO `t_industry_province_city_qu`(`href`,`flag`) VALUES ('%s','%d')"
            print(sql%(href, False))
            # cursor.execute(sql%(href, False))
        # cursor.executemany(sql, data)
        # connect.commit()

        print('OK')


@timer
def save_to_file():
    qu_list = get_qu()
    print(len(qu_list))
    with open("qu_list1.csv", encoding="UTF-8", mode='w') as f:
        for ii in range(1, 96):
            i = str(ii)
            if ii<10:
                i='0'+i
            print("#####################################################"+i)
            # data = []
            for qu in qu_list:
                # print(qu['href'])
                href =qu['href'].replace("oc01","oc"+i)
                f.write('"%s","%d"'%(href, 0)+"\n")

# save_to_mysql()
# insert_industry_province_city_qu("ssssss")

# print(get_company_task())