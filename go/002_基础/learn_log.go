/*

1. 日志格式枚举
const (
	Ldate         = 1 << iota     // 日期: 2009/01/23
	Ltime                         // 时间: 01:23:23
	Lmicroseconds                 // 毫秒级时间: 01:23:23.123123。该设置会覆盖 Ltime
	Llongfile                     // 完整路径的文件名和行号: /a/b/c/d.go:23
	Lshortfile                    // 最终的文件名元素和行号: d.go:23. 覆盖 Llongfile
	LstdFlags     = Ldate | Ltime // 标准日志记录器的初始值
)

2.
Fatal 系列函数用来写日志消息,然后使用 os.Exit(1) 终止程序
Panic 系列函数用来写日志消息,然后触发一个 panic
除非程序执行 recover 函数,否则会导致程序打印调用栈后终止

3.
将输出写到stdout ,将日志记录到 stderr







*/
package main

import (
	"io"
	"io/ioutil"
	"log"
	"os"
)

//可以给每个日志记录器配置一个单独日志记录器
var (
	//声明4个指针变量
	All     *log.Logger
	Info    *log.Logger
	Warning *log.Logger
	Error   *log.Logger
)

//在main前执行
func init() {
	//每行日志前缀. 一般全部大写
	log.SetPrefix("GLF LOG: ")
	//日志格式
	log.SetFlags(log.Ldate | log.Lmicroseconds | log.Llongfile)

	file, err := os.OpenFile("error.text", os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0666)
	if err != nil {
		log.Fatalln("open file error: ", err)
	}

	//New 函数,它创建并正确初始化一个 Logger 类型的值。函数 New 会返回新创建的值的地址
	/*
		Discard 变量的类型被声明 为 io.Writer 接口类型,并被给定了一个 devNull 类型的值 0
		基于 devNull 类型实现的 Write 方法,会忽略所有写入这一变量的数据, 当某个等级的日志不重要时,使用 Discard 变 量可以禁用这个等级的日志。
	*/
	All = log.New(ioutil.Discard, "ALL", log.Ldate|log.Lmicroseconds|log.Llongfile)
	Info = log.New(os.Stdout, "INFO", log.Ldate|log.Lmicroseconds|log.Llongfile)
	Warning = log.New(os.Stdout, "WARNING", log.Ldate|log.Lmicroseconds|log.Llongfile)
	Error = log.New(io.MultiWriter(file, os.Stderr), "ERROR", log.Ldate|log.Lmicroseconds|log.Llongfile)

}

func main() {
	log.Printf("Println 写到标准日志记录器")
	All.Printf("all msg")
	Info.Printf("info msg")
	Warning.Printf("warning msg")
	Error.Printf("error msg")
	log.Fatalf("系列函数用来写日志消息,然后使用 os.Exit(1) 终止程序")

}
