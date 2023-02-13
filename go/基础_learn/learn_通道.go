/*
通道（channel）是用来传递数据的一个数据结构。
通道可用于两个 goroutine 之间通过传递一个指定类型的值来同步运行和通讯。操作符 <- 用于指定通道的方向，发送或接收。如果未指定方向，则为双向通道。
默认情况下，通道是不带缓冲区的。发送端发送数据，同时必须有接收端相应的接收数据。


缓冲区
1. 带缓冲区的通道允许发送端的数据发送和接收端的数据获取处于异步状态，就是说发送端发送的数据可以放在缓冲区里面，可以等待接收端去获取数据，而不是立刻需要接收端去获取数据
2. 缓冲区有大小是有限, 缓冲区一满，数据发送端就无法再发送数据. 接收方在有值可以接收, 之前会一直阻塞
3. 如果通道不带缓冲，发送方会阻塞直到接收方从通道中接收了值
*/

package main

import "fmt"

func testChan(m []int, n chan int) {
	tmp := 0
	for _, v := range m {
		tmp += v
	}
	//把tmp发送到通道n
	n <- tmp
}

func main() {
	fmt.Println("-------------------- 通道")
	a := []int{1, 2, 3, 4}
	//创建通道
	b := make(chan int)
	go testChan(a, b)
	//从通道b获取数据并赋值个变量c
	c := <-b
	fmt.Println(c)

	fmt.Println("-------------------- 通道缓冲区")
	d := make(chan string, 2)
	d <- "aaa"
	d <- "bbb"
	// 从通道获取值
	h := <-d
	fmt.Println(h)

	fmt.Println("-------------------- 关闭通道")
	//关闭后的通道不能再使用
	e := make(chan int, 10)
	e <- 1
	e <- 2
	e <- 3
	e <- 44
	e <- 55
	close(e)

	fmt.Println("-------------------- 遍历通道")
	//如果通道不关闭, 那么rang 函数就不会结束, 从而在接收第5个数据的时候就阻塞了
	for i := range e {
		fmt.Println(i)
	}

}
