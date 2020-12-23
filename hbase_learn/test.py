"""
https://blog.csdn.net/xc_zhou/article/details/80868332

https://zhuanlan.zhihu.com/p/145551967





图形管理工具
https://github.com/Observe-secretly/HbaseGUI/wiki
https://github.com/Observe-secretly/HbaseGUI/wiki/Release-history
https://support.huaweicloud.com/usermanual-cloudtable/cloudtable_01_0080.html

hbase-thrift 和  happybase
"""

"""
happybase

https://cloud.tencent.com/developer/article/1406584  **** 
https://www.cnblogs.com/yanwuliu/p/10695892.html
"""
import happybase

pool = happybase.ConnectionPool(
    size=3,
    host='172.18.0.13',
    # 表的命名空间
    # table_prefix='test_1',
)
with pool.connection() as connection:
    print(connection.tables())


def create_table():
    """创建表"""
    # cf1、cf2、cf3 三个列族
    families = {
        'cf1': dict(max_versions=10),
        'cf2': dict(max_versions=1, block_cache_enabled=False),
        'cf3': dict(),
    }
    connection.create_table('student', families)  # 如果连接时，有传递表前缀参数时，真实表名将会是："{}_{}".format(table_prefix,name)
    # connection.open()
    connection.close()


def delete_table():
    """删除表
    disable_table()
    enable_table()
    is_table_enabled()
    tables()                 # 获取表的list
    """
    # disable：是否先禁用表
    connection.delete_table('student', disable=True)


def get_table_inf():
    # 获取表实例
    # 两个方法返回的对象相同
    # user_prefix：是否使用表前缀，默认为True
    table_1 = connection.table('student', use_prefix=True)
    table_2 = happybase.Table('test_1_student', connection)
    print('-------------------- 获取所有列族信息 ')
    print(table_1.families())
    print('-------------------- 此表的区域服务器信息 ')
    print(table_1.regions())


def get_row():
    table_1 = connection.table('student', use_prefix=True)
    # 获取单元格数据
    # row：行
    # column：列
    # versions：获取的最大版本数量，默认None，即获取所有
    # timestamp：时间戳，默认None，即获取所有时间戳版本的数据。可指定一个时间戳，获取小于此时间戳版本的所有数据
    # include_timestamp：是否返回时间戳，默认False
    cells_1 = table_1.cells('row2', 'cf1:2', include_timestamp=True)
    print(cells_1)
    # 获取前3个版本
    cells_2 = table_1.cells('row2', 'cf1', versions=3)
    print(cells_2)

    # 获取一行数据
    # row：行
    # columns: 列，默认为None，即获取所有列，可传入一个list或tuple来指定获取列
    # timestamp：时间戳。默认为None，即返回最大的那个时间戳的数据。可传入一个时间戳来获取小于此时间戳的最大时间戳的版本数据
    # include_timestamp：是否返回时间戳数据，默认为False
    row = table_1.row('row1', columns=None, timestamp=None, include_timestamp=False)
    row = table_1.row('row1', columns=['cf1'])
    row = table_1.row('row1', columns=['cf1:name', 'cf1:age'])
    row = table_1.row('row1', timestamp=1489070666)
    print(row)
    rows = table_1.rows(['row1', 'row2'])
    print(rows)
    # 转为字典
    print(dict(rows))

    # 删除数据
    with table_1.batch() as bat:
        bat.delete('row1')

    print('-------------------- 扫描表 ')
    # 扫描表, 返回一个generator
    # row_start：起始行，默认None，即第一行，可传入行号指定从哪一行开始
    # row_stop：结束行，默认None，即最后一行，可传入行号指定到哪一行结束(不获取此行数据)
    # row_prefix：行号前缀，默认为None，即不指定前缀扫描，可传入前缀来扫描符合此前缀的行
    # columns：列，默认为None，即获取所有列，可传入一个list或tuple来指定获取列
    # filter：过滤字符串
    # timestamp：时间戳。默认为None，即返回最大的那个时间戳的数据。可传入一个时间戳来获取小于此时间戳的最大时间戳的版本数据
    # include_timestamp：是否返回时间戳数据，默认为False
    # batch_size：用于检索结果的批量大小
    # scan_batching：服务端扫描批处理
    # limit：数量
    # sorted_columns：是否返回排序的列(根据行名称排序)
    # reverse：是否执行反向扫描
    # for key, value in table_1.scan(row_start='1',row_stop='5'):
    for key, value in table_1.scan():
        print(key)
        print(value)


def insert_row():
    table_1 = connection.table('student', use_prefix=True)
    # 插入数据, 无返回值, 使用put一次只能存储一行数据, 如果row key已经存在，则变成修改数据, 立刻发送
    # row: 行
    # data: 数据，dict类型，{列: 值}
    # 构成，列与值皆为str类型
    # timestamp：时间戳，默认None，即写入当前时间戳
    # wal：是否写入wal，默认为True
    table_1.put('row1', {'cf1:1': 'aaa'})

    # 批量插入
    bat = table_1.batch()
    bat.put('row1', {'cf2:name': '批量写入1', 'cf2:age': '1001', 'cf2:long': '101.12'})
    bat.put('row1', {'cf2:name': '批量写入2', 'cf2:age': '1002', 'cf2:long': '102.12'})
    bat.send()

    # 不用手动发送数据调用 bat.send()
    # batch将数据保存在内存中, 数据量大占用内存大, 可以设置大小
    with table_1.batch(batch_size=3) as bat:
        for i in range(5):
            bat.put('row{}'.format(i), {'cf2:name': 'name2', 'cf2:age': str(i + 100), 'cf2:long': 'long2'})


def delete():
    table_1 = connection.table('student', use_prefix=True)
    # 删除整行
    table_1.delete('row1')
    # 删除一个列族的数据
    table_1.delete('row1', columns=['cf1'])
    # 删除一个列族中几个列的数据
    # table_1.delete('row1', columns=['cf1：name', 'cf1:age'])


if __name__ == '__main__':
    pass
    # create_table()
    # delete_table()
    # get_table_inf()
    # insert_row()
    # delete()
    get_row()
