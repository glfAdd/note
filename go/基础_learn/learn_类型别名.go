/*
注意:
	mystring 虽然好似基于 string 创建的, 但并不是同一个类型, 不能互相赋值
*/
package main

import "fmt"

type mystring string

func main() {
	//int64的别名为bigin
	type bigint int64
	var a bigint = 100

	type (
		age  bigint
		name mystring
	)
	var b age = 200
	var c name = "name"
	fmt.Println(a, b, c)

	fmt.Println("-------------------- 不能互相赋值")
	//var m mystring
	//m = "my"
	//var n string
	//m = n

}
