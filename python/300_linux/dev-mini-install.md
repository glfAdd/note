# 新的

```bash
$ yum install epel-release
$ yum update -y
$ yum makecache
$ yum install vim git tree wget htop supervisor redis nginx net-tools zsh gcc lvm2 libcurl-devel glibc-devel lrzsz ncurses-devel gdbm-devel libffi-devel krb5-devel glibc zlib-devel bzip2-devel readline-devel gcc-c++ bzip2 tcpdump sqlite-devel openssl-devel keyutils-libs-devel postgresql-devel yum-utils libinput-devel mesa-libgbm-devel libfm  sg3_utils libevent libinput-devel mesa-libgbm-devel libfm  sg3_utils libevent

bison
```

##### python 3.7.10

> 项目编译时 python 版本必须用 3.7.10, python3.pc 文件必须和 python 版本对应
>
> python3-devel 安装时时 3.6.8 和 python 版本不匹配, 不能用

```bash
$ cd Python-3.7.10
$ ./configure --enable-optimizations
$ make
$ make install
```

```bash
$ python3 -m pip install virtualenv
```

```
$ mv /usr/bin/python /usr/bin/python2.7.0                  
$ ln -s /usr/self/Python3.5.2/bin/python3 /usr/bin/python  #把系统默认python命令改成python3
```

##### 关闭 selinux

```bash
将 /etc/selinux/config
SELINUX=enforcing
改为
SELINUX=disabled
$ setenforce 0
可通过 getenforce 查看 selinux 状态
```

##### 关防火墙

```bash
$ systemctl stop firewalld
$ systemctl disable firewalld
```



```bash
go1.19.1
jdk-11.0.12
redis 开机启动
nginx 开机启动
docker 开机启动

$ systemctl enable redis
$ systemctl enable nginx
```

# 旧的

##### 依赖库

```bash
$ yum reinstall openssh-server openssh
$ yum install epel-release
$ yum install dnf
$ yum update -y
$ yum install epel-release
$ yum install vim git tree wget htop supervisor redis nginx net-tools zsh
$ yum install gcc lvm2 libcurl-devel glibc-devel lrzsz ncurses-devel gdbm-devel libffi-devel krb5-devel glibc zlib-devel bzip2-devel readline-devel gcc-c++ bzip2 tcpdump sqlite-devel openssl-devel keyutils-libs-devel


$ yum install postgresql11-contrib postgresql11-llvmjit postgresql11-odbc postgresql11-plperl postgresql11-pltcl postgresql11-tcl postgresql11 postgresql11-libs postgresql11-libs
$ yum install postgresql-devel postgresql postgresql-libs
```

```
yum list libpq*
yum list postgresql11*
```

##### 系统python升级到 3.7.1

```
可以不升级, 用 pyenv 安装虚拟环境, 将 pgkconfig 的环境变量指向 python3.pc 路径也可以
```

##### pipeline

```
sh /sdwan/script/run-pipelinedb.sh start
```

##### pgkconfig 文件指定

##### 编译成功

```
Compiling './zk_log/zk_log.py'...
Compiling './zk_log/zk_statistics_format.py'...
make[1]: Leaving directory `/root/source/Aquila/build/py-service'
make[1]: Entering directory `/root/source/Aquila/build/oem'
make[2]: Entering directory `/root/source/Aquila/build/oem/qianxin'
make[2]: Nothing to be done for `all'.
make[2]: Leaving directory `/root/source/Aquila/build/oem/qianxin'
make[2]: Entering directory `/root/source/Aquila/build/oem/report_webui'
make[2]: Nothing to be done for `all'.
make[2]: Leaving directory `/root/source/Aquila/build/oem/report_webui'
make[1]: Leaving directory `/root/source/Aquila/build/oem'
[root@CTL build]# 
```

##### pg

```
PGPASSWORD
export PGPASSWORD='sdwan#2018'
export ROOTDIR="/media/data"


psql -U  postgres -p 5432 -h 127.0.0.1


先 init 再 check
```

```
check 失败


BINDIR=$(/usr/local/pipelinedb/bin/pg_config --bindir)


yum 安装的 pg 覆盖了以前的路径, 做一次软连接
ln -s /usr/lib/pipelinedb/bin/pg_isready /usr/bin/pg_isready



init 命令不再使用了
```



##### vmware 扩容

> 成功 https://www.cnblogs.com/friendwang1001/p/15725732.html

> 记录下面的命令
>
> https://blog.csdn.net/monkeyzh123/article/details/117779216
>
> https://blog.csdn.net/lc1183759671/article/details/125601925

```
在创建之后, 用 t 设置格式的时候, 要扩展什么类型, 新建的就选则什么类型


