/*

sync/pool.go



这个包用于展示如何使用有缓冲的通道实现资源池, 来管理可以在任意数量的goroutine之间共享及独立使用的资源
这种模式在需要共享一组静态资源的情况(如共享数据库连接或者内存缓冲区)下非常有用
如果goroutine需要从池里得到这些资源中的一个, 它可以从池里申请,使用完后归还到资源池里





Pool 管理一组可以安全地在多个 goroutine 间共享的资源, 被管理的资源必须实现 io.Closer 接口



*/
package main

import (
	"io"
	"sync"
)

type Pool struct {
	m         sync.Mutex
	resources chan io.Closer
	factory   func() (io.Closer, error)
	closed    bool
}
