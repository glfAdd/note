##### 快捷键

```
0		移动至行首
^		跳至行首的第一个字符
$		跳至行尾
R		开始替换
C + b		上一页
C + f		下一页
C - u 		上翻半页
C - d 		下翻半页

yX  	给出一个移动命令 X （如 h、j、H、L 等），复制适当数量的字符、单词或者从光标开始到一定数量的行
yy 或 Y 复制当前整行
.   	重复最后一个命令

:n  下一个文件，编辑多个指定文件时，该命令加载下一个文件。
:e file  加载新文件来替代当前文件
:r file  将新文件的内容插入到光标所在位置的下一行
:q  退出并放弃更改
:w file  将当期打开的缓存区保存为file。如果是追加到已存在的文件中，则使用 ：w >> file 命令
:wq  保存当前文件的内容并退出。等效于 x! 和 ZZ
:r! command  执行 command 命令，并将命令的输出插入到光标所在位置的下一行

fa		下一个a出现的位置
Fa		上一个a出现的位置
;		重复一次f F 命令

5gg		
5G
gd 		跳至当前光标所在的变量的声明处		

#　		开始向文件头的方向搜索光标所在位置的单词的下一个出现位置
*　		开始向文件尾的方向搜索光标所在位置的单词的下一个出现位置

/hello		向下搜索
?hello		向上搜索

^ 跳至行首的第一个字符
$ 跳至行尾

VIM 函数跳转函数快捷键 gd
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

##### 配置文件

```
~/.vimrc
```

##### 插件管理器

```
https://github.com/junegunn/vim-plug

安装
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

##### Vundle 插件管理器

```
https://github.com/VundleVim/Vundle.vim

git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
:PluginList       - lists configured plugins
:PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
:PluginSearch foo - searches for foo; append `!` to refresh local cache
:PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
```

##### Vundle 插件管理器

##### 配置文件

