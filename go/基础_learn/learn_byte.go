/*
本质是int类型
*/
package main

import "fmt"

func main() {
	var a byte
	var b byte = 'x'
	c := 'y'
	var d byte = 97
	fmt.Printf("a = %d,b = %d, c = %d\n", a, b, c)
	fmt.Printf("a = %c,b = %c, c = %c\n", a, b, c)

	//大小写相差32
	fmt.Printf("b1 = %c\n", 'A'+32)
	fmt.Printf("b2 = %d\n", d+32)
}
