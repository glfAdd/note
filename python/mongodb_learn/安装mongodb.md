##### 版本

```
5.0.4
```

##### 官网下载地址

```
https://www.mongodb.com/download-center/community/releases
```

#####  MongoDB 数据库默认角色

```
数据库用户角色：read、readWrite
数据库管理角色：dbAdmin、dbOwner、userAdmin
集群管理角色：clusterAdmin、clusterManager、clusterMonitor、hostManager
备份恢复角色：backup、restore
所有数据库角色： readAnyDatabase、readWriteAnyDatabase、userAdminAnyDatabase、
dbAdminAnyDatabase
超级用户角色：root
```

##### 编译安装(失败)

- ubuntu 依赖

  ```bash
  $ aptitude install liblzma-dev 
  $ aptitude install libcurl4-openssl-dev
  ```

- centos 依赖

  ```
  ```

- 编译

  ```
  0. 查看电脑核心数
  $ cat /proc/cpuinfo | grep processor | wc -l
  
  
  1. 需要 python3
  
  
  2. 下载社区版源代码
  $ wget https://fastdl.mongodb.org/src/mongodb-src-r5.0.4.zip
  
  
  3. 编译
  $ python buildscripts/scons.py --help
  $ python -m pip install requirements_parser
  $ python -m pip install -r etc/pip/compile-requirements.txt
  $ python buildscripts/scons.py -j 12
  	prefix: 指定安装路径
  	-j: 指定核心数, 加快编译速度, 不能设置的过大, 会使电脑死机
  ```

##### deb 包安装(未使用)

- 安装

  ```bash
  $ wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu2004-5.0.4.tgz
  
  1. 下载系统对应的二进制包
  
  
  2. apt-get install ./mongodb-org-server_5.0.4_amd64.deb
  ```
  
- 命令

  ```
  mongod --version
  
  systemctl status mongod
  systemctl stop mongod
  systemctl start mongod
  systemctl restart mongod
  systemctl disable mongod
  systemctl enable mongod
  ```

- 配置文件 /etc/mongod.conf

  ```
  
  ```

##### 二进制包安装

- 下载包

  ```
  $ wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu2004-5.0.4.tgz
  ```

- 配置环境变量 /etc/profile.d/my_env.sh

  ```
  export MONGODB_HOME=/opt/mongodb-linux-x86_64-ubuntu2004-5.0.4 
  export PATH=$PATH:$MONGODB_HOME/bin
  
  使环境变量生效
  $ source /etc/profile
  ```

-  数据存储目录

  ```
  /opt/mongodb-linux-x86_64-ubuntu2004-5.0.4/data
  ```

- 日志文件目录

  ```
  /opt/mongodb-linux-x86_64-ubuntu2004-5.0.4/logs
  ```

- 配置文件 

  ```
  /opt/mongodb-linux-x86_64-ubuntu2004-5.0.4/config
  /opt/mongodb-linux-x86_64-ubuntu2004-5.0.4/config/mongodb.conf
  ```

- 官网配置文件文档

  ```
  http://docs.mongodb.org/manual/reference/configuration-options/
  ```

- mongodb.conf

  ```
  storage:
    dbPath: /opt/mongodb-linux-x86_64-ubuntu2004-5.0.4/data
    journal:
      enabled: true
  
  systemLog:
    destination: file
    logAppend: true
    path: /opt/mongodb-linux-x86_64-ubuntu2004-5.0.4/logs/mongodb.log
  
  net:
    port: 27017
    bindIp: 0.0.0.0
  
  processManagement:
    timeZoneInfo: /usr/share/zoneinfo
    fork: true
  ```

- 参数说明

  | 参数    | 参数                                                       |
  | ------- | ---------------------------------------------------------- |
  | bind_ip | 0.0.0.0 允许远程访问, 或直接注释, 127.0.0.1 只允许本地访问 |
  | fork    | true, false 守护进程运行                                   |

- 启动

  ```
  $ /opt/mongodb-linux-x86_64-ubuntu2004-5.0.4/bin/mongod -f /opt/mongodb-linux-x86_64-ubuntu2004-5.0.4/config/mongodb.conf
  ```

- 命令

  ```bash
  $ /opt/mongodb-linux-x86_64-ubuntu2004-5.0.4/bin/mongod --help
  $ /opt/mongodb-linux-x86_64-ubuntu2004-5.0.4/bin/mongod  --version
  
  # 命令行进入数据库
  $ /opt/mongodb-linux-x86_64-ubuntu2004-5.0.4/bin/mongo
  ```

##### 创建 admin 和 root 用户

- shell 进入数据库

- 产看数据库

  ```
  > show dbs
  admin   0.000GB
  config  0.000GB
  local   0.000GB
  >
  ```

- 进入 admin 数据库, 如果数据库不存在则创建数据库

  ```
  > use admin
  ```

- 创建管理员账户, 用于管理账号，不能进行关闭数据库等操作

  ```
  > db.createUser({ user: "admin", pwd: "password", roles: [{ role: "userAdminAnyDatabase", db: "admin" }] });
  Successfully added user: {
  	"user" : "admin",
  	"roles" : [
  		{
  			"role" : "userAdminAnyDatabase",
  			"db" : "admin"
  		}
  	]
  }
  > 
  ```

- 创建root, 用于关闭数据库

  ```
  > db.createUser({user: "root",pwd: "123456", roles: [ { role: "root", db: "admin" } ]});
  ```

- 查看用户

  ```
  > show users
  或
  > db.system.users.find()
  ```

- 关闭服务(不要直接kill)

  ```
  > db.shutdownServer()
  ```

##### 创建指定数据库用户

```
use yourdatabase

db.createUser({user: "user",pwd: "password",roles: [ { role: "dbOwner", db: "yourdatabase" } ]})
```

##### 删除用户

```
删除用户必须由账号管理员来删，所以，切换到admin角色
use admin

db.auth("admin","password")

删除单个用户
db.system.users.remove({user:"XXXXXX"})

删除所有用户
db.system.users.remove({})
```

##### web ui

```
http://127.0.0.1:27017/
```

- 问题

  ```
  It looks like you are trying to access MongoDB over HTTP on the native driver port.
  
  ```

  

```


```



#####  shell 命令

```
查看数据库
show dbs



```