/dev/sda1   *        2048     2099199     1048576   83  Linux
/dev/sda2         2099200    48250879    23075840   8e  Linux LVM
/dev/sda3        48250880   629145599   290447360   8e  Linux LVM
/dev/sda4       629145600   692060159    31457280   83  Linux

扩展 sda1 就创建 Linux 类型
扩展 sda2 就创建 Linux LVM 类型
否则出错




扩展文件系统时
先查看文件系统格式 (这里查看的是 /dev/mapper/centos-root 的)
	cat /etc/fstab | grep centos-root
	
如果是 xfs 用 
	xfs_growfs /dev/mapper/centos-root
如果是 ext2 ext3 ext4 文件系统用
	resize2fs /dev/mapper/centos-root

```

# 新项 clone 项目

##### cfg.json 文件

```
执行 
/sdwan/script/prepare.sh 生成 /sdwan/py-service/public_config/cfg.json 文件
将这个文件拷贝到 代码下的 public_config/cfg.json 中
```

##### media

```
手动创建 Aquila/src/py-service/mgt_portal/media 目录, 用于暂存上传的文件和其他临时文件
```

# 问题

### 编译问题

##### deploy-sh 失败

```
[root@CTL py-service]# sh deploy-sh 
++++++++++++++++++++++++++++++++++++++++++++++++
taskd
[taskd] venv/bin/pip install -q -r requirement.txt --no-index --find-links=file:///opt/pypi
ERROR: Could not find a version that satisfies the requirement certifi==2022.12.7 (from versions: 2020.12.5)
ERROR: No matching distribution found for certifi==2022.12.7


方法1
重命名 /opt/pypi 这个文件, 会从服务器下载, 速度慢

方法2 (未使用)
下载文件到路径下
```

##### 前置

```bash
# 这 3 个须都是 su 权限, 否则有时会失败
# 例如安装时 go 会下载新的包, 包的安装目录需要权限, 否则失败
$ ../src/config/configure
$ make
$ make install 


编译失败后删除 build 里面的所有内容, 重新执行
```

##### sg_py_call.c:1:20

- 描述

  ```
  sg_py_call.c:1:20: fatal error: Python.h: No such file or directory
   #include <Python.h>
  ```

- 解决办法 

  ```
  复制和 python 3.7.10 对应的 python3.pc 文件
  ```

##### sg_postgresql.c:4:22

- 描述

  ```
  sg_postgresql.c:4:22: fatal error: libpq-fe.h: No such file or directory
   #include <libpq-fe.h>
  ```

- 解决办法

  ```bash
  $ dnf install postgresql-devel
  ```

##### libsg_db.so

- 描述

  ```
  /bin/ld: cannot find -lsqlite3
  collect2: error: ld returned 1 exit status
  make[2]: *** [libsg_db.so] Error 1
  ```

- 解决办法

  ```bash
  $ dnf install sqlite-devel
  
  (没用这个)
  $ dnf install postgresql-devel postgresql postgresql-libs
  ```

##### libfm.so

- 描述

  ```
  /bin/ld: cannot find -lsg_ssl
  collect2: error: ld returned 1 exit status
  make[2]: *** [libfm.so] Error 1
  ```

- 解决办法

  ```
  (为了安装 libfm)
  yum install epel-release
  
  dnf install libinput-devel mesa-libgbm-devel libfm  sg3_utils libevent
  ```

##### 编译失败 autoreconf

```
autoreconf: command not found


yum install autoconf automake libtool
```

### 运行问题

##### 前置

```
所有环境刚刚安装好时执行
sh src/script/run.sh start
以后执行
sh src/script/run.sh restart
```

##### 问题: run.sh restart 卡住

```
停止所有进程, 脚本无法停止的手动 kill, 否则锁表, sql 脚本无法执行, 例如
	alter table business_define drop constraint IF EXISTS business_define_customer_id_name_net_name_net_type_key;
```

##### 请求卡死

```
运行到 state, src_ip, peer_ip = ext.get_ha_config() 时卡死

调用封装的 .so 库时不同用户没有权限

让 pycharm 启动时用使用 sudo 权限的 python 启动项目
https://zhuanlan.zhihu.com/p/296715567
```

##### 问题6

```
sh run-postgres.sh check 失败提示
docker does not exist, skip !!!


原因:
脚本问题, 必须设置开机启动 nginx和redis 才可以正常运行

(其他脚本可能也存在这个问题)
systemctl enable nginx
systemctl enable redis
```



```
ln -s /usr/lib/pipelinedb/bin/pg_isready /usr/bin/pg_isready


