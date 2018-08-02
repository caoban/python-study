import pymysql

#创建连接

conn = pymysql.connect(host='10.101.9.11', port=3306, user='root',passwd='suhna', db='111')

#创建游标
cursor = conn.cursor()

#执行sql，并返回影响行数

effect_row = cursor.execute("select * from student")
#打印一条
print(cursor.fetchone())
print(cursor.fetchone())
print("-----------")
#获取所有。但是上面已经获取过了，不会再获取了
# 跟读文件一样的，游标已经过了
print(cursor.fetchall())



#批量插入多个数据
data = [
    ("N1","2018-08-02","M"),
    ("N1","2018-08-02","M"),
    ("N1","2018-08-02","M"),
]
#批量插入多个数据。默认是开启事务的，所以需要提交下
cursor.executemany("insert into student (name,register_date,gender) values(%s,%s,%s)" ,data)
#提交.才能生效
conn.commit()
















