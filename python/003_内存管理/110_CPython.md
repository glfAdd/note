# CPython

##### 下载

```bash
git clone https://github.com/python/cpython
#切换我们需要的分支
git checkout v3.8.0b3 
```

##### 目录结构

```
cpython/
│
├── Doc      ← 源代码文档说明
├── Grammar  ← 计算机可读的语言定义
├── Include  ← C 语言头文件（头文件中一般放一些重复使用的代码）
├── Lib      ← Python 写的标准库文件
├── Mac      ← Mac 支持的文件
├── Misc     ← 杂项
├── Modules  ← C 写的标准库文件
├── Objects  ← 核心类型和对象模块
├── Parser   ← Python 解析器源码
├── PC       ← Windows 编译支持的文件
├── PCbuild  ← 老版本的 Windows 系统 编译支持的文件
├── Programs ← Python 可执行文件和其他二进制文件的源代码
├── Python   ← CPython  解析器源码
└── Tools    ← 用于构建或扩展 Python 的独立工具
```





