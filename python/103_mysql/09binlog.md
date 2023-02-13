参考

https://www.jianshu.com/p/a0bcb778b7f5

##### 是什么

Binlog 记录所有数据库表结构变更以及表数据修改的二进制日志, 不会记录SELECT和SHOW这类操作

##### 作用

```
1. 主从复制：在主库中开启Binlog功能，这样主库就可以把Binlog传递给从库，从库拿到Binlog后实现数据恢复达到主从数据一致性
2. 数据恢复：通过 bin log 工具来恢复数据
```

##### 

```

```



##### 

```

```



##### 

```

```

# 复制流程

https://win-man.github.io/2019/12/01/MySQL%20Binlog(%E4%B8%89)%E2%80%94%E2%80%94MySQL%20%E5%A4%8D%E5%88%B6%E6%B5%81%E7%A8%8B%E8%AF%A6%E8%A7%A3/



https://blog.51cto.com/u_3522866/2717256

https://zhuanlan.zhihu.com/p/33504555

# 主从复制

##### 过程

<img src=".\image\主从1.png" alt="主从1" style="zoom:75%;" />

```
1. master在每次准备提交事务完成数据更新前，将改变记录到二进制日志(binary log)中（这些记录叫做二进制日志事件，binary log event，简称event)

2. slave启动一个I/O线程来读取主库上binary log中的事件，并记录到slave自己的中继日志(relay log)中。

3. slave还会起动一个SQL线程，该线程从relay log中读取事件并在备库执行，从而实现备库数据的更新
```

##### 问题



# 123



```



```





