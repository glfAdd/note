/*





 */
package main

import (
	"runtime"
	"sync"
)

var (
	//goroutine都在修更改的变量
	number int
	//用来等待程序结束
	w sync.WaitGroup
	//定义代码临界区
	mutex sync.Mutex
)

func addNumber() {
	//在函数退出时调用 Done 来通知 main 函数工作已经完成
	defer w.Done()
	for i := 0; i < 2; i++ {
		//同一时刻只允许一个 goroutine 进入这个临界区
		mutex.Lock()
		{
			a := number
			//当前 goroutine 从线程退出,并放回到队列
			//当强制将当前 goroutine 退出当前线程后, 调度器会再次分配这个 goroutine 继续运行
			runtime.Gosched()
			a++
			number = a
		}
		//释放锁,允许其他正在等待的 goroutine 进入临界区
		mutex.Unlock()
	}
}

func main() {
	//等待2个 goroutine
	w.Add(2)
	//创建两个 goroutine
	go addNumber()
	go addNumber()
	println("waiting")
	//等待所有 goroutine 结束
	w.Wait()
	println("over")
}
