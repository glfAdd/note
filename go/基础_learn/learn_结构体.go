/*
数组可以存储同一类型的数据, 结构体可以定义不同的数据类型
	struct 语句定义一个新的数据类型
	type 语句设定了结构体的名称
	没有赋值时显示默认值






*/
package main

import "fmt"

type Person struct {
	name, tel string
	age       int
}

//变量类型使用结构体
type Tom struct {
	address string
	number  int
	p       Person
}

func main() {
	fmt.Println("-------------------- 初始化")
	//方式1
	var a Person
	a.name = "小明"
	fmt.Println(a.name, a.age)
	//方式2
	b := Person{
		"Tom",
		"010-32898872",
		11,
	}
	//方式3
	c := Person{
		age:  44,
		name: "Tome",
	}
	fmt.Println(b, c)

	fmt.Println("-------------------- 变量类型使用结构体")
	e := Tom{
		address: "中国",
		number:  3001,
		p: Person{
			name: "Jack",
			age:  25,
		},
	}
	fmt.Println(e)

	fmt.Println("-------------------- 结构体作为参数")
	test5(a)
	fmt.Println(a)

	fmt.Println("-------------------- 结构体指针")
	test6(&a)
	fmt.Println(a)

}

func test5(s Person) {
	s.age = 100
}

func test6(s *Person) {
	s.age = 200
}
