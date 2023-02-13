/*
http://maoqide.live/post/golang/golang-data-race-detector/

竞争检测器
在同一个线程中执行多个 goroutine, 有数据安全问题
当两个 goroutine 同时访问同一个变量并且至少有一个是写入时，就会发生 data race(数据竞争)

命令
	$ go test -race mypkg    // to test the package
	$ go run -race mysrc.go  // to run the source file
	$ go build -race mycmd   // to build the command
	$ go install -race mypkg // to install the package

 $ go run -race test.go
==================
WARNING: DATA RACE
Write at 0x000000555e40 by goroutine 7:
  main.printCount()
      /home/glfadd/Desktop/go_learn/test.go:21 +0x77

Previous write at 0x000000555e40 by goroutine 6:
  main.printCount()
      /home/glfadd/Desktop/go_learn/test.go:21 +0x77

Goroutine 7 (running) created at:
  main.main()
      /home/glfadd/Desktop/go_learn/test.go:15 +0x84

Goroutine 6 (running) created at:
  main.main()
      /home/glfadd/Desktop/go_learn/test.go:14 +0x6c
==================
Found 1 data race(s)
exit status 66




*/

package main

import (
	"runtime"
	"sync"
)

var wg sync.WaitGroup
var i int

func main() {
	runtime.GOMAXPROCS(1)
	wg.Add(2)
	go printCount()
	/*
		每个 goroutine 都会覆盖另一个 goroutine 的工作。这种覆盖发生在 goroutine 切换的时候。
		每个 goroutine 创造了一个 counter 变量的副本, 之后就切换到另一个 goroutine。
		当这个 goroutine再次运行的时候, counter 变量的值已经改变了,但是 goroutine 并没有更新自己的那个副本的值,
		而是继续使用这个副本的值,用这个值递增,并存回 counter 变量,结果覆盖了另一个 goroutine 完成的工作
	*/
	go printCount()
	wg.Wait()
}

func printCount() {
	defer wg.Done()
	for i = 0; i < 10; i++ {
		runtime.Gosched()
		i++
		println(i)
	}
}
