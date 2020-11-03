# -*- coding: utf-8 -*-

import MySQLdb
from DBUtils.PooledDB import PooledDB

config = {
    'host': 'rm-2ze72hfw6y2v2s1xiio.mysql.rds.aliyuncs.com',
    "user": 'ndc_test_all_user',
    "passwd": 'ndc123456--',
    "db": 'ndc_test',
    "port": 3306,
    "charset": 'utf8'
}


class Mdb(object):
    db_pool_hci = PooledDB(
        creator=MySQLdb,
        mincached=5,
        maxcached=5,
        host=config.get('host'),
        user=config.get('user'),
        password=config.get('passwd'),
        port=config.get('port'),
        db=config.get('db'),
        charset='utf8mb4'
    )

    def __init__(self):
        self.conn = self.db_pool_hci.connection()
        self.cursor = self.conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

    def close_connection(self):
        """
        关闭连接
        """
        self.conn.close()
        self.cursor.close()

    def execute(self, sql, *args):
        """
        执行语句
        :param sql: string 语句
        :param args: list 参数 ['', '']
        :return: list
        """
        self.cursor.execute(sql, *args)
        return self.cursor.fetchall()

    def executemany(self, sql, *args):
        """
        批量执行语句
        :param sql: 语句
        :param args: 参数 [(), ()]
        :return: list
        """
        self.cursor.executemany(sql, *args)
        return self.cursor.fetchall()

    def commit(self):
        """
        提交事务
        """
        self.conn.commit()

    def rollback(self):
        """
        回滚
        """
        self.conn.rollback()
        self.cursor.close()
        self.conn.close()
