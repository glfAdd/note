# 命令

##### 用户 / 用户组

```bash
# cat /etc/group							所有用户组
# groups glfadd								查看用户所在的组
# groupadd test								新建用户组
# cat /etc/passwd							所用用户
# cat /etc/passwd|grep xxx		查看某个用户

将glfadd用户添加到test组
usermod -s /bin/bash -g test glfadd
```

##### 定时任务

```bash
查看定时任务
# crontab -l

编辑定时任务
# crontab -e

0 1 * * * nohup pyton /sources/LFFlightChange/tools/ak_change.py > /dev/null 2>&1 &
01 0 * * * sh /root/source/log_split.sh
```

##### 目录文件

```bash
查看SL目录大小
# du -sh aaa
将5J、SL目标打包成5j_sl.tar.gz压缩包
# tar zcf 5j_sl.tar.gz aaa/ bbb/ 
查看文件个数
# ll SL|wc -l
查看磁盘空间
# df -h
```



```bash
查看ip
netstat -anp|grep postmaster

查看占用端口的进程
netstat -antup | grep 5432

将引号中内容写入某文件中 echo
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile

访问网址看看返回什么
curl https://www.baidu.com

查看源
yum list | grep postgresql

检查80端口是否被占用
netstat -ano|grep 80
```

##### 环境变量

```bash
查看设置的变量
export

当前窗口临时添加
export PYTHONPATH=$PYTHONPATH:/root/code/Web/website
```

##### 服务器端口

```bash
netstat -anp																			查看开放的端口
firewall-cmd --query-port=666/tcp									查询端口是否开放
firewall-cmd --add-port=123/tcp --permanent				开放的端口
firewall-cmd --permanent --remove-port=123/tcp		移除指定端口


systemctl status firewalld				查看防火墙状态 
systemctl start firewalld  				开启防火墙 
systemctl stop firewalld					关闭防火墙 
firewall-cmd --reload							重载入添加的端口
```

##### linux 查看图片

```bash
1.开放端口

2.在图片目录下启动
python -m SimpleHTTPServer

3.浏览区查看图片
http://10.211.55.3:8000/
```

##### 防火墙

```bash
开启防火墙
# systemctl start firewalld
查看已打开的端口  
# netstat -anp
查看想开的端口是否已开, 提示no表示未开, yes表示成功
# firewall-cmd --query-port=666/tcp
开永久端口号. success表示成功
# firewall-cmd --add-port=666/tcp --permanent
若移除端口 
# firewall-cmd --permanent --remove-port=666/tcp
重新载入
# firewall-cmd --reload
```

##### ss

```

```



##### 文件目录

```bash
/usr
系统级的目录，可以理解为C:/Windows/

/usr/lib
理解为C:/Windows/System32

/usr/local
用户级的程序目录，可以理解为C:/Progrem Files/。
用户自己编译的软件默认会安装到这个目录下. 里主要存放那些手动安装的软件，即不是通过apt-get安装的软件。
它和/usr目录具有相类似的目录结构。让软件包管理器来管理/usr目录，而把自定义的脚本(scripts)放到/usr/local目录下面，我想这应该是个不错的主意。

/usr/src
系统级的源码目录

/usr/local/src
用户级的源码目录

/opt
用户级的程序目录，可以理解为D:/Software，这里可以用于放置第三方大型软件（或游戏），当你不需要时，直接rm -rf掉即可。在硬盘容量不够时，也可将/opt单独挂载到其他磁盘上使用
这里主要存放那些可选的程序。
你想尝试最新的firefox测试版吗?那就装到/opt目录下吧，这样，当你尝试完，想删掉firefox的时候，你就可 以直接删除它，而不影响系统其他任何设置。
安装到/opt目录下的程序，它所有的数据、库文件等等都是放在同个目录下面。
举个例子：刚才装的测试版firefox，就可以装到/opt/firefox_beta目录下，/opt/firefox_beta目录下面就包含了运 行firefox所需要的所有文件、库、数据等等。要删除firefox的时候，你只需删除/opt/firefox_beta

/etc
习惯上存放配置文件的目录，.d 的意思是目录，里面包含了配置文件，前面的名字你可以自己起，这是 linux 的惯例。
```



```
ctrl + c 杀死结束程序
ctrl + z 程序后台运行
bg 查看当前终端后台运行的程序
fg 把当前终端后台后台运行的拿到前台运行
```

##### ssh不输入密码

```
在目标机器的 〜/.ssh/authorized_keys 中添加自己的ssh公钥
```

##### ssh 简化输入IP

