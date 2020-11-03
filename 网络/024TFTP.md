```python
简单文件传输协议
简单、占用资源小、适合传递小文件、适合在局域网进行传递、TFTP服务器默认监听69号端口、基于UDP实现

CS架构：客户端服务器
BS架构：浏览器服务器
--------------------------------------------
TFTP下载过程
1.当客户端发送“下载”请求（即读请求）时，需要向服务器的69端口发送。服务器若批准此请求,则使用一个新的、临时的端口进行数据传输
2.当服务器找到需要现在的文件后，会立刻打开文件，把文件中的数据通过TFTP协议发送给客户端。如果文件的总大小较大（比如3M），那么服务器分多次发送，每次会从文件中读取512个字节的数据发送过来。每次都使用一个随机端口发送数据。
3.因为发送的次数有可能会很多，所以为了让客户端对接收到的数据进行排序，所以在服务器发送那512个字节数据的时候，会多发2个字节的数据，用来存放序号，并且放在512个字节数据的前面，序号是从1开始的
4.因为需要从服务器上下载文件时，文件可能不存在，那么此时服务器就会发送一个错误的信息过来，为了区分服务发送的是文件内容还是错误的提示信息，所以又用了2个字节 来表示这个数据包的功能（称为操作码），并且在序号的前面
5.因为udp的数据包不安全，即发送方发送是否成功不能确定，所以TFTP协议中规定，为了让服务器知道客户端已经接收到了刚刚发送的那个数据包，所以当客户端接收到一个数据包的时候需要向服务器进行发送确认信息，即发送收到了，这样的包成为ACK(应答包)。发送到随机端口。
6.为了标记数据已经发送完毕，所以规定，当客户端接收到的数据小于516（2字节操作码+2个字节的序号+512字节数据）时，就意味着服务器发送完毕了

# 读写请求 
操作码 + 文件名 + 0 + 模式 + 0
2byte + nbyte + 1B + nByte + 1B
1或2	123.jpg	0 octet 0

# 数据包（发送回来的数据）
操作码 + 块编码（序号） + 数据
2byte + 2byte + 512Byte
3	  

# ACK 
操作码 + 块编码
2byte + 2byte
4

# ERROR 
操作码 + 错误码 + 错误信息 + 0
2byte + 2byte + nbyte + 1B
5

操作码 		功能
1			读请求，即下载
2 			写请求，即上传
3 			表示数据包，即DATA
4 			确认码，即ACK
5 			错误
--------------------------------------------
如果有个十六进制的数据0x1122要内存储存。会拆成0x11和0x22两部分。
大端：第内存地址存高位数据
小端：低内存地址存低位数据
pc机一般用小端
IBM等大型服务器用大端
为了统一发送时所有多字节组成的数据格式，都转成大端发送。

# 创建请求时需要打包
struct.pack("!H8sb5sb",1,"tests.jpg",0,"octet",0)
!	表示数据按照网络数据大端格式
H	占位置，表示2个字节大小
8s	8个1字节大小
b	1字节大小

# 接收数据后需要解包
struct.unpack("!HH", recvData[:4])c
!	表示数据按照网络数据大端格式
H	每两个字节看成一个整体处理，得到新数据
[:4]字符串取4个字节长度
--------------------------------------------
#coding=utf-8

from socket import *
import struct
import sys

if len(sys.argv) != 2:
    print('-'*30)
    print("tips:")
    print("python xxxx.py 192.168.1.1")
    print('-'*30)
    exit()
else:
    ip = sys.argv[1]

# 创建udp套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

#构造下载请求数据
cmd_buf = struct.pack("!H8sb5sb",1,"tests.jpg",0,"octet",0)

#发送下载文件请求数据到指定服务器
sendAddr = (ip, 69)
udpSocket.sendto(cmd_buf, sendAddr)

p_num = 0

recvFile = ''

while True:
    recvData,recvAddr = udpSocket.recvfrom(1024)
    recvDataLen = len(recvData)
    # print recvAddr # for tests
    # print len(recvData) # for tests
    cmdTuple = struct.unpack("!HH", recvData[:4])c
    # print cmdTuple # for tests
    cmd = cmdTuple[0]
    currentPackNum = cmdTuple[1]        

    if cmd == 3: #是否为数据包
        # 如果是第一次接收到数据，那么就创建文件
        if currentPackNum == 1:
            recvFile = open("tests.jpg", "a")

        # 包编号是否和上次相等
        if p_num+1 == currentPackNum:
            recvFile.write(recvData[4:]);
            p_num +=1
            print '(%d)次接收到的数据'%(p_num)

            ackBuf = struct.pack("!HH",4,p_num)

            udpSocket.sendto(ackBuf, recvAddr)
        # 如果收到的数据小于516则认为出错
        if recvDataLen<516:
            recvFile.close()
            print '已经成功下载！！！'
            break

    elif cmd == 5: #是否为错误应答
        print "error num:%d"%currentPackNum
        break

udpSocket.close()
```

