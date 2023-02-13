##### 问题

```
python3.7m

```

# python

##### 编译安装 pyton

```bash
# 3.7.10 / 3.9.16
$ wget https://registry.npmmirror.com/-/binary/python/3.7.10/Python-3.7.10.tar.xz
$ wget https://registry.npmmirror.com/-/binary/python/3.9.16/Python-3.9.16.tar.xz

$ cd Python-3.7.10
$ ./configure --prefix=/opt/python-3.7.10 --enable-optimizations
$ make
$ make install

$ python3 -m pip install virtualenv
```

##### 删除编译安装 python

```bash
# 1. 搜索安装包
$ rpm -qa|grep python3

# 2. 卸载
$ rpm -e python3-rpm-macros-3-34.el7.noarch
或
$ rpm -e --nodeps python3-rpm-macros-3-34.el7.noarch
    -e: 卸载   
    --nodeps: 忽略依赖
    
# 3. 查看是否都卸载了
$ whereis python3
```

##### 开发工具

```bash
$ yum install python-devel python3-devel
```

##### pip 安装

- centos 8 stream

  ```bash
  $ dnf reinstall python2-pip
  $ dnf reinstall python3-pip
  ```

- centos 7

  ```bash
  $ yum install python-pip
  $ pip install --upgrade pip
  
  
  https://pypi.org/project/pip/
  
  $ wget https://files.pythonhosted.org/packages/a3/50/c4d2727b99052780aad92c7297465af5fe6eec2dbae490aa9763273ffdc1/pip-22.3.1.tar.gz
  
  $ python setup.py install
  ```

#####  pip 安装(2)

- 在 Python2.x 中安装

  ```bash
  $ curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip2.py
  $ sudo python get-pip2.py
  $ pip --version
  $ pip install --upgrade pip
  ```

- 在 Python3.x 中安装

  ```bash
  $ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  $ sudo python3 get-pip.py
  $ pip3 --version
  $ pip3 install --upgrade pip
  ```

# pip

##### pip 参数

| 参数    | 说明                                                         |
| ------- | ------------------------------------------------------------ |
| --user  | 安装第三方库时只对当前用户可见<br />会将程序包安装到 $HOME/.local 路径下, 其中包含三个字文件夹 bin, lib 和 share<br />在虚拟环境下不可使用 --user 选项, 因为用户目录在该环境下不可见 |
| --force |                                                              |

##### 临时改变源

```bash
$ pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

##### 永久改变源 

```bash
# windows
%APPDATA%\pip\pip.ini

# linux
创建并添加 ~/.pip/pip.conf

[global]
index-url = https://pypi.mirrors.ustc.edu.cn/simple/
[install]
trusted-host = https://pypi.mirrors.ustc.edu.cn/
```

# pyenv

##### 依赖 - centos

```bash
$ dnf install gcc gcc-c++ glibc glibc-devel libffi-devel sqlite-devel bzip2-devel bzip2 readline-devel openssl-devel bzip2-devel make zlib zlib-devel patch lzma xz-devel
```

##### 依赖 - mac

```bash
# 升级系统python
$ brew reinstall python
$ brew install zlib openssl
```

##### 依赖 - ubuntu

```bash
$ apt-get install build-essential zlib1g-dev
```

##### pyenv

> [github](https://github.com/pyenv/pyenv)
>
> pip 包安装在虚拟环境的 ~/.pyenv/versions/p-3.9.2-learn/lib 目录下

- clone

  ```bash
  $ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
  ```

- 设置变量 - zsh

  ```shell
  $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
  $ echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
  $ echo 'eval "$(pyenv init -)"' >> ~/.zshrc
  ```

##### pyenv-virtualenv

> [github](https://github.com/pyenv/pyenv-virtualenv)
>
> 用于创建 python 虚拟环境

- clone

  ```bash
  $ git clone https://github.com/pyenv/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
  ```
  
- .zshrc 添加如下内容:

  ```bash
  $ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
  ```

```
exec $SHELL -l
```

##### 命令

```bash
pyenv help install
pyenv commands				# 所有可用的 pyenv 命令
pyenv version  				# 显示当前目录下采用的 python 版本
pyenv versions 				# 列出系统中安装的 python 版本
pyenv install --list		# 列出可安装版本
pyenv install <version>		# 安装对应版本 
pyenv install -v <version>	# 安装对应版本，若发生错误，可以显示详细的错误信息 
pyenv uninstall <version>	# 卸载 python 3.4.0
pyenv which python			# 显示当前python安装路径 
pyenv global <version>		# 全局设置, 整个系统生效 
pyenv local <version>		# 当前路径创建一个.python-version, 以后进入这个目录自动切换为该版本 
pyenv shell <version>		# 当前shell的session中启用某版本，优先级高于global 及 local
pyenv rehash 				# 安装完成之后需要对数据库进行更新



