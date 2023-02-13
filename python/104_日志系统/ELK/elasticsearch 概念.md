## elasticsearch 概念



##### 集群 cluster

```
1. 在一个分布式系统里面,可以通过多个elasticsearch运行实例组成一个集群
2. 这个集群里面有一个节点叫做主节点 master ,elasticsearch 是去中心化的,所以这里的主节点是动态选举出来的,不存在单点故障. 
3. 在同一个子网内，只需要在每个节点上设置相同的集群名,elasticsearch就会自动的把这些集群名相同的节点组成一个集群。节点和节点之间通讯以及节点之间的数据分配和平衡全部由elasticsearch自动管理. 在外部看来elasticsearch就是一个整体。

    
```

