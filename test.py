"""
run：用于执行远程命令的封装
sudo：以sudo权限执行远程命令
env：保存用户配置的字典

"""
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.utils import abort
from fabric.colors import *

env.hosts = ['10.211.55.11']
env.port = 22
env.user = 'root'
env.password = 'weiyi'


def hostname():
    run('hostname')


def ls(path='.'):
    run('ls {0}'.format(path))


def tail(path='/etc/pas', line=10):
    run('tail -n {0} {1}'.format(line, path))


def hello():
    with settings(hide('everything'), warn_only=True):  # 关闭显示
        result = run('anetstat -lntup|grep -w 25')
        print(result)  # 命令执行的结果
        print(result.return_code)  # 返回码，0表示正确执行，1表示错误
        print(result.failed)
