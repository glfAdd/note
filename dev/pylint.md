https://www.jianshu.com/p/c0bd637f706d

##### pylint

```bash
安装
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

