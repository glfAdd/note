/*
函数内定义的变量称为局部变量
函数外定义的变量称为全局变量
函数定义中的变量称为形式参数, 作为局部变量

1. 全局变量和局部变量可以名字相同, 先使用局部变量
2.




*/

package main

import "fmt"

var a int = 1
var c = 2

//这种方式不能用
//d := 10

func main() {
	b := 3
	a := "ccc"
	fmt.Println(a, b, c)

}
