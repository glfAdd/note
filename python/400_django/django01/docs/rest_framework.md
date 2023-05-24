```
Django rest framework 简称 DRF
```

```
https://blog.51cto.com/ch3nnn/5483713
https://www.cnblogs.com/kuck/p/11921941.html




```



### GenericAPIView

```
类属性: 
queryset: 指定当前类视图下用到的查询集
serializer_class: 指定当前类视图下用到的序列化器类
search_fields: 指定模型类中前端能够支持搜索的字段
ordering_fields: 指定模型类中前端能够支持排序的字段
filter_backends: 指定在特定的类视图下进行操作（例如过滤和排序），优先级高于全局
pagination_class: 指定在特定的类视图下指定分页引擎类，优先级高于全局
look_field: models中的字段名或者url中的参数名，参数默认为pk
look_url_kwarg: 指定url路由条目中外键的路径参数名称，lookup_url_kwarg默认为None；如果lookup_url_kwarg默认为None，那么lookup_url_kwarg与look_field相同（pk）
lookup_url_kwarg指定url路由条目中外键的路径参数名称

方法: 
get_queryset(): 获取查询集对象
get_object(): 获取单个模型类对象
get_serializer(): 获取序列化的类，返回的是序列化对象
get_serializer_class(): 获取我们定义的序列化类
get_serializer_context(): 获取上下文信息，主要有 request， format， view（self)
filter_queryset(): 过滤 queryset ， 只要传入 queryset，返回过滤后的 queryset。
paginate_queryset(): 
1. 判断是否有分页属性
2. 没有则返回None，有则进行分页操作，
get_paginated_response():  返回的是具有额外属性 Response 的分页对象
paginator(): 
1. 判断是否有分页对象
2. 有则赋值给 self._paginator 没有则赋值 None 给 self._paginator
```