/*
func function_name( [parameter list] ) [return_types] {
   函数体
}

*/

package main

import "fmt"

//值传递
func test1(x int, y string) {
	x++
	y = "cc"
}

//引用传递
func test2(x *int, y *string) {
	*x = 20
	*y = "bb"
}

func main() {
	a := 10
	b := "aa"
	fmt.Println(a, b)
	test1(a, b)
	fmt.Println(a, b)
	test2(&a, &b)
	fmt.Println(a, b)

	//函数作为参数
	//闭包
	//结构体
}
