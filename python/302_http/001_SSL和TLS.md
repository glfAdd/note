##### SSL 和 TLS关系

```
SSL Secure Sockets Layer 安全套接层协议
TLS Transport Layer Security 传输层安全协议

TLS 与 SSL 在传输层(如TCP)与应用层（如HTTP）之间对网络连接进行加密

1994年，NetScape 公司设计了 SSL 协议的1.0版，但是未发布。
1995年，NetScape 公司发布 SSL 2.0版，很快发现有严重漏洞。
1996年，SSL 3.0 版问世，得到大规模应用。
1999年，互联网标准化组织 ISOC 接替 NetScape 公司，发布了 SSL 的升级版 TLS 1.0 版(或称 SSL 3.1)
2006年, TLS 1.1(或称SSL 3.2)
2008，TLS 1.2 (或称SSL 3.3)
```



```
SSL 是个二进制协议，与 http 完全不同, 其流量是承载在另一个端口上的（SSL通常是有端口443承载的）。如果SSL和http流量都从端口80到达，大部分web服务器会将二进制SSL流量理解为错误的http并关闭连接。将安全服务进一步整合到http层中去就无需使用多个目的端口了，在实际中这样不会引发严重的问题。



HTTPS 在HTTP 的基础下加入SSL 层
```

