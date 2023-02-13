/*

 */
package main

import "fmt"

func test10(a int) int {
	if a < 2 {
		return a
	}
	return test10(a-2) + test10(a-1)

}
func main() {
	var i int
	for i = 0; i < 10; i++ {
		b := test10(i)
		fmt.Println(b)
	}
}
