# 参考

[三种网络模式及配置详解](https://blog.csdn.net/zhangxm_qz/article/details/122612605)

# 网络设置

##### centos 网卡

1. 查看网卡

   ![](.\image\centos网卡001.png)

2. 查看宿主机网卡信息

   <img src=".\image\centos网卡002.png" style="zoom:80%;" />

3. 编辑网卡配置文件 ` /etc/sysconfig/network-scripts/ifcfg-ens33`

4. 桥接方式

   <img src=".\image\centos网卡003.png" style="zoom:100%;" />

   

5. NAT 方式

   <img src=".\image\centos网卡006.png" style="zoom:80%;" />

   <img src=".\image\centos网卡007.png" style="zoom:80%;" />

   <img src=".\image\centos网卡005.png" style="zoom:80%;" />

6. 重启 network

   <img src=".\image\centos网卡004.png" style="zoom:80%;" />

7. 检测是否能上网

   ```bash
   $ ping 114.114.114.114
   ```

##### 中文乱码

```bash
# 查看中文字符集
$ locale -a |grep "zh_CN"

# 安装字体
$ yum groupinstall "fonts"

```



##### DNS 设置

编辑 `/etc/resolv.conf` 添加

```
nameserver 114.114.114.114
nameserver 8.8.8.8
```

##### 虚拟机无法上网

1. 

<img src=".\image\网络001.png" style="zoom:80%;" />

2. 

<img src=".\image\网络002.png" style="zoom:80%;" />

3. 

<img src=".\image\网络003.png" style="zoom:80%;" />

4. 选择一个能上网的网卡

<img src=".\image\网络004.png" style="zoom:80%;" />













