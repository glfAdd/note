/*

声明可变参数函数的方式是在其参数类型前带上省略符 ... 前缀



*/

package main

import "fmt"

func testArgs(name ...string) {
	fmt.Println(name)
}
func main() {
	testArgs()
	testArgs("小明", "小红")

}
