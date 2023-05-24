##### 创建 django 项目

```bash
$ django-admin startproject django01
$ cd django01
$ python manage.py startapp glf
```

##### 

```
设置 setting 文件



```

##### orm 错误

```bash
django.db.utils.ProgrammingError: (1146, "Table 'test01.glf_usermodels' doesn

表不存在的意思，其实就是数据库迁移出了问题，需要重新迁移一下


# 记录对 model 所有的改动, 生成数据库版本文件
$ python manage.py makemigrations
# 执行文件更新数据库
$ python manage.py migrate


操作数据库要通过 django 操作, 不能手动删除表
如果手动删除了表, 需要删除 migrations 里面对应的文件
```



