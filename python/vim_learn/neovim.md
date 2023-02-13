##### 参考案例

```
https://www.zhihu.com/column/c_1527964562929893376
https://github.com/ayamir/nvimdots/wiki/Plugins


单词拼写 待验证
https://github.com/octaltree/cmp-look


(不好用)右边的图片: https://github.com/edluffy/hologram.nvim
quickfix
数据库支持: https://github.com/tpope/vim-dadbod



重点:
https://github.com/nshen/learn-neovim-lua/commit/2635dec11c52292cd93dc5320a7d1df5f397acc4
v2 分支
```

##### [neovim map](https://neovim.io/doc/user/map.html)

##### [neovim lua document](https://github.com/glepnir/nvim-lua-guide-zh)

# 安装

[homepage](http://neovim.io/)

[github](https://github.com/neovim/neovim/releases)

##### 二进制

```bash
$ dnf install python3 bison
$ wget https://github.com/neovim/neovim/releases/download/v0.8.1/nvim-linux64.tar.gz
$ tar xvf nvim-linux64.tar.gz
$ ln -s /opt/nvim-linux64/bin/nvim /usr/bin/nvim
```

##### linux (centos 7 弃用)

##### gcc

- gcc 版本太旧, 安装时需要临时切换到新版本的gcc, 否则编译失败

  ```
  configure: error:
  *** These critical programs are missing or too old: make bison compiler
  *** Check the INSTALL file for required versions.
  ```

- 安装 bison

  ```bash
  $ yum install bison
  ```

- 临时切换 gcc 版本

##### install GLIBC_2.29

> [download](https://ftp.gnu.org/gnu/glibc/)

- 运行 neovim 时出现错误

  ```
  ./nvim: /lib64/libc.so.6: version `GLIBC_2.28' not found (required by ./nvim)
  ./nvim: /lib64/libm.so.6: version `GLIBC_2.29' not found (required by ./nvim)
  ```

- 安装

  ```bash
  # 查看版本
  $ strings /lib64/libc.so.6 | grep GLIBC_
  
  # 依赖 
  $ dnf install bison
  
  $ wget https://ftp.gnu.org/gnu/glibc/glibc-2.29.tar.gz
  $ cd glibc-2.29
  $ mkdir build
  $ cd build
  $ ../configure --prefix=/usr --disable-profile --enable-add-ons --with-headers=/usr/include --with-binutils=/usr/bin
$ make
  # 有保存, 但不影响 glibc 升级
  $ make install
  ```
  
- 问题

  ```
  collect2: error: ld returned 1 exit status
  Execution of gcc -B/usr/bin/ failed!
  The script has found some problems with your installation!
  Please read the FAQ and the README file and check the following:
  - Did you change the gcc specs file (necessary after upgrading from
    Linux libc5)?
  - Are there any symbolic links of the form libXXX.so to old libraries?
    Links like libm.so -> libm.so.5 (where libm.so.5 is an old library) are wrong,
    libm.so should point to the newly installed glibc file - and there should be
    only one such link (check e.g. /lib and /usr/lib)
  You should restart this script from your build directory after you've
  fixed all problems!
  Btw. the script doesn't work if you're installing GNU libc not as your
  primary library!
  make[1]: *** [Makefile:111: install] Error 1
  make[1]: Leaving directory '/opt/glibc-2.29'
  make: *** [Makefile:12: install] Error 2
  
  
  暂时没法解决, 但不影响 glibc 的升级
  ```


# 依赖

```
$ pip install autopep8 black click debugpy isort pyaml PyYAML yapf pyright

$ pip install pynvim
```

```bash
$ dnf install npm

# 安装速度慢, 使用 -g 指定源 (临时)
$ npm install vscode-langservers-extracted -g --registry=https://registry.npm.taobao.org

(永久)
$ npm config set registry https://registry.npm.taobao.org
```



##### python 3 支持

```bash
1. 查看是否支持 python
:checkhealth

$ pip install pynvim

(未使用这个命令安装)
$ /usr/bin/python3 -m pip install pynvim

(未使用这个命令安装)
$ pip install neovim
$ pip3 install neovim


# 安装 python3 支持
$ dnf install libevent-devel python-gevent python-devel python3-devel
```

##### python 环境

```bash
$ pyenv virtualenv 3.9.2 p-3.9.2-neovim
$ pyenv activate p-3.9.2-neovim
$ pip install --upgrade pip
$ pip install neovim pynvim pytest debugpy isort ueberzug ranger-fm

$ pip install autopep8 yapf black
```

##### lua

##### java (lsp 需要)

##### node (lsp 需要)

```bash
$ brew install node
$ aptitude install nodejs npm
$ dnf install nodejs npm
```

##### lazygit (git 工具)

> [github](https://github.com/jesseduffield/lazygit)

```
$ sudo dnf copr enable atim/lazygit
$ sudo dnf install lazygit 


git clone https://github.com/jesseduffield/lazygit.git
cd lazygit
go install
```

##### lipboard 支持

> Vim 与系统共用剪切板

查看帮助信息

```
:help clipboard
```

安装

```bash
$ aptiotude install xsel
$ ndf install xsel
```

##### rg

```bash
$ aptitude install ripgrep
$ dnf install ripgrep
```

##### fd

```bash
$ aptitude install fd-find
$ dnf install fd-find
```

##### ranger

```bash
$ dnf install ranger
或
$ pip install ranger-fm


```

##### ueberzug (失败)

```bash
安装依赖
$ sudo aptitude install libx11-dev libxext-dev python-dev python3-dev

pip install ueberzug
```

##### tmux

```bash
$ aptitude install tmux
$ dnf install tmux
```

##### words (cmp-look 使用)

```
dnf install words
```

##### xshell

```

```

##### github 加速地址

```bash
$ git config --global url."https://hub.fastgit.xyz/".insteadOf "https://github.com/"
```



# package

##### 配置文件

```
~/.config/nvim/init.vim (弃用)
~/.config/nvim/init.lua (推荐)
```

##### packer.nvim (包管理)

> [github](https://github.com/wbthomason/packer.nvim)
>
> 包保存在 ~/.local/share/nvim/site/pack/packer/start/

- install

  ```bash
  $ git clone --depth 1 https://github.com/wbthomason/packer.nvim ~/.local/share/nvim/site/pack/packer/start/packer.nvim
  ```

- setting

  ```
  use {
    'myusername/example',        -- The plugin location string
    -- The following keys are all optional
    disable = boolean,           -- Mark a plugin as inactive
    as = string,                 -- Specifies an alias under which to install the plugin
    installer = function,        -- Specifies custom installer. See "custom installers" below.
    updater = function,          -- Specifies custom updater. See "custom installers" below.
    after = string or list,      -- Specifies plugins to load before this plugin. See "sequencing" below
    rtp = string,                -- Specifies a subdirectory of the plugin to add to runtimepath.
    opt = boolean,               -- Manually marks a plugin as optional.
    branch = string,             -- Specifies a git branch to use
    tag = string,                -- Specifies a git tag to use. Supports '*' for "latest tag"
    commit = string,             -- Specifies a git commit to use
    lock = boolean,              -- Skip updating this plugin in updates/syncs. Still cleans.
    run = string, function, or table, -- Post-update/install hook. See "update/install hooks".
    requires = string or list,   -- Specifies plugin dependencies. See "dependencies".
    rocks = string or list,      -- Specifies Luarocks dependencies for the plugin
    config = string or function, -- Specifies code to run after this plugin is loaded.
    -- The setup key implies opt = true
    setup = string or function,  -- Specifies code to run before this plugin is loaded.
    -- The following keys all imply lazy-loading and imply opt = true
    cmd = string or list,        -- Specifies commands which load this plugin. Can be an autocmd pattern.
    ft = string or list,         -- Specifies filetypes which load this plugin.
    keys = string or list,       -- Specifies maps which load this plugin. See "Keybindings".
    event = string or list,      -- Specifies autocommand events which load this plugin.
    fn = string or list          -- Specifies functions which load this plugin.
    cond = string, function, or list of strings/functions,   -- Specifies a conditional test to load this plugin
    module = string or list      -- Specifies Lua module names for require. When requiring a string which starts
                                 -- with one of these module names, the plugin will be loaded.
    module_pattern = string/list -- Specifies Lua pattern of Lua module names for require. When
    requiring a string which matches one of these patterns, the plugin will be loaded.
  }
  ```

- 命令

  ```
  packer.install(plugins)：如果指定的插件尚未安装，请安装它们
  packer.update(plugins)：更新指定的插件，安装任何缺失的插件
  packer.clean()：删除任何已禁用或不再管理的插件
  packer.sync(plugins)：执行一个clean，后跟一个update
  packer.compile(path)：编译lazy-loader代码并保存到path。
  packer.snapshot(snapshot_name, ...)：创建将位于config.snapshot_path/<snapshot_name>下的快照文件。如果snapshot_name是一条绝对路径，那么这将是拍摄快照的位置。或者，可以提供插件名称列表，以有选择地选择要快照的插件。
  packer.rollback(snapshot_name, ...)：回滚插件状态将位于config.snapshot_path/<snapshot_name>下的快照文件。如果snapshot_name是一条绝对路径，那么这将是拍摄快照的位置。或者，可以提供插件名称列表，以有选择地选择要还原的插件。
  packer.delete(snapshot_name)：删除config.snapshot_path/<snapshot_name>下的快照文件。如果snapshot_name是一个绝对路径，那么这将是快照将被删除的位置。
  ```

- 缓存

  ```
  packer.nvim 的缓存在 ~/.cache/nvim
  ```

#####  gruvbox.nvim (主题配色)

> [github](https://github.com/ellisonleao/gruvbox.nvim)

#####  alpha-nvim (启动画面)

> [github](https://github.com/goolord/alpha-nvim)

##### bufferline (上)

> [github](https://github.com/akinsho/bufferline.nvim)

#####  lualine.nvim (下)

> [github](https://github.com/nvim-lualine/lualine.nvim)

##### trouble.nvim (语法错误列表)

> [github](https://github.com/folke/trouble.nvim)

##### undotree

> [github](https://github.com/mbbill/undotree)

##### lazygit

> [github](https://github.com/kdheepak/lazygit.nvim)

##### gitsigns.nvim

> [github](https://github.com/lewis6991/gitsigns.nvim)

##### nvim-tree.lua (文件管理)

> [github](https://github.com/kyazdani42/nvim-tree.lua)

```
o 打开关闭文件夹
a 创建文件
r 重命名
x 剪切
c 拷贝
p 粘贴
d 删除
```

##### which-key.nvim (列表页快捷键)

> [github](https://github.com/folke/which-key.nvim)

##### nvim-treesitter (语法高亮)

> [github](https://github.com/nvim-treesitter/nvim-treesitter)

```bash
# 查看已安装的 Language parser
:TSInstallInfo

# 手动安装 Language parser
:TSInstall python
:TSInstall java
:TSInstall comment
:TSInstall json
:TSInstall lua
:TSInstall markdown
:TSInstall vim
:TSInstall yaml


# 显示/隐藏 高亮
:TSBufToggle highlight
```

##### Comment.nvim (注释)

> [github](https://github.com/numToStr/Comment.nvim)

- normal

  `gcc` - Toggles the current line using linewise comment
  `gbc` - Toggles the current line using blockwise comment
  `[count]gcc` - Toggles the number of line given as a prefix-count using linewise
  `[count]gbc` - Toggles the number of line given as a prefix-count using blockwise
  `gc[count]{motion}` - (Op-pending) Toggles the region using linewise comment
  `gb[count]{motion}` - (Op-pending) Toggles the region using linewise comment

- visual

  `gc` - Toggles the region using linewise comment
  `gb` - Toggles the region using blockwise comment

##### symbols-outline.nvim (边栏显示函数对象)

> [github](https://github.com/simrat39/symbols-outline.nvim)

##### vim-easy-align (文本对齐)

> [github](https://github.com/junegunn/vim-easy-align)

- install

  ```
  Plug 'junegunn/vim-easy-align'
  ```

- use

  ```bash
  # 原文本
  abc   |    1901 |2300000
  histort |19012021 |   C001H2
  PersonAction    |2201        |             HHKI!HA
  
  
  # ga|
  abc          | 1901 |2300000
  histort      | 19012021 |   C001H2
  PersonAction | 2201        |             HHKI!HA
  
  
  # ga2|
  abc          | 1901     | 2300000
  histort      | 19012021 | C001H2
  PersonAction | 2201     | HHKI!HA
  ```

  

  ```bash
  # 原文本
  abc,       1901
  histort   ,19012021,     C001H2
  PersonAction  ,    2201                     ,HHKI!HA
  
  
  # ga*,
  abc,          1901
  histort,      19012021, C001H2
  PersonAction, 2201,     HHKI!HA
  
  
  # ga向右的箭头*,
  abc          , 1901
  histort      , 19012021 , C001H2
  PersonAction , 2201     , HHKI!HA
  ```

##### vim-translator (词典)

> [github](https://github.com/voldikss/vim-translator)

- 翻译句子

  ```
  
  ```

##### markdown

> [github](https://github.com/plasticboy/vim-markdown)

##### preview-markdown

> 实时预览
>
> [github](https://github.com/iamcco/markdown-preview.nvim)

- 如果要安装必须执行

  ```
  :call mkdp#util#install()
  ```

- 问题 1

  - 问题描述

    ```
    安装失败
    ```

  - 解决办法

    ```bash
    进入插件 app 目录
    $ ~/.vim/plugged/markdown-preview.nvim/app
    
    执行 install.sh 脚本
    $ ./install.sh
    ```

- 问题 2

  - 描述

    ```
    执行 MarkdownPreview 时报错: 
    E492: Not an editor command: MarkdownPreview
    ```

  - 原因

    ```
    打开的文件不是 .md
    ```

##### nvim-notify (通知栏)

[github](https://github.com/rcarriga/nvim-notify)

##### vim-floaterm (终端模式)

> [github](https://github.com/voldikss/vim-floaterm)

```
:FloatermNew lazygit
```

##### toggleterm.nvim (终端模式)

> [github](https://github.com/akinsho/toggleterm.nvim)
>
> 一个窗口多个终端切换

```
:ToggleTerm size=40 dir=~/Desktop direction=horizontal
:ToggleTerm direction=float


关闭所有
:ToggleTermToggleAll


1<C-\>	第 1 个窗口最大化
2<C-\>	第 2 个窗口最大化
```

##### telescope-media-files.nvim

> [github](https://github.com/nvim-telescope/telescope-media-files.nvim)

```bash
$ pip3 install Pillow
```

#####  yode-nvim (window内的悬浮终端)

> [github](https://github.com/hoschi/yode-nvim)

```
map <Leader>yc      :YodeCreateSeditorFloating<CR>
map <Leader>yr :YodeCreateSeditorReplace<CR>
nmap <Leader>bd :YodeBufferDelete<cr>
imap <Leader>bd <esc>:YodeBufferDelete<cr>
" these commands fall back to overwritten keys when cursor is in split window
map <C-W>r :YodeLayoutShiftWinDown<CR>
map <C-W>R :YodeLayoutShiftWinUp<CR>
map <C-W>J :YodeLayoutShiftWinBottom<CR>
map <C-W>K :YodeLayoutShiftWinTop<CR>
```

##### nvim-window (编号选择 window)

> [gitlab](https://gitlab.com/yorickpeterse/nvim-window)

##### hop.nvim (单词跳转)

> [github](https://github.com/phaazon/hop.nvim#installation)

```
:HopWord：通过突出显示单词来跳。
:HopPattern: 通过匹配一个模式来跳转（如/）。
:HopChar1：键入一个键并跳到文档中该键的任何出现处。
:HopChar2：输入一个二元组（两个键）并跳到文档中该二元组的任何出现处。
:HopLine: 跳转到缓冲区中的任何可见行。
:HopLineStart: 跳转到缓冲区中每一行的任何可见的第一个非空白字符。:q
```

##### rnvimr (ranger)

> [github](https://github.com/kevinhwang91/rnvimr)

- Install Ranger

  ```bash
  $ brew install ranger
  $ aptitude install ranger
  $ dnf install ranger
  ```

- install Ueberzug

  ```bash
  # ArchLinux install all requirements is extremely convenient
  yay -S ranger python-pynvim ueberzug
  
  # pip
  # macOS users please install ranger by `pip3 ranger-fm` instead of `brew install ranger`
  # There're some issues about installation, such as https://github.com/ranger/ranger/issues/1214
  # Please refer to the issues of ranger for more details
  pip3 install ranger-fm pynvim
  
  # ueberzug is not supported in macOS because it depends on X11
      python3 -m pip install ueberzug
  ```

- 查看是否成功

  ```
  :checkhealth
  
  看 Ranger 和 Ueberzug
  ```

##### formatter.nvim(代码格式化)

> [github](https://github.com/mhartington/formatter.nvim)
>
> 不同语言格式化方式参考 https://github.com/sbdchd/neoformat

- json

  ```
  打开 json 文件后输入
  :%!python -m json.tool
  ```

- yaml

  ```bash
  $ pip install pyaml
  
  # 格式化
  python -m pyaml ~/111.yaml
  
  # 格式化并覆盖原来的文件
  python -m pyaml -r ~/111.yaml
  ```

- c

  ```bash
  # 安装 clang 
  $ sudo dnf install clang
  
  
  # 安装 clang-format
  $ dnf search clang-format
  $ dnf install git-clang-format
  
  # 使用
  $ clang-format -version
  
  # 格式化(不修改源文件)
  $ clang-format main.cpp
  
  # 格式化(修改源文件)
  $ clang-format -i main.cpp
  
  # 设置格式化代码的风格
  #  LLVM, GNU, Google, Chromium, Microsoft, Mozilla, WebKit
  $ clang-format -style=google main.cpp
  ```

- sql

  ```
  sql = {
          -- sqlformat
          -- 安装方法:pip3 install --upgrade sqlparse
          function()
            return {
              exe = "sqlformat",
              -- upper|lower
              args = {"-k", "lower", "-i", "lower", "-r", "-"},
              stdin = true
            }
          end
        }
  
  ```



##### vim-startuptime (启动时间)

> [github](https://github.com/dstein64/vim-startuptime)

```
:StartupTime
```

##### nvim-bqf

> [github](https://github.com/kevinhwang91/nvim-bqf)

### lsp

##### mason.nvim (lsp 和 dap 安装管理工具)

> [github](https://github.com/williamboman/mason.nvim)
>
> 安装时 npm 失败因为源速度慢, 设置npm 源
>
> ​	$ npm config set registry https://registry.npm.taobao.org

```bash
# 依赖
$ dnf install unzip gzip curl git wget

```



| 类型 | 语言     | lsp name    | mason 包 (安装时用这个名) |      |
| ---- | -------- | ----------- | ------------------------- | ---- |
| lsp  | lua      | sumneko_lua | lua-language-server       | v    |
| lsp  | python   | pyright     | pyright                   | v    |
| lsp  | go       | gopls       | gopls                     | v    |
| lsp  | json     | jsonls      | json-lsp                  | v    |
| lsp  | c        | clangd      | clangd                    | v    |
| lsp  | xml      | lemminx     | lemminx                   | v    |
| lsp  | yaml     | yaml        | yamlls                    |      |
| lsp  | html     | html        | html-lsp                  |      |
|      | markdown |             |                           |      |

##### mason-lspconfig.nvim

> [github](https://github.com/williamboman/mason-lspconfig.nvim)
>
> https://github.com/williamboman/mason-lspconfig.nvim/blob/main/doc/server-mapping.md

##### nvim-lspconfig

> [github]([GitHub - neovim/nvim-lspconfig: Quickstart configs for Nvim LSP](https://github.com/neovim/nvim-lspconfig))

#####  lsp_signature.nvim (参数提示)

> [github](https://github.com/ray-x/lsp_signature.nvim)

##### lspsaga.nvim (ui 增强)

> [github](https://github.com/glepnir/lspsaga.nvim)

##### c

```
ccls
https://github.com/MaskRay/ccls/wiki/Build
3.3k



clangd (用这个, 背后有大公司)
```

### dap

##### nvim-dap

> [github](https://github.com/mfussenegger/nvim-dap)
>
> [Debug-Adapter-installation](https://github.com/mfussenegger/nvim-dap/wiki/Debug-Adapter-installation)

```
https://github.com/mfussenegger/nvim-dap/wiki/Debug-Adapter-installation
```

##### nvim-dap-ui

> [github](https://github.com/rcarriga/nvim-dap-ui)

##### DAPInstall.nvim

> [github](https://github.com/ravenxrz/DAPInstall.nvim)

##### nvim-dap-python

> [github](https://github.com/mfussenegger/nvim-dap-python)

require

```bash
$ pip install pytest debugpy
```

##### nvim-dap-java

> [github](https://github.com/mfussenegger/nvim-jdtls)
>
> 安装到 `/opt/neovim-dap` 目录下
>
> 每次启动后先执行 `JdtRefreshDebugConfigs`

- 安装 eclipse.jdt.ls 语言服务器

  [github](https://github.com/eclipse/eclipse.jdt.ls)

  [完整配置示例](https://github.com/mfussenegger/nvim-jdtls/wiki/Sample-Configurations)

  ```bash
  $ wget https://download.eclipse.org/jdtls/snapshots/jdt-language-server-1.9.0-202202210521.tar.gz
  $ gzip -d  jdt-language-server-1.8.0-202201261434.tar.gz 
  $ tar xvf jdt-language-server-1.8.0-202201261434.tar
  ```
  
- 安装 java-debug

  ```bash
  $ git clone https://github.com/microsoft/java-debug.git
  $ cd java-debug
  $ ./mvnw clean install
  ```

- 安装 vscode-java-test

  [github](https://github.com/microsoft/vscode-java-test)

  ```bash
  $ git clone https://github.com/microsoft/vscode-java-test.git
  $ cd vscode-java-test
  $ npm install
  $ npm run build-plugin
  ```

### cpm

##### nvim-cmp (自动补全)

> [github](https://github.com/hrsh7th/nvim-cmp)

### telescope

> [github](https://github.com/nvim-telescope/telescope.nvim)

```

```

##### telescope-frecency.nvim (搜索结果排序优化)

> [github](https://github.com/nvim-telescope/telescope-frecency.nvim)

### 未使用

##### scrollbar.nvim (滚动条)

> [github](https://github.com/Xuyuanp/scrollbar.nvim)

##### coq

> [github](https://github.com/ms-jpq/coq_nvim)

##### [git]([github](https://github.com/tpope/vim-fugitive))

##### DAPInstall

> [github](https://github.com/Pocco81/DAPInstall.nvim)
>
> 不好用

##### nvim-autopairs

> [github](https://github.com/windwp/nvim-autopairs)
>
> 符号配对 []{}()''""

##### vim-startify (启动画面)

> [github](https://github.com/mhinz/vim-startify)

##### dashboard-nvim

[开始画面顶部图片](https://github.com/glepnir/dashboard-nvim/wiki/Ascii-Header-Text)

#####  neoformat (代码格式化)

> [github](https://github.com/sbdchd/neoformat)

```
:Neoformat! python
:Neoformat! python yapf
```

##### asyncrun.vim (执行系统 shell)

> [github](https://github.com/skywind3000/asyncrun.vim)

##### winshift.nvim (移动窗口)

> [github](https://github.com/sindrets/winshift.nvim)
>
> 不好用

##### nvim-lspconfig (核心)

> [github](https://github.com/neovim/nvim-lspconfig)
>
> 被 mason 代替

##### nvim-lsp-installer (lsp 安装工具) 

> [github](https://github.com/williamboman/nvim-lsp-installer)
>
> [github](https://github.com/williamboman/nvim-lsp-installer#available-lsps)
>
> [语言对应的语言服务器](https://github.com/williamboman/nvim-lsp-installer#available-lsps)
>
> 被 mason 代替

命令 

```
:LspInstallInfo
:LspUninstallAll	卸载所有语言服务器
:LspInstallLog		在新选项卡窗口中打开日志文件
:LspPrintInstalled	打印所有已安装的语言服务器
:LspInstall pyright				python
:LspInstall jdtls				java
:LspInstall jsonls				json
:LspInstall yamlls				yaml
:LspInstall lemminx				xml
:LspUninstall jdtls
:LspInfo
```



# python

##### import 管理

>  [github](https://github.com/PyCQA/isort)
>
> https://blog.csdn.net/u010751000/article/details/119013304

- 安装

  ```bash
  $ pip install isort
  # 支持 requirements
  $ pip install isort[requirements_deprecated_finder]
  # 支持 requirements 和 pipfile
  $ pip install isort[requirements_deprecated_finder,pipfile_deprecated_finder]
  ```

- 使用

  ```bash
  # 多个文件
  $ isort a.py b.py
  
  # 文件夹
  $ isort .
  
  # 智能平衡格式
  $ isort a.py -e
  
  # 查看不同, 不执行
  $ isort a.py --diff
  
  # 如果上面无法执行, 使用下面的命令
  $ python -m isort code_test.py --diff
  
  # 忽略某行
  import module  # isort:skip
  或
  from xyz import (abc,  # isort:skip
                   yo,
                   hey)                
  ```

# 快捷键

##### 命令

```
:messages								neovim 命令行显示的消息
:lua print(vim.fn.stdpath('cache'))		neovim 日志目录
```

##### 分屏幕

```
$ vim -On file1 file2 file3		垂直分
$ vim -on file1 file2 file3 	水平

C+w s			上下分割当前打开的文件
:sp filename	上下分割, 并打开一个新的文件
C+w v			左右分割当前打开的文件
:vsp filename	左右分割，并打开一个新的文件

C+w L
C+w H
C+w K
C+w J

C+W =			让所有的屏都有一样的高度
C+W +			增加高度
C+W -			减少高度
C+w w			把光标移到下一个的屏中

C+w c			关闭
C+w q			如果只剩最后 1 个则退出 Vim
```

##### 移动光标

```
0				移动至行首
^				跳至行首的第一个字符
$				跳至行尾
#				开始向文件头的方向搜索光标所在位置的单词的下一个出现位置
*				开始向文件尾的方向搜索光标所在位置的单词的下一个出现位置
R				开始替换
C + b			上一页
C + f			下一页
C - u 			上翻半页
C - d 			下翻半页

yX  			给出一个移动命令 X （如 h、j、H、L 等），复制适当数量的字符、单词或者从光标开始到一定数量的行
yy 或 Y 			复制当前整行
.   			重复最后一个命令

:n  			下一个文件，编辑多个指定文件时，该命令加载下一个文件。
:e 				file  加载新文件来替代当前文件
:r 				file  将新文件的内容插入到光标所在位置的下一行
:w file  		将当期打开的缓存区保存为file。如果是追加到已存在的文件中，则使用 ：w >> file 命令
:r! command  	执行 command 命令，并将命令的输出插入到光标所在位置的下一行

fa				下一个a出现的位置
Fa				上一个a出现的位置
;				重复一次f F 命令

5gg		
5G
gd 				跳至当前光标所在的变量的声明处	
ctrl + o 		回调到上次的位置

/hello			向下搜索
?hello			向上搜索
```

##### 替换命令

```
from和to都可以是任何字符串, 其中from还可以是正则表达式
:[range]s/from/to/[flags]
把from指定的字符串替换成to指定的字符串，from可以是正则表达式。


1. 替换当前行中的内容
:s/from/to/     ：  将当前行中的第一个from，替换成to。如果当前行含有多个 from，则只会替换其中的第一个。
:s/from/to/g    ：  将当前行中的所有from都替换成to。
:s/from/to/gc   ：  将当前行中的所有from都替换成to，但是每一次替换之前都会询问请求用户确认此操作。


2.  替换某一行的内容：
:.s/from/to/g   ：  在当前行进行替换操作。
:33s/from/to/g  ：  在第33行进行替换操作。
:$s/from/to/g   ：  在最后一行进行替换操作。

3.  替换某些行的内容
:10,20s/from/to/g   ：  对第10行到第20行的内容进行替换。
:1,$s/from/to/g     ：  对第一行到最后一行的内容进行替换（即全部文本）。
:1,.s/from/to/g     ：  对第一行到当前行的内容进行替换。
:.,$s/from/to/g     ：  对当前行到最后一行的内容进行替换。
:'a,'bs/from/to/g   ：  对标记a和b之间的行（含a和b所在的行）进行替换。 其中a和b是之前用m命令所做的标记。

4.  替换所有行的内容
:%s/from/to/g   ：  对所有行的内容进行替换。

5.2 [range]
不写range   ：  默认为光标所在的行。
.           ：  光标所在的行。
1           ：  第一行。
$           ：  最后一行。
33          ：  第33行。
'a          ：  标记a所在的行（之前要使用ma做过标记）。
.+1         ：  当前光标所在行的下面一行。
$-1         ：  倒数第二行。（这里说明我们可以对某一行加减某个数值来取得相对的行）。
22,33       ：  第22～33行。
1,$         ：  第1行 到 最后一行。
1,.         ：  第1行 到 当前行。
.,$         ：  当前行 到 最后一行。
'a,'b       ：  标记a所在的行 到标记b所在的行。

%           ：  所有行（与 1,$ 等价）。

?chapter?   ：  从当前位置向上搜索，找到的第一个chapter所在的行。（ 其中chapter可以是任何字符串或者正则表达式。
/chapter/   ：  从当前位置向下搜索，找到的第一个chapter所在的行。（ 其中chapter可以是任何字符串或者正则表达式。

注意，上面的所有用于range的表示方法都可以通过 +、- 操作来设置相对偏移量。

5.3 [flags]
无      ：  只对指定范围内的第一个匹配项进行替换。
g       ：  对指定范围内的所有匹配项进行替换。
c       ：  在替换前请求用户确认。
e       ：  忽略执行过程中的错误。

注意：上面的所有flags都可以组合起来使用，比如 gc 表示对指定范围内的
所有匹配项进行替换，并且在每一次替换之前都会请用户确认。
```

| Command 命令 | Normal  常规模式 | Visual 可视化模式 | Operator Pending 运算符模式 | Insert Only 插入模式 | Command Line 命令行模式 |
| ------------ | ---------------- | ----------------- | --------------------------- | -------------------- | ----------------------- |
| `:map`       | y                | y                 | y                           |                      |                         |
| `:nmap`      | y                |                   |                             |                      |                         |
| `:vmap`      |                  | y                 |                             |                      |                         |
| `:omap`      |                  |                   | y                           |                      |                         |
| `:map!`      |                  |                   |                             | y                    | y                       |
| `:imap`      |                  |                   |                             | y                    |                         |
| `:cmap`      |                  |                   |                             |                      | y                       |

##### 键表

```
<k0> - <k9> 小键盘 0 到 9 *keypad-0* *keypad-9* 
<S-...> Shift＋键 *shift* *<S-* 
<C-...> Control＋键 *control* *ctrl* *<C-* 
<M-...> Alt＋键 或 meta＋键 *meta* *alt* *<M-* <A-...> 同 <m-...> *<A-* <t_xx> termcap 里的 "xx" 入口键<Esc><D> CommandAlt 可以是 <M-key>或<A-key>
```

##### 特殊参数

```
<buffer> <silent> <special> <script> <expr> <unique> 
```

##### buffer

```
打开nvim a.py b.py
:ls, :buffers       列出所有缓冲区
:bn[ext]            下一个缓冲区
:bp[revious]        上一个缓冲区
:b {number, expression}     跳转到指定缓冲区
:sb 3               分屏并打开编号为3的Buffer
:vertical sb 3      同上，垂直分屏
:vertical rightbelow sfind file.txt
:bd
:bd! 不保存退出
:bd3
:e /path/to/file 也可以打开文件到当前 buffer 中
:new 和 
:vnew
:badd {filename} 添加到缓冲区，光标保持在当前缓冲
```

##### 终端模式

```
打开
:terminal
:term
:te
:te bash
:te zsh:terminal {cmd}                当前窗口创建缓冲区

:split | terminal {cmd}      横向分割创建窗口
:vsplit | terminal {cmd}     纵向分割创建窗口
:tabedit | terminal {cmd}        新标签页创建窗口# 纵向分屏
:vs term
://$SHELL# 横向分屏
:split term://$SHELL# 新标签打开
:tabe term://$SHELL命令行中执行插入（i）或者附加（a）操作就可以进入命令行的交互模式。


退出终端模式
<c-\><c-n>C-w


# 纵向分屏
:vs term://$SHELL

# 横向分屏
:split term://$SHELL

# 新标签打开
:tabe term://$SHELL

```

##### 查看命令行历史

```
普通模式下:
    q/ 查看使用/输入的搜索历史
    q? 查看使用？输入的搜索历史
    q: 查看命令行历史
```

