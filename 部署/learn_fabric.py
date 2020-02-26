"""
python 自动化部署工具

pip install fabric3
"""

""" ============================ 命令参数
-g	指定网关（中转设备），比如堡垒机环境，填写堡垒机IP即可
-P	以异步并行方式运行多台主机任务，默认为串行运行
-R	指定角色（Role）
-l  列出指定文件的任务函数名，只有使用了装饰器 @task 的才会列出
-H  指定目标主机, 多台主机用","号分割
-u  指定远程用户名
-f  指定fab的任务文件, 默认的任务文件名是fabfile.py
-t  设置超时时间, 单位s
-T	远程主机命令执行超时时间
-V  查看版本
-h  帮助
-H	指定目标主机，多台主机用“，”分隔
-w	当命令执行失败，发出告警，而非默认终止任务


启动命令
fab -f fabric_test.py main
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

""" ============================ fabric全局属性设定
env.host            主机列表 env.host=['192.168.17.192', '192.168.17.193']
env.user            用户名
env.port            主机端口, 默认为22
env.password        密码
env.passwords       不同的主机不同的密码 env.passwords={'itcast@192.168.17.192:22':'chuanzhi', 'itcast@192.168.17.193:22':'python'}
"""
