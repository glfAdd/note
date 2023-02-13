```
Redis Sentinel 与 Redis Cluster
https://blog.csdn.net/angjunqiang/article/details/81190562
```

##### redis的并发竞争问题如何解决?

```
Redis为单进程单线程模式，采用队列模式将并发访问变为串行访问。Redis本身没有锁的概念，Redis对于多个客户端连接并不存在竞争
```

##### 事务

```

```

##### redis二级缓存

```

```

##### Redlock

```

```

##### pipline

```
pipeline就是用来将n次的网络时间优化为一次的网络时间, 耗时为1次网络时间 + n次命令时间


redis原生有类似 mget mset的批量操作命令，这些命令都是原子的，即会阻塞其他的命令，知道命令完成返回。而pipeline的每一条命令是拆分过的（非原子），假设打包1000个命令的pipeline传到服务端，则服务端会把pipeline的每个命令当成原子。但无论是pipeline还是M操作 返回的结果都是一样的。



pipeline与M操作都会将数据顺序的传送顺序地返回（redis 单线程）

1.每次pipeline携带数量不推荐过大，否则会影响网络性能;
2.pipelinepipeline每次只能作用在一个Redis节点上;
```

##### 原生M操作

```

```
