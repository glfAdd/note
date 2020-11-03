"""
api压力测试工具

apt-get install apache2-utils

ab -n 100000 -c 500 http://47.93.122.31:8080/
ab -n 100000 -c 500 http://47.93.122.31:15743/v1/tool/ip/proxy


用法：ab [选项] [http [s] :/ /主机名[：端口] /路径
-n  个请求执行的请求数
-c  多个请求的并发数
-t  最大的timeLimit秒。等待回应
-b  windowSize的大小，TCP发送/接收缓冲区，以字节为单位
-p  postfile文件包含数据的POST。也请记住集-T
-U  PUTFILE文件包含数据的PUT。也请记住集-T
-v  冗长多少故障排除信息打印
-w HTML表格打印出结​​果
-i   使用的头，而不是GET
-x  属性字符串插入表属性
-y  属性字符串插入TR属性
-z  属性作为TD或TH属性的字符串插入
-C 属性的cookie，例如添加。 “阿帕奇= 1234。 （可重复）
-H 属性添加任意标题行，例如。 “接受编码：gzip”插入后一切正常的标题行。 （可重复）
-A 属性添加基本的WWW认证，属性冒号分隔的用户名和密码。
-P 属性基本代理身份验证，属性添加冒号分隔的用户名和密码。
-X 代理：端口访问代理服务器使用的端口号
-V 打印版本号并退出
-k 使用HTTP K​​eepAlive功能
-d 不显示百分担任表。
-S 不显示信心估计和警告。
-g 的文件名输出收集的数据与gnuplot格式的文件。
-e 名输出百分比CSV文件服
-r 不退出套接字接收错误。
-h 显示用法信息（此消息）
-Z 的密码组指定SSL / TLS加密套件（见OpenSSL密码）
-f  协议指定SSL / TLS协议（SSL3，TLS1或ALL）
"""

"""
测试结果解析
 $ ab -n 100000 -c 500 http://47.93.122.31:8080/
This is ApacheBench, Version 2.3 <$Revision: 1843412 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 47.93.122.31 (be patient)
Completed 10000 requests
Completed 20000 requests
Completed 30000 requests
Completed 40000 requests
Completed 50000 requests
Completed 60000 requests
Completed 70000 requests
Completed 80000 requests
Completed 90000 requests
Completed 100000 requests
Finished 100000 requests


Server Software:        
Server Hostname:        47.93.122.31
Server Port:            8080

Document Path:          /
Document Length:        15 bytes                HTTP响应数据的正文长度

Concurrency Level:      500                     并发数
Time taken for tests:   68.986 seconds          本次测试总共花费的时间
Complete requests:      100000                  本次测试总共发起的请求数量
Failed requests:        0                       失败的请求数量
Total transferred:      13200000 bytes          所有请求的响应数据长度总和
HTML transferred:       1500000 bytes           所有请求的响应数据中正文数据的总和，也就是减去了Total transferred中HTTP响应数据中的头信息的长度
Requests per second:    1449.57 [#/sec] (mean)  平均每秒完成请求数. 吞吐量，计算公式：Complete requests/Time taken for tests  总请求数/处理完成这些请求数所花费的时间
Time per request:       344.931 [ms] (mean)     用户平均请求等待时间，计算公式：Time token for tests/（Complete requests/Concurrency Level）。处理完成所有请求数所花费的时间/（总请求数/并发用户数）     
Time per request:       0.690 [ms] (mean, across all concurrent requests)       服务器完成一个请求的时间. 服务器平均请求等待时间，计算公式：Time taken for tests/Complete requests，正好是吞吐率的倒数。Time per request/Concurrency Level
Transfer rate:          186.86 [Kbytes/sec] received                            表示这些请求在单位时间内从服务器获取的数据长度，计算公式：Total trnasferred/ Time taken for tests，这个统计很好的说明服务器的处理能力达到极限时，其出口宽带的需求量。

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        9  171 128.1    147    3146
Processing:    17  166  87.2    146    2230
Waiting:        6  165  86.8    146    2229
Total:         26  337 160.0    305    3265

Percentage of the requests served within a certain time (ms)
  50%    305        有50%的请求都是在305毫秒完成
  66%    320        有66%的请求都是在320毫秒完成
  75%    331
  80%    338
  90%    388
  95%    600
  98%    728
  99%    919
 100%   3265 (longest request)

一个请求的响应时间可以分成
    网络链接（Connect）
    系统处理（Processing）
    等待（Waiting）三个部分
min         最小值 
mean        平均值
[+/-sd]     标准差也称均方差, 表示数据的离散程度，数值越大表示数据越分散，系统响应时间越不稳定。 
median      中位数
max         最大值了。



"""