pyenv virtualenvs
pyenv virtualenv <version> <name> 	# 创建3.6.4版本的虚拟环境 
pyenv activate <name> 				# 激活 env-3.6.4 这个虚拟环境 
pyenv deactivate 					# 停用当前的虚拟环境 
pyenv uninstall env-3.6.4 			# 删除 env-3.6.4 这个虚拟环境
```

```
# 安装时使用 -v 查看详细信息, 缺少哪个依赖安装哪个
$ pyenv install -v 3.9.2
```



```
pyenv global 3.3.3 2.7.6
pyenv versions
  system
* 2.7.6 (set by /Users/yyuu/.pyenv/version)
* 3.3.3 (set by /Users/yyuu/.pyenv/version)
  venv27
```

##### 离线包安装python

> [linux 阿里源下载](https://registry.npmmirror.com/binary.html?path=python/)
>
> [windows 下载](https://www.python.org/downloads/windows/)

```
wget https://registry.npmmirror.com/-/binary/python/3.7.10/Python-3.7.10.tar.xz
wget https://registry.npmmirror.com/-/binary/python/3.9.16/Python-3.9.16.tar.xz

*.tar.xz
创建目录放安装文件 ~/.pyenv/cache
使用 pyenv install 2.7.16 查看下载文件的目录, 并用wget下载
安装 pyenv install 2.7.16
```

# venv

```bash
# venv 模块是 Python3.3 后自带的虚拟环境创建和管理工具, Python2.X不能使用, 因此只能创建 python3 的虚拟环境, 并且是系统已经存在的.
$ python3 -m venv /home/yan/env3
```

# virtualenv

> virtualenv 同时支持 Python2.X 和 Python3.X, 并且是系统已经存在的.

```bash
# 安装
$ pip install virtualenv


# 参数
	--no-site-packages: 已经安装到系统 python 环境中的所有第三方包都不会复制过来
	--system-site-packages: 与上面相反
	--distribute: 
	-p:


# 安装python2.7虚拟环境
$ virtualenv /home/yan/env 
# 安装 python3.5 虚拟环境
$ virtualenv -p /usr/bin/python3.5 --no-site-packages test


# 激活虚拟环境
$ source /home/yan/env3/bin/activate
$ source ./venv/bin/activate
$ source ./venv/Scripts/activate

# 退出环境
$ deactivate 
```

# virtualenvwrapper

> 对 virtualenv 的一个封装
>
> 所有环境保存在 ~/.virtualenvs 
>
> [pip](https://pypi.org/project/virtualenvwrapper/)
>
> [Python Releases for Windows | Python.org](https://www.python.org/downloads/windows/)

##### 安装

- 安装 (依赖 virtualenv)

  ```bash
  $ pip3 install --user virtualenv
  $ pip3 install --user virtualenvwrapper
  ```

-  设置环境变量 (~/.zshrc)

  ```bash
  # 所有的虚拟环境会创建在 WORKON_HOME 目录下
  export WORKON_HOME=$HOME/.virtualenvs
  export PROJECT_HOME=$HOME/workspace
  # 指定 python 路径
  export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
  # 指定 virtualenv 路径
  export VIRTUALENVWRAPPER_VIRTUALENV=~/.local/bin/virtualenv
  ```

- 激活

  ```bash
  $ source ~/.zshrc
  $ source ~/.local/bin/virtualenvwrapper.sh
  ```

##### 环境变量

```bash
# 指定使用 mkproject 创建的项目路径
PROJECT_HOME

# 指定 hooks 目录, 默认 $WORKON_HOME
VIRTUALENVWRAPPER_HOOK_DIR

# hooks 日志
VIRTUALENVWRAPPER_LOG_FILE

# 1 (默认): 使用 mkproject projectname 创建虚拟环境及工程目录后, workon projectname 默认会自动切换项目目录
# 0: workon projectname 不进入工程目录只激活虚拟环境
VIRTUALENVWRAPPER_WORKON_CD

# python 路径
VIRTUALENVWRAPPER_PYTHON

# virtualenv 路径
VIRTUALENVWRAPPER_VIRTUALENV

