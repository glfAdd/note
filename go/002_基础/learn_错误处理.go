/*
go语言定义的error类型是一个接口类型
type error interface {
    Error() string
}





*/
package main

import "fmt"

//定义结构体
type MyError struct {
	name string
	msg  string
}

//结构体实现接口Error的方法
func (e MyError) Error() string {
	return "错误"
}

func testError(a int, b int) (c int, e string) {
	if a > b {
		return
	} else {
		//创建结构体变量, 调用实现的error方法
		tmp := MyError{"Tom", "Not"}
		return a, tmp.Error()
	}
}

func main() {
	m, n := testError(3, 5)
	fmt.Println(m, n)
}
