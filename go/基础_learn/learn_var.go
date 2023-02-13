/*

4. var 声明变量
5. const 声明常量
6. 常量、变量、类型、函数名、结构字段等, 以一个大写字母开头, 这种形式的标识符的对象就可以被外部包的代码所使用, 这被称为导出. 如果以小写字母开头，则对包外是不可见的
7. 如果将多个语句写在同一行需要用 ; 分隔(不推荐这么写)
8. 标识符第一个必须是子母或下划线

声明变量没有初始化默认值: 0 "" false nil
*/

package main

import "fmt"

func test() (l, m, n int) {
	return 11, 22, 33
}

func main() {
	//只声明没有初始化默认为 0
	var a int
	a = 1
	fmt.Println("a =", a)

	var b int = 2
	fmt.Println("b =", b)

	//自动判断类型
	var aa = 11
	fmt.Println(aa)

	//自动推导类型. 通过初始化的值确定类型
	c := 3
	d, e := 4, 5
	fmt.Printf("c = %d, d = %d, e = %d\n", c, d, e)

	//%T 打印变量类型
	fmt.Printf("c 的类型 %T\n", c)

	//匿名变量, 丢弃数据不处理
	var f int
	_, f, _ = test()
	fmt.Printf("f = %d\n", f)

	// 声明和初始化分开
	var (
		k int
		l float64
	)
	k, l = 10, 11.2
	fmt.Printf("k = %d, l = %f\n", k, l)

	// 一行定义多个
	var x, y int = 32, 33
	var x1, y1 = 44, 44.1
	fmt.Printf("x = %d, y =%d, x_1 = %d, y_1 = %f,\n", x, y, x1, y1)

	// 多个自动推导
	m1, n1 := 11, "22"
	fmt.Printf("m1 = %d, n1 = %s\n", m1, n1)
}
