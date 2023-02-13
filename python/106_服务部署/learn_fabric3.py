""" ============================ 参考
https://www.cnblogs.com/xiao-apple36/p/9124292.html

不推荐使用

安装
    pip intall fabric3

不同版本区别
    Fabric 1.x：支持 Python 2.5-2.7，但不支持 Python 3
    Fabric 2.x：支持 Python 2.7 与 3.4+，但不兼容 Fabric 1.x 的 fabfile
    Fabric2：等同于 Fabric 2.x，为了使不同版本共存（装一个 1.x 旧版本，再装它作为新版本）
    Fabric3：一个基于 Fabric 1.x 的 fork（非官方），兼容 Python 2&3，兼容 Fabric1.x 的 fabfile
"""

""" ============================ 命令参数
-g	指定网关（中转设备），比如堡垒机环境，填写堡垒机IP即可
-P	以异步并行方式运行多台主机任务，默认为串行运行
-R	指定角色（Role）
-l  列出任务函数名，只有使用了装饰器 @task 的才会列出
-H  指定目标主机, 多台主机用","号分割
-u  指定远程用户名
-f  指定fab的任务文件, 默认fabfile.py
-t  设置超时时间, 单位s
-T	远程主机命令执行超时时间
-V  查看版本
-h  帮助
-H	指定目标主机，多台主机用“，”分隔
-w	当命令执行失败，发出告警，而非默认终止任务
-- Fabric参数     其他包含fabric脚本的中的参数的快捷操作，比如--user,--port，或者直接跟要执行的Linux命令


启动命令. 默认引用名为fabfile.py的文件, 通过-f指定
fab -f fabric_test.py main


获取任务列表
fab -f fabric_test.py --list


一次可以多个task，按照顺序执行
fab -f fab_util.py hostname ls


给task传递参数
fab -f fab_util.py hostname ls:/doument


'ip a' --后面的参数会当做一个命令处理
fab -H 192.168.5.128 --port 22 --user='root' --password='mysql123' -- 'ip a '

"""

""" ============================ api
local       执行本地命令，如：local('uname -s')
lcd         切换本地目录，如：lcd('/home')
cd          切换远程目录，如：cd('/etc')
run         执行远程命令，如：run('free -m')
sudo        sudo方式执行远程命令，如：sudo('touch /abc')
put         上传本地文件到远程主机，如：put('/hello', '/home/itcast/hello')
get         从远程主机下载文件到本地，如：get('/home/python/world', '/home/itcast/world')
reboot      重启远程主机，如：reboot()
@task       函数装饰器，标识的函数为fab可调用的，非标记的对fab不可见
@runs_once  函数装饰器，标识的函数只会执行一次，不受多台主机影响
"""

""" ============================ env 对象
env是一个全局唯一的字典，保存了Fabric所有的配置
在Fabric的实现中，他是一个_AttributeDict()对象，之所以封装成_AttributeDict()对象，是覆盖了__getattr__和__setattr__，使我们可以使用“对象.属性=值”的方式，操作字典


env.host            主机列表 env.host=['192.168.17.192', '192.168.17.193']
env.exclude_hosts   排除特定的服务器
env.user            ssh用户名
env.port            主机端口, 默认为22
env.password        ssh密码
env.passwords       不同的主机不同的密码 env.passwords={'itcast@192.168.17.192:22':'chuanzhi', 'itcast@192.168.17.193:22':'python'}


针对不同主机不同密码的情况
env.hosts = [
    'root@192.168.10.201:22',
    'root@192.168.10.202:22',
    'root@192.168.10.203:22'
]
env.passwords = {
    'root@192.168.10.201:22':'123456201',
    'root@192.168.10.202:22':'123456202',
    'root@192.168.10.203:22':'123456203'
"""

""" ============================ run 
在远程服务器上执行Linux命令
1. 参数pty，如果我们执行命令以后需要有一个常驻的服务进程，那么就需要设置pty=False，避免因为Fabric退出导致进程的退出
run('service mysqld start',pty=False)


2. 执行完毕会返回输出的信息，我们可以定义变量接受，同时这个返回信息有一个方法return_code，当返回的是正确执行的结果时code为0，否则不为0	
def hello():
    with settings(hide('everything'),warn_only=True):   # 关闭显示
        result = run('anetstat -lntup|grep -w 25')
        print(result)                                   # 命令执行的结果
        print(result.return_code)                       # 返回码，0表示正确执行，1表示错误
"""

""" ============================ sudo 
使用管理员权限在远程服务器上执行Linux命令
参数pty
"""

""" ============================ local 
用以执行本地命令
ef tests():
    result = local('make tests',capture=True)
    print(result)
    print(result.failed)
    print(result.succeeded)
  
# 返回执行的命令
# 如果执行失败那么 result.failed 为True
# 如果执行成功那么 result.succeeded 为True
"""

""" ============================ get 
从远程服务器上获取文件
    - emote_path 从何处下载. 支持通配符。
    - local_path表示下载到何处
get(remote_path='/etc/passwd',local_path='/tmp/passwd')
"""

