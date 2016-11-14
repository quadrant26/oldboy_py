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

print(conn)
print(cursor)

# 关闭连接
cursor.close()
conn.close()