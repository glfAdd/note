/*









 */
package main

const (
	Ldate         = 1 << iota // 1<<0 = 000000001 = 1
	Ltime                     // 1<<1 = 000000010 = 2
	Lmicroseconds             // 1<<2 = 000000100 = 4
	Llongfile                 // 1<<3 = 000001000 = 8
	Lshortfile                // 1<<4 = 000010000 = 16
)