```
vim ~/.ssh/config

Host github-A
    HostName github.com
    User git
    IdentityFile /Users/xxx/.ssh/id_rsa_A
    IdentitiesOnly yes
Host github-B
    HostName github.com
    User git
    IdentityFile /Users/xxx/.ssh/id_rsa_B
    IdentitiesOnly yes

Host: 名字随便起
Hostname: ip
User: 用户名
Port: 端口
IdentityFile: ssh私钥路径
IdentitiesOnly yes就可以
```















##### su

```bash
1. su为switch user, 即切换用户的简写。
2. 默认username是root, 切换方式
        su
        su root
        su - 
        su - root
3. 输入 root 用户的密码
    su: 只是切换了root身份, 但Shell环境仍然是当前用户的Shell, 环境变量不变 
    su -: 用户和Shell环境一起切换, 环境变量切换


su [-fmp] [-c command] [-s shell] [--help] [--version] [-] [USER [ARG]] 
参数: 
    -m -p       执行 su 时不改变环境变数
    -c          切换用户执行命令, 执行完毕后切回用户
    -s shell    指定要执行的 shell （bash csh tcsh 等），预设值为 /etc/passwd 内的该使用者（USER） shell
    - -l 
    USER        欲变更的使用者帐号
    ARG         传入新的 shell 参数
    --help 
    --version 
```



##### sudo

```bash
https://www.cnblogs.com/ftl1012/p/sudo.html

1. sudo是一种权限管理机制, 依赖于/etc/sudoers, 其定义了授权给哪个用户可以以管理员的身份能够执行什么样的管理命令, 更灵活.
2. 默认情况下只有root用户可以执行sudo命令. root用户编辑配置文件/etc/sudoers才可以授权其他普通用户执行sudo命令
3. 输入当前用户的密码


参数:
    -b 在后台执行指令
    -h 
    -H 将HOME环境变量设为新身份的HOME环境变量。
    -k 结束密码的有效期限，也就是下次再执行sudo时便需要输入密码。
    -l 列出目前用户可执行与无法执行的指令。
    -p 改变询问密码的提示符号。
    -s 执行指定的shell。
    -u <用户>  以指定的用户作为新的身份。若不加上此参数，则预设以root作为新的身份。
    -v 延长密码有效期限5分钟。
    -V 
    -S 从标准输入流替代终端来获取密码


who  where  whom  command 哪个用户可以在哪个主机以谁的身份来执行哪些命令


root    ALL=(ALL:ALL)       ALL
    root: 用户名
    ALL: 从任何的主机上都可以执行，也可以这样 192.168.100.0/24。
    (ALL:ALL): 以谁的身份来执行，ALL:ALL 就代表 root 可以任何人的身份来执行命令。
    ALL: 表示任何命令。
    那么整条规则就是 root 用户可以在任何主机以任何人的身份来执行所有的命令。


root    ALL=(ALL)       ALL              #  (All)表示允许用户以哪个用户的权限做事情
omd     ALL=(ALL)       ALL              #  omd用户在任何机器上，可以只需任何用户的任何命令 == root用户
omd     ALL=(ALL)     NOPASSWD: ALL      #  免密而且omd用户在任何机器上，可以只需任何用户的任何命令
ftl     ALL=(ALL)   /bin/cp,/bin/touch   # 只允许ftl用户只需root用户的cp,touch命令


nick   192.168.10.0/24=(root) /usr/sbin/useradd
允许 nick 在 192.168.10.0/24 网段上连接主机并且以 root 权限执行 useradd 命令
```



##### cat

```bash

    -n 输出行号
    -b 输出行号, 除了空行
    -s 当遇到有连续两行以上的空白行，就代换为一行的空白行。
    -v 使用 ^ 和 M- 符号，除了 LFD 和 TAB 之外。
    -E 在每行结束处显示 $。
    -T 将 TAB 字符显示为 ^I。
    -A 等价于 -vET。
    -e 等价于"-vE"选项；
    -t 等价于"-vT"选项；


1. 显示整个文件
cat aaa

2. 从键盘创建一个文件, 只能创建新文件, 不能编辑已有文件
cat -n a > b

3. 将几个文件合并为一个文件
cat file1 file2 > file
```



##### ifconfig

```bash

    eth0        网卡的代号 
    lo          回环地址loopback
    inet        IPv4的Ip地址
    netmask     子网掩码
    broadcast   广播地址
    RX/TX       流量发/收情况     tx是发送（transport），rx是接收(receive)
    packets     数据包数
    errors      数据包错误数
    dropped     数据包有问题被丢弃的数量
    collisions  数据包碰撞情况，数值太多代表网络状况差
```

