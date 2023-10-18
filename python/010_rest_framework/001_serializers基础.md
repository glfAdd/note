##### 参考

- [ ] https://www.cnblogs.com/AbnerLc/p/11953544.html
- [ ] https://www.cnblogs.com/x945669/p/13307795.html
- [ ] https://blog.csdn.net/prigilm/article/details/121150796

choices 枚举

- [ ] https://www.jianshu.com/p/c7dff360c941
- [ ] 



##### 文档





##### 安装

```bash
```

##### 

```
这个数据从字典或者Queryset对象转为json的操作，便是序列化类StudentSerializes做的


# Serializer的构造方法为：
Serializer(instance=None, data=empty, **kwarg)
"""
1）用于序列化时，将模型类对象传入instance参数
2）用于反序列化时，将要被反序列化的数据传入data参数
3）除了instance和data参数外，在构造Serializer对象时，还可通过context参数额外添加数据
"""
serializer = AccountSerializer(account, context={'request': request})
"""
1、使用序列化器的时候一定要注意，序列化器声明了以后，不会自动执行，需要我们在视图中进行调用才可以。
2、序列化器无法直接接收数据，需要我们在视图中创建序列化器对象时把使用的数据传递过来。
3、序列化器的字段声明类似于我们前面使用过的表单系统。
4、开发restful api时，序列化器会帮我们把模型数据转换成字典.
5、drf提供的视图会帮我们把字典转换成json,或者把客户端发送过来的数据转换字典.
"""

```

