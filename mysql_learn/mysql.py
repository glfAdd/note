自定生成变量编号
Select * from (select @number:=@number+1 as num, b.* from (select @number:=0) a,(select * from ih_area_info order by ai_name)b) c where num between 3 and 7 ;
Select * from (select @number:=@number+1 as num, b.ai_name, b.ai_ctime from (select @number:=0) a,(select * from ih_area_info order by ai_name)b) c where num between 3 and 7 ;
Select ai_ares_id from (select @number:=@number+1 as num, b.* from (select @number:=0) a,(select * from ih_area_info order by ai_name)b) c where num > 3 limit 2 ;

@			表示生成的变量
b			是目标表
b.ai_name 	搜索表中的字段
a			是表名




指定python解析器
#!/usr/bin/env python