pg_config

mkdir /media/sys /media/config /media/data /media/sig /media/stats /media/store 
ln -s /media/sys /sdwan
ln -s /media/config /sdwan/config

```

##### pip 安装报错

```
ModuleNotFoundError: No module named '_ctypes'

安装 python 全需要安装
$ yum install libffi-devel
```

##### 启动zk报错

```
kafka-run-class.sh: line 306: exec: java: not found


ln -s /usr/java/jdk-11.0.1/bin/java /usr/bin/java
```

##### python 启动错误

```
nohup: failed to run command ‘venv/bin/python’: Permission denied


原因 /sdwan/py-server 下面 venv/bin 里面的 python 没有可执行权限


解决办法, 修改文件权限
$ chmod -R 777 py-server
```



```
docker 连接时使用 172.17.0.2 不是 127.0.0.1
```

##### dev-6

```
数据库连接池 (dev-6 需要安装后才能正常启动)


yum install libevent-devel
rpm -ivh pgbouncer-1.17.0-1.el7.x86_64.rpm
```

##### 编译 dev-6 后再编译 dev-5 后启动失败

```
网页启动失败
查看日志 /sdwan/debug/logs/mgt_portal.log


报错如下
.127.0.0.1 6432 Can Not Be Connected. Is Waiting 127.0.0.1 6432 To Be Connected...
.127.0.0.1 5672 Can Not Be Connected. Is Waiting 127.0.0.1 5672 To Be Connected...


原因:
6432 和 5672 这两个端口是 dev-6 的
编译 dev-6 后再编辑 dev-5 的项目后 /sdwan/py-service/public_config/wait_service.list 文件会有残留, 将这两个删除
127.0.0.1 5672
127.0.0.1 6432


或者删除 py-service 重新编译
```

```
127.0.0.1 6379
127.0.0.1 2181
127.0.0.1 9092
127.0.0.1 5672
127.0.0.1 5433
172.17.0.2 5432
127.0.0.1 6432
```

##### 

```bash
问题: pg_config
[root@CTL software]# cat /opt/monitor/postgresql.conf
cat: /opt/monitor/postgresql.conf: No such file or directory


解决办法
$ ln -sf /usr/lib/pipelinedb/bin/pg_config /usr/bin/pg_config 
```

### 使用问题

##### 日志路径

```
/sdwan/debug/site.log
```

##### 任务一直不执行

```
supervisor 重启 
base:task_worker 和 base:task_main 
```

##### 添加设备后无法上线

```
租户许可过期


cpe调试命令
    cpe4> debug sdwan-agent 
    cpe4> debug to terminal 
1. 项目运行 Aquila/src/py-service/mgt_portal/ 目录下创建 media 临时存储文件

2. 登陆 https://https://10.48.112.88/ 创建许可
ctl许可生产 -> 运营许可 -> 导出 license
	机器序列号: 只用运营管理员登陆 -> 账号 -> 关于 -> 软件序列号
	客户名称: 租户的名称
	
3. 运营管理员登陆管控 -> 运维 -> 许可管理 -> 运营许可 -> 导入
```

##### pg 表添加字段

```
例如 admin_user_db 添加 lang 字段

需要修改下面两个脚本
Aquila/src/database/manager/config_create.sql/config_create.sql
CREATE TABLE IF NOT EXISTS admin_user_db (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER DEFAULT '0',
    customer_name varchar(128) DEFAULT '',
    name varchar(128) NOT NULL,
    description varchar(128) DEFAULT '',
    role varchar(128) DEFAULT '',
    password varchar(128) DEFAULT '',
    create_time DATE NOT NULL DEFAULT '1970-01-01',
    login_time DATE NOT NULL DEFAULT '1970-01-01',
    ispredefine INTEGER DEFAULT '0',
    issuper INTEGER DEFAULT '0',
    time_out INTEGER DEFAULT '15',
    phone varchar(128) DEFAULT '',
    mail varchar(128) DEFAULT '',
    wechat_state INTEGER DEFAULT 0,
    wechat_qr_code_url text,
    wechat_qr_code_time VARCHAR(32) DEFAULT '',
    lang VARCHAR(32) DEFAULT '',
    UNIQUE (name)
);



Aquila/src/database/manager/config_create.sql/update.sql
alter table admin_user_db ADD COLUMN IF NOT EXISTS lang VARCHAR(32) DEFAULT '';
```

##### modify url 问题

```
登陆后页面显示 Oops! 我们遇到了一些小问题...


重启服务, 看 site.log 输出的错误

原因
	1. 新增加了 pip 包
```



