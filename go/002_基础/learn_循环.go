/*


 */
package main

import "fmt"

func main() {
	for i := 6; i <= 10; i++ {
		fmt.Println(i)
	}

	num := 1
	for ; num < 4; {
		num++
	}
	fmt.Println(num)

	//无限循环
	a := 1
	for {
		if a > 50 {
			break
		} else {
			a++
			continue
		}
	}
	fmt.Println(a)

	//循环便利元素
}
