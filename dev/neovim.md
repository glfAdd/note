# mac & linux

##### 安装

```
brew install neovim
brew install python3
pip3 install neovim --upgrade
```

##### 配置文件

```
~/.config/nvim/init.vim

配置教程
https://www.jianshu.com/p/c382222e5151
https://www.cnblogs.com/cjy15639731813/p/5886158.html
```

##### 插件管理器

```
https://github.com/junegunn/vim-plug

安装
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
    
    
call plug#begin('~/.vim/plugged')
Plug 'junegunn/vim-easy-align'
call plug#end()    

:PlugInstall			安装配置好的插件
:PlugUpdate				更新已安装的插件
:PlugClean				清理插件
:PlugUpgrade			升级自身
:PlugStatus
```

##### shell补全

```
https://github.com/Shougo/neocomplete.vim

```

##### 美化

```
https://github.com/vim-airline/vim-airline


字体
https://github.com/powerline/fonts
# clone
git clone https://github.com/powerline/fonts.git --depth=1
# install
cd fonts
./install.sh
# clean-up a bit
cd ..
rm -rf fonts
./uninstall.sh
```

###### 自动补全

```
https://github.com/davidhalter/jedi-vim
pip install jedi
```

##### 文件管理

```
https://github.com/scrooloose/nerdtree
```

##### 语法检测

```
https://github.com/w0rp/ale

```

##### git插件

```
https://github.com/airblade/vim-gitgutter
```

##### 括号自动补全

```
https://github.com/jiangmiao/auto-pairs
```

##### 配置文件

```
""===============基本设置================= 
syntax on    						"开启语法高亮"
set nocompatible 				"去掉vi的一致性"
set number							"显示行号
set showtabline=1 			"隐藏顶部标签栏"
set nowrap    					"设置不折行"
set tabstop=4    				"设置table长度"
set shiftwidth=4        "同上"
set showmatch    				"显示匹配的括号"
set scrolloff=5        	"距离顶部和底部5行"
set laststatus=2    		"命令行为两行"
set mouse=a        			"启用鼠标"
set hlsearch        		"高亮搜索项"
set noexpandtab        	"不允许扩展table"
set cursorline        	"突出显示当前行"
set cursorcolumn        "突出显示当前列"
set encoding=utf-8
set t_Co=256
set background=dark
let mapleader=','

call plug#begin('~/.vim/plugged')
Plug 'scrooloose/nerdtree'
Plug 'davidhalter/jedi-vim'
Plug 'w0rp/ale'
Plug 'vim-airline/vim-airline'
Plug 'Shougo/neocomplete.vim'
Plug 'airblade/vim-gitgutter'
Plug 'jiangmiao/auto-pairs'
call plug#end()

""===============airline=================
" 使用powerline打过补丁的字体
"let g:airline_powerline_fonts = 1
let g:airline_theme='dark_minimal'
" 开启tabline
let g:airline#extensions#tabline#enabled = 1
" 显示buffer编号
let g:airline#extensions#tabline#buffer_nr_show = 1
" tabline中当前buffer两端的分隔字符
let g:airline#extensions#tabline#left_sep = ' '
" tabline中未激活buffer两端的分隔字符
let g:airline#extensions#tabline#left_alt_sep = '|'
" 关于buffer使用：
"     :ls 查看buffer
"     :bn (buffer next)
"     :bp (buffer previous)
"     :b <num> 打开编号为num的buffer
" color scheme
map <F2> :bp<CR>
map <F3> :bn<CR>

""===============nerdtree=================
"开启和关闭树"
map <Leader>w :NERDTreeToggl<CR>
let NERDTreeChDirMode=1
"显示书签"
let NERDTreeShowBookmarks=1
"设置忽略文件类型"
let NERDTreeIgnore=['\~$', '\.pyc$', '\.swp$']
"窗口大小"
let NERDTreeWinSize=25
```

