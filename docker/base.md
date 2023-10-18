##### 参考

- [ ] https://blog.csdn.net/m0_49569199/article/details/110481050
- [ ] https://blog.csdn.net/wangleleb/article/details/119953170

```
Docker使用Cgroups完成对宿主机资源的管理和限制
```

# cpu

##### 查看命令详情

```bash
$ docker container run --help  cpu
```

##### 参数

| 选项          | 类型 | 描述                | 例子 |
| ------------- | ---- | ------------------- | ---- |
| --cpus        |      | 使用 cpu 个数       |      |
| --cpuset-cpus |      | 最大使用CPU核数区间 |      |
| --cpu-shares  |      | cpu 共享 (相对权重) |      |
|               |      |                     |      |





```bash


CPU、内存、磁盘 IO


```

````bash



--cpu-shares 参数值不能保证可以获得 1 个 vcpu 或者多少 GHz 的 CPU 资源，它仅是一个弹性的加权值


#--cpu-shares 1024设置CPU份额为1024（两倍512）
$ docker run -tid --name test1 --cpu-shares 1024 centos:stress stress -c 10 
````

##### CPU 周期限制

Docker 使用 cpu-period 和 cpu-quota 分配到的 CPU 时钟周期, 通常一起使用

- cpu-period

  -  用来指定容器对 CPU 的使用要在多长时间内做一次重新分配
  - 单位为微秒（μs）
  - 最小值为 1000 微秒， 最大值为 1 秒（10^6 μs），默认值为 0.1 秒（100000 μs）

- cpu-quota

  - 用来指定在这个周期内，最多可以有多少时间用来跑这个容器, 这种配置是指定一个绝对值，容器对 CPU 资源的使用绝对不会超过配置的值。
  - 单位为微秒（μs）
  - 值默认为 -1, 表示不做控制

- 实例

  ```
  ```

  

```bash

容器进程需要每 1 秒使用单个 CPU 的 0.2 秒时间，可以将 cpu-period 设置 为 1000000（即 1 秒），cpu-quota 设置为 200000（0.2 秒）。
当然，在多核情况下，如果允许容器进程完全占用两个 CPU，则可以将 cpu-period 设置为 100000（即 0.1 秒）， cpu-quota 设置为 200000（0.2 秒）。


# 启动容器
$ docker run -tid --name c1 --cpu-period 100000 --cpu-quota 200000 centos:centos7


# 进入容器查看
$ docker exec -it 49ab26152631 bash
[root@49ab26152631 /]# cat /sys/fs/cgroup/cpu/cpu.cfs_period_us 
100000
[root@49ab26152631 /]# cat /sys/fs/cgroup/cpu/cpu.cfs_quota_us 
200000
# 容器只能用 0, 1, 2, 3 内核
[root@49ab26152631 /]# cat /sys/fs/cgroup/cpuset/cpuset.cpus
0-3
```

##### cpuset-cpus

```bash
控制容器运行使用哪些 CPU 内核
# 

# 容器只能用 0、1两个内核
$ docker run -itd --name c2 --cpuset-cpus 0-1 centos:centos7




```

# 内存

##### 查看命令详情

```bash
$ docker container run --help memory
```

##### 参数

| 选项                | 类型        | 描述                              | 例子 |
| ------------------- | ----------- | --------------------------------- | ---- |
| -m, --memory        |             | 最大内存                          |      |
| --memory-swap       |             | 交换分区内存                      |      |
| --memory-swappiness |             | 使用交换分区百分比 0-100, 默认 -1 |      |
| --oom-kill-disable  | true, false | 禁用 OOM kill                     |      |

```
--oom-kill-disable
容器在使用内存超过限制之后，docker有权利将容器杀死，但有些容器服务很重要，不能被杀死






```





##### 

容器可使用的内存包括两部分: 物理内存和 Swap

```
-m 或 --memory: 最大内存例如 100M、1024M
–memory-swap: 内存+swap 的使用限额
```



- -m 或 --memory：最大内存例如 100M、1024M
- –memory-swap：设置 内存+swap 的使用限额

```bash
# 执行如下命令允许该容器最多使用 200M 的内存和 300M 的 swap。
$ docker run -it -m 200M --name c3 --memory-swap=300M progrium/stress --vm 1 --vm-bytes 280M
  --vm 1：启动1个内存工作线程
  --vm-bytes 280M：每个线程分配280M内存


默认情况下，容器可以使用主机上的所有空闲内存。
与cpu的cgroups配置类似，Docker会自动为容器在目录/sys/fs/cgroup/memory/docker/<容器的完整长id>中创建相应cgroup配置文件
注意：如果让工作线程分配的内存超过300M，分配的内存超过限额，stress线程报错，容器退出。

```

