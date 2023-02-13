[download page](https://docs.conda.io/en/latest/miniconda.html)

##### conda 国内源

```
源的配置文件保存位置: 用户目录下 .condarc 文件

# 重置源配置
conda config --remove-key channels

# 添加源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes
```

##### pip 国内源

```
1. 在windows文件管理器中,输入 %APPDATA%

2. 会定位到一个新的目录下，在该目录下新建 pip 文件夹，然后到pip文件夹里面去新建个 pip.ini 文件

3. 在新建的pip.ini文件中输入以下内容，搞定文件路径："C:\Users\Administrator\AppData\Roaming\pip\pip.ini"
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = https://pypi.tuna.tsinghua.edu.cn
```

##### 命令

```
conda upgrade conda				更新conda
conda create -n p392_lean python=3.9.2

conda activate p392_lean
```

##### 问题 1

```
描述问题:
An unexpected error has occurred. Conda has prepared the above report.


解决办法:
conda clean -i
```

##### 问题 2

```
创建环境失败：
CondaHTTPError: HTTP 000 CONNECTION FAILED for url


解决办法：
    1. 编辑其中的 .condarc 文件, 删除 - default
    2. 将 - https://... 改成 - http://...
```

##### 问题 3

```
启动以后显示：
        . : 无法加载文件 C:\Users\lg\Documents\WindowsPowerShell\profile.ps1，因为在此系统上禁止运行脚本。有关详细信息，请参阅
        https:/go.microsoft.com/fwlink/?LinkID=135170 中的 about_Execution_Policies。
        所在位置 行:1 字符: 3
        + . 'C:\Users\lg\Documents\WindowsPowerShell\profile.ps1'
        +   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            + CategoryInfo          : SecurityError: (:) []，PSSecurityException
            + FullyQualifiedErrorId : UnauthorizedAccess


解决办法：
    1. 以管理员身份运行PowerShell
    2. 执行：get-ExecutionPolicy，回复Restricted，表示状态是禁止的
    3. 执行：set-ExecutionPolicy RemoteSigned
```