##### 用户

```bash

useradd oldboy      添加用户
passwd redhat       设置密码       
su - username       切换用户. su命令中间的-号很重要，意味着完全切换到新的用户，即环境变量信息也变更为新用户的信息
whoami              当前用户
logout              退出用户登录
ctrl + d            退出用户登录
```



##### 定向输出

```bash

<     覆盖, 不存在则创建
<<    追加, 不存在则创建


1. EOF是 END Of File 的缩写, 表示自定义终止符, ctrl-d 就代表EOF
2. 通常与EOF结合, 表示后续输入作为输入，直到遇到EOF为止
3. 可以定义成其他的, 比如abc


先输入, 然后输入EOF停止(ctrl + d), 输入的内容写入了 c 文件
[root@centos1 tests]# cat << EOF > c
> 123
> abc abc
> 111
> EOF
[root@centos1 tests]# cat c
123
abc abc
111
[root@centos1 tests]#
```



##### ls

```bash

    -a 
    -A 列出除.及..的其它文件
    -r 反序排列
    -t 以文件修改时间排序
    -S 以文件大小排序
    -h 以易读大小显示
    -l 
    -i 参数显示文件的 inode 节点信息
```



##### rm

```bash

删除文件
    -i 逐一询问
    -f 不逐一询问删除, 只读也可以删
    -r 逐一询问删除目录和文件
```



##### 链接

```bash

硬链接 软链接
ln      硬链接
ln -s   软链接


硬连接
    - 硬连接指通过索引节点来进行连接
    - 在 Linux 的文件系统中, 保存在磁盘分区中的文件不管是什么类型都给它分配一个编号, 称为索引节点号 Inode Index. 
    - 多个文件名可以指向同一索引节点 (允许一个文件拥有多个有效路径名), 用户可以建立硬连接到重要文件, 以防止误删
    - 只删除一个连接并不影响索引节点本身和其它的连接, 只有当最后一个连接被删除后, 文件的数据块及目录的连接才会被释放


硬连接2个限制:
1. 目录不能创建硬链接
2. 只有在同一文件系统中的文件之间才能创建链接, 即不同硬盘分区上的两个文件之间不能够建立硬链接


软连接
    - 类似 Windows 的快捷方式 
    - 可以是任意文件或目录, 可以链接不同文件系统的文件
    - 可以链接不存在的文件, 称为"断链"
    - 可以循环链接自己


[root@centos1 tests]# touch a
[root@centos1 tests]# ln a a2
[root@centos1 tests]# ln -s a a3
[root@centos1 tests]# ll -i
总用量 0
34209411 -rw-r--r--. 2 root root 0 2月   4 10:39 a
34209411 -rw-r--r--. 2 root root 0 2月   4 10:39 a2
34209414 lrwxrwxrwx. 1 root root 1 2月   4 10:39 a3 -> a
[root@centos1 tests]# rm -rf a
[root@centos1 tests]# cat a3
cat: a3: 没有那个文件或目录
[root@centos1 tests]#

1. 硬链接 a a2 的inode节点相同都是34209411, 软连接的不同
2. 删除原始文件a后, 硬链接a2不受影响, 但软连接a3文件无效
3. 硬链接文件都删除才能真正删除
```



##### pwd

```bash

    - P 查看软连接的实际路径
    
[root@centos1 tests]# mkdir a
[root@centos1 tests]# ln -s a a2
[root@centos1 tests]# ll
总用量 0
drwxr-xr-x. 2 root root 6 2月   4 10:43 a
lrwxrwxrwx. 1 root root 1 2月   4 10:43 a2 -> a
[root@centos1 tests]# cd a2/
[root@centos1 a2]# pwd
/root/tests/a2
[root@centos1 a2]# pwd -P
/root/tests/a
[root@centos1 a2]#
```



##### more

```bash

参数
    +num        从第 num 行开始显示
    -num        一次显示的行数
    -d          提示使用者，在画面下方显示 [Press space to continue, 'q' to quit.] ，如果使用者按错键，则会显示 [Press 'h' for instructions.] 而不是 '哔' 声
    -l          取消遇见特殊字元 ^L（送纸字元）时会暂停的功能
    -f          计算行数时，以实际上的行数，而非自动换行过后的行数（有些单行字数太长的会被扩展为两行或两行以上）
    -p          不以卷动的方式显示每一页，而是先清除萤幕后再显示内容
    -c          跟 -p 相似，不同的是先显示内容再清除其他旧资料
    -s          当遇到有连续两行以上的空白行，就代换为一行的空白行
    -u          不显示下引号 （根据环境变数 TERM 指定的 terminal 而有所不同）
    +/pattern   在每个文档显示前搜寻该字串（pattern），然后从该字串之后开始显示
    fileNames   欲显示内容的文档，可为复数个数


常用操作命令
    Enter       向下一行
    n Enter     向下n行
    Ctrl+F      向下滚动一屏
    空格键       向下滚动一屏
    Ctrl+B      返回上一屏
    =           输出当前行的行号
    :f          输出文件名和当前行的行号
    V           调用vi编辑器
    !命令        调用Shell，并执行命令
    q           退出more
```



