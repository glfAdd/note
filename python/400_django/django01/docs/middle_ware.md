```
middleware需要在settints.py的MIDDLEWARE中注册激活，MIDDLEWARE是一个列表，middleware的执行顺序是MIDDLEWARE 列表的索引顺序。

middleware 可以 request 请求到达django之后views之前，对request进行预处理。



process_request 方法如果返回 None，按MIDDLEWARE列表中的顺序执行完middleware后，到urls.py中匹配views，执行views。

process_request方法如果返回Httpresponse，如果当前middleware中没有process_response方法，则从此处middleware一层一层向上返回。

process_request方法如果返回Httpresponse，如果当前middleware中有process_response方法，则从当前middleware中process_response处一层一层向上返回。

```


```
process_request(request)
process_response(request,response)
process_view(request, view_func, view_args, view_kwargs)
process_exception(request, exception)
process_template_response(request, response)
```