##### 编译安装

| 配置选项                                            | 解释                                               |
| --------------------------------------------------- | -------------------------------------------------- |
| –with-features=huge                                 | 支持最大特性                                       |
| –enable-pythoninterp                                | 打开对python编写的插件的支持                       |
| –enable-python3interp                               | 打开对python3编写的插件的支持                      |
| –enable-rubyinterp                                  | 打开对ruby编写的插件的支持                         |
| –enable-luainterp                                   | 打开对lua编写的插件的支持                          |
| –enable-perlinterp                                  | 打开对perl编写的插件的支持                         |
| –enable-multibyte                                   | 打开多字节支持，可以在Vim中输入中文                |
| –enable-cscope                                      | 打开对cscope的支持，cscope是一款优秀的代码浏览工具 |
| –with-python-config-dir=/usr/lib/python2./config*/  | 指定python 路径                                    |
| –with-python3-config-dir=/usr/lib/python3./config*/ | 指定python3路径                                    |
| –prefix=/usr/local/vim                              | 指定将要安装到的路径(默认 /usr/local/bin/vim)      |
| –enable-fontset                                     | 支持字体设置                                       |
| –enable-gui=gtk2                                    | gtk2支持,也可以使用gnome，表示生成gvim             |
| –with-compiledby                                    | 编译者                                             |

```sh
$ dnf install libevent-devel python-gevent python-devel python3-devel
$ wget https://github.com/vim/vim/archive/refs/tags/v9.0.0954.tar.gz
$ ./configure --with-features=huge \
                --enable-pythoninterp=yes \
                --with-python-config-dir=/usr/lib64/python2.7/config \
                --enable-cscope \
                --enable-fontset \
                --enable-python3interp=yes \
                --with-python3-config-dir=/usr/lib64/python3.6/config-3.6m-x86_64-linux-gnu \
                --with-python3-command=/usr/bin/python3 \
                --enable-multibyte\
                --prefix=/opt/vim9
$ make 
$ make install
$ ln -s /opt/vim9/bin/vim /usr/bin/vim
```

##### 命令

```bash
$ vim --version



:set filetype			查看编码
:h key-notation			查看键盘映射
```

##### 配置

文件路径 ~/.vimrc





# 快捷键

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
```



##### 查看命令行历史

```
普通模式下:
    q/ 查看使用/输入的搜索历史
    q? 查看使用？输入的搜索历史
    q: 查看命令行历史
```

##### powerline fonts

> [github](https://github.com/powerline/fonts)

```bash
$ apt-get install fonts-powerline
$ dnf install powerline-fonts


# source
$ git clone https://github.com/powerline/fonts.git --depth=1
$ cd fonts
$ ./install.sh
```

# 插件

##### vim-plug 包管理

[github](https://github.com/junegunn/vim-plug)

- install - linux

```
curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

- 命令

| Command                             | Description                                                  |
| ----------------------------------- | ------------------------------------------------------------ |
| `PlugInstall [name ...] [#threads]` | Install plugins                                              |
| `PlugUpdate [name ...] [#threads]`  | Install or update plugins                                    |
| `PlugClean[!]`                      | Remove unlisted plugins (bang version will clean without prompt) |
| `PlugUpgrade`                       | Upgrade vim-plug itself                                      |
| `PlugStatus`                        | Check the status of plugins                                  |
| `PlugDiff`                          | Examine changes from the previous update and the pending changes |
| `PlugSnapshot[!] [output path]`     | Generate script for restoring the current snapshot of the plugins |

- 选项

| Option                  | Description                                      |
| ----------------------- | ------------------------------------------------ |
| `branch`/`tag`/`commit` | Branch/tag/commit of the repository to use       |
| `rtp`                   | Subdirectory that contains Vim plugin            |
| `dir`                   | Custom directory for the plugin                  |
| `as`                    | Use different name for the plugin                |
| `do`                    | Post-update hook (string or funcref)             |
| `on`                    | On-demand loading: Commands or `<Plug>`-mappings |
| `for`                   | On-demand loading: File types                    |
| `frozen`                | Do not update unless explicitly specified        |

