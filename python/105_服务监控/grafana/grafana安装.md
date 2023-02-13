## 安装

##### 下载

> 官网: https://grafana.com/grafana/download

```bash
wget https://dl.grafana.com/oss/release/grafana-8.0.3.linux-amd64.tar.gz
```

##### 环境变量

- 环境变量的值会覆盖配置文件

- 环境变量命名规则

  ```
  GF_<SectionName>_<KeyName>
  
  说明:
      SectionName 是 [] 中的文本
      所有信息都需要大写
      . 应该使用 _ 替代
  ```

- 示例

  ```
  # default section
  instance_name = ${HOSTNAME}
  [security]
  admin_user = admin
  [auth.google]
  client_secret = oldS3cretKey
  
  上面的这些设置用环境变量覆盖
  
  export GF_DEFAULT_INSTANCE_NAME=my-instance
  export GF_SECURITY_ADMIN+USER=admin
  export GF_AUTH_GOOGLE_CLIENT_SECRET=oldS3cretKey
  ```

##### 配置文件

```
默认配置文件是在$WORKING_DIR/conf/defaults.ini
用户配置文件是在$WORKING_DIR/conf/custom.ini
用户配置文件中的配置信息可以被启动参数 --config参数覆盖


说明:
    1. 分号; 是`.ini`文件注释
    使用deb或者rpm包安装Grafana, 配置文件位于/etc/grafana/grafana.ini. 这个路径是在Grafana 的init.d脚本中使用--config参数指定的。
```

##### defaults.ini

| 参数               | 说明                                                         |
| ------------------ | ------------------------------------------------------------ |
| instance_name      | grafana-server实例的名称。在日志记录、内置度量、集群信息中会被使用到。默认值是`${HOSTNAME}`,即实例名称这可以使用系统变量`HOSTNAME`来替换。如果获得是是空值或者不存在，Grafana将尝试使用系统调用来获取机器名称 |
| data               | 存储sqlite3数据库文件的位置, sessions文件, 以及其他数据      |
| temp_data_lifetime | 在data目录中的临时副本需要保存多久。默认是24h。支持的模式有h(hours),m(minutes),例如168h，30m，10h30m。使用0表示永久保存 |
| logs               | log的路径                                                    |
| plugins            | 自动搜索和查找插件的目录                                     |
| provisioning       | 启动时使用的提供配置文件的文件                               |
| protocal           | http or https                                                |
| http_addr          | 服务器将要绑定的ip地址，如果是空值则绑定所有的网卡接口       |
| http_port          | 服务器将要绑定的端口，默认是3000                             |
| url                |                                                              |
| type               | mysql,postgres或者sqlite3                                    |
| path               | 只适用于sqlite3数据库。数据库文件的存储路径。                |
| host               | 只适用于mysql或者postgres. 例如 host = 127.0.0.1:3306        |
| name               | Grafana数据库的名称。一般使用grafana或者其他名字。           |
| user               | 数据库用户(不适用于sqlite3)                                  |
| password           | 数据库用户的密码(不适用于sqlite3)。如果密码包含#或者;则必须使用双引号，如 """#123456;""" |

##### database

```
Grafana需要一个数据库存储用户、仪表盘等其他信息。默认配置是使用sqlite3，是一个嵌入式数据库(包含在Grafana的二进制文件中)。
```

##### 启动

```
/opt/grafana-8.0.3/bin/grafana-server
```

##### grafana_conf.conf

```
[program:grafana]
directory=/opt/grafana-8.0.3
command=/opt/grafana-8.0.3/bin/grafana-server
autostart=false
autorestart=false
user=glfadd
log_stdout=true
log_stderr=true
redirect_stderr = true
stdout_logfile_maxbytes = 20MB
stdout_logfile_backups = 20     
stdout_logfile = /opt/logs/supervisord_grafana.log
```

##### 在线安装插件

> https://www.cnblogs.com/wuyukangkang/articles/Grafana_P4.html

```bash
1. 安装的默认路径
$ ./grafana-cli plugins install grafana-piechart-panel


2. 安装到指定路径
$ ./grafana-cli --pluginsDir=/opt/grafana-8.0.3/data/plugins plugins install grafana-piechart-panel  


3. 修改 grafana-cli 中插件默认安装路径
```

##### 离线安装插件(未实验)

```
下载插件.zip
上传，解压 unzip -q .zip
将解压的文件夹移动到grafana插件文件夹下
mv corpglory-progresslist-panel /var/lib/grafana/plugins/corpglory-progresslist-panel
重启grafana服务
sudo service grafana-server restart
```

##### Web UI

```
web地址
http://localhost:3000

账号密码：admin / admin
```

##### 重设密码

```
1. 首先打开数据库
sqlite3 /var/lib/grafana/grafana.db

2. 查看数据库中包含的表
.tables

3. 查看user表内容
select * from user;

4. 重置admin用户的密码为默认admin
update user set password = '59acf18b94d7eb0694c61e60ce44c110c7a683ac6a8f09580d626f90f4a242000746579358d77dd9e570e83fa24faa88a8a6', salt = 'F3FAxVm33R' where login = 'admin';

5. 退出
.exit
```



## 监控

##### grafana dashboards 地址

```
https://grafana.com/grafana/dashboards
```

##### grafana plugins 地址

```
https://grafana.com/grafana/plugins/
```

