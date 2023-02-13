```
开源网站地址: https://sourceforge.net/projects/zabbix/files/ZABBIX%20Latest%20Stable/
```

##### 创建用户

```
groupadd zabbix
useradd -g zabbix zabbix
```

##### 下载

> 官网: https://www.zabbix.com/cn/download_sources
>
> 文档: https://www.zabbix.com/documentation/current/zh/manual/installation/install_from_packages
>
> 源代码安装: https://www.zabbix.com/documentation/3.4/zh/manual/installation/install

```bash
$ wget https://cdn.zabbix.com/zabbix/sources/stable/5.4/zabbix-5.4.2.tar.gz

# 查看编译帮助
$ ./configure --help
$ ./configure --prefix=/home/glfadd/Desktop/aaa --enable-server --enable-agent --with-mysql --enable-ipv6 --with-net-snmp --with-libcurl --with-libxml2

$ ./configure --prefix=/home/glfadd/Desktop/aaa --enable-server --enable-agent --enable-ipv6 --with-net-snmp --with-libcurl --with-libxml2

```

| 123               | 123                       |
| ----------------- | ------------------------- |
| --with-libcurl    | SMTP认证需要/虚拟机监控需 |
| --with-libxml2    | 虚拟机监控需              |
| --with-postgresql | 使用 PostgreSQL           |
| --with-sqlite3    | 使用 SQLite               |
| --with-mysql      | 使用mysql                 |
| --prefix=/usr     |                           |
|                   |                           |
|                   |                           |



##### 编译选项

```



```



##### 环境变量

```
```

##### 配置文件

```

```

##### 启动

```

```

##### Web UI

```

```

