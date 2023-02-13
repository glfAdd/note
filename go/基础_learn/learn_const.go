/*
1. iota 只能给常量赋值
2. 常量生成器, 每行一个, 自动累加1
3. iota 每次遇到 const 时重置为 0
4. 可以只写一个 iota
5. 如果同一行写多个, 这一行的值都相同
*/

package main

import "fmt"

func main() {
	const a int = 1
	fmt.Printf("g = %d\n", a)

	// 自动推导类型
	const (
		b = 21
		c = 22.1
	)
	fmt.Printf("b = %d, c = %f\n", b, c)

	const (
		e = iota
		f = iota
		g = iota
	)

	const (
		h = iota
		i
		j
	)
	fmt.Printf("e = %d, f = %d, g = %d , h= %d, i = %d, j = %d\n", e, f, g, h, i, j)

	const (
		m = iota
		n
		o, p = iota, iota
		q    = "aaa"
		s    = iota
	)
	fmt.Printf("m = %d, n = %d, o = %d, p = %d, q = %s, s = %d\n", m, n, o, p, q, s)

	const (
		t = iota
		u
		v, w = iota, iota
		x    = iota
	)
	fmt.Printf("t = %d, u = %d, v = %d, w = %d , x = %d\n", t, u, v, w, x)

	//位移
	//??????
	const (
		a1 = iota
		b1
		c1 = 10 << iota
		d1 = 10 << iota
		e1
	)
	fmt.Printf("a1 = %d, b1 = %d, c1 = %d, d1 = %d, e1 = %d\n", a1, b1, c1, d1, e1)
}
