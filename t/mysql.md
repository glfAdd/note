##### 联合索引最左匹配原则

```
https://bbs.huaweicloud.com/blogs/169243
```



```










```

##### EXPLAIN

- type
  - ALL: 遍历全表以找到匹配的行
  - index: Index与ALL虽然都是读全表，但index是从索引中读取，而ALL是从硬盘读取
  - range: 只检索给定范围的行，使用一个索引来选择行。key列显示使用了那个索引。一般就是在where语句中出现了bettween、<、>、in等的查询。这种索引列上的范围扫描比全索引扫描要好。只需要开始于某个点，结束于另一个点，不用扫描全部索引
  - ref: 非唯一性索引扫描，返回匹配某个单独值的所有行。本质是也是一种索引访问，它返回所有匹配某个单独值的行，然而他可能会找到多个符合条件的行，所以它应该属于查找和扫描的混合体
  - const: 表示通过索引一次就找到了，const用于比较primary key 或者 unique索引。因为只需匹配一行数据，所有很快。如果将主键置于where列表中，mysql就能将该查询转换为一个const

- key_len: 显示MySQL实际决定使用的索引的长度
  - 

```
计算规则：
1.定长字段，int占用4个字节，date占用3个字节，char(n)占用n个字符。
2.变长字段varchar(n)，则占用n个字符+两个字节。
3.不同的字符集，一个字符占用的字节数是不同的。Latin1编码的，一个字符占用一个字节，gdk编码的，一个字符占用两个字节，utf-8编码的，一个字符占用三个字节。
（由于我数据库使用的是Latin1编码的格式，所以在后面的计算中，一个字符按一个字节算）
4.对于所有的索引字段，如果设置为NULL，则还需要1个字节。




```

##### 联合索引最左前缀匹配原则

```
https://bbs.huaweicloud.com/blogs/169243

```

- MySQL中有查询优化器explain，所以sql语句中字段的顺序不需要和联合索引定义的字段顺序相同，查询优化器会判断纠正这条SQL语句以什么样的顺序执行效率高，最后才能生成真正的执行计划
- 可以根据key_len推算使用的哪个索引

```
示例: 创建 age_name_address 的联合索引相当于创建了3个索引, age, age_name, age_name_address

# 1. 只使用age索引, (可以看key_len长度)
EXPLAIN select * from person WHERE age=11;
# (不是依次匹配, 所以只用到了索引age)
EXPLAIN select * from person WHERE age=11 and address='china';

# 2. 只使用 age_name 索引
EXPLAIN select * from person WHERE name='tom' and age=11;

# 3. 使用 age_name_address 索引
(
通过观察发现上面key字段发现在搜索中也使用了id_name_age_index索引，可能许多同学就会疑惑它并没有遵守最左匹配原则，按道理会索引失效，为什么也使用到了联合索引？因为没有从id开始匹配，且name单独来说是无序的，所以它确实不遵循最左匹配原则，然而从type字段可知，它虽然使用了联合索引，但是它是对整个索引树进行了扫描，正好匹配到该索引，与最左匹配原则无关，一般只要是某联合索引的一部分，但又不遵循最左匹配原则时，都可能会采用index类型的方式扫描，但它的效率远不如最做匹配原则的查询效率高，index类型类型的扫描方式是从索引第一个字段一个一个的查找，直到找到符合的某个索引，与all不同的是，index是对所有索引树进行扫描，而all是对整个磁盘的数据进行全表扫描。
)
EXPLAIN select * from person WHERE name='tom';
EXPLAIN select * from person WHERE address='china';
EXPLAIN select * from person WHERE name='tom' and address='china';
EXPLAIN select * from person WHERE name='tom' and address='china' and age=11;


# 前缀都是排好序的，使用的都是联合索引
select * from staffs where age like 'A%';
# 全表查询
select * from staffs where age like '%A%';
# 全表查询
select * from staffs where age like '%A';


# age精确匹配, name范围匹配
# (age范围内name是无序的所以只用了age索引)


```

##### 单列索引

```
https://www.jianshu.com/p/7850b14c9e35

有三个单列索引 age name address

# 多个单列索引在多条件查询时优化器会选择最优索引策略，可能只用一个索引，也可能将多个索引全用上！ 但多个单列索引底层会建立多个B+索引树，比较占用空间，也会浪费一定搜索效率，故如果只有多条件联合查询时最好建联合索引！
EXPLAIN select * from person WHERE name='tom' and address='china' and age=11;
# or 连接用到了所有索引
EXPLAIN select * from person WHERE name='tom' or address='china' or age=11;
```



##### 单独索引和联合索引同时存在时

```
优先使用单独索引，单独索引里有重复项时才用到联合索引
能用单独索引时，MySQL会认为没必要用到组合索引

当同时存在单列索引和联合索引，mysql会根据查询优化策略选择其中一个索引。




```



















