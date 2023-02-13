/*
默认 case 最后自带 break 语句，匹配成功后就不会执行其他 case，如果我们需要执行后面的 case，可以使用 fallthrough


*/

package main

import (
	"fmt"
)

func main() {
	a := 1
	if a > 10 {
		fmt.Println("a > 10")
	} else if a == 10 {
		fmt.Println("a = 10")
	} else {
		fmt.Println("a < 10")
	}

	num := 90
	var lv string
	switch num {
	case 50:
		lv = "c"
		fmt.Println("A")
	case 70:
		lv = "B"
		fmt.Println("B")
	case 90:
		lv = "A"
		fmt.Println("C")
	default:
		lv = "D"
		fmt.Println("D")
	}

	switch {
	case lv == "A":
		fmt.Println("level A")
		fallthrough
	case lv == "B":
		fmt.Println("level B")
	case lv == "C":
		fmt.Println("level C")
	default:
		fmt.Println("level D")
	}

	//select {
	//case num = 1:
	//	fmt.Println("num > 1")
	//	fmt.Println(num)
	//case num = 10:
	//	fmt.Println("num > 10")
	//	fmt.Println(num)
	//default:
	//	fmt.Println("num > 10")
	//	fmt.Println(num)
	//}

}