# 产生的临时文件位置 ( 默认 $TMPDIR, 如果没有使用 /tmp)
VIRTUALENVWRAPPER_TMPDIR
```

##### 命令

```bash
mkvirtualenv [-a project_path] [-i package] [-r requirements_file] [virtualenv options] env_name

# 创建虚拟环境：
$ mkvirtualenv my_venv
$ mkvirtualenv -p /opt/python-3.11.1/bin/python3 p3111-nvim
# 环境列表
$ workon
# 开始在虚拟环境
$ workon my_venv
# 注销当前已经被激活的虚拟环境：
$ deactivate
# 删除虚拟环境：
$ rmvirtualenv my_venv  
# 退出环境
$ deactivate
# 虚拟环境的列表
$ lsvirtualenv
# 进入当前激活的虚拟环境
$ cdvirtualenv
# 进入虚拟环境中的site-packages目录
$ cdsitepackages
# 列出当前环境安装了的包
$ lssitepackages


mkproject mic：创建mic项目和运行环境mic
mktmpenv：创建临时运行环境
```

# virtualenvwrapper-win

```
pip install virtualenvwrapper-win

安装在
C:\Users\username\Envs
```

##### 删除环境是禁止访问

原因是有其他进程在使用这个环境

```
PS C:\Users\gonglongfei> rmvirtualenv p3710-dev
p3710-dev\Scripts\python.exe - 拒绝访问。
p3710-dev\Scripts\python3.dll - 拒绝访问。
p3710-dev\Scripts\python39.dll - 拒绝访问。
p3710-dev\Scripts\vcruntime140.dll - 拒绝访问。
```

# pipenv

##### 安装

```
pip 包管理工具
```

```bash
$ pip3 install --user pipenv
```

```
会在项目目录下生成2个文件Pipfile和Pipfile.lock


pipenv install --dev生成自己的虚拟环境。

Pipfile.lock 文件是通过hash算法将包的名称和版本，及依赖关系生成哈希值，可以保证包的完整性。
```

##### 命令

```bash
$ pipenv --version
$ pipenv install				# 安装 Pipfile 虚拟环境
安装完虚拟环境后会创建两个文件, 存在则覆盖:
	Pipfile: 保存项目的python版本、依赖包等相关信息
	Pipfile.lock: 用于对Pipfile的锁定	
$ pipenv install XXX  			# 安装模块并加入到 Pipfile
$ pipenv install XXX==1.11
$ pipenv install pytest --dev	# 仅安装开发环境下的依赖包（项目部署上线不需要的包）
$ pipenv uninstall XXX  		# 卸载XXX模块并从Pipfile中移除
$ pipenv uninstall --all  		# 卸载全部包并从Pipfile中移除
$ pipenv uninstall --all-dev  	# 卸载全部开发包并从Pipfile中移除

$ pipenv shell					# 进入虚拟环境(项目目录下)
$ exit							# 退出虚拟环境
$ pipenv graph					# 查看包依赖关系
$ pipenv lock                  	#更新Pipfile.lock文件锁定当前环境的依赖版本
$ pipenv check  				# 检查安全漏洞
$ pipenv --venv					# 查看虚拟环境安装路径


$ pipenv --python 3  # 指定使用Python3创建环境
$ pipenv --python 3.6  # 指定使用Python3.6创建环境
$ pipenv --python 2.7.14  # 指定使用Python2.7.14创建环境
```

- Pipfile 文件

```
[[source]]
url = "https://pypi.tuna.tsinghua.edu.cn/simple"
verify_ssl = true
name = "pypi"
 
[packages]
requests = "*"
pyyaml = "*"
Django = "*"
 
[dev-packages]
pytest = "*"
 
[requires]
python_version = "3.7"
 
[scripts]
django = "python manage.py runserver 0.0.0.0:8080"
```

```
source 用来设置仓库地址，即指定镜像源下载虚拟环境所需要的包
packages 用来指定项目依赖的包，可以用于生产环境和生成requirements文件
dev-packages 用来指定开发环境需要的包，这类包只用于开发过程，不用与生产环境。
requires 指定目标Python版本
scripts 添加自定义的脚本命令，并通过 pipenv run + 名称 的方式在虚拟环境中执行对应的命令 。

pipenv run django 相当于 执行命令 pipenv run python manage.py runserver 0.0.0.0:8080
```

##### pipenv 与 virtualenvwrapper 结合使用

```
0. 操作系统安装 virtualenvwrapper 和 pipenv
1. 先 workon 进入虚拟环境
2. 在用 pipenv 安装虚拟环境
```

# pip-tools

##### 安装

```
https://github.com/jazzband/pip-tools/
https://github.com/jazzband/pip-tools/

