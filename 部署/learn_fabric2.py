""" ============================ 参考
https://www.jianshu.com/p/b17a420f39fb?utm_campaign=hugo&utm_medium=reader_share&utm_content=note&utm_source=weixin-friends

https://pypi.org/project/fabric2/
http://docs.fabfile.org/en/2.5/
(2.7, 3.4+)
安装
    pip install fabric
"""

from fabric import Connection, task

import invoke

""" ============================ connection 
def __init__(
　　　　self,
　　　　host,                       #主机ip
　　　　user=None,                  #用户名
　　　　port=None,                  #ssh端口，默认是22
　　　　config=None,                #登录配置文件
　　　　gateway=None,               #连接网关
　　　　forward_agent=None,         #是否开启agent forwarding
　　　　connect_timeout=None,       #设置超时
　　　　connect_kwargs=None,        #设置 密码登录connect_kwargs={"password": "123456"}) 还是 密钥登录connect_kwargs={"key_filename": "/home/myuser/.ssh/private.key"}
　　　　inline_ssh_env=None,      
　　　　):
"""

""" ============================ 参考 
run：    #执行远程命令，如：run('uname -a')
cd：     #切换远程目录，如：cd('/root');   with conn.cd('/root'):继承这个状态
put：    #上传本地文件到远程主机，如：put('/root/tests.py','/root/tests.py')
get:     #获取服务器上文件，如：get('/root/project/tests.log')
sudo：   #sudo方式执行远程命令，如：sudo('service docker start')
"""

""" ============================ 命令
fab --list可以查看执行的函数名：
"""

""" ============================ 调用本地命令
invoke.run('uname -a')
"""

print('1 location')
print('2 debug')
print('3 pro')
env = input('选择环境'.center(50, '-') + '\n')
if env == '3':
    pass
elif env == '2':
    pass
elif env == '1':
    pass
else:
    print('输入错误! 结束'.center(50, '-'))
    exit()

invoke.run('git status')
action_1 = input('是否继续 y/n'.center(50, '-') + '\n')
if action_1 == 'y':
    pass
else:
    exit()

invoke.run('git branch')
branch = input('输入分支:\n')
invoke.run('git checkout {}'.format(branch))
invoke.run('git pull origin {}'.format(branch))
invoke.run('git push origin {}'.format(branch))

# con = Connection(host='47.93.122.31', port=22, user='root')
con = Connection(host='10.211.55.11', port=22, user='root', connect_kwargs={"password": "weiyi"})
con.cd('/home/production/debug')
con.run('ls')

invoke.run('git status')
action_2 = input('是否继续 y/n'.center(50, '-') + '\n')
if action_2 == 'y':
    pass
else:
    exit()

invoke.run('git pull origin {}'.format(branch))
invoke.run('git pull origin {}'.format(branch))


