/*
连接池

https://mynamezy.github.io/2020/02/18/golang-datasql-connection-pool/



database/sql 定义了sql的接口, 具体的实现还需要不同的数据库驱动
mysql使用 github.com/go-sql-driver/mysql


prepared


    避免通过引号组装拼接sql语句。避免sql注入带来的安全风险
    可以多次执行的sql语句。









*/

package main

import (
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
)

func main() {
	db, err := sql.Open("mysql", "root:123456@tcp(172.17.0.1)/learn?charset=utf8&allowOldPasswords=1")
	var (
		id        int
		age       int
		user_name string
	)
	if err != nil {
		fmt.Println(err)
	}
	defer db.Close()

	fmt.Println("-------------------- 查询所有")
	res, _ := db.Query("select * from person where age = ?", 22)
	//Next 遍历
	for res.Next() {
		//Scan 获取每一行
		e := res.Scan(&id, &age, &user_name)
		//每次判断时候有错误
		if e != nil {
			fmt.Println(e)
		}
		fmt.Println(id, age, user_name)
	}

	//检查错误
	if res.Err() != nil {
		fmt.Println(res.Err())
	}

	fmt.Println("-------------------- 单行查询")
	e2 := db.QueryRow("select * from person where age = ?", 22).Scan(&id, &age, &user_name)
	if e2 != nil {
		fmt.Println(e2)
	}
	fmt.Println(id, age, user_name)

	fmt.Println("-------------------- 更新")
	db.Prepare()

	fmt.Println("-------------------- 事务")




}
