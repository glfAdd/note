/*
var variable_name [SIZE1][SIZE2]...[SIZEN] variable_type

1. 数组是一个长度固定的数据类型, 用于存储一段具有相同的类型的元素的连续块
2. 占用的内存是连续分配的, 容易计算索引,可以快速迭代数组里的所有元素
3. 数组的类型信息可以提供每次访问一个元素时需要在内存中移动的距离
4. 一旦声明, 数组里存储的数据类型和数组长度就都不能改变
5. 没有初始化的元素使用类型的空值


设置长度以后没有初始化的值使用默认值
元素个数不能大于设置的size
如果忽略size, 会根据元素数自动设置大小, 确定大小以后设置range意外的值会index out of range
类型相同的数组(长度和元素类型都相同)的素族可以相互赋值

*/
package main

import "fmt"

func main() {
	fmt.Println("-------------------- 自动设置长度")
	var b = []string{"aa", "bb", "cc"}
	var b2 = [...]int{1, 2, 3, 4, 5}

	fmt.Println("-------------------- 给特定的元素指定值")
	var b3 = [5]int{1: 220, 3: 4411}
	fmt.Println(b, b2, b3)

	fmt.Println("-------------------- 多维数组")
	var d [2][4]int
	d[0][2] = 6666
	fmt.Println(d)

	var e = [2][4]int{
		{1, 2, 3, 4},
		{5, 6, 7, 8},
	}

	e1 := [3][9]int{0: {5: 1}, 1: {33, 44, 55}}
	fmt.Println(e, e1)

	fmt.Println("-------------------- 指针数组")
	// 用整型指针初始化索引为0和2的元素, 其他没有初始化的为nil
	g := [5]*int{0: new(int), 2: new(int)}
	//给元素赋值
	*g[0] = 10
	*g[2] = 22
	//没有初始化的元素不能赋值, 否则报错
	//*g[4] = 44

	//指针数组赋值给另一个指针数组, 复制的是指针地址, 而不是指针地址保存的值
	var g1 [5]*int
	g1 = g
	fmt.Println(g, g1)
	*g1[2] = 33
	fmt.Println(*g[2], *g1[2])

	fmt.Println("-------------------- 数组当作参数")
	//可以直接传递值也可以传递指针
	//未定义长度的数组只能传给不限制数组长度的函数
	//定义了长度的数组只能传给限制了相同数组长度的函数
	var f1 = array1(&b2)
	var f2 = array2(b2)
	fmt.Println(f1, f2)
}
func array1(l *[5]int) int {
	var a = l[0] + l[4]
	return a
}

func array2(l [5]int) int {
	var a = l[0] + l[4]
	return a
}
