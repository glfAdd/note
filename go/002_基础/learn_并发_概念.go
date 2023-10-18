/*
1.
Go 语言里的并发指的是能让某个函数独立于其他函数运行的能力。
当一个函数创建为 goroutine 时,Go 会将其视为一个独立的工作单元。这个单元会被调度到可用的逻辑处理器上执行。
Go 语言运行时的调度器是一个复杂的软件,能管理被创建的所有 goroutine 并为其分配执行时间。
这个调度器在操作系统之上,将操作系统的线程与语言运行时的逻辑处理器绑定,并在逻辑处理器上运行 goroutine。
调度器在任何给定的时间,都会全面控制哪个 goroutine 要在哪个逻辑处理器上运行。
Go 语言的并发同步模型来自一个叫作通信顺序进程(Communicating Sequential Processes, CSP) 的范型(paradigm)
CSP 是一种消息传递模型,通过在 goroutine 之间传递数据来传递消息,而不是对数据进行加锁来实现同步访问。
用于在 goroutine 之间同步和传递数据的关键数据类型叫作通道 (channel)
使用多个逻辑处理器并不意味着性能更好

2.
操作系统会在物理处理器上调度线程来运行,而 Go 语言的运行时会在逻辑处理器上调度goroutine来运行。 每个逻辑处理器都分别绑定到单个操作系统线程。
在 1.5 版本以后, Go语言的运行时默认会为每个可用的物理处理器分配一个逻辑处理器。
在 1.5 版本之前的版本中,默认给整个应用程序只分配一个逻辑处理器。
这些逻辑处理器会用于执行所有被创建的goroutine。即便只有一个逻辑处理器,Go也可以以神奇的效率和性能,并发调度无数个goroutine。

3.
有时,正在运行的 goroutine 需要执行一个阻塞的系统调用,如打开一个文件。当这类调用发生时,线程和 goroutine 会从逻辑处理器上分离,该线程会继续阻塞,等待系统调用的返回。
与此同时,这个逻辑处理器就失去了用来运行的线程。所以,调度器会创建一个新线程,并将其绑定到该逻辑处理器上。
之后,调度器会从本地运行队列里选择另一个 goroutine 来运行。一旦被阻塞的系统调用执行完成并返回,对应的 goroutine 会放回到本地运行队列,而之前的线程会保存好,以便之后可以继续使用。

4.
如果一个 goroutine 需要做一个网络 I/O 调用,流程上会有些不一样。在这种情况下, goroutine 会和逻辑处理器分离,并移到集成了网络轮询器的运行时。
一旦该轮询器指示某个网络读或者写操作已经就绪,对应的 goroutine 就会重新分配到逻辑处理器上来完成操作。
调度器对可以创建的逻辑处理器的数量没有限制,但语言运行时默认限制每个程序最多创建 10 000 个线程。这个限制值可以通过调用 runtime/debug 包的 SetMaxThreads 方法来更改。如果程序试图使用更多的线程,就会崩溃。

5.
并发(concurrency)不是并行(parallelism).
并行是让不同的代码片段同时在不同的物理处理器上执行。并行的关键是同时做很多事情,
而并发是指同时管理很多事情,这些事情可能只做了一半就被暂停去做别的事情了。
在很多情况下,并发的效果比并行好,因为操作系统和硬件的总资源一般很少,但能支持系统同时做很多事情

6.
如果希望让 goroutine 并行,必须使用多于一个逻辑处理器。
当有多个逻辑处理器时,调度器会将 goroutine 平等分配到每个逻辑处理器上。这会让 goroutine 在不同的线程上运行。不过要想真的实现并行的效果,用户需要让自己的程序运行在有多个物理处理器的机器上。
只有在有多个逻辑处理器且可以同时让每个 goroutine 运行在一个可用的物理处理器上的时候,goroutine 才会并行运行

7.
基于调度器的内部算法,一个正运行的 goroutine 在工作结束前,可以被停止并重新调度。调度器这样做的目的是防止某个 goroutine 长时间占用逻辑处理器。
当 goroutine 占用时间过长时, 调度器会停止当前正运行的 goroutine,并给其他可运行的 goroutine 运行的机会





*/

/*
Go 语言支持并发，我们只需要通过 go 关键字来开启 goroutine 即可。
goroutine 是轻量级线程，goroutine 的调度是由 Golang 运行时进行管理的。
goroutine 语法格式：
	go 函数名( 参数列表 )

同一个程序中的所有 goroutine 共享同一个地址空间







*/
package main

import (
	"fmt"
	"runtime"
	"sync"
)

func main() {
	/*
		分配一个逻辑处理器给调度器使用
		这个函数允许程序更改调度器可以使用的逻辑处理器的数量。
		如果不想在代码里做这个调用,也可以通过修改和这个函数名字一样的环境变量的值来更改逻辑处理器的数量。
		给这个函数传入 1,是通知调度器只能为该程序使用一个逻辑处理器
	*/
	runtime.GOMAXPROCS(2)

	/*
		WaitGroup 是一个计数信号量,可以用来记录并维护运行的 goroutine。如果 WaitGroup的值大于 0, Wait 方法就会阻塞
		将这个 WaitGroup 的值设置为 2,表示有两个正在运行的 goroutine
	*/
	var wg sync.WaitGroup
	wg.Add(1)
	fmt.Println("Start Goroutines")

	//声明一个匿名函数,并创建一个 goroutine
	go func() {
		//在函数退出时调用 Done 来通知 main 函数工作已经完成
		defer wg.Done()
		for count := 0; count < 50; count++ {
			fmt.Println(count)
			runtime.Gosched()
		}
	}()

	go func() {
		defer wg.Done()
		for i := 1000; i < 1050; i++ {
			fmt.Println(i)
			//当前 goroutine 从线程退出,并放回到队列
			runtime.Gosched()
		}
	}()

	//等待 goroutines 结束
	fmt.Println("waiting")
	wg.Wait()

	fmt.Println("over")

}