##### head

```bash

默认显示文件前10行


    - n 显示前x行
    - c 显示前x个字节

head -n 5 aaa
```



##### which

```bash

在环境变量$PATH指定的路径中, 搜索某个系统命令的位置, 并且返回第一个搜索结果


    -n 指定文件名长度，指定的长度必须大于或等于所有文件中最长的文件名。
    -p 与-n参数相同，但此处的包括了文件的路径。
    -w 指定输出时栏位的宽度。
    -V 显示版本信息
```



##### whereis

```bash

在特定目录中查找符合条件的文件


-b 　只查找二进制文件。
-B<目录> 　只在设置的目录下查找二进制文件。
-f 　不显示文件名前的路径名称。
-m 　只查找说明文件。
-M<目录> 　只在设置的目录下查找说明文件。
-s 　只查找原始代码文件。
-S<目录> 　只在设置的目录下查找原始代码文件。
-u 　查找不包含指定类型的文件。
```



##### locate

```bash

查找文件或目录
locate命令要比find -name快得多, 因为它不搜索具体目录, 而是搜索一个数据库/var/lib/mlocate/mlocate.db
这个数据库中含有本地所有文件信息
Linux系统自动创建这个数据库, 并且每天自动更新一次, 因此用whereis和locate 查找文件时, 有时会找到已经被删除的数据, 或者刚刚建立文件，却无法查找到，原因就是因为数据库文件没有被更新。
为了避免这种情况，可以在使用locate之前，先使用updatedb命令，手动更新数据库。

整个locate工作其实是由四部分组成
/usr/bin/updatedb               主要用来更新数据库，通过crontab自动完成的
/usr/bin/locate                 查询文件位置
/etc/updatedb.conf              updatedb的配置文件
/var/lib/mlocate/mlocate.db     存放文件信息的文件
```



##### find

```bash

查找文件


find <目录> <条件> <动作>
    -name                   文件名, 区分大小写
    -iname                  文件名, 不区分大小写
    -perm                   根据文件权限查找
    -prune                  该选项可以排除某些查找目录
    -user                   根据文件属主查找
    -group                  根据文件属组查找
    -mtime -n | +n          根据文件更改时间查找

    -nogroup                查找无有效属组的文件
    -nouser                 查找无有效属主的文件
    -newer file1 ! file2    查找更改时间比le 1新但比le2|日IDE文件
    -type                   按文件类型查找
        f 文件          find . -type f
        d 目录
        c 字符设备文件
        b 块设备文件
        l 链接文件
        p 管道文件
        s socket
    -size -n +n             按文件大小查找
    -mindepth n             从n级子目录开始搜索
    -maxdepth n             最多搜索到n级子目录


# 查找 /etc 目录下以 conf 结尾的文件，文件名区分大小写
find /etc -name '*.conf'
```



##### gerp

