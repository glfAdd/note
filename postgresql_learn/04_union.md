- union: 用于合并两个或多个select语句的结果，不返回任何重复的行.
- union all: 用于结合两个select语句，包括重复行.
- select语句中必须保持列数，列类型一致，否则会报错.

```sql
select * from test2 union select * from test2;
select * from test2 union all select * from test2;
```