""" ============================ put 
将本地的文件上传到远程服务器
get(remote_path='/etc/passwd',local_path='/tmp/passwd')
"""

""" ============================ reboot 
重启远程服务器
    - wait: 等待几秒钟重启
reboot(wait=30)
"""

""" ============================ propmt 
用以在Fabric执行任务的过程中与管理员进行交互，类似于python的input
key = prompt('Please specify process nice level:',key='nice',validate=int)
"""

""" ============================ cd 
切换远程目录
def change(dir='/tmp'):
    with cd(dir):
        run('pwd')     # /tmp
    run('pwd')         # /root
"""

""" ============================ lcd 
切换本地目录
"""

""" ============================ path 
配置远程服务器PATH环境变量，只对当前会话有效，不会影响远程服务器的其他操作
1. append：(默认) 将给定的路径添加到PATH后面
2. prepend：将给定的路径添加到PATH的前面
3. replace：替换当前环境的PATH变量

def addpath():
    with path('/tmp','prepend'):
        run("echo $PATH")
    run("echo $PATH")

"""

""" ============================ prefix 
它接受一个命令作为参数，表示在其内部执行的代码块，都要先执行prefix的命令参数。

def testprefix():
    with cd('/tmp'):
        with prefix('echo 123'):
            run('echo 456')
            run('echo 789')
  
# 转换为Linux命令为：
cd /tmp && echo '123' && echo '456'
cd /tmp && echo '123' && echo '789'　
"""

""" ============================ shell_env 
设置shell脚本的环境变量　

def setenv():
    with shell_env(HTTP_PROXY='1.1.1.1'):
        run('echo $HTTP_PROXY')
    run('echo $HTTP_PROXY')
  
# 等同于shell中的export
export HTTP_PROXY='1.1.1.1'
"""

""" ============================ settings 
通用配置，用于临时覆盖env变量

def who():
    with settings(user='dev'):    # 临时修改用户名为dev
        run('who')
    run('who')
"""

""" ============================ remote_tunnel 
通过SSH的端口转发建立的链接

with remote_tunnel(3306):
    run('mysql -uroot -p password')
"""

""" ============================ hide 
用于隐藏指定类型的输出信息，hide定义的可选类型有7种
    1. status：状态信息，如服务器断开链接，用户使用ctrl+C等，如果Fabric顺利执行，不会有状态信息
    2. aborts：终止信息，一般将fabric当作库使用的时候需要关闭
    3. warnings：警告信息，如grep的字符串不在文件中
    4. running：fabric运行过程中的数据
    5. stdout：执行shell命令的标准输出
    6. stderr：执行shell命令的错误输出
    7. user：用户输出，类似于Python中的print函数

为了方便使用，fabric对以上其中类型做了进一步的封装
    1. output：包含stdout，stderr
    2. everything：包含stdout，stderr，warnings，running，user
    3. commands：包含stdout，running
"""

""" ============================ show 
与hide相反，表示显示指定类型的输出

def hello():
    with settings(show('everything'),warn_only=True):   # 显示所有
        result = run('netstat -lntup|grep')
        print('1='+result)                                   # 命令执行的结果
        print('2='+str(result.return_code))                  # 返回码，0表示正确执行，1表示错误
        print('3='+str(result.failed))
"""

""" ============================ quiet 
隐藏全部输出，仅在执行错误的时候发出告警信息，功能等同于 with settings(hide('everything'),warn_only=True)

# 比如创建目录的时候，如果目录存在，默认情况下Fabric会报错退出，我们是允许这种错误的，所以针对这种错误，我们进行如下设置，使fabric只打出告警信息而不会中断执行。
with settings(warn_only=True)
"""

""" ============================ @task 
task就是fabric需要在远程服务器上执行的函数, 3中方法定义
    1. 默认情况下，fabfile中每一个函数都是一个task。
    2. 继承自fabric的task类，这种方式比较难用，不推荐。
    3. 使用fabric的task装饰器，这是使用fabric最快速的方式，也是推荐的用法。
    
默认情况下，fabfile中的所有函数对象都是一个task，但使用了task装饰器, 其他task装饰器的函数将不会被认为是一个task

from fabric.api import *
  
env.user='root'
env.password='mysql123'
  
@task
def hello():
    run('echo hello')
  
def world():
    run('echo world')
"""

""" ============================ @host 
1. 通过env.hosts来执行
2. 在fab执行命令的时候使用-H参数
3. 使用装饰器


from fabric.api import *
  
env.hosts = [
    'root@192.168.10.201:22',
    'root@192.168.10.202:22',
    'root@192.168.10.203:22'
]
env.passwords = {
    'root@192.168.10.201:22':'123456201',
    'root@192.168.10.202:22':'123456202',
     'root@192.168.10.203:22':'123456203'
}
  
@hosts('root@192.168.10.201:22')
@task
def hello():
    run('ifconfig br0')
  
  
# 命令行的方式：
fab hello:hosts="root@192.168.10.201;root@192.168.10.202"
"""

