package main

import "fmt"

func main() {
	var a1 string = "hello"
	var a2 string = "word"
	var a3 string = a1 + a2
	// 自动换行
	fmt.Println(a3)
	fmt.Printf(a1 + a2)
	fmt.Printf("\n")

	// Sprintf 返回字符串
	// Printf 标准输出
	var b1 int = 1
	var b2 string = "hello"
	var b3 = "---%d----%s"
	var b4 string = fmt.Sprintf(b3, b1, b2)
	fmt.Printf(b4)
	fmt.Printf(b3, b1, b2)

	// 	var a string = "home"
	// 	b := []byte(a)
	// 	b[0] = 'Z'
	// 	c := string(b)
	// 	fmt.Println(a, b, c)

	// 	//多行字符串使用 ``
	// 	e := `多行
	//   字符串`
	// 	fmt.Println(e)

}
