""" ============================ 正向代理
http server location 中设置, 一般在server中
正向代理, 不支持正向代理到https

resolver address ... [valid=time];
    address: DNS服务器ip地址, 端口号不指定默认53
    time: 数据包在网络中的有效时间
            在访问站点时，有很多情况使得数据包在一定时间内不能被传递到目的地，但是又不能让该数据包无期限地存在，
            需要设定一段时间，当数据包在这段时间内没有到达目的地，就会被丢弃，然后发送者会接收到一个消息，并决定是否要重发该数据包。
    - resolver 127.0.0.1 [::1]:5353 valid=30s;


resolver_timeout time;
    DNS解析域名超时时间


proxy_pass URL;
    设置代理服务器的协议和地址
    - proxy_pass http:tests.com;
"""

""" ============================ 实例
1. DNS服务器使用8.8.8.8, DNS端口号使用默认53
2. 代理服务器监听端口号82
3. 收到所有请求由location处理

server{
    resolver 8.8.8.8;
    listen 82;
    location / {
        proxy_pass http://test.com;
    }
}
"""
