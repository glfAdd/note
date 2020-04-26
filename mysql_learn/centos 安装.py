""" ============================ yum
https://www.cnblogs.com/luohanguo/p/9045391.html


wget -i -c http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm
yum -y install mysql57-community-release-el7-10.noarch.rpm
yum -y install mysql-community-server

systemctl start  mysqld.service
systemctl status mysqld.service
grep "password" /var/log/mysqld.log
2020-04-03T11:41:31.358793Z 1 [Note] A temporary password is generated for root@localhost: 0bt_%+,1ieuE


mysql -uroot -p
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new password';





"""


