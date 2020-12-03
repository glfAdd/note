""" ============================ 安装
1. wget http://repo.mysql.com/mysql-apt-config_0.8.13-1_all.deb
2. apt-get install ./mysql-apt-config_0.8.13-1_all.deb
3. 都选择 OK
4. apt-get update
5. apt-get install mysql-server
6. 密码选择第一个

123456
"""

""" ============================ 命令
service mysql start
service mysql stop
service mysql restart
"""

""" ============================ 配置用户和权限
登录
mysql -u root -p

创建用户 (%表示 可以远程登录该数据库)
create user '用户名'@'%' identified by '密码';

赋予root账号对所有据库的所有权限
GRANT ALL PRIVILEGES ON *.* TO '用户名'@'%';

刷新权限
FLUSH PRIVILEGES;

修改ip
vim /etc/mysql/mysql.conf.d/mysqlld.cnf
- bind-address    = 127.0.0.1
+ bind-address    = 0.0.0.0 
"""

""" ============================ 基本配置 
检查debian服务器防火墙状态
iptables -L -n

添加端口
iptables -A INPUT -p tcp --dport 3306 -j ACCEPT

保存 重启
iptables-save > /etc/iptables.up.rules
/etc/init.d/ssh restart

删除端口就删除这个文件里的内容
"""

""" ============================ 导入sql文件
mysql -h localhost -u root -p hcialias_test < /document/tmp_area.sql
mysql -h localhost -u root -p hcialias_test < /document/*.sql
"""
