##### 参考

- [ ] https://blog.csdn.net/tiger_lin1/category_11642003.html
  - [x] https://linwei.blog.csdn.net/article/details/131002467
  - [x] https://blog.csdn.net/Tiger_lin1/article/details/131323968
- [ ] https://www.yii666.com/blog/338145.html?action=onAll
- [ ] https://blog.csdn.net/m0_48638643/article/details/127188762
- [ ] `https://blog.csdn.net/hguisu/article/details/124228252?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-124228252-blog-126824797.235^v38^pc_relevant_sort&spm=1001.2101.3001.4242.1&utm_relevant_index=3`  详细
- [ ] https://blog.csdn.net/weixin_44729138/article/details/106054025
- [ ] https://murphy.blog.csdn.net/article/details/129862923?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EYuanLiJiHua%7EPosition-2-129862923-blog-126824797.235%5Ev38%5Epc_relevant_sort&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EYuanLiJiHua%7EPosition-2-129862923-blog-126824797.235%5Ev38%5Epc_relevant_sort&utm_relevant_index=5
- [ ] `https://blog.csdn.net/cuichongxin/article/details/121403914?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-8-121403914-blog-126824797.235^v38^pc_relevant_sort&spm=1001.2101.3001.4242.5&utm_relevant_index=11`
- [ ] 



##### 区别

```
Deployment 和 StatefulSet 的

Deployment和StatefulSet的区别：Deployment没有唯一标识而StatefulSet有唯一标识。
StatefulSet的唯一标识是根据主机名+一定规则生成的。
StatefulSet的唯一标识是主机名.无头Service名称.命名空间.svc.cluster.local。
```

##### StatefulSet 的限制

- Pod 的存储要么由 storage class 对应的 PersistentVolume Provisioner提供，要么由集群管理员事先创建
- 删除或 scale down 一个 StatefulSet 将不会删除其对应的数据卷。这样做的考虑是数据安全
- 删除 StatefulSet 时，将无法保证 Pod 的终止是正常的。如果要按顺序 gracefully 终止 StatefulSet 中的 Pod，可以在删除 StatefulSet 前将其 scale down 到 0
- 当使用默认的 Pod Management Policy(OrderedReady) 进行滚动更新时，可能进入一个错误状态，并需要人工介入才能修复

```
StatefulSet 顾名思义，用于管理 Stateful（有状态）的应用程序。

StatefulSet 管理 Pod 时，确保其 Pod 有一个按顺序增长的 ID。

与 Deployment相似，StatefulSet 基于一个 Pod 模板管理其 Pod。与 Deployment 最大的不同在于 StatefulSet 始终将一系列不变的名字分配给其 Pod。这些 Pod 从同一个模板创建，但是并不能相互替换：每个 Pod 都对应一个特有的持久化存储标识。

同其他所有控制器一样，StatefulSet 也使用相同的模式运作：用户在 StatefulSet 中定义自己期望的结果，StatefulSet 控制器执行需要的操作，以使得该结果被达成。




```

```
StatefulSet 使用场景

对于有如下要求的应用程序，StatefulSet 非常适用：

    稳定、唯一的网络标识（dnsname）
    每个Pod始终对应各自的存储路径（PersistantVolumeClaimTemplate）
    按顺序地增加副本、减少副本，并在减少副本时执行清理
    按顺序自动地执行滚动更新

其实一句话总结StatefulSet 适用于有状态的控制器

如果一个应用程序不需要稳定的网络标识，或者不需要按顺序部署、删除、增加副本，您应该考虑使用 Deployment 这类无状态（stateless）的控制器。

```



# 更新策略

>  `.spec.updateStrategy`

### OnDelete

> `.spec.updateStrategy.type`

```
当 updateStrategy 设置为 OnDelete 时，StatefulSet Controller 并不会自动更新 StatefulSet 中的 Pod 实例，而是需要用户手动删除这些Pod并触发StatefulSet Controller 创建新的Pod实例来弥补，因此这其实是一种手动升级模式
```

