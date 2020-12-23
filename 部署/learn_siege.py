""" ============================ mac 安装
确保open files足够大, 否则会报TOO MANY FILES OPEN错误, 通过 ulimit -a 查看
使用sudo ulimit -n 10000可以修改该值, 临时生效


安装siege
wget http://download.joedog.org/siege/siege-latest.tar.gz
tar -xvf siege-latest.tar.gz
cd siege-4.0.2/
./configure
make
sudo make install
"""

""" ============================ 参数说明
启动参数
-C, --config            在屏幕上打印显示出当前的配置,配置是包括在他的配置文件$HOME/.siegerc中,可以编辑里面的参数,这样每次siege 都会按照它运行.
-v, --verbose           运行时能看到详细的运行信息.
-c, --concurrent=NUM    模拟有n个用户在同时访问,n不要设得太大,因为越大,siege消耗本地机器的资源越多.
-r, --reps=NUM          重复运行测试n次,不能与-t同时存在
-t, --time=NUMm         持续运行siege ‘n’秒(如10S),分钟(10M),小时(10H)
-d, --delay=NUM         每个url之间的延迟,在0-n之间.
-b, --benchmark         请求无需等待 delay=0.
-i, --internet          随机访问urls.txt中的url列表项.
-f, --file=FILE         指定用特定的urls文件运行 ,默认为urls.txt,位于siege安装目录下的etc/urls.txt
-R, --rc=FILE           指定用特定的siege 配置文件来运行,默认的为$HOME/.siegerc
-l, --log[=FILE]        运行结束,将统计数据保存到日志文件中siege .log,一般位于/usr/local/var/siege .log中,也可在.siegerc中自定义

结果
Transactions:		         100 hits           总共测试次数
Availability:		      100.00 %              成功次数百分比
Elapsed time:		        0.92 secs           总共耗时多少秒
Data transferred:	        0.00 MB             总共数据传输
Response time:		        0.09 secs           等到响应耗时
Transaction rate:	      108.70 trans/sec      平均每秒处理请求数
Throughput:		            0.00 MB/sec         吞吐率
Concurrency:		        9.92                最高并发
Successful transactions:     100                成功的请求数
Failed transactions:	       0                失败的请求数
Longest transaction:	    0.85                每次传输所花最长时间
Shortest transaction:	    0.00                每次传输所花最短时
"""

""" ============================ 命令
siege -h

200个并发对百度发送请求100次
siege -c 200 -r 100 http://www.baidu.com

对urls.txt中列出所有的网址进行压测
siege -c 200 -r 100 -f urls.txt

随机选取urls.txt中列出的网址,按照100*100的并发度进行测试
siege -c 100 -r 100 -f urls.txt -i

指定http请求头 文档类型
siege -H "Content-Type:application/json" -c 200 -r 100 -f urls.txt -i -b

发送post请求，在网址后添加POST说明，并且紧跟参数在其后
需要注意的是，如果地址和参数中含有中文或非ASCII字符时，首先需要对这些字符进行url编码，这样才可正确的进行测试
siege -c 100 -r 100 http://www.baidu.com/ POST k1=v1&k2=v2

接口地址: http://118.212.149.xx:8080/xx/xx/xx
请求类型: POST
请求参数: {“accountId”:”123”,”platform”:”ios”}
请求次数: 10次
请求并发数量: 200
siege "http://118.212.149.xx:8080/xx/xx/xx POST {\"accountId\":\"123\",\"platform\":\"ios\"}" -r 10 -c 200
"""



""" ============================ 命令
问题1:
================================================================
WARNING: The number of users is capped at 255.  To increase this
         limit, search your .siegerc file for 'limit' and change
         its value. Make sure you read the instructions there...
================================================================
解决办法:
修改 vim /home/glfadd/.siege/siege.conf
limit = 100000



问题2:
[error] Exceeded thread limit for this system crew.c:89: Cannot allocate memory
[fatal] unable to allocate memory for 100000 simulated browser: Cannot allocate memory


问题3:
[error] socket: read error Resource temporarily unavailable sock.c:635: Resource temporarily unavailable
修改系统最大进程数

查看进程总数
ps -ef | wc -l
查看系统设置的最大进程数
sysctl kernel.pid_max
查看当前进程数
ps -eLf | wc -l
修改最大进程数
echo "kernel.pid_max=1000000 " >> /etc/sysctl.conf
sysctl -p
查看某个服务的进程数 eg：http服务：
ps -ef | grep httpd | wc -l
查看物理cpu个数
grep 'physical id' /proc/cpuinfo | sort -u
查看核心数量
grep 'core id' /proc/cpuinfo | sort -u | wc -l
查看线程数
grep 'processor' /proc/cpuinfo | sort -u | wc -l


问题4:
[error] socket: unable to connect sock.c:282: Connection refused


问题5:
[error] socket: unable to connect sock.c:282: Operation already in progress


"""