pip install pip-tools

python 包管理工具, 包含 pip-compile 和 pip-sync 两部分
```

##### pip-compile

- pip-compile 命令根据 requirements.in 或 setup.py 生成 requirements.txt 文件
- requirements.in 或 setup.py 需要手动创建
- 直接运行 pip-compile 会默认查找 requirements.in 或 setup.py 这两个文件, 也可以指定文件

#####  使用 setup.py 文件

```

```

##### 不使用 setup.py 文件

- 1. 手动创建 requirements.in 文件. 例如 Flask 项目写入一下内容

```
# requirements.in
# 可以指定版本
flask==1.0.1
```

- 2. 生成 requirements.txt 文件

```
$ pip-compile requirements.in

# 启动 hash 检测
$ pip-compile --generate-hashes requirements.in
```

- 3. 如果需要根据多个 *.in 文件生成 *.txt 文件时必须制定输出的文件, 否则报错

```
$ pip-compile requirements_test.in requirements.in --output-file aaa.txt
```

- 4. 更新包. 如果 requirements.txt 指定了版本则会被更新, 使用指定的版本

```
# 更新所有包
$ pip-compile --upgrade

# 更新指定包
$ pip-compile --upgrade-package flask

# 同时更新两个包
$ pip-compile --upgrade-package django --upgrade-package requests

# django 更新到最新, requests 更新到 2.0.0
$ pip-compile --upgrade-package django --upgrade-package requests==2.0.0
$ pip-compile --upgrade --upgrade-package 'requests<3.0'
$ pip-compile --upgrade-package 'django<1.0' --output-file requirements-django0x.txt
```

- CUSTOM_COMPILE_COMMAND

```

```

##### pip-sync

- pip-sync 根据 *.txt 文件安装包, 直接运行时默认使用 requirements.txt

```
$ pip-sync
$ pip-sync requirements.txt
$ pip-sync dev-requirements.txt
$ pip-sync dev-requirements.txt requirements.txt
```





# pylint

##### 参考

```
https://www.jianshu.com/p/c0bd637f706d
```

##### 安装



##### pylint

```bash
$ pip install pylint
版本信息
$ pylint --version
在当前目录生成默认配置文件 pylint.conf
$ pylint --persistent=n --generate-rcfile > pylint.conf
检测单个文件
$ pylint --rcfile=pylint.conf abc.py
```

```
C表示convention，规范
W表示warning，告警；
pylint结果总共有四个级别：error，warning，refactor，convention，可以根据首字母确定相应的级别。1, 0表示告警所在文件中的行号和列号。
```

##### pycharm

```
program：是python安装路径下的Scripts路径
/Users/gladd/.pyenv/versions/2.7.16/envs/p27/bin/pylint
Arguments:--reports=n --disable=C0103 $FilePath$  （最后必须以$FilePath$结尾）
--reports=n --disable=C0103,C0301,W0703 $FilePath$

working directory：$FileDir$（必须是这个）
output filters：$FILE_PATH$:$LINE$:
```

##### 命令行命令

```
pylint pylint_example.py
显示统计报告
pylint -r y pylint_example.py
不显示某个类型的信息
pylint -r y pylint_example.py --disable=C
pylint -r y pylint_example.py --disable=C0301
```



# 错误 / 失败

##### pip list

- 报错信息

  ```
  DEPRECATION: The default format will switch to columns in the future. You can use --format=(legacy|columns) (or define a format=(legacy|columns) in your pip.conf under the [list] section) to disable this warning.
  ```

- 解决办法, 在 .pip/pip.conf 中添加

  ```
  [list]
  format = columns
  ```

##### pyltp 安装

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

##### 安装 psycopg2

- centos

  ```bash
  $ yum install libjpeg libjpeg-devel zlib zlib-devel freetype freetype-devel lcms lcms-devel
  $ yum install postgresql-devel*
  $ yum install python-imaging
  ```

- mac

  ```bash
  $ brew update
  $ brew install --force ossp-uuid
  $ brew install postgresql
  $ pip install psycopg
  ```

##### mysqldb

https://pypi.org/project/mysqlclient/

```
mysqlclient安装

centos7
先安装依赖
yum install mysql-devel
在安装
pip install mysqlclient

mac 安装
brew install mysql-connector-c
brew install mariadb
pip install mysqlclient


debian
apt-get install default-libmysqlclient-dev build-essential
```



