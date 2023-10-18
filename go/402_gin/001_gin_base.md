##### 参考

- [ ] [重点 1](https://www.topgoer.com/gin%E6%A1%86%E6%9E%B6/%E4%BC%9A%E8%AF%9D%E6%8E%A7%E5%88%B6/cookie%E4%BB%8B%E7%BB%8D.html)
- [ ] https://www.w3cschool.cn/golang_gin/golang_gin-3vd23lry.html

##### Restful API

```
gin 支持 Restful (Representational State Transfer) 风格的 API

获取 /blog/getXxx Get blog/Xxx
添加 /blog/addXxx POST blog/Xxx
修改 /blog/updateXxx PUT blog/Xxx
删除 /blog/delXxxx DELETE blog/Xxx
```

##### 简单项目

- 初始化项目

  ```bash
  $ mkdir k8s-service-gin
  $ cd k8s-service-gin
  # 初始化 go mod
  $ go mod init k8s-service-gin
  # 安装 gin
  $ go get -u github.com/gin-gonic/gin
  ```

- examp.go

  ```go
  package main
  
  import "github.com/gin-gonic/gin"
  
  func main() {
  	r := gin.Default()
  	r.GET("/ping", func(c *gin.Context) {
  		c.JSON(200, gin.H{
  			"message": "pong",
  		})
  	})
  	r.Run() // 监听并在 0.0.0.0:8080 上启动服务
  }
  ```

- 运行

  ```bash
  $ go run example.go
  ```

- 访问

  ```
  http://127.0.0.1:8080/ping
  ```

##### 项目目录结构

https://www.kancloud.cn/lhj0702/sockstack_gin/1805357 1

https://juejin.cn/post/7002406442875486245
https://18211167516.github.io/Go-Gin-Api/%E6%A0%B8%E5%BF%83%E6%9E%B6%E6%9E%84/

##### 路由

https://chai2010.cn/advanced-go-programming-book/ch5-web/ch5-02-router.html





##### 获取 api 参数

- example.go

  ```go
  package main
  
  import (
  	"github.com/gin-gonic/gin"
  	"net/http"
  	"strings"
  )
  
  func main() {
    // 默认使用了2个中间件Logger(), Recovery()
  	r := gin.Default()
  	r.GET("/user/:name/*action", func(c *gin.Context) {
  		name := c.Param("name")
  		action := c.Param("action")
  		//截取/
  		action = strings.Trim(action, "/")
  		c.String(http.StatusOK, name+" is "+action)
  	})
  	//监听端口
  	r.Run(":8000")
  }
  ```

- 访问

  ```
  http://127.0.0.1:8000/user/aaa/123123
  ```

##### 获取 url 参数

- example.go

  ```go
  package main
  
  import (
  	"fmt"
  	"github.com/gin-gonic/gin"
  	"net/http"
  )
  
  func main() {
  	r := gin.Default()
  	r.GET("/user", func(c *gin.Context) {
  		name := c.DefaultQuery("name", "枯藤")
  		c.String(http.StatusOK, fmt.Sprintf("hello %s", name))
  	})
  	r.Run()
  }
  ```

- 访问

  ```
  http://127.0.0.1:8000/user?name=aaa
  ```

##### 获取 json 参数

http 常用表单格式

```
application/json
application/x-www-form-urlencoded
application/xml
multipart/form-data
```

- examp.go

  ```go
  package main
  
  import (
  	"github.com/gin-gonic/gin"
  	"net/http"
  )
  
  // 定义接收数据的结构体
  type userInfo struct {
  	UserName string `json:"username" from:"username"`
  	Passwd   string `json:"passwd" from:"passwd"`
  }
  
  func main() {
  	r := gin.Default()
  	r.POST("/login", func(c *gin.Context) {
  		userInfo := &userInfo{}
  		// ShouldBindJSON 给结构体赋值
  		if err := c.ShouldBindJSON(&userInfo); err == nil {
  			// gin.H封装了生成json数据的工具
  			c.JSON(http.StatusOK, gin.H{
  				"username": userInfo.UserName,
  				"passwd":   userInfo.Passwd,
  				"action":   123,
  			})
  
  		} else {
  			// 响应结构体
  			c.JSON(http.StatusBadRequest, userInfo)
  		}
  	})
  	r.Run(":8000")
  }
  ```

- 访问

  ```
  http://127.0.0.1:8000/login
  post
  json
  {
      "username": "Tom",
      "passwd": "123"
  }
  ```

  

##### group

outes group 是为了管理一些相同的URL

- exapmle.go

  ```go
  package main
  
  import (
  	"github.com/gin-gonic/gin"
  )
  
  func main() {
  	r := gin.Default()
  	v1 := r.Group("/v1")
  	v2 := r.Group("/v2")
  	// {} 是书写规范
  	{
  		v1.GET("/login", login)
  		v1.GET("/logout", logout)
  	}
  	{
  		v2.GET("/login", login)
  		v2.GET("/logout", logout)
  	}
  	r.Run(":8000")
  }
  
  func login(c *gin.Context) {
  	c.String(200, "login")
  }
  func logout(c *gin.Context) {
  	c.String(200, "logout")
  }
  ```

- 访问

  ```
  http://127.0.0.1:8000/v1/login
  http://127.0.0.1:8000/v1/logout
  
  http://127.0.0.1:8000/v2/login
  http://127.0.0.1:8000/v2/logout
  ```

##### 重定向

- example.go

  ```go
  package main
  
  import (
  	"net/http"
  
  	"github.com/gin-gonic/gin"
  )
  
  func main() {
  	r := gin.Default()
  	r.GET("/index", func(c *gin.Context) {
  		c.Redirect(http.StatusMovedPermanently, "https://www.baidu.com/")
  	})
  	r.Run(":8000")
  }
  ```

- 访问

  ```
  ```

##### 同步 / 异步

- exampl.go

  ```go
  package main
  
  import (
  	"log"
  	"time"
  
  	"github.com/gin-gonic/gin"
  )
  
  func main() {
  	// 默认使用了2个中间件Logger(), Recovery()
  	r := gin.Default()
  	// 1.异步
  	r.GET("/long_async", func(c *gin.Context) {
  		// 需要搞一个副本
  		copyContext := c.Copy()
  		// 异步处理
  		go func() {
  			time.Sleep(5 * time.Second)
  			log.Println("异步执行：" + copyContext.Request.URL.Path)
  		}()
  	})
  	// 2.同步
  	r.GET("/long_sync", func(c *gin.Context) {
  		time.Sleep(5 * time.Second)
  		log.Println("同步执行：" + c.Request.URL.Path)
  	})
  
  	r.Run(":8000")
  }
  ```

- 访问

  ```
  
  ```

##### 中间件

所有请求都经过此中间件

- example.go

  ```go
  package main
  
  import (
  	"fmt"
  	"github.com/gin-gonic/gin"
  	"time"
  )
  
  // MiddleWare 定义中间
  func MiddleWare() gin.HandlerFunc {
  	return func(c *gin.Context) {
  		t := time.Now()
  		fmt.Println("中间件开始执行了")
  		// 设置变量到Context的key中，可以通过Get()取
  		c.Set("request", "中间件")
  		status := c.Writer.Status()
  		fmt.Println("中间件执行完毕", status)
  		t2 := time.Since(t)
  		fmt.Println("time:", t2)
  	}
  }
  
  func main() {
  	r := gin.Default()
  	// 注册中间件
  	r.Use(MiddleWare())
  	// {}为了代码规范
  	{
  		r.GET("/index", func(c *gin.Context) {
  			// 取值
  			req, _ := c.Get("request")
  			fmt.Println("request:", req)
  			// 页面接收
  			c.JSON(200, gin.H{"request": req})
  		})
  
  	}
  	r.Run(":8000")
  }
  ```

- 访问

  ```
  
  ```

##### 局部中间件

给某个函数增加日志

- example.go

  ```go
  package main
  
  import (
  	"fmt"
  	"github.com/gin-gonic/gin"
  	"time"
  )
  
  func MiddleWare() gin.HandlerFunc {
  	return func(c *gin.Context) {
  		t := time.Now()
  		fmt.Println("中间件开始执行了")
  		// 设置变量到Context的key中，可以通过Get()取
  		c.Set("request", "中间件")
  		// 执行函数
  		c.Next()
  		// 中间件执行完后续的一些事情
  		status := c.Writer.Status()
  		fmt.Println("中间件执行完毕", status)
  		t2 := time.Since(t)
  		fmt.Println("time:", t2)
  	}
  }
  
  func main() {
  	r := gin.Default()
  	//局部中间键使用
  	r.GET("/index", MiddleWare(), func(c *gin.Context) {
  		req, _ := c.Get("request")
  		fmt.Println("request:", req)
  		c.JSON(200, gin.H{"request": req})
  	})
  	r.Run(":8000")
  }
  ```

- 访问

  ```
  
  ```

##### Next()

> https://blog.dianduidian.com/post/gin-%E4%B8%AD%E9%97%B4%E4%BB%B6next%E6%96%B9%E6%B3%95%E5%8E%9F%E7%90%86%E8%A7%A3%E6%9E%90/
>
> https://segmentfault.com/q/1010000020256918
>
> 

```

```

##### handler

```
```

##### cookie

- example.go

  ```go
  ```

- 访问

  ```
  ```

##### session

##### 参数验证

##### 自定义参数验证

##### 日志

