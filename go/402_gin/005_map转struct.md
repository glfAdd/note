# mapstructure

通过结构体的 mapstructure 映射, 实现 map 到 struct 的转换

##### 文档

[官网](https://pkg.go.dev/github.com/mitchellh/mapstructure)

##### 安装

```bash
$ go get github.com/mitchellh/mapstructure
```

##### Decode

```
如果不使用 mapstructure, 则不能将带有下划线 _ 的变量赋值给结构体
```

```go
package main

import (
	"fmt"
	"github.com/mitchellh/mapstructure"
)

type Person struct {
	Name        string `mapstructure:"full_name"`
	Age         int    `mapstructure:"age"`
	AddressLine string `mapstructure:"address_line"`
}

func main() {
	data := map[string]interface{}{
		"full_name":    "John Doe",
		"age":          30,
		"address_line": "123 Main St",
	}

	var person Person
	err := mapstructure.Decode(data, &person)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	fmt.Println("Person:", person)
}
```

# json

利用结构体的 json 映射, 通过序列化和反序列化实现 map 与 struct 的装换

```go
package main

import (
	"encoding/json"
	"fmt"
)

type Person struct {
	Name        string `json:"full_name"`
	Age         int    `json:"age"`
	AddressLine string `json:"address_line"`
}

func main() {
	data := map[string]interface{}{
		"full_name":    "John Doe",
		"age":          30,
		"address_line": "123 Main St",
	}

	jData, jErr := json.Marshal(data)
	if jErr != nil {
		fmt.Println(jErr)
		return
	}

	var person Person
	err := json.Unmarshal(jData, &person)
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println("Person:", person)
}
```

