/*
1. 方法能给用户定义的类型添加新的行为. 方法实际上也是函数,只是在声明时,在关键字func和方法名之间增加了一个参数
2. 两种类型的接收者:值接收者和指针接收者
3. 方法和函数的区别在于, 函数可以直接调用(通过包名.函数名称), 而方法只能通过绑定的数据类型对应的变量来调用(变量.函数名称)
4. 函数名称和方法名称可以重名
5. 接收者的类型必须是用户定义的(自己定义或者第三方库的)


格式:
func (接收者名称 接收者类型)函数名称(形参列表)(返回值列表){
	逻辑语句;
}

引用类型:
1. 引用类型有字符串, 切片, 映射, 通道, 接口和函数. 这些类型的变量称为 标头值
2. 每个引用类型创建的标头值包含一个指向底层数据结构的指针, 还包含一组独特的字段用于管理底层数据结构







*/
package main

import (
	"fmt"
)

type Animal struct {
	name string
	age  int
}

//地址传递
//指定接收者名称
//给接收者定义方法
func (a *Animal) run() {
	a.name = "Lucy"
	a.age = 1
	fmt.Println("run1", a.name, a.age)
}

//值传递
//指定接收者名称
//给接收者定义方法
func (a Animal) run3() {
	a.name = "小明"
	a.age = 2
	fmt.Println("run3")
}

//值传递
//没有指定接收者名称
//给接收者定义方法
func (Animal) run2() {
	fmt.Println("run2")
}

func main() {
	a := Animal{"Tom", 22}
	//Animal类型的变量调用
	//如果指定了接收者名称,那么调用方法时会将调用者传递给接收者(可以把接收者看做函数的形参)
	fmt.Println(a)
	a.run()
	fmt.Println(a)
	a.run2()
	fmt.Println(a)
	a.run3()
	fmt.Println(a)

	//Animal类型的指针也可以调用
	b := &Animal{name: "小红", age: 95}
	b.run()
	//但 run3 接收者 还是副本
	b.run3()
	fmt.Println(b)
	//通过指针获取变量调用
	(*b).run()
	//但 run3 接收者 还是副本
	(*b).run3()

}
