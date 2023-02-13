##### 切换国内源

```
1.获取install文件把官网给的脚本拿下来
curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install >> brew_install

2.替换
BREW_REPO = “https://github.com/Homebrew/brew“.freeze
CORE_TAP_REPO = “https://github.com/Homebrew/homebrew-core“.freeze
更改为
BREW_REPO = "https://mirrors.ustc.edu.cn/brew.git".freeze
CORE_TAP_REPO = "https://mirrors.ustc.edu.cn/homebrew-core.git".freeze

3.执行脚本
/usr/bin/ruby brew_install
```

##### 使用 Alibaba 的 Homebrew 镜像源进行加速

```
平时我们执行 brew 命令安装软件的时候，跟以下 3 个仓库地址有关：
brew.git
homebrew-core.git
homebrew-bottles
通过以下操作将这 3 个仓库地址全部替换为 Alibaba 提供的地址
 
1. 替换 / 还原 brew.git 仓库地址
# 替换成阿里巴巴的 brew.git 仓库地址: 
cd "$(brew --repo)" 
git remote set-url origin https://mirrors.aliyun.com/homebrew/brew.git 
#======================================================= # 
还原为官方提供的 brew.git 仓库地址 
cd "$(brew --repo)" 
git remote set-url origin https://github.com/Homebrew/brew.git
 
2. 替换 / 还原 homebrew-core.git 仓库地址
# 替换成阿里巴巴的 homebrew-core.git 仓库地址: 
cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core" 
git remote set-url origin https://mirrors.aliyun.com/homebrew/homebrew-core.git 
#======================================================= # 
还原为官方提供的 homebrew-core.git 仓库地址 
cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core" 
git remote set-url origin https://github.com/Homebrew/homebrew-core.git
 
3. 替换 / 还原 homebrew-bottles 访问地址
BASH 终端操作方式
# 替换 homebrew-bottles 访问 URL: 
echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.aliyun.com/homebrew/homebrew-bottles' >> ~/.bash_profile 
source ~/.bash_profile 
#======================================================= # 
还原为官方提供的 homebrew-bottles 
访问地址 vi ~/.bash_profile 
# 然后，删除 HOMEBREW_BOTTLE_DOMAIN 这一行配置 
source ~/.bash_profile
```
