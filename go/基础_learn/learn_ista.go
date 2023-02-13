/*
1. iota 只能给常量赋值
2. 常量生成器, 每行一个, 自动累加1, 初始值0
3. iota 每次遇到 const 时重置为 0
4. 可以只写一个 iota
5. 如果同一行写多个, 这一行的值都相同
*/

package main

import "fmt"

func main() {
	const (
		a = iota
		b = iota
		c = iota
	)

	const (
		d = iota
		e
		f
	)
	fmt.Printf("a = %d, b = %d, c = %d , d= %d, e = %d, f = %d\n", a, b, c, d, e, f)

	const (
		m = iota
		n
		x, y = iota, iota
	)
	fmt.Printf("m = %d, n = %d, x = %d, y = %d", m, n, x, y)
}
