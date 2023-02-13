/*
1. 不能夸函数代码快跳转
2. goto定义的代码块只能goto调用
3. 跳转到goto的为位置继续向下执行

可以用于跳出for循环嵌套
处理异常. 再有异常的地方goto

*/
package main

import "fmt"

func main() {
	fmt.Println("1")
	goto End
	fmt.Println("2")
End:
	fmt.Println("goto end")
	fmt.Println("3")

}
