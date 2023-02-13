""" ============================ 数据库连接池
数据库连接池
https://www.jianshu.com/p/43f8cae2aea8

高频度高并发的数据库访问提供更好的性能，可以自动管理连接对象的创建和释放。并允许对非线程安全的数据库接口进行线程安全包装

PersistentDB：提供线程专用的数据库连接，并自动管理连接。
PooledDB：提供线程间可共享的数据库连接，并自动管理连接。
实测证明 PersistentDB 的速度是最高的，但是在某些特殊情况下，数据库的连接过程可能异常缓慢，而此时的PooledDB则可以提供相对来说平均连接时间比较短的管理方式。
另外，实际使用的数据库驱动也有所依赖，比如SQLite数据库只能使用PersistentDB作连接池
"""

import PyMySQL
from DBUtils.PooledDB import PooledDB

""" ============================ PooledDB
dbapi           数据库接口
mincached       启动时开启的空连接数量
maxcached       连接池最大可用连接数量
maxshared       连接池最大可共享连接数量
maxconnections  最大允许连接数量
blocking        达到最大数量时是否阻塞
maxusage        单个连接最大复用次数
setsession      用于传递到数据库的准备会话，如 [”set name UTF-8″] 。
"""
pool = PooledDB(PyMySQL, 5, host='localhost', user='root', passwd='pwd', db='myDB', port=3306)  # 5为连接池里的最少连接数

# 以后每次需要数据库连接就是用connection（）函数获取连接就好了
conn = pool.connection()
cur = conn.cursor()
SQL = "select * from table1"
r = cur.execute(SQL)
r = cur.fetchall()
# 关闭连接
cur.close()
conn.close()
