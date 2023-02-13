##### 参考

```
https://blog.51cto.com/u_14012942/2432243
```

##### 参数缩写

```
connection ---> c
connection ---> con
```

##### 查看所有网络接口信息

```
 $ nmcli connection show
NAME                    UUID                                  TYPE      DEVICE          
SensorsData-office      1e1f813c-12c2-4140-b480-961c48567587  wifi      wlp4s0          
br-631c35d5c67a         7f318de1-ff13-4175-85f5-43c35be13c8c  bridge    br-631c35d5c67a 
docker0                 3b9ea63b-29df-4cb3-b866-9d51b0c444fd  bridge    docker0         
2D09                    8ba1805a-18d7-4962-aa47-0bb77d804134  wifi      --              
BQ                      ba634dac-6672-46c4-b660-4c9467f1c474  wifi      --              
BQ_5G                   6f7528fb-e455-4676-a23b-058afd5826e5  wifi      --              
CMCC-333222444 1        7b306beb-23b1-43b1-8aa2-a00793397bfb  wifi      --              
la_5G                   367257b5-8d69-4f52-99f4-5052f944e537  wifi      --              
SensorsData-19F-office  1f2428a5-4650-4d97-97ae-b4fb2ae0b0f7  wifi      --              
Wired connection 1      df390aca-73e6-32bf-ae94-66329aa6db56  ethernet  --   
```

##### 显示所有活动链接

```
 $ nmcli c show
 $ nmcli con show
 $ nmcli connection show --active
NAME                UUID                                  TYPE    DEVICE          
SensorsData-office  1e1f813c-12c2-4140-b480-961c48567587  wifi    wlp4s0          
br-631c35d5c67a     7f318de1-ff13-4175-85f5-43c35be13c8c  bridge  br-631c35d5c67a 
docker0             3b9ea63b-29df-4cb3-b866-9d51b0c444fd  bridge  docker0
```

##### 查看指定接口详细信息

```
 $ nmcli connection show SensorsData-office
connection.id:                          SensorsData-office
connection.uuid:                        1e1f813c-12c2-4140-b480-961c48567587
connection.stable-id:                   --
connection.type:                        802-11-wireless
connection.interface-name:              wlp4s0
connection.autoconnect:                 yes
connection.autoconnect-priority:        0
connection.autoconnect-retries:         -1 (default)
connection.multi-connect:               0 (default)
connection.auth-retries:                -1
connection.timestamp:                   1638348658
```

##### 修改网络名字

```
2D09 名字改为 123321
$ nmcli connection modify 2D09 con-name 123321
```

##### 删除

```
 $ nmcli connection delete la_5G
Connection 'la_5G' (367257b5-8d69-4f52-99f4-5052f944e537) successfully deleted.
```

##### 启动

```
nmcli connection up 123321
```

##### 停止

```
nmcli connection down 
```

##### 重启网络

```
$ nmcli connection reload 
$ systemctl restart network
```

##### 增加IP / 删除IP

```
$ nmcli connection modify ens37 +ipv4.addresses 192.168.38.161/24
$ nmcli connection modify ens37 -ipv4.addresses 192.168.38.161/24
```

##### 网络设置 shell ui

```bash
$ nmtui
```

## 配置文件

##### 配置文件路径

```
/etc/sysconfig/network-scripts
```

##### ifcfg 文件

| nmcli 参数       | ifcfg  文件参数 | 说明                                                         |
| ---------------- | --------------- | ------------------------------------------------------------ |
| c 的 con-name    | NAME=           | 网络名字, 不会更改ifcfg文件名                                |
| c 的 ipv4.method | BOOTPROTO       | ipv4.method默认为auto，对应为BOOTPROTO=dhcp<br />ipv4.method设置为manual表示BOOTPROTO=none，即只有静态ip |