```bash
 
用于查找文件里符合条件的字符串

grep [选项] [文本] [文件] 


    -a	            不要忽略二进制数据。
    -A<显示列数>     除了显示符合范本样式的那一行之外，并显示该行之后的内容。
    -B<显示列数>     除了显示符合范本样式的那一行之外，并显示该行之前的内容。
    -b	            显示符合范本样式的那一行，以及字符偏移量。
    -c	            统计匹配到的行数
    -C<显示列数>或-<显示列数>    除了显示符合范本样式的那一列之外，并显示该列之前后的内容。
    -d<进行动作>	    当指定要查找的是目录而非文件时，必须使用这项参数，否则grep命令将回报信息并停止动作。
    -e              匹配的字符串
    -E	            将范本样式为延伸的普通表示法来使用，意味着使用能使用扩展正则表达式。
    -f<范本文件>	    指定范本文件，其内容有一个或多个范本样式，让grep查找符合范本条件的文件内容，格式为每一列的范本样式。
    -F              特殊字符只是字符串
    -G	            特殊字符执行各自的意思
    -h	            在显示符合范本样式的那一列之前，不标示该列所属的文件名称。
    -H	            在显示符合范本样式的那一列之前，标示该列的文件名称。
    -i	            忽略大小写
    -l	            列出匹配的文件名
    -L	            列出不匹配的文件名
    -n	            显示匹配的行号
    -q	            不会输出任何信息，如果命令运行成功返回0，失败则返回非0值。一般用于条件测试
    -R/-r	        此参数的效果和指定“-d recurse”参数相同。
    -s	            不显示错误信息。
    -v	            结果取反
    -w	            只显示全字符合的列。
    -x	            只显示全列符合的列。
    -y	            此参数效果跟“-i”相同。
    -o	            只输出文件中匹配到的字符
    
# 文件中搜索包含aaa的行
grep "aaa" file_name

# 多个文件中搜索
grep "aaa" file_name_1 file_name_2

# 使用正则表达式
grep -E "[1-9]+"
egrep "[1-9]+"

# 多级目录中递归搜索
grep -r "aaa" .
grep 'world' -d recurse ~/projects/

# 匹配多个字符串
grep -e "tests" -e "aaa" file_name

# 显示匹配和之 前 / 后 / 前后 n行
grep -A 4 "aaa" a
grep -B 4 "aaa" a
grep -C 4 "aaa" a

#只在目录中所有的.php和.html文件中递归搜索字符"aaa"
grep "aaa" . -r --include *.{php,html}

#在搜索结果中排除所有README文件
grep "aaa" . -r --exclude "README"

#在搜索结果中排除filelist文件列表里的文件
grep "aaa" . -r --exclude-from filelist

# 特殊字符
grep -F ".*" a
grep -G ".*" a
```



##### chmod

```bash


参数
    -c          若该文件权限确实已经更改，才显示其更改动作
    -f          若该文件权限无法被更改也不要显示错误讯息
    -v          显示权限变更的详细资料
    -R          目录下所有文件都改
    --help      显示辅助说明
    --version   显示版本


权限分为三级: 文件拥有者、群组、其他用户

-   非目录文件
d   目录文件

u   拥有者
g   同组用户
o   其他用户
a   三者皆是

+   增加权限
-   取消权限
=   唯一设定权限。

r   4 只读
w   2 写
x   1 可执行
X   表示只有当该文件是个子目录或者该文件已经被设定过为可执行。

rwx     4+2+1=7
rw-     4+2=6
r-x     4+1=5

drwxr-xr-x. 2 root root 33 2月   6 10:46 c

# 将文件 file1.txt 设为所有人皆可读取
chmod ugo+r file1.txt
chmod a+r file1.txt

# 将文件 file1.txt 与 file2.txt 设为该文件拥有者，与其所属同一个群体者可写入，但其他以外的人则不可写入
chmod ug+w,o-w file1.txt file2.txt
chmod 221 file1.txt file2.txt

# 将目前目录下的所有文件与子目录皆设为任何人可读取
chmod -R a+r *


chmod a=rwx file
chmod 777 file
```

##### du

```bash

显示文件或目录大小

du [选项][文件]

参数：
    -a 显示所有文件
    -k 以KB为单位
    -m 以MB为单位
    -g 以GB为单位
    -h 以易读方式显示文件大小
    -s 仅显示总计
    -c 显示所有文件和总计
```

##### wc

```bash

计算文件的Byte数、字数、或是列

    -c 字节数
    -l 行数
    -m 字符数. 不能与 -c 标志一起使用
    -w 统计字数。一个字被定义为由空白、跳格或换行字符分隔的字符串
    -L 打印最长行的长度
    -help 显示帮助信息
    --version 显示版本信息


$ wc testfile testfile_1 testfile_2  #统计三个文件的信息  
3 92 598 testfile                    #第一个文件行数为3、单词数92、字节数598  
9 18 78 testfile_1
3 6 32 testfile_2 
15 116 708 总用量                    #三个文件总共的行数为15、单词数116、字节数708 
```



##### ps

