# coding:utf-8

"""
参考
https://www.cnblogs.com/xfxing/p/9322199.html

https://www.jianshu.com/p/1ba64df4fd15

"""

import pymysql

""" ============================ 1. 连接数据库 """
conn = pymysql.connect(
    host='10.211.55.11',
    user='root',
    password='123456',
    database='hcialias_test',
    charset='utf8'
)

""" ============================ 2. 获取游标 
1. 获取游标之后才能进行执行、提交等操作
2. 无缓冲游标类型，适用于数据量很大，一次性返回太慢，或者服务端带宽较小

查询时默认返回的数据类型为元组, 可以修改返回类型, 几种常用游标类型
    Cursor: 默认，元组类型
    DictCursor: 字典类型
    SSCursor: 无缓冲元组类型
    SSDictCursor: 无缓冲字典类型
"""
# 得到一个可以执行SQL语句游标对象, 返回元组
# cursor = conn.cursor()
# 得到一个可以执行SQL语句游标对象, 返回字典
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

""" ============================ 手动拼接好字符串直接执行 
lastrowid

# 游标. 会记录上一次获取的位置. 
# 同一个游标执行了一次fetchall, 游标已经在最后了, 再次执行的时候没有结果
fetchone    获取一条
fetchmany   获取多条
fetchall    获取全部

# 游标移动
scroll

# lastrowid
# 获取最新 insert 自增的 id ，也就是最后插入的一条数据ID，如果没有insert过，执行cursor.lastrowid会报错


"""
# 定义要执行的SQL语句
sql_1 = """SELECT * from tmp_user """
cursor.execute(sql_1)

# 获取所有行
print(cursor.fetchone())
print(cursor.fetchmany(2))
# 相对绝对位置移动
cursor.scroll(1, mode="absolute")
# 相对当前位置移动
cursor.scroll(1, mode="relative")
print(cursor.fetchall())

""" ============================ execute 自动拼接字符串 """
# %s需要去掉引号, pymysql会自动加上
# 不能使用 {}
sql_2 = """SELECT * FROM tmp_user WHERE nickname = %s AND idList = %s """
# sql_2 = """SELECT * FROM tmp_user WHERE nickname = {} AND idList = {} """
cursor.execute(sql_2, ['qwe', 24])
b = cursor.fetchall()
print(b)

cc = """select * from tmp_user where userName = %s and nickname = %s"""
cursor.execute(cc, (None, 'asd1'))
print(cursor.fetchall())

""" ============================ in 条件查询 """
# 直接传递元组包裹列表即可
# select hciName from tmp_hcimaster where hciName in ('海淀区社区卫生服务中心', '北京市海淀区妇幼保健院', '哈哈2')
name_list = ['海淀区社区卫生服务中心', '北京市海淀区妇幼保健院', '哈哈2']
sql = """ SELECT HCInAME FROM TMP_HCIMASTER WHERE HCInAME IN %s """
res = cursor.execute(sql, (name_list,))

""" ============================ executemany 
少量使用 execute, 大量使用 executemany (性能好)
"""
sql_3 = """ INSERT INTO tmp_user ( userName, passwd, nickname ) VALUES (%s, %s, %s) """
data_3 = [(None, 'aa', None), (20, None, 'bb')]
cursor.executemany(sql_3, data_3)

""" ============================ 关闭连接和游标 """
conn.commit()
# 关闭游标
cursor.close()
# 关闭数据库连接
conn.close()
