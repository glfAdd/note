""" ============================ 参考
https://blog.csdn.net/u010898329/article/details/83064373
"""


""" ============================ 参考
1. 下载地址. 
    https://dev.mysql.com/downloads/mysql/5.7.html#downloads
    Select Operating System 选择 Linux - Generic
    Select OS Version 选择 Linux - Generic (glibc 2.12) (x86, 64-bit)
    下载后 mysql-5.7.29-linux-glibc2.12-x86_64.tar.gz 文件, 约634M


2. 解压到需要安装的位置, 重命名
    tar -zxvf mysql-5.7.29-linux-glibc2.12-x86_64 mysql3307
    mv mysql-5.7.29-linux-glibc2.12-x86_64 mysql3307
   
     
3. 进入目录文件夹 data, var, etc, log
    [root@iZ2zedkdcnxsz2pnlwuc50Z]/usr/local/mysql3307# ls                                                                                                                                                                  
    bin  data  docs  etc  include  lib  LICENSE  log  man  README  share  support-files  var


3. 创建用户和用户组, 并修改权限
    groupadd mysql
    useradd mysql -g mysql 
    chown -R mysql:mysql /usr/local/mysql3307
    chmod -R 755 /usr/local/mysql3307

4. 安装依赖包
    yum -y install make gcc-c++ cmake bison-devel ncurses ncurses-devel libaio-devel


5. 在 etc 里创建数据库配置文件 my.cnf, 写入下面内容
    [root@iZ2zedkdcnxsz2pnlwuc50Z]/usr/local/mysql3307/etc# vim my.cnf 
    
[mysqld]
basedir= /usr/local/mysql3307
datadir = /usr/local/mysql3307/data
port = 3307
socket = /usr/local/mysql3307/mysql.sock
log-error=/usr/local/mysql3307/log/error.log
log=/usr/local/mysql3307/log/mysql.log
long_query_time=2
log-slow-queries= /usr/local/mysql3307/log/slowquery.log
log-bin= /usr/local/mysql3307/log/bin.log
expire_logs_days = 15
sync_binlog = 1
local-infile=0
default-storage-engine=INNODB
 
[client]
socket = /usr/local/mysql3307/mysql.sock
 
lower_case_table_names = 1
    
    
6. 指定配置文件初始化
    [root@iZ2zedkdcnxsz2pnlwuc50Z]/usr/local/mysql3307# ./bin/mysqld --defaults-file=/usr/local/mysql3307/etc/my.cnf --initialize --user=mysql &
    得到数据库密码
    2020-04-07T06:40:34.144763Z 1 [Note] A temporary password is generated for root@localhost: xxxxxxxxxxx
    
    
7. 初始化数据库
    [root@iZ2zedkdcnxsz2pnlwuc50Z]/usr/local/mysql3307# ./bin/mysqld_safe --defaults-file=/usr/local/mysql3307/etc/my.cnf  --user=mysql &
    
    
8. 修改 mysql 启动文件. 将这三处换成自己的路径
    [root@iZ2zedkdcnxsz2pnlwuc50Z]/usr/local/mysql3307# vim support-files/mysql.server
    
    basedir=/usr/local/mysql3307                                                                                                                                                                                            
    datadir=/usr/local/mysql3307/data
    conf=/usr/local/mysql3307/my.cnf
    
    
9. 启动 mysql
    [root@iZ2zedkdcnxsz2pnlwuc50Z]/usr/local/mysql3307# /usr/local/mysql3306/bin/mysqld_safe --defaults-file=/usr/local/mysql3306/etc/my.cnf &
    [root@iZ2zedkdcnxsz2pnlwuc50Z]/usr/local/mysql3307# /usr/local/mysql3307/bin/mysqld_safe --defaults-file=/usr/local/mysql3307/etc/my.cnf &
    [root@iZ2zedkdcnxsz2pnlwuc50Z]/usr/local/mysql3307# /usr/local/mysql3308/bin/mysqld_safe --defaults-file=/usr/local/mysql3308/etc/my.cnf &
    # [root@iZ2zedkdcnxsz2pnlwuc50Z]/usr/local/mysql3307# ./support-files/mysql.server start
    
    
10. 登录数据库
    登录服务器第一个启动的数据库使用: ./bin/mysql --port=3307 -u root -p
    登录服务器后面启动的数据库使用: [root@iZ2zedkdcnxsz2pnlwuc50Z]/usr/local/mysql3307# ./bin/mysql --socket=/usr/local/mysql3307/mysql.sock --port=3307 -u root -p 
    查看数据库进程, 如果进程有--socket就加socket启动, 没有就不加
    
[root@iZ2zedkdcnxsz2pnlwuc50Z]/usr/local/mysql3308# ps -ef|grep mysql                                                                                                                                                   
root     26795     1  0 11:45 ?        00:00:00 /bin/sh /usr/local/mysql3306/bin/mysqld_safe --datadir=/usr/local/mysql3306/data --pid-file=/usr/local/mysql3306/data/iZ2zedkdcnxsz2pnlwuc50Z.pid                       
mysql    26882 26795  0 11:45 ?        00:00:06 /usr/local/mysql3306/bin/mysqld --basedir=/usr/local/mysql3306 --datadir=/usr/local/mysql3306/data --plugin-dir=/usr/local/mysql3306/lib/plugin --user=mysql --log-error=iZ2zedkdcnxsz2pnlwuc50Z.err --pid-file=/usr/local/mysql3306/data/iZ2zedkdcnxsz2pnlwuc50Z.pid                                                                                                                           
root     27351 27154  0 14:42 pts/1    00:00:00 /bin/sh ./bin/mysqld_safe --defaults-file=/usr/local/mysql3307/etc/my.cnf --user=mysql                                                                                  
mysql    27478 27351  0 14:42 pts/1    00:00:01 /usr/local/mysql3306/bin/mysqld --defaults-file=/usr/local/mysql3307/etc/my.cnf --basedir=/usr/local/mysql3307 --datadir=/usr/local/mysql3307/data --plugin-dir=/usr/local/mysql3307/lib/plugin --user=mysql --log-error=iZ2zedkdcnxsz2pnlwuc50Z.err --pid-file=iZ2zedkdcnxsz2pnlwuc50Z.pid --socket=/usr/local/mysql3307/mysql.sock --port=3307                                                
root     28294 27154  0 15:19 pts/1    00:00:00 /bin/sh ./bin/mysqld_safe --defaults-file=/usr/local/mysql3308/etc/my.cnf --user=mysql                                                                                  
mysql    28421 28294  0 15:19 pts/1    00:00:00 /usr/local/mysql3308/bin/mysqld --defaults-file=/usr/local/mysql3308/etc/my.cnf --basedir=/usr/local/mysql3308 --datadir=/usr/local/mysql3308/data --plugin-dir=/usr/local/mysql3308/lib/plugin --user=mysql --log-error=iZ2zedkdcnxsz2pnlwuc50Z.err --pid-file=iZ2zedkdcnxsz2pnlwuc50Z.pid --socket=/usr/local/mysql3308/mysql.sock --port=3308                                                
root     28535 27154  0 15:20 pts/1    00:00:00 grep --color=auto mysql
    
    
11. 停止数据库
    # mysqladmin  -u root --socket=/var/lib/mysql3307/mysql.sock --port=3307 -p shutdown
    ./support-files/mysql.server stop
    
    
12. 修改密码
    格式：mysql> set password for 用户名@localhost = password('新密码');  
    例子：mysql> set password for root@localhost = password('123');  

    
12. 远程访问
    mysql --> use mysql;
    mysql --> select host,user from user;
    mysql --> update user set host = '%' where user = 'root';
    mysql --> delete from user where host='127.0.0.1' and user = 'root';
    mysql --> flush privileges;
    
    
    
    
    
高级内容
https://blog.csdn.net/weixin_33716154/article/details/91504537
https://www.jianshu.com/p/5e29228ce897


    
    
    
    
    
    

    


    










"""
