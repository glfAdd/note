/*
不支持隐式转换类型
bool和int不能相互转换
*/
package main

import "fmt"

func main() {
	a := "10"
	b := string(a)
	fmt.Println(b)
}
