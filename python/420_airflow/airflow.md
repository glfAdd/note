##### 文档

[文档](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)

[中文文档](http://static.kancloud.cn/apachecn/airflow-doc-zh/1944255)

## 安装

##### mysql 创建 airflow 数据库

```sql
CREATE DATABASE airflow_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
create user 'airflow'@'%' identified by '123123';
-- 授权用户远程访问
GRANT all privileges on airflow_db.* TO 'airflow'@'%'  IDENTIFIED BY '123123';
-- 刷新授权
FLUSH PRIVILEGES;
set explicit_defaults_for_timestamp = 1;

grant all privileges on *.* to 'root'@'%' identified by '123456';
```

##### 安装 airflow

```bash
# 依赖
$ yum install python3-devel libevent-devel mysql-devel openssl
# 为airflow 安装mysql模块
$ pip install 'apache-airflow[mysql]'
# 设置环境变量
export AIRFLOW_HOME=/opt/airflow
# 运行 airflow, 会在指定目录下创建文件
$ airflow

# 配置文件 airflow.cfg
sql_alchemy_conn = mysql+mysqldb://root:123456@127.0.0.1:3306/airflow_db



# 再次运行 airflow
$ airflow


(命令失败)
airflow config get-value database sql_alchemy_conn mysql+mysqldb://root:123456@127.0.0.1:3306/airflow_db
```

##### 

```
sql_alchemy_conn  数据库连接方式
broker_url   队列的存储
result_backend  状态的存储

sql_alchemy_conn = mysql+mysqldb://用户名:密码@主机:端口/数据库

sql_alchemy_conn = mysql+mysqldb://airflow:Caocao1818.cn@test-hadoop01:3306/airflow
broker_url = sqla+mysql://airflow:Caocao1818.cn@test-hadoop01:3306/airflow
result_backend = db+mysql://airflow:Caocao1818.cn@test-hadoop01:3306/airflow
values的构成是airflow:Caocao1818.cn@test-hadoop01:3306/airflow
```

##### 初始化 airflow 数据

```bash
$ airflow initdb (弃用)
$ airflow db init
```

###### 执行 airflow db init 报错

```
错误信息:
ImportError: urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with OpenSSL 1.0.2k-fips  26 Jan 2017


解决办法
降低 urllib3 的版本
pip install urllib3==1.26.6
```

###### mysql 和 airflow 分别在两个 docker 容器中

```bash
将两个容器添加通一个网络中
# 查看所有的网络模式
$ docker network ls
# 删除自定义网络
$ docker network rm 网络名称
# 创建一个自定义网络
$ docker network create --driver bridge --subnet 192.168.50.1/16 --gateway 192.168.50.1 network01
    参数
      --driver bridge  设置网络模式
      --subnet 192.168.0.1/16  设置子网
      --gateway 192.168.0.1 设置网关
      network01  自定义网络的名称
# 查看网路详情
$ docker network inspect network01
# 启动容器后检查网络之间是否可以互通
$ docker exec -it c1 ping c2
# 将外界容器添加到项目容器中来
# docker network connect 自定义网络名称 要添加的容器名
$ docker network connect network01 centos7
$ docker network connect network01 mysql-test
```

###### 链接数据库失败

```
报错:
sqlalchemy.exc.OperationalError: (MySQLdb.OperationalError) (1045, "Access denied for user 'airflow'@'192.168.0.1' (using password: YES)")


mysql 授权用户远程访问

```

###### 

```
(MySQLdb.OperationalError) (1067, "Invalid default value for 'updated_at'")
```



##### 命令

```bash
$ airflow version
```

## 安装 (docker)

##### 安装 docker-compose

````bash
# 是否安装 docker-compose
$ docker-compose --version
````

##### 安装 airflow

```bash
$ cd
$ mkdir airflow
$ cd airflow
$ curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.5/docker-compose.yaml'
$ mkdir -p ./dags ./logs ./plugins ./config
	./dags DAG文件
	./plugins 自定义的插件
$ echo -e "AIRFLOW_UID=$(id -u)" > .env
# 初始化数据库 (需要 docker-compose.yaml 文件)
```

##### 命令

```bash
$ docker-compose up airflow-init
# 运行 Airflow 启动所有服务 (需要 docker-compose.yaml 文件)
$ docker-compose up
$ docker-compose up -d
$ docker-compose -f docker-compose.yaml up -d
# 停止服务
$ docker-compose down
```

##### 登录

```
登录地址
	http://localhost:8080
登录名/密码
	airflow airflow
```



```bash
# 日志：				
$ docker-compose logs [-f] [service_name]
# 构建Airflow镜像
$ docker-compose build
# 清除未使用的镜像、容器、网络和卷
$ docker system prune
# 查看容器所在的网络IP地址
$ docker network inspect 容器名字
# docker 保存镜像
$ docker save -o airflow2.tar apache/airflow:2.6.0
# tar 文件导入到另一台机器上
$ docker load -i airflow2.tar
```

