/*
1. Map是一种无序的键值对的集合, 通过key来快速检索数据
2. 如果不初始化 map，那么就会创建一个 nil map。nil map 不能用来存放键值对

声明变量，默认 map 是 nil
var map_variable map[key_data_type]value_data_type

使用 make 函数
map_variable := make(map[key_data_type]value_data_type)


*/
package main

import "fmt"

func main() {
	fmt.Println("-------------------- 创建映射")
	//创建nil映射
	var a map[string]string
	//如果初始化直接赋值会报错
	//a["name"] = "Tome"
	//给nil映射初始化
	a = make(map[string]string)
	a["name"] = "Tom"

	//初始时创建默认值
	a2 := map[string]int{"age": 12, "num": 300}

	//数组作为value
	a3 := map[string][2]int{"address": {1, 2}, "all": [2]int{22, 33}}
	fmt.Println(a, a2, a3)

	fmt.Println("-------------------- 判断元素是否存在")
	//如果没有找到b为空字符串, c为false
	b, c := a["haha"]
	fmt.Println(b, c)

	fmt.Println("-------------------- 根据key删除元素")
	delete(a, "name")
	fmt.Println(a)

	fmt.Println("-------------------- 映射当作参数")
	//在函数间传递映射并不会制造出该映射的一个副本
	change(a)
	fmt.Println(a)

}

func change(item map[string]string) {
	//传递的item是指针, 不是副本
	item["name"] = "Lucy"
}
