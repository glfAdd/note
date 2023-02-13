https://blog.csdn.net/LYLLOAD/article/details/81664322

##### 文档

```
一个Flask拓展, 简化了Flask使用SQLAlchemy操作. 

Flask-SQLAlchemy 
http://www.pythondoc.com/flask-sqlalchemy/api.html#flask.ext.sqlalchemy.SQLAlchemy
http://www.pythondoc.com/flask-sqlalchemy/quickstart.html
```

##### 安装

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple flask-sqlalchemy
```

##### 数据库URL

| 引擎     | URL                                              |
| -------- | ------------------------------------------------ |
| MySQL    | mysql://username:passwork@hostname/database      |
| Postgres | postgresql://username:password@hostname/database |

##### 配置

| 选项                      | 说明                                                         |
| ------------------------- | ------------------------------------------------------------ |
| SQLALCHEMY_DATABASE_URI   | 用于连接的数据库 URI 。 mysql://username:password@server/db  |
| SQLALCHEMY_BINDS          | 一个映射 binds 到连接 URI 的字典。更多 binds 的信息见 用 Binds 操作多个数据库 。 |
| SQLALCHEMY_ECHO           | 如果设置为 Ture ， SQLAlchemy 会记录所有 发给 stderr 的语句，这对调试有用。Flask可以降低内存 |
| SQLALCHEMY_RECORD_QUERIES | 可以用于显式地禁用或启用查询记录。查询记录 在调试或测试模式自动启用。更多信息见 get_debug_queries() 。 |
| SQLALCHEMY_NATIVE_UNICODE | 可以用于显式禁用原生 unicode 支持。当使用 不合适的指定无编码的数据库默认值时，这对于 一些数据库适配器是必须的（比如 Ubuntu 上某些版本的 PostgreSQL ）。 |
| SQLALCHEMY_POOL_SIZE      | 数据库连接池的大小。默认是引擎默认值（通常 是 5 ）           |
| SQLALCHEMY_POOL_TIMEOUT   | 设定连接池的连接超时时间。默认是 10 。                       |
| SQLALCHEMY_POOL_RECYCLE   | 多少秒后自动回收连接。这对 MySQL 是必要的， 它默认移除闲置多于 8 小时的连接。注意如果 使用了 MySQL ， Flask-SQLALchemy 自动设定这个值为 2 小时 |

##### 属性

|     类型     |       python       | 说明                                                  |
| :----------: | :----------------: | ----------------------------------------------------- |
|   Integer    |        int         | 普通整数，一般是 32 位                                |
| SmallInteger |        int         | 取值范围小的整数，一般是 16 位                        |
| Big Integer  |    int 或 long     | 不限制精度的整数                                      |
|    Float     |       float        | 浮点数                                                |
|   Numeric    |  decimal.Decimal   | 定点数                                                |
|    String    |        str         | 变长字符串                                            |
|     Text     |        str         | 变长字符串，对较长或不限长度的字符串做了优化          |
|   Unicode    |      unicode       | 变长 Unicode 字符串                                   |
| Unicode Text |      unicode       | 变长 Unicode 字符串，对较长或不限长度的字符串做了优化 |
|   Boolean    |        bool        | 布尔值                                                |
|     Date     |   datetime.date    | 日期                                                  |
|     Time     |   datetime.time    | 时间                                                  |
|   DateTime   | datetime.datetime  | 日期和时间                                            |
|   Interval   | datetime.timedelta | 时间间隔                                              |
|     Enum     |        str         | 一组字符串                                            |
|  PickleType  |  任何 Python 对象  | 自动使用 Pickle 序列化                                |
| LargeBinary  |        str         | 二进制文件                                            |

#####列选项

|    选项     | 说明                                                         |
| :---------: | ------------------------------------------------------------ |
| primary_key | 如果设为 True，这列就是表的主键                              |
|   unique    | 如果设为 True，这列不允许出现重复的值                        |
|    index    | 如果设为 True，为这列创建索引，提升查询效率                  |
|  nullable   | 如果设为 True，这列允许使用空值；如果设为 False，这列不允许使用空值 |
|   default   | 默认值                                                       |

##### relationship 关系选项

|     选项      | 说明                                                         |
| :-----------: | ------------------------------------------------------------ |
|    backref    | 在关系的另一个模型中添加反向引用                             |
|  primaryjoin  | 明确指定两个模型之间使用的联结条件。只在模棱两可的关系中需要指定. |
|     lazy      | 指定如何加载相关记录。可选值如下 :                           |
|               | select（首次访问时按需加载）                                 |
|               | immediate（源对象加载后就加载）                              |
|               | joined（加载记录，但使用联结）                               |
|               | subquery（立即加载，但使用子查询）                           |
|               | noload（永不加载）                                           |
|               | dynamic（不加载记录，但提供加载记录的查询）                  |
|    uselist    | 如果设为 Fales，不使用列表，而使用标量值                     |
|   order_by    | 指定关系中记录的排序方式                                     |
|   secondary   | 指定多对多关系中关系表的名字                                 |
| secondaryjoin | SQLAlchemy 无法自行决定时，指定多对多关系中的二级联结条件    |

##### 外键约束

```python
db.ForeignKey
```





```





```





























