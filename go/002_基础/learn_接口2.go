/*







 */
package main

import "fmt"

type animal interface {
	run()
}

type cat struct {
	name string
	age  int
}

func (c cat) run() {
	fmt.Println("cat run")

}
func main() {
	//用户定义的类型实现了某个接口类型声明的一组方法, 那么这个用户定义的类型的值就可以赋给这个接口类型的值. 这个赋值会把用户定义的类型的值存入接口类型的值 (定义了cat类型, 赋值给接口animal)
	/*
		接口 animal 值是一个两个字长度的数据结构
			第1个: 包含一个指向内部表的指针。这个内部表叫作 iTable, 包含了已存储的值的类型信息以及与这个值相关联的一组方法。
			第2个: 保存指向实体值的指针
	*/
	var a animal
	a = cat{name: "Tom", age: 21}
	/*
		接口 animal 值是一个两个字长度的数据结构
			第1个: 指向保存的类型的指针
			第2个: 保存指向实体值的指针
	*/
	var b animal
	b = &cat{name: "Jack", age: 35}
	fmt.Println(a, b)

}
