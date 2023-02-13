/*
var var_name *var-type

& 获取变量的内存地址
* 获取指针指向内存保存的值
空指针: 定义指针后没有分配任何变量, 值位nil

指向指针的指针变量, 第一个指针存放第二个指针的地址, 第二个指针存放变量的地址
*/
package main

import "fmt"

func main() {
	//获取变量地址
	a := 10
	fmt.Println(&a)

	//声明指针
	var b *int
	b = &a
	fmt.Println(b)

	c := "aaaa"
	var d *string
	d = &c
	//变量存储的指针地址
	fmt.Println(d)
	//变量的值
	fmt.Println(*d)

	//指针数组
	e := []int{10, 20, 30}
	var f [3]*int
	var i int
	for i = 0; i < 3; i++ {
		f[i] = &e[i]
	}
	for i = 0; i < 3; i++ {
		fmt.Println(f[i], *f[i])
	}

	//指向指针的指针
	//可以嵌套多层
	var h int
	var ptr *int
	var ptrr **int
	var ptrrr ***int
	h = 1000
	ptr = &h
	ptrr = &ptr
	ptrrr = &ptrr
	fmt.Println(h, ptr, ptrr, ptrrr)
	fmt.Println(h, *ptr, **ptrr, ***ptrrr)

	//指针作为参数
	test4(&h)
	fmt.Println(h)
}

func test4(h *int) {
	*h = 2000
}