""" ============================ @role 
role是对服务器进行分类的手段，通过role可以定义服务器的角色，以便对不同的服务器执行不同的操作，Role逻辑上将服务器进行了分类，分类以后，我们可以对某一类服务器指定一个role名即可。进行task任务时，对role进行控制。
hosts装饰器可以和roles装饰器一起使用(全集)，看起来容易造成混乱，不建议混搭。

# role在env.roledefs中进行定义
env.roledefs = {
    'web':['root@192.168.10.201','192.168.10.202']    # role名称为：web
    'db':['root@192.168.10.203',]                     # role名称为：db
}
　　当我们定义好role以后，我们就可以通过roles装饰器来指定在哪些role上运行task。
 
 
from fabric.api import *
  
env.roledefs = {
    'web':['root@192.168.10.201:22','root@192.168.10.202:22',],
    'db':['root@192.168.10.203:22',]
}
env.passwords = {
    'root@192.168.10.201:22':'123456201',
    'root@192.168.10.202:22':'123456202',
    'root@192.168.10.203:22':'123456203'
}
  
@roles('db')       # 只对role为db的主机进行操作
@task
def hello():
    run('ifconfig br0')
"""

""" ============================ @runs_once 
只执行一次，防止task被多次调用
"""

""" ============================ @serial 
强制当前task穿行执行。使用该参数时优先级最高，即便是制定了并发执行的参数
"""

""" ============================ 任务的执行 
fabric执行任务的步骤如下：
    1. 创建任务列表，这些任务就是fab命令行参数指定的任务，fab会保持这些任务的顺序
    2. 对于每个任务，构造需要执行该任务的服务器列表，服务器列表可以通过命令行参数指定，或者env.hosts指定，或者通过hosts和roles装饰器指定
    3. 遍历任务列表，对于每一台服务器分别执行任务，可以将任务列表和服务器列表看作是两个for循环，任务列表是外层循环，服务器列表是内存循环，fabric默认是串行执行的可以通过装饰器或者命令行参数确定任务执行的方式
    4. 对于没有指定服务器的任务默认为本地任务，仅执行一次


关于并行模式：
    1. 通过命令行参数-P(--parallel)通知Fabric并行执行task
    2. 通过env.parallel设置设否需要并行执行
    3. 通过parallel装饰器通知Fabric并行执行task，它接受一个pool_size作为参数(默认为0)，表示可以有几个任务并行执行
"""

""" ============================ 封装task 
fabric提供了一个execute函数，用来对task进行封装。它最大的好处就是可以将一个大的任务拆解为很多小任务，每个小任务互相独立，互不干扰

from fabric.api import *
  
env.roledefs = {
    'web':['root@192.168.10.201:22','root@192.168.10.202:22',],
    'db':['root@192.168.10.203:22',]
}
env.passwords = {
    'root@192.168.10.201:22':'123456201',
    'root@192.168.10.202:22':'123456202',
    'root@192.168.10.203:22':'123456203'
}
  
@roles('db')
def hello():
    run('echo hello')
  
@roles('web')
def world():
    run('echo world')
  
@task
def helloworld():
    execute(hello)   
    execute(world)
"""

""" ============================ utils函数 
包含一些辅助行的功能函数，这些函数位于fabric.utils下，常用的函数如下：
    1. abort：终止函数执行，打印错误信息到stderr，并且以退出码1退出。
    2. warn：输出警告信息，但是不会终止函数的执行
    3. puts：打印输出，类似于Python中的print函数

def helloworld():
    execute(hello)
    abort('----->abort')     # 执行到这里时，直接退出
    warn('----->warn')       # 会发出提示信息，不会退出
    puts('----->puts')       # 会打印括号中的信息
    execute(world)


"""

""" ============================ 带颜色的输出 

blue(text，blod=False)  蓝色
cyan(text，blod=False)  淡蓝色
green(text，blod=False)  绿色
magenta(text，blod=False)  紫色
red(text，blod=False)  红色
white(text，blod=False)  白色
yellow(text，blod=False)   黄色

def ls(path='.'):
    run('ls {0}'.format(path))
 
def hello():
 
    execute(hell)  # task任务hell
    warn(yellow('----->warn'))  # 会发出提示信息，不会退出
    puts(green('----->puts'))  # 会打印括号中的信息
    execute(ls) # task任务ls
    print(green('the text is green')) # 单纯的渲染文字:
 
def hell(name='world'):
    print('hello %s' % name)
 
 
 
"""

""" ============================ 确认信息
有时候我们在某一步执行错误，会给用户提示，是否继续执行时，confirm就非常有用了，它包含在 fabric.contrib.console中

def testconfirm():
 
    result = confirm('Continue Anyway?')
    print(result)
  
  
# 会提示输入y/n
# y 时 result为True
# n 时 result为False
"""
