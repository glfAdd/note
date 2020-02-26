https://www.jianshu.com/p/77fb7c054016?utm_campaign=hugo&utm_medium=reader_share&utm_content=note&utm_source=weixin-friends

- with语句通常被称为通用表表达式（Common Table Expressions）或者CTEs。
- with语句和主语句都可以是SELECT，INSERT，UPDATE，DELETE中的任何一种语句
- with在复杂查询中定义一个辅助语句, 可以理解为查询中定义一个临时表. 简化SQL减少嵌套.
- 可以不使用CTEs而使用两层嵌套子查询来实现，但使用CTEs更简单，更清晰，可读性更强

##### with查询数据

```sql
create table test2 (id int4, age int4, name text);
insert into test2 (id, age, name) values(1, 10, 'xiao');
insert into test2 (id, age, name) values(2, 20, 'ming');
insert into test2 (id, age, name) values(3, 30, 'Tom');
insert into test2 (id, age, name) values(4, 40, 'Lucy');

with t1 as (select array_i from list_test) 
select * from t;
-- 定义t1 和 t2, 后面继续使用
with t1 as (select age, name from test2), 
		 t2 as (select age from t1) 
select * from t2 where age>10;
```

##### with修改数据

- with 中的 delete 语句从 test2 表中删除数据，并通过 returning 子句将删除的数据集赋给 t 这一CTE，最后在主语句中通过 insert 将删除的商品插入 test2 中.

- 如果 with 里面使用的不是 select 语句，并且没有通过returning子句返回结果集，则主查询中不可以引用该CTE，但主查询和 with 语句仍然可以继续执行。这种情况可以实现将多个不相关的语句放在一个SQL语句里，实现了在不显式使用事务的情况下保证WITH语句和主语句的事务性

- with 中的数据修改语句会被执行一次，并且肯定会完全执行，无论主语句是否读取或者是否读取所有其输出。而 with 中的 select 语句则只输出主语句中所需要记录数。

- with 中使用多个子句时，这些子句和主语句会并行执行，所以当存在多个修改子语句修改相同的记录时，它们的结果不可预测。

- 所有的子句所能“看”到的数据集是一样的，所以它们看不到其它语句对目标数据集的影响。这也缓解了多子句执行顺序的不可预测性造成的影响。

- 如果在一条SQL语句中，更新同一记录多次，只有其中一条会生效，并且很难预测哪一个会生效。

- 如果在一条SQL语句中，同时更新和删除某条记录，则只有更新会生效。

  目前，任何一个被数据修改CTE的表，不允许使用条件规则，和ALSO规则以及INSTEAD规则。

```sql
with t as (delete from test2 where id=1 returning *) 
insert into test2 select * from t;

with a as(update test2 set age=33 where id=1), 
		 b as (delete from test2 where id=3) 
update test2 set name='jack' where id=4;
```

##### 递归使用CTE

- recursive: 递归, 可以引用自己的输出.

```sql













```

