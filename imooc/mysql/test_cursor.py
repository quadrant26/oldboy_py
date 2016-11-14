# -*- coding:utf-8 -*-

import MySQLdb

conn = MySQLdb.Connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    passwd = "",
    db = "imooc",
    charset = "utf8"
    )

cursor = conn.cursor()

sql = "select * from user"
cursor.execute(sql)

print( cursor.rowcount)

# 获取一条数据
rs = cursor.fetchone()
print(rs)

# 获取三条数据
rs = cursor.fetchmany(3)
print(rs)

# 说去剩下的全部数据
rs = cursor.fetchall()
print(rs)

cursor.close()
conn.close()