```bash

执行ps命令的那个时刻的进程
如果想要动态的显示进程信息，就可以使用top命令


ps命令支持3种使用的语法格式：
1. UNIX 风格，选项可以组合在一起，并且选项前必须有“-”连字符
2. BSD 风格，选项可以组合在一起，但是选项前不能有“-”连字符
3. GNU 风格的长选项，选项前有两个“-”连字符
风格可以混用，但是可能会发生冲突


Linux上进程有5种状态:
R 运行 runnable (on run queue)                    正在运行或在运行队列中等待	                                    
S 中断 sleeping                                   休眠中, 受阻, 在等待某个条件的形成或接受到信号	                
D 不可中断 uninterruptible sleep (usually IO)      收到信号不唤醒和不可运行, 进程必须等待直到有中断发生	            
Z 僵死 a defunct (”zombie”) process               进程已终止, 但进程描述符存在, 直到父进程调用wait4()系统调用后释放	
T 停止 traced or stopped                          进程收到SIGSTOP, SIGSTP, SIGTIN, SIGTOU信号后停止运行运行	    


字段说明:
UID     用户ID
PID     进程ID
PPID    父进程ID
C       占用CPU
%CPU    占用CPU
TIME    该进程实际使用CPU运行的时间
STIME   进程启动的时间 	
CMD     命令的名称和参数
USER    用户名	
%MEM    占用内存
VSZ     该进程使用的虚拟內存量（KB）
RSS     该进程占用的固定內存量（KB）
STAT    进程状态
            D 无法中断的休眠状态（通常 IO 的进程）
            R 正在运行可中在队列中可过行的
            S 处于休眠状态
            T 停止或被追踪
            X 死掉的进程
            Z 僵尸进程
            < 优先级高的进程 
            N 优先级较低的进程 
            L 有些页被锁进内存
            s 进程的领导者（在它之下有子进程）
            l 多线程，克隆线程（使用 CLONE_THREAD, 类似 NPTL pthreads）
            + 位于后台的进程组
TTY     该进程在那个终端上运行. 
        若与终端无关，则显示"?". 
        若为pts/0等，则表示由网络连接主机进程.


参数:
    -a              显示所有终端机下执行的进程，除了阶段作业领导者之外。
    a               显示现行终端机下的所有进程，包括其他用户的进程。
    -A              显示所有进程。
    -c              显示CLS和PRI栏位。
    c               列出进程时，显示每个进程真正的指令名称，而不包含路径，参数或常驻服务的标示。
    -C<指令名称> 　  指定执行指令的名称，并列出该指令的进程的状况。
    -d 　            显示所有进程，但不包括阶段作业领导者的进程。
    -e 　            此参数的效果和指定"A"参数相同。
    e 　             列出进程时，显示每个进程所使用的环境变量。
    -f 　            显示UID,PPIP,C与STIME栏位。
    f 　             用ASCII字符显示树状结构，表达进程间的相互关系。
    -g<群组名称> 　  此参数的效果和指定"-G"参数相同，当亦能使用阶段作业领导者的名称来指定。
    g 　             显示现行终端机下的所有进程，包括群组领导者的进程。
    -G<群组识别码> 　 列出属于该群组的进程的状况，也可使用群组名称来指定。
    h 　             不显示标题列。
    -H 　            显示树状结构，表示进程间的相互关系。
    -j或j 　          采用工作控制的格式显示进程状况。
    -l或l 　          采用详细的格式来显示进程状况。
    L 　             列出栏位的相关信息。
    -m或m 　          显示所有的执行绪。
    n 　             以数字来表示USER和WCHAN栏位。
    -N 　            显示所有的进程，除了执行ps指令终端机下的进程之外。
    -p<进程识别码>   指定进程识别码，并列出该进程的状况。
    p<进程识别码>    此参数的效果和指定"-p"参数相同，只在列表格式方面稍有差异。
    r 　             只列出现行终端机正在执行中的进程。
    -s<阶段作业> 　  指定阶段作业的进程识别码，并列出隶属该阶段作业的进程的状况。
    s 　             采用进程信号的格式显示进程状况。
    S 　             列出进程时，包括已中断的子进程资料。
    -t<终端机编号> 　指定终端机编号，并列出属于该终端机的进程的状况。
    t<终端机编号> 　此参数的效果和指定"-t"参数相同，只在列表格式方面稍有差异。
    -T 　            显示现行终端机下的所有进程。
    -u<用户识别码> 　此参数的效果和指定"-U"参数相同。
    u 　             以用户为主的格式来显示进程状况。
    -U<用户识别码> 　列出属于该用户的进程的状况，也可使用用户名称来指定。
    U<用户名称>     列出属于该用户的进程的状况。
    v 　             采用虚拟内存的格式显示进程状况。
    -V或V 　          版本信息
    -w或w 　          采用宽阔的格式来显示进程状况。　
    x 　             显示所有进程，不以终端机来区分。
    -y              配合参数"-l"使用时，不显示F(flag)栏位，并以RSS栏位取代ADDR栏位。
    
    
# 根据 CPU 使用来升序排序
ps -aux --sort -pcpu | less  

# 根据内存使用来升序排序
ps -aux --sort -pmem | less

# 合并到一个命令，并通过管道显示前10个结果：
ps -aux --sort -pcpu,+pmem | head -n 10
```



