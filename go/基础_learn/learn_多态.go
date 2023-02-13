/*

 */

package main

import (
	"fmt"
)

type animal1 interface {
	run()
}

type cat1 struct {
	name string
	age  int
}

type dog struct {
	name string
	age  int
}

//使用指针接收者实现 animal1 接口
func (c *cat1) run() {
	fmt.Println("cat1 run")
}

//使用值接受者实现 animal1 接口
func (d dog) run() {
	fmt.Println("dog run")
}

//接收实现 animal1 接口的值
func animal1Run(t animal1) {
	t.run()
}

func main() {
	c := cat1{name: "花花", age: 10}
	animal1Run(&c)
	d := dog{name: "旺旺", age: 5}
	animal1Run(&d)
}