- 全局选项

| Flag                | Default                           | Description                                                  |
| ------------------- | --------------------------------- | ------------------------------------------------------------ |
| `g:plug_threads`    | 16                                | Default number of threads to use                             |
| `g:plug_timeout`    | 60                                | Time limit of each task in seconds (*Ruby & Python*)         |
| `g:plug_retries`    | 2                                 | Number of retries in case of timeout (*Ruby & Python*)       |
| `g:plug_shallow`    | 1                                 | Use shallow clone                                            |
| `g:plug_window`     | `vertical topleft new`            | Command to open plug window                                  |
| `g:plug_pwindow`    | `above 12new`                     | Command to open preview window in `PlugDiff`                 |
| `g:plug_url_format` | `https://git::@github.com/%s.git` | `printf` format to build repo URL (Only applies to the subsequent `Plug` commands) |



##### vim-startify 启动画面

> [github](https://github.com/mhinz/vim-startify)
>
> [开始画面顶部图片](https://github.com/glepnir/dashboard-nvim/wiki/Ascii-Header-Text)

##### nerdtree

[github](https://github.com/preservim/nerdtree)

```
:NERDTree

使用
https://blog.huati365.com/dcfb9b6d48bac807

coc-explorer
```



# 依赖

##### python 环境

```bash
$ pyenv virtualenv 3.9.2 p-3.9.2-neovim
$ pyenv activate p-3.9.2-neovim
$ pip install --upgrade pip
$ pip install neovim pynvim pytest debugpy isort ueberzug ranger-fm
```

##### pip3(非必备)

```
aptitude install python3-pip
```

##### java

> lsp 需要

##### node

> lsp 需要

```bash
$ brew install node

$ aptitude install nodejs npm
```

##### lazygit

> git 工具
>
> [github](https://github.com/jesseduffield/lazygit)

```
$ sudo dnf copr enable atim/lazygit
$ sudo dnf install lazygit 
```

##### devicons 字体

> [homepage](https://www.nerdfonts.com/)
>
> [devicons](https://github.com/vorillaz/devicons)

- mac

  ```bash
  $ brew tap homebrew/cask-fonts
  $ brew install --cask font-hack-nerd-font
  
  
  在终端中选择安装的字体, 字体的名字包含 "Nerd"
  ```

- ubuntu

  ```
  $ npm install devicons
  ```

- Centos / fedora

  ```
  $ npm install devicons
  ```

##### clipboard 支持

Vim 与系统共用剪切板

查看帮助信息

```
:help clipboard
```

安装

```bash
$ aptiotude install xsel
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

##### tmux

```bash
$ aptitude install tmux
```



# package

#####  gruvbox.nvim

> 主题配色
>
> [github](https://giters.com/ellisonleao/gruvbox.nvim)



#####  lualine.nvim

> 状态栏
>
> [github](https://github.com/nvim-lualine/lualine.nvim)

##### trouble.nvim

> 语法错误列表
>
> [github](https://github.com/folke/trouble.nvim)

##### lazygit

> [github](https://github.com/kdheepak/lazygit.nvim)

##### gitsigns.nvim

> [github](https://github.com/lewis6991/gitsigns.nvim)

##### nvim-tree.lua

> 文件管理
>
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

##### bufferline

> [github](https://github.com/akinsho/bufferline.nvim)

##### which-key.nvim

> [github](https://github.com/folke/which-key.nvim)

##### nvim-treesitter

> 语法高亮
>
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

##### Comment.nvim

> 注释
>
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

##### nvim-autopairs(x)

> 符号配对 []{}()''""
>
> [github](https://github.com/windwp/nvim-autopairs)

##### symbols-outline.nvim

> 边栏显示函数对象
>
> [github](https://github.com/simrat39/symbols-outline.nvim)

##### formatter.nvim(未使用)

> 代码格式化
>
> [github](https://github.com/mhartington/formatter.nvim)
>
> [config](https://github.com/mhartington/formatter.nvim/blob/master/CONFIG.md)

#####  neoformat

> [github](https://github.com/sbdchd/neoformat)

```
:Neoformat! python
:Neoformat! python yapf
```



```
https://github.com/vim-autoformat/vim-autoformat 2k


```



##### vim-easy-align

> 文本对齐
>
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

##### vim-translator

> 词典(功能不全)
>
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

##### vim-floaterm

> 终端模式
>
> [github](https://github.com/voldikss/vim-floaterm)

use

```
:FloatermNew lazygit
```

##### toggleterm.nvim

> 终端模式
>
> [github](https://github.com/akinsho/toggleterm.nvim)

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
$ pip3 install ueberzug


$ pip3 install Pillow
```



##### winshift.nvim

> 移动窗口
>
> [github](https://github.com/sindrets/winshift.nvim)

#####  yode-nvim

> window内的悬浮终端
>
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

##### nvim-window

> 编号选择 window
>
> [github](https://gitlab.com/yorickpeterse/nvim-window)

##### hop.nvim

> 单词跳转
>
> [github](https://github.com/phaazon/hop.nvim#installation)

```
:HopWord：通过突出显示单词来跳。
:HopPattern: 通过匹配一个模式来跳转（如/）。
:HopChar1：键入一个键并跳到文档中该键的任何出现处。
:HopChar2：输入一个二元组（两个键）并跳到文档中该二元组的任何出现处。
:HopLine: 跳转到缓冲区中的任何可见行。
:HopLineStart: 跳转到缓冲区中每一行的任何可见的第一个非空白字符。:q
```

##### rnvimr

> neovim ranger
>
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

  

```
打开文件后设置窗口尺寸
tnoremap <silent> <M-i> <C-\><C-n>:RnvimrResize<CR>


nnoremap <silent> <M-o> :RnvimrToggle<CR>
tnoremap <silent> <M-o> <C-\><C-n>:RnvimrToggle<CR>

```

- 问题 1:

  - 描述

    ```
    pip3 install ueberzug 安装失败
    ```

  - 解决办法

    ```
    安装依赖
    
    ubuntu
    $ sudo aptitude install libx11-dev libxext-dev python-dev python3-dev
    ```

# lsp

##### lsp

> [github](https://github.com/williamboman/nvim-lsp-installer#available-lsps)
>
> 参考 https://zhuanlan.zhihu.com/p/444836713?utm_source=wechat_session&utm_medium=social&utm_oi=1269928803658530816
>
> [语言对应的语言服务器](https://github.com/williamboman/nvim-lsp-installer#available-lsps)

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

#####  lsp_signature.nvim

> [github](https://github.com/ray-x/lsp_signature.nvim)

# dap

##### nvim-dap

> [github](https://github.com/mfussenegger/nvim-dap)
>
> [Debug-Adapter-installation](https://github.com/mfussenegger/nvim-dap/wiki/Debug-Adapter-installation)

help

```
:help dap.txt
:help dap-adapter
:help dap-configuration
:help dap-api
```

##### nvim-dap-ui

> [github](https://github.com/rcarriga/nvim-dap-ui)

```


















```

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

# cpm

##### nvim-cmp

> [github](https://github.com/hrsh7th/nvim-cmp)

```
:COQdeps
:COQnow
```

# telescope

> [github](https://github.com/nvim-telescope/telescope.nvim)

```

```

##### telescope-frecency.nvim

> 搜索结果排序优化
>
> [github](https://github.com/nvim-telescope/telescope-frecency.nvim)

# 未使用

##### [代码运行](https://github.com/skywind3000/asyncrun.vim)

##### [滚动条](https://github.com/Xuyuanp/scrollbar.nvim)

##### [coq](https://github.com/ms-jpq/coq_nvim)

##### [git]([github](https://github.com/tpope/vim-fugitive))

##### [DAPInstall(python 支持, java 不支持, 暂时不用)](https://github.com/Pocco81/DAPInstall.nvim)




# python

##### import 管理

```
https://github.com/PyCQA/isort


```



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

