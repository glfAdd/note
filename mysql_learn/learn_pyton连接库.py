""" ============================ 数据库返回的结果tuple转为字典
在DBUtils.PooledDB中增加
cursorclass=pymysql.cursors.DictCursor
或
cursorclass = MySQLdb.cursors.DictCursor
"""
