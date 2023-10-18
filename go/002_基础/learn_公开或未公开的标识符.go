/*
当一个标识符的名字以小写字母开头时,这个标识符就是未公开的,即包外的代码不可见
当一个标识符以大写字母开头,这个标识符就是公开的,即被包外的代码可见
永远不能显式创建一个未公开的类型的变量,不过短变量声明操作符可以这么做。




*/

package main

type myInt1 int
type MyInt2 int

//类型未公开
type animal3 struct {
	//公开字段
	Age int
	//未公开字段
	name string
}

//将工厂函数命名为 New 是 Go 语言的一个习惯
func New(number int) animal3 {
	return animal3{Age: number}
}

//类型公开
type Cat struct {
	//嵌入的类型未公开
	//即便内部类型是未公开的,内部类型里声明的字段依旧是公开的。既然内部类型的标识符提升到了外部类型,这些公开的字段也可以通过外部类型的字段的值来访问
	animal3
	//公开字段
	Name string
}

func main() {

}
