""" ============================ 用户操作
# 查看MYSQL数据库中所有用户
mysql> SELECT DISTINCT CONCAT('User: ''',user,'''@''',host,''';') AS query FROM mysql.user;

# 查看数据库中具体某个用户的权限
mysql> show grants for 'cactiuser'@'%';
mysql> select * from mysql.user where user='cactiuser' \G

# 查看user表结构　需要具体的项可结合表结构来查询
mysql> desc mysql.user;

# 删除用户
drop user zhangsan@'%';



"""