##### kill

```bash

会向操作系统内核发送一个信号和目标进程的PID, 然后系统内核根据收到的信号, 对指定进程进行相应的操作


参数：
    -l 信号，若果不加信号的编号参数，则使用“-l”参数会列出全部的信号名称
    -a 当处理当前进程时，不限制命令名和进程号的对应关系
    -p 指定kill 命令只打印相关进程的进程号，而不发送任何信号
    -s 指定发送信号
    -u 指定用户


信号:
0	EXIT 	    程序退出时收到该信息。
1	HUP	        重启进程
2	INT	        结束进程，但并不是强制性的，"Ctrl+C" 就是 kill -2 的信号
3	QUIT	    退出
9	KILL	    强制结束进程
11	SEGV 	    段错误
15	TERM	    正常结束进程(默认)
18  CONT        继续（与STOP相反， fg/bg命令）
19  STOP        暂停（同 Ctrl + Z）
```



##### scp

```bash

基于ssh远程文件拷贝


参数:
    -r 递归复制整个目录
    -v 详细方式输出
    -q 不显示传输进度条
    -C 允许压缩
    
    
scp 本地文件  远程用户名@远程ip:远程文件夹/远程文件名
scp -r  本地文件夹  远程用户名@远程ip:远程文件夹/


# 本地发送到服务器
scp /home/work/source.txt work@192.168.0.10:/home/work/
scp -P 63122 conf_pro.ini root@47.93.121.126:/root/source/ndc_data/conf/conf_pro.ini

# 服务器下载到本地
scp work@192.168.0.10:/home/work/source.txt work@192.168.0.11:/home/work/
 scp -P 63122 glf@47.93.122.31:/home/glf/source/ndc_data/logs/ndc_data_develop.log .
 scp -P 63122 root@47.93.121.126:/logs/ndc_data_develop.log .

# 文件夹
scp -r /home/work/sourcedir work@192.168.0.10:/home/work/
```



##### PATH

```bash

PATH中的环境变量有顺序,如果你添加的变量需要优先被搜索出,需要添加在变量首,否则放在尾部


# 查看PATH
echo $PATH

# 临时修改PATH变量
export PATH=/usr/local/mongdb/bin:$PATH   # 将mongdb下的bin目录放在临时放在PATH变量中,以:号进行分割,

# 永久修改
vim ~/.bashrc 
export PATH=/usr/local/mongodb/bin:$PATH
source ~/.bashrc  

# 全局修改PATH变量
vim /etc/profile
export PATH=/usr/local/mongodb/bin:$PATH
```

##### locale



```bash
 $ locale
locale: Cannot set LC_ALL to default locale: No such file or directory
LANG=en_US.UTF-8
LC_CTYPE="en_US.UTF-8"
LC_NUMERIC="en_US.UTF-8"
LC_TIME="en_US.UTF-8"
LC_COLLATE="en_US.UTF-8"
LC_MONETARY="en_US.UTF-8"
LC_MESSAGES="en_US.UTF-8"
LC_PAPER="en_US.UTF-8"
LC_NAME="en_US.UTF-8"
LC_ADDRESS="en_US.UTF-8"
LC_TELEPHONE="en_US.UTF-8"
LC_MEASUREMENT="en_US.UTF-8"
LC_IDENTIFICATION="en_US.UTF-8"
LC_ALL=
```



##### 查看进程占用的端口

```bash
ss -tlnp | grep mongo
```

##### pkg-config

> 在编译时, 如果库的头文件不在 /usr/include 目录中, 需要用 -I 参数指定其路径. 
>
> 但同一个库在不同系统安装路径不同, 造成 -I 或 -L 参数不同
>
> 把库的位置信息保存在文件中, 编译时都到这个文件中读取, 使编译命令一致, 例如使用 pkg-config

```
1. 返回已安装库文件的元信息, 这些信息记录在 .pc 文件中
2. 不同的库会读取对应的 .pc 文件 (用 python3 会去读 python3.pc)
3. 文件保存在 
	默认路径 /usr/lib/pkgconfig 或 /usr/lib64/pkgconfig
	环境变量 PKG_CONFIG_PATH 指定的路径
4. 库编译完成后目录中有该库的 .pc 文件 (用 find 找), 将该文件复制到 pkg-config 默认目录或在环境变量中指定该文件的路径. 使依赖此库的其他库可以通过 pkg-config 自动加载该库, 避免编译期错误.
```

