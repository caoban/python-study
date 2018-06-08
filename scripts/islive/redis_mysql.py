#!/usr/bin/env python
import redis
import pymysql


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


#连接redis
pool = redis.ConnectionPool(host='10.101.11.107', port=6379, db=3)
r = redis.Redis(connection_pool=pool)
#获取所有的key
keys = r.keys()
for key in keys:
    value = r.get('ip1').decode()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()


#
# # 关闭数据库连接
# db.close()





