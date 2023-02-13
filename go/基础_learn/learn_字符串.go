/*


 */
package main

import "fmt"

func main() {
	// + 拼接字符串
	fmt.Println("hello" + "word")

	var a string = "home"
	b := []byte(a)
	b[0] = 'Z'
	c := string(b)
	fmt.Println(a, b, c)

	//多行字符串使用 ``
	e := `多行
  字符串`
	fmt.Println(e)

}
