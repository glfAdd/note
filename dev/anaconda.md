# anaconda

```python
# 添加Anaconda的TUNA镜像
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
```

##### iterm默认启动anaconda

```python
vim ~/.bash_profile
export PATH="/anaconda2/bin:$PATH"
source activate
source deactivate
```

##### 命令

```
查看版本
conda --version
前已有的Python环境
conda info --envs
添加一个aaa环境
conda create --name aaa python=2.7
当前使用的Python版本
python --version
切换环境
activate aaa
退出环境
deactivate aaa
删除环境
conda remove --name aaa --al

conda list
conda install numpy
anaconda search -t conda XXXXX
anaconda show XXXXX
```

