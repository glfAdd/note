/*
range关键字用于for循环中迭代数组(array)、切片(slice)、通道(channel)或集合(map)的元素. 在数组和切片中它返回元素的索引和索引对应的值，在集合中返回 key-value 对
*/
package main

import "fmt"

func main() {
	a := []int{1, 2, 3, 4}
	for index, value := range a {
		fmt.Println(index, value)
	}
	for _, value := range a {
		fmt.Println(value)
	}
	for index, value := range "776655" {
		fmt.Println(index, value)
	}
	for key, value := range map[string]string{"name": "Tom", "tel": "010-1141223"} {
		fmt.Println(key, value)
	}
	//集合如何只有一个变量接收, 则只返回key
	for i := range map[string]string{"name": "Tom", "tel": "010-1141223"} {
		fmt.Println(i)
	}

}