- 参数

  ```
  --list-all 	已安装的库
  --cflags	一般用于指定头文件
  --libs		一般用于指定库文件
  
  $ gcc sample.c -o sample `pkg-config --cflags --libs glib-2.0`
  ```

- 添加环境变量

  ```
  PKG_CONFIG_PATH=$PKG_CONFIG_PATH:~/.pyenv/versions/3.7.10/lib/pkgconfig
  export PKG_CONFIG_PATH
  ```

- 实例

  ```
  # See: man pkg-config
  prefix=/usr/local
  exec_prefix=${prefix}
  libdir=/sdwan/lib
  includedir=${prefix}/include
  
  Name: Python
  Description: Python library
  Requires: 
  Version: 3.7
  Libs.private: -lpthread -ldl  -lutil
  Libs: -L${libdir} -lpython3
  Cflags: -I${includedir}/python3.7m
  ```

  



```
Name: 名字, 不会影响 pkg-config 使用, pkg-config 用 .pc 文件名来工作
Description: 简短描述
URL: 获取package的更多信息或者package的下载地址
Version: 指定 package 版本号
Requires: 本库所依赖的其他库文件。所依赖的库文件的版本号可以通过使用如下比较操作符指定：=,<,>,<=,>=
Requires.private: 本库所依赖的一些私有库文件，但是这些私有库文件并不需要暴露给应用程序。这些私有库文件的版本指定方式与Requires中描述的类似。
Conflicts: 描述与本package所冲突的其他package。版本号的描述也与Requires中的描述类似。本字段也可以取值为同一个package的多个不同版本实例。例如: Conflicts: bar < 1.2.3, bar >= 1.3.0
Cflags: 编译器编译本package时所指定的编译选项，和其他并不支持pkg-config的library的一些编译选项值。假如所需要的library支持pkg-config,则它们应该被添加到Requires或者Requires.private中
Libs: 链接本库时所需要的一些链接选项，和其他一些并不支持pkg-config的library的链接选项值。与Cflags类似
Libs.private: 本库所需要的一些私有库的链接选项。
```

# 目录

##### 目录说明

> usr 是 Unix System Resource

```
lrwxrwxrwx.   1 root root    7 Jan 19 03:17 bin -> usr/bin
dr-xr-xr-x.   5 root root 4.0K Jan 19 06:58 boot
drwxr-xr-x.  18 root root 3.2K Jan 19 18:53 dev
drwxr-xr-x.  80 root root 8.0K Jan 19 18:54 etc
drwxr-xr-x.   2 root root    6 Apr 11  2018 home
lrwxrwxrwx.   1 root root    7 Jan 19 03:17 lib -> usr/lib
lrwxrwxrwx.   1 root root    9 Jan 19 03:17 lib64 -> usr/lib64
drwxr-xr-x.   2 root root    6 Apr 11  2018 media
drwxr-xr-x.   2 root root    6 Apr 11  2018 mnt
drwxr-xr-x.   9 root root  135 Jan 19 22:56 opt
dr-xr-xr-x. 260 root root    0 Jan 19 18:52 proc
dr-xr-x---.  14 root root 4.0K Jan 19 23:10 root
drwxr-xr-x.  24 root root  680 Jan 19 22:52 run
lrwxrwxrwx.   1 root root    8 Jan 19 03:17 sbin -> usr/sbin
drwxr-xr-x.   2 root root    6 Apr 11  2018 srv
dr-xr-xr-x.  13 root root    0 Jan 19 18:53 sys
drwxrwxrwt.  19 root root 4.0K Jan 19 22:54 tmp
drwxr-xr-x.  13 root root  155 Jan 19 03:17 usr
drwxr-xr-x.  19 root root  267 Jan 19 03:21 var
```

| 目录            | 说明                                                         |
| --------------- | ------------------------------------------------------------ |
| /bin            | 系统预装的可执行程序, 会随着系统升级而改变 (所有用户可用)    |
| /usr/bin        |                                                              |
| /sbin           | 系统预装的可执行程序, 会随着系统升级而改变 (只有超管可用)    |
| /usr/sbin       |                                                              |
| /usr/local/bin  | 用户可执行程序的地方, 不会被系统升级而覆盖同名文件 (所有用户可用) |
| /usr/local/sbin | 用户可执行程序的地方, 不会被系统升级而覆盖同名文件 (只有超管可用) |
|                 |                                                              |
|                 |                                                              |
|                 |                                                              |
|                 |                                                              |

##### 环境变量

```bash
# 前面的优先级高
$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/opt/jdk-11.0.12/bin:/opt/go1.19.1/bin:/opt/go1.19.1/gopath/bin
```



