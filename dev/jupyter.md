# jupyter

##### 安装

```python
pip install jupyter
```

##### 启动

```
jupyter notebook
# 指定端口
jupyter notebook --port 12341
# 启动服务器但不打开浏览器
jupyter notebook --no-browser
# 指定目录
jupyter notebook /Users/laddg/Desktop/lfobject/
# 运行
python -m IPython notebook
http://127.0.0.1:8888/?token=b741f1726522a66f4eb57f37365c635ba29a2fa6a2a55ba2
# 查看配置文件路径
jupyter notebook --generate-config
```

##### 命令

```python
# 为需要在jupyter-notebook中使用的虚拟环境安装ipykernel，如我为自己的py27-caffe虚拟环境添加ipykernel
conda install -n p27 ipykernel
# 激活py27-caffe虚拟环境
conda activate p27
# 然后用如下命令生成ipykernel的配置文件（--name之后跟的是在jupyter-notebook中对应虚拟环境的kernel名称）
python -m ipykernel install --name p27
# 查看已有的kernel
jupyter kernelspec list
# 删除已有的kernel
jupyter kernelspec remove p27
# 以上的命令删除仅仅是配置文件，并没有卸载相应虚拟环境的ipykernel，因此若要再次安装相应python虚拟环境的kernel，只需激活虚拟环境，然后
python -m ipykernel install --name p27
```

##### 插件管理工具Nbextensions

```
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

插件
Code prettify 对代码进行格式化 ctrl + L
```

