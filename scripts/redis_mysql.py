#!/usr/bin/env python
import redis
import pymysql

#连接redis
pool = redis.ConnectionPool(host='10.101.11.107', port=6379, db=3)
r = redis.Redis(connection_pool=pool)

# r.set('name', 'test')
# print(r.get('name'))



# 打开数据库连接
db = pymysql.connect(
    host="10.101.11.107",
    port=3306,
    user='suhan',
    password='shuhan',
    db='',
    charset='utf8mb4')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("show databases")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()





