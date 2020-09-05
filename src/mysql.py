# -*- coding: utf-8 -*-
import pymysql

connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='dev',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)
cursor = connect.cursor()

def insert(sql, data):
    cursor.execute(sql % data)
    connect.commit()


def update_company(data):
    sql = 'update t_company set img= "%s", compCh= "%s", compEn= "%s", sscym= "%s", gsdj= "%s", zczb= "%s", ' \
          'sshy= "%s", dsz= "%s", dm= "%s", fddbr= "%s", zjl= "%s", ygrs= "%s", glryrs= "%s", kggd= "%s", sjkzr= "%s", ' \
          'zzkzr= "%s", zyyw= "%s", agdm= "%s", agjc= "%s", bgdm= "%s", bgjc= "%s", hgdm= "%s", hgjc= "%s", zqlb= "%s", ' \
          'lxdh= "%s", dzyx= "%s", cz= "%s", gswz= "%s", qy= "%s", yzbm= "%s", bgdz= "%s", zcdz= "%s", flag="%d" ' \
          'where id= "%s" '
    cursor.execute(sql % data)
    connect.commit()

def update_company_qybj(data):
    sql = 'update t_company set  fddbrr = "%s", zczb1 = "%s", sjzb1 = "%s", clrq1 = "%s", jyzt1 = "%s", ' \
          'tyshxxdm1 = "%s", gszc1 = "%s", nsrsbh1 = "%s", zzjgdm1 = "%s", gslx1 = "%s", hy1 = "%s", ' \
          'hzrq1 = "%s", djjg1 = "%s", yyqx1 = "%s", nsrzz1 = "%s", rygm1 = "%s", cbrs1 = "%s", cym1 = "%s", ' \
          'ywmc1 = "%s", zcdz1 = "%s", jyfw1 = "%s", flag="%d" ' \
          'where id= "%s" '
    cursor.execute(sql % data)
    connect.commit()


def update_company_qyjj(data):
    sql = 'update t_company set compCh= "%s", compEn= "%s", sscym= "%s", gsdj= "%s", zczb= "%s", ' \
          'sshy= "%s", dsz= "%s", dm= "%s", fddbr= "%s", zjl= "%s", ygrs= "%s", glryrs= "%s", kggd= "%s", sjkzr= "%s", ' \
          'zzkzr= "%s", zyyw= "%s" ' \
          'where id= "%s" '
    cursor.execute(sql % data)
    connect.commit()


def update_company_zqxx(data):
    sql = 'update t_company set agdm= "%s", agjc= "%s", bgdm= "%s", bgjc= "%s", hgdm= "%s", hgjc= "%s", zqlb= "%s" ' \
          'where id= "%s" '
    cursor.execute(sql % data)
    connect.commit()


def update_company_lxxx(data):
    sql = 'update t_company set lxdh= "%s", dzyx= "%s", cz= "%s", gswz= "%s", qy= "%s", yzbm= "%s", bgdz= "%s", zcdz= "%s" ' \
          'where id= "%s" '
    cursor.execute(sql % data)
    connect.commit()


def insert_company(id):
    sql = "INSERT IGNORE INTO `t_company`(`id`, `flag`) VALUES ('%s', '%d')"
    cursor.execute(sql % (id, False))
    connect.commit()


def do_industry(href):
    sql = 'update t_industry  set flag= "%d" where href = "%s"'
    cursor.execute(sql % (True, href))
    connect.commit()


def get_todo_industry():
    sql = 'select href from t_industry where flag = false'
    cursor.execute(sql)
    todo_href_list = cursor.fetchall()
    return todo_href_list
