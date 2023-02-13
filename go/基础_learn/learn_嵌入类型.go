/*
1. 嵌入类型是将已有的类型直接声明在新的结构类型里
2. 外部类型也可以通过声明与内部类型标识符同名的标识符来覆盖内部标识符的字段或者方法。这就是扩展或者修改已有类型的方法。
3. 内部类型实现的接口会自动提升到外部类型. 由于内部类型的实现,外部类型也同样实现了这个接口

*/
package main

import "fmt"

type animal2 interface {
	run2()
}

type cat2 struct {
	name string
}

type blackCat2 struct {
	// 嵌入类型
	cat2
	age int
}

func (c cat2) run2() {
	c.name = "aaa"
	fmt.Println("cat2 run2", c.name)
}

//外部类型实现了接口就不会调用内部类型的实现
func (bc blackCat2) run2() {
	fmt.Println("blackCat2 run2", bc.name)
}

func funcTest2(a animal2) {
	a.run2()
}

func main() {
	b := blackCat2{
		cat2: cat2{name: "花花"},
		age:  12,
	}
	//通过内部类型调用方法
	b.cat2.run2()
	//外部类型直接访问方法
	//内部类型实现的接口会自动提升到外部类型. 由于内部类型的实现,外部类型也同样实现了这个接口
	b.run2()
	fmt.Println(b.cat2.name)

	funcTest2(&b)
}