```
"去掉vi的一致性"
set nocompatible
set number
" 隐藏滚动条"
set guioptions-=r
set guioptions-=L
set guioptions-=b
"隐藏顶部标签栏"
set showtabline=1
syntax on    "开启语法高亮"
let g:solarized_termcolors=256    "solarized主题设置在终端下的设置"
set nowrap    "设置不折行"
set fileformat=unix    "设置以unix的格式保存文件"
set cindent        "设置C样式的缩进格式"
set tabstop=4    "设置table长度"
set shiftwidth=4        "同上"
set showmatch    "显示匹配的括号"
set scrolloff=5        "距离顶部和底部5行"
set laststatus=2    "命令行为两行"
set fenc=utf-8      "文件编码"
set backspace=2
set mouse=a        "启用鼠标"
set selection=exclusive
set selectmode=mouse,key
set matchtime=5
set ignorecase        "忽略大小写"
set incsearch
set hlsearch        "高亮搜索项"
set noexpandtab        "不允许扩展table"
set whichwrap+=,h,l
set autoread
"set cursorline        "突出显示当前行"
"set cursorcolumn        "突出显示当前列"
"set splitbelow
"set splitright
set tw=160
"set encoding=utf-8
let mapleader=','


call Plug#begin('~/.vim/Plugged')
Plug 'VundleVim/Vundle.vim'
Plug 'scrooloose/nerdtree'
"Plug 'Valloric/YouCompleteMe'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
"Plug 'jiangmiao/auto-pairs'               "括号补全"
Plug 'scrooloose/nerdcommenter'           "注释"
Plug 'Yggdroot/indentLine'                "缩进对齐标注"
Plug 'hhatto/autopep8'
Plug 'ctrlpvim/ctrlp.vim'                 "搜索文件"
Plug 'mileszs/ack.vim'                    "在项目里全局搜索某个单词"
Plug 'majutsushi/tagbar'                  "跳转函数 map"
Plug 'tmhedberg/SimpylFold'               "自定义标注"
Plug 'w0rp/ale'                           "语法检测"
Plug 'skywind3000/asyncrun.vim'           "编译"
Plug 'bronson/vim-trailing-whitespace'    "表出末尾空格 可以删除"
Plug 'tell-k/vim-autopep8'
call Plug#end()


" YouCompleteMe settings
let g:ycm_collect_identifiers_from_comments_and_strings = 0
" 输入第0个字符开始补全
let g:ycm_min_num_of_chars_for_completion=0
" 禁止缓存匹配项,每次都重新生成匹配项
let g:ycm_cache_omnifunc=0
" 开启语义补全
let g:ycm_seed_identifiers_with_syntax=1
" 在注释输入中也能补全
let g:ycm_complete_in_comments = 1
" 在字符串输入中也能补全
let g:ycm_complete_in_strings = 1
let g:ycm_autoclose_preview_window_after_completion = 1
let g:ycm_autoclose_preview_window_after_insertion = 1
"python解释器路径"
let g:ycm_path_to_python_interpreter='/usr/local/bin/python'
map <C-G>  :YcmCompleter GoToDefinitionElseDeclaration<CR>
"let g:ycm_global_ycm_extra_conf = '~/.vim/Plugged/YouCompleteMe/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py'
set complete-=i


"开启和关闭树"
map <Leader>w :NERDTreeToggl<CR>
let NERDTreeChDirMode=1
"显示书签"
let NERDTreeShowBookmarks=1
"设置忽略文件类型"
let NERDTreeIgnore=['\~$', '\.pyc$', '\.swp$']
"窗口大小"
let NERDTreeWinSize=25


" airline
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
set background=dark        " Assume a dark background
set t_Co=256
map <F2> :bp<CR>
map <F3> :bn<CR>


" 窗口调整
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>
nnoremap ˙ <C-W><
nnoremap ¬ <C-W>>
nnoremap ∆ <C-W>+
nnoremap ˚ <C-W>-


au BufNewFile,BufRead *
\ set tabstop=4 |
\ set softtabstop=4 |
\ set shiftwidth=4 |
\ set expandtab |
\ set autoindent |
\ set fileformat=unix |
\ set list listchars=tab:>-


" 自定义代码折叠，折叠（和取消折叠）
"set foldmethod=syntax
set nofoldenable " default unfolded when open file
nnoremap <space> za
map <F4> :call ToggleFold()<CR>
function! ToggleFold()
  if(&foldlevel == '0')
      exec "normal! zR"
  else
      exec "normal! zM"
  endif
  echo "foldlevel:" &foldlevel
endfunction


" 运行pyton
"nnoremap <F5> :call CompileRunGcc()<cr>
"func! CompileRunGcc()
          "exec "w"
          "if &filetype == 'python'
                  "if search("@profile")
                          "exec "AsyncRun kernprof -l -v %"
                          "exec "copen"
                          "exec "wincmd p"
                  "elseif search("set_trace()")
                          "exec "!python2 %"
                  "else
                          "exec "AsyncRun -raw python2 %"
                          "exec "copen"
                          "exec "wincmd p"
                  "endif

"endfunc



" tagbar跳转
"nmap <F3> :TagbarToggle<CR>
map <Leader>e :TagbarToggle<CR>


" ack
" i 忽略大小写
"nnoremap <Leader>a :Ack!<Space>
"ack
"<Leader>c进行搜索，同时不自动打开第一个匹配的文件"
map <Leader>c :Ack!<Space>
"调用ag进行搜索
if executable('ag')
  let g:ackprg = 'ag --vimgrep'
endif
"高亮搜索关键词
let g:ackhighlight = 1
"修改快速预览窗口高度为15
let g:ack_qhandler = "botright copen 15"
"在QuickFix窗口使用快捷键以后，自动关闭QuickFix窗口
let g:ack_autoclose = 1
"使用ack的空白搜索，即不添加任何参数时对光标下的单词进行搜索，默认值为1，表示开启，置0以后使用空白搜索将返回错误信息
let g:ack_use_cword_for_empty_search = 1
"部分功能受限，但对于大项目搜索速度较慢时可以尝试开启
"let g:ack_use_dispatch = 1


"autopep8设置"
let g:autopep8_disable_show_diff=1
" 自动代码格式化
map <leader>a :Autopep8<cr>


" 删除末尾空格
map <leader>q :FixWhitespace<cr>


map <Leader>o :CtrlP<CR>
```