### RollingUpdate (滚动更新)

> `.spec.updateStrategy.type`

```
当 updateStrategy 设置为 RollingUpdate时，StatefulSet Controller 会删除并创建 StatefulSet 相关的每个 Pod 对象，从序号最大的 Pod 开始重建，每次更新一个Pod

????? 待验证
注意，如果StatefulSet的Pod Management Policy 被设置为 OrderedReady，则可能在更新过程中发生一些意外，从而导致StatefulSet陷入奔溃状态，此时需要用户手动修复
```

```
从序号最大的 Pod 开始，逐个删除和更新每一个 Pod，直到序号最小的 Pod 被更新


当正在更新的 Pod 达到了 Running 和 Ready 的状态之后，才继续更新其前序 Pod



```

##### partition (分片)

- 指定 .spec.updateStrategy.rollingUpdate.partition 可以分片执行 RollingUpdate 更新策略
- 当更新 StatefulSet 的 .spec.template 时
  - 序号大于等于 .spec.updateStrategy.rollingUpdate.partition 的 Pod 将被删除重建
  - 序号小于 .spec.updateStrategy.rollingUpdate.partition 的 Pod 将不会更新，即使手工删除该 Pod 后 k8s 也会使用前一个版本的 .spec.template 重建该 Pod
  - 如果 .spec.updateStrategy.rollingUpdate.partition 大于 .spec.replicas, 更新 .spec.tempalte 将不会影响到任何 Pod

- 使用场景
  - 执行预发布
  2. 执行金丝雀更新
  3. 执行按阶段的更新

```


Forced Rollback

当使用默认的 Pod 管理策略时（OrderedReady），很有可能会进入到一种卡住的状态，需要人工干预才能修复。

如果您更新 Pod template 后，该 Pod 始终不能进入 Running 和 Ready 的状态（例如，镜像错误或应用程序配置错误），StatefulSet 将停止滚动更新并一直等待。

此时，如果您仅仅将 Pod template 回退到一个正确的配置仍然是不够的。由于一个已知的问题，StatefulSet 将继续等待出错的 Pod 进入就绪状态（该状态将永远无法出现），才尝试将该 Pod 回退到正确的配置。

在修复 Pod template 以后，您还必须删除掉所有已经尝试使用有问题的 Pod template 的 Pod。StatefulSet此时才会开始使用修复了的 Pod template 重建 Pod。

```



##### 实例

```
updateStrategy:
  rollingUpdate: # 如果更新的策略是OnDelete，那么rollingUpdate就失效
    partition: 2 # 表示从第2个分区开始更新，默认是0
  type: RollingUpdate /OnDelete # 滚动更新


    分段更新 partition（简单的灰度发布）
```

##### OrderedReady

```



https://www.cnblogs.com/bigcarcar/p/16206160.html

在StatefulSets中，并行podManagementPolicy比OrderedReady podManagementPolicy

https://www.zhblog.net/qa/podmanagementpolicy-in-statefulsets.html



https://caixm.blog.csdn.net/article/details/127090862?spm=1001.2101.3001.6650.5&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-5-127090862-blog-126824797.235%5Ev38%5Epc_relevant_sort&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-5-127090862-blog-126824797.235%5Ev38%5Epc_relevant_sort&utm_relevant_index=10
```

##### Parallel

```
```



```
updateStrategy 也支持特殊的分区升级策略（Partitioned），
指定一个序号 partition, StatefulSet 中序号 >= 此序号的 Pod 会全部被升级，<= 此序号的 Pod 则保留旧版本不变，即使这些 Pod 被删除、重建，也仍然保持原来的旧版本。


这种分区升级策略通常用于按计划分步骤的系统升级过程中。
```

# 问题

```
Running 和 Ready 等待的时间
```

##### statefulset node故障

```
K8S集群中Node节点资源不足导致Pod无法运行的故障排查思路
https://blog.csdn.net/weixin_44953658/article/details/126517766
```







