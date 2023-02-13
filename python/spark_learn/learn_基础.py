"""
Spark的架构和部署方式
采用主从（master/slaves）架构，一个active master 节点（如果是高可用HA则还有一个standby master节点）和若干个worker节点（slaves）。



Spark通过减少磁盘IO来达到性能的提升，它们将中间处理数据全部放到了内存中。
Spark使用了RDD（Resilient Distributed Datasets）数据抽象，这允许它可以在内存中存储数据，只在需要时才持久化到磁盘。这种做法大大的减少了数据处理过程中磁盘的读写，大幅度的降低了运行时间。
"""

""" ============================ 
Spark Core是Spark的核心计算引擎，提供了任务调度、003内存管理、错误恢复、与存储系统交互等模块。其中的弹性分布式数据集(RDD)，是计算时的主要编程抽象，基于RDD对数据进行创建、操作与计算。
Spark SQL是用来操作结构化数据的程序包，支持多种数据源(Hive表、Parquet、JSON),可以基于Spark SQL进行数据的查询，为数据计算提供数据入口。
Spark Streaming是对实时数据进行流式计算的组件，比如处理服务器日志或者消费消息队列。
Mllib作为Spark组件中机器学习的程序库，具有包括分类、回归、聚类、协同过滤等算法。
GraphX是用来操作图的程序库、可以并行进行图计算，并支持常用的图算法。

Spark四种运行模式
    1、本地单机模式：所有Spark进程都运行在一个Java虚拟机中
    2、集群单机模式：使用Spark自己内置的任务调度框架
    3、基于Mesos
    4、基于YRAN

Spark用户与用途

用户：数据科学家与工程师
用途：数据科学应用与数据处理应用


Spark应用是由一个驱动器程序(driver programmer)和多个执行器(executor)节点组成。在启动Spark应用后，会通过创建一个上下文对象(SparkContext)对Spark应用进行操作，上下文对象代表对计算集群的一个连接。


"""
