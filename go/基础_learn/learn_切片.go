/*
长度可变

1. 切片组成: 指向底层数组的指针、长度和容量
2. 底层数组的长度是指定的容量
3. 不管是使用 nil 切片还是空切片,对其调用内置函数 append 、 len 和 cap 的效果都是一样的
4. 只能访问切片范围内的元素
*/
package main

import (
	"fmt"
)

func main() {
	fmt.Println("-------------------- 创建长度为4的数组")
	// 在[]里指定的长度创建的就是数组
	e := [4]int{1, 2, 3, 4}
	e[0] = 100
	fmt.Println(e)

	fmt.Println("-------------------- 通过字面量确定切片的长度")
	a := []int{1, 2, 3, 4}

	//1. 指定了切片的长度为100
	//2. 第100个元素的默认值为aaa
	a2 := []string{99: "aaa"}
	//cap返回切片的容量
	fmt.Println(a, len(a), cap(a), a2)

	fmt.Println("-------------------- make 创建切片")
	//长度和容量都是5
	c := make([]int, 5)
	//长度2, 容量10. 长度不能大于容量
	d := make([]int, 2, 10)
	fmt.Println(c, d)

	fmt.Println("-------------------- nil切片")
	// 指针nil, 长度nil, 容量nil
	var f []int
	fmt.Println(f)

	fmt.Println("-------------------- 空切片")
	//空切片在底层数组包含 0 个元素,也没有分配任何存储空间
	g := make([]int, 0)
	h := []int{}
	fmt.Println(g, h)

	fmt.Println("-------------------- 通过切片创建的新切片, 底层相同")
	// 新切片的容量是底层数组长度减去开头部分
	m1 := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	m2 := m1[2:6]
	m2[1] = 400
	//1. append 返回新的切片
	//2. append时, m3还有容量, 在底层操作底层数组增加元素, 原来 "7" 的位置变成了 "500" ,所有使用这个底层数组的切片都受到了影响
	//3. append首先使用可用容量, 没有可用容量时创建新的底层数组. 将被引用的现有的值复制到新数组里,再追加新的值
	//4. 在切片的容量小于 1000 个元素时，总是会成倍地增加容量。一旦元素个数超过 1000，容量的增长因子会设为 1.25，也就是会每次增加 25%的容量(随着语言的演化，这种增长算法可能会有所改变)
	//5. 创建切片时设置切片的容量和长度一样, 就可以强制让新切片的第一个 append 操作创建新的底层数组，与原有的底层数组分离
	m3 := append(m2, 500)
	fmt.Println(m1, m2, m3)
	//手动设置切片的容量 [开始:结束:容量]
	//如果试图设置的容量比可用的容量还大,就会得到一个语言运行时错误 "panic: runtime error: slice bounds out of range [::50] with capacity 9"
	//可以方式切片之间互相影响
	m4 := m1[1:3:5]
	fmt.Println(m4)

	fmt.Println("-------------------- 切片追加")
	j1 := []int{101, 102, 103}
	j2 := []int{104, 105}
	j3 := append(j1, j2...)
	fmt.Println(j3)

	fmt.Println("-------------------- 遍历")
	//range返回两个值: 当前迭代到的索引位置, 该位置对应元素值的一份副本
	for index, value := range a {
		fmt.Println(index, value)
		value = 1000
	}
	for index := 1; index < 3; index++ {
		fmt.Println(index, a[index])
	}

	fmt.Println("-------------------- 多维切片")
	p1 := [][]int{{500}, {600, 700}}
	fmt.Println(p1)
	p1[0] = append(p1[0], 501)
	fmt.Println(p1)
	p2 := [][][]int{{{500}}, {{600, 700}}}
	fmt.Println(p2)

	fmt.Println("-------------------- 拷贝")
	//func copy(dst, src []Type) int
	//把切片src中的元素拷贝到切片dst中, 返回值为拷贝成功的元素个数.
	//如果src比dst长就截断, 如果src比dst短则只拷贝src那部分, 其他部分保持不变
	b1 := []string{"a", "b", "c"}
	b2 := []string{"e", "f"}
	b3 := copy(b2, b1)
	fmt.Println(b1, b2, b3)

	b4 := []string{"1", "2", "3", "4", "5"}
	b5 := copy(b4, b2)
	fmt.Println(b4, b5)

	fmt.Println("-------------------- 切片在函数见传递")
	//切片使用值传递的, 切片数据很小, 因为切片的数据包含在底层数组里,不属于切片本身.
	//在 64 位架构的机器上，一个切片需要 24 字节的内存：指针字段需要 8 字节，长度和容量字段分别需要 8 字节
	//由于与切片关联的数据包含在底层数组里，不属于切片本身，所以将切片复制到任意函数的时候，对底层数组大小都不会有影响。复制时只会复制切片本身，不会涉及底层数组
	//地址指针保存的是底层数组的指针

	fmt.Println("-------------------- 删除元素")
	c1 := []string{"a", "b", "c", "d", "e", "f", "g", "h"}
	fmt.Println(c1)
	//使用索引删除元素
	c2 := c1[1:3]
	fmt.Println(c2)

	//删除开头3个元素
	c3 := append(c1[:0], c1[3:]...)
	fmt.Println(c3)

	//删除中间的元素
	c4 := append(c1[:2], c1[4:]...)
	fmt.Println(c4)

	//为什么少了第一个元素? [d e f g h f g h]
	fmt.Println(c1)
}
