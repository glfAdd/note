##### 返回 DML 修改的数据

```sql
-- 返回插入数据
insert into test2 (id, age, name) values (8, 22, 'LI') returning *;

-- 返回更新后数据
update test2 set age=21 where id=2 returning *;

-- 返回删除的数据
delete from test2 where id=1 returning *;
```

