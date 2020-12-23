# github

```
https://github.com/pyenv/pyenv
https://github.com/pyenv/pyenv-virtualenv
```

# macOS

##### brew安装

```
$ brew uninstall pyenv
$ brew update
$ brew install pyenv
```

##### 安装 pyenv

```bash
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv

配置环境变量 (如果你使用 bash，就依次执行如下命令)
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
配置环境变量 (如果你使用 zsh，就依次执行如下命令)
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.zshrc

重新初始化 shell 环境, 或者关闭在打开
$ exec $SHELL
```

##### 安装 pyenv-virtualenv

```bash
$ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv

如果你使用 bash，就执行如下命令：
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
如果你使用 zsh，就执行如下命令：
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

重新初始化 shell 环境, 或者关闭在打开
$ exec $SHELL
```

# debian

```
先安装依赖
apt-get update
apt-get install --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
apt-get install zlibc zlib1g-dev
```

# centos

##### 安装 pyenv

```bash
python依赖的库文件
# yum install gcc
# yum install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel libffi-devel


# mkdir ~/.pyenv
# git clone git://github.com/yyuu/pyenv.git ~/.pyenv  
# echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc  
# echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc  
# echo 'eval "$(pyenv init -)"' >> ~/.bashrc  
# exec $SHELL -l 
```

##### 安装 pyenv-virtualenv

```bash
# git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv

如果你使用 bash，就执行如下命令：
# echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
如果你使用 zsh，就执行如下命令：
# echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

重新初始化 shell 环境, 或者关闭在打开
# exec $SHELL
```

# 命令

```bash
which pyenv												# 安装路径
cd $(pyenv root) & git pull				# 更新 pyenv
rm -rf $(pyenv root)							# 卸载 pyenv

pyenv commands 										# 显示所有可用命令
pyenv --version										# pyenv版本
pyenv versions										# pyenv python版本
pyenv install --list							# 可以安装的版本
pyenv install 3.7.4								# 安装python
pyenv virtualenv 3.7.4 p37				# 创建虚拟环境
pyenv activate p37								# 激活虚拟环境
```

# 离线包安装python

```
创建目录放安装文件 ~/.pyenv/cache
使用pyenv install 2.7.16 查看下载文件的目录, 并用wget下载
安装 pyenv install 2.7.16
```

# pip

##### centos

```bash
指定版本
pip install flask==0.10.1
临时使用某个源
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
导入出文件
pip freeze > abc.text

安装错误的时候需要先安装
yum install python-devel
pip install turtle
python -m pip install --upgrade --force pip 

永久改变源
[root@localhost ~]# cd ~
[root@localhost ~]# mkdir .pip
[root@localhost ~]# cd .pip
[root@localhost .pip]# vim pip.conf
添加
[global]
index-url = https://mirrors.aliyun.com/pypi/simple
[install]
trusted-host = https://mirrors.aliyun.com


项目安装psycopg2失败需要安装
yum install libjpeg libjpeg-devel zlib zlib-devel freetype freetype-devel lcms lcms-devel
yum install postgresql-devel*
yum install python-imaging
```

##### 安装psycopg2失败

```
brew update
brew install --force ossp-uuid
brew install postgresql
pip install psycopg
```

##### pyltp 安装失败

```
error: $MACOSX_DEPLOYMENT_TARGET mismatch: now "10.12" but "10.15" during configure

切换到虚拟环境
$ git clone https://github.com/HIT-SCIR/pyltp
$ cd pyltp
$ git submodule init
$ git submodule update
vim setup.py 修改文件121行
os.environ['MACOSX_DEPLOYMENT_TARGET'] = '10.12'
修改为后问题解决
os.environ['MACOSX_DEPLOYMENT_TARGET'] = '10.14' 
$ python setup.py install


$ MACOSX_DEPLOYMENT_TARGET=10.7 python setup.py install


```


##### sqlalchemy init 失败

```
执行 python gendb.py db init报错 Error: Directory migrations already exists and is not empty
解决办法:

删除目录下的 migrations
```





