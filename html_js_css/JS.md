##### 发送json数据

```
$('#id').click(function(){
     var $btn = $(this);
         $btn.prop('disabled', true);
         if($('#id').hasClass('red')){
            return
         }else{
            $.ajax({
             type: 'GET',
                url:'https://www.easy-mock.com/mock/5ac4e25ad847035fb5080f18/example/xinde/assistant',
                contentType: 'application/json',
                data: JSON.stringify({
                    users: userList,
                    sendNum: $('#sendNum').val()
                }),
                success: function(response) {
                    if (response.status == 0) {
                        // 展示发送状态
                        for ( var i = 0; i < response.data.length; i++) {
                            if ( response.data[i].status ) {
                                $("#userList .user-item[data-id='" + response.data[i].id + "']").find('.user-status').text('发送成功');
                            } else {
                                $("#userList .user-item[data-id='" + response.data[i].id + "']").find('.user-status').text('发送失败：' + response.data[i].msg);
                            }
                            
                        }
                        $('#id').removeClass('red')

                    } else {
                        alert(response.msg);
                    }
                },
                error: function() {
                    alert('网络错误，请稍后再试!');
                }
    }); 
         }
    
})
```



#### JS

```python
var a;//变量定义，这个时候a是undefined，
a = "sss";//变量赋值，a是string类型。所以var只代表定义变量。


Number 数字类型，包括正数负数和小数
String 字符串，双引号单引号的都是字符串
Boolean 布尔数据类型，非零即真



```





#### PyExecJS

```javascript
# 安装
pip install PyExecJS


```



##### nodejs

```python
# 安装
https://nodejs.org/en/download/
```



```javascript
源码中给出， 可执行execjs的环境：

PyV8           = "PyV8"
Node           = "Node"
JavaScriptCore = "JavaScriptCore"
SpiderMonkey   = "SpiderMonkey"
JScript        = "JScript"
PhantomJS      = "PhantomJS"
SlimerJS       = "SlimerJS"
Nashorn        = "Nashorn"
```

