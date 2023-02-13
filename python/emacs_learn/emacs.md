##### 参考

```
Emacs高手修炼手册: 
https://www.jianshu.com/p/42ef1b18d959

插件整理
https://zhuanlan.zhihu.com/p/441612281

推荐1
https://huadeyu.tech/tools/emacs-setup-notes.html#orga1adbf9

新配置 
https://huadeyu.tech/tools/emacs-setup-notes.html
https://phenix3443.github.io/notebook/emacs/modes/lsp-mode.html



基础设置   
https://blog.csdn.net/neo_liukun/article/details/115189475?spm=1035.2023.3001.6557&utm_medium=distribute.pc_relevant_bbs_down.none-task-blog-2~default~OPENSEARCH~Rate-5.nonecase&depth_1-utm_source=distribute.pc_relevant_bbs_down.none-task-blog-2~default~OPENSEARCH~Rate-5.nonecase
```

[emacs wiki](https://www.emacswiki.org)

[中文论坛](https://emacs-china.org/)

[插件作者 abo-abo ](https://github.com/abo-abo)

# 安装

### linux

> [官网](http://www.gnu.org/software/emacs/emacs.html)
>
> version 27.2
>
> [下载地址](http://ftp.gnu.org/gnu/emacs/)

##### install - centos

```bash
$ dnf install emacs
$ dnf remove emacs

安装编译的依赖
$ dnf install gnutls-devel make gcc clang ncurses-devel 
$ wget https://mirrors.nju.edu.cn/gnu/emacs/emacs-27.2.tar.xz
$ xz -d emacs-27.2.tar.xz
$ tar xvf emacs-27.2.tar

$ ./configure --prefix=/opt/emacs (不用这个)
$ ./configure --prefix=/opt/emacs --without-x (用这个)

$ make
$ make install
$ ln -s /opt/emacs/bin/emacs /usr/bin/emacs
```

##### install - ubuntu

```bash
$ apt-get install emacs
$ apt-get remove emacs

安装编译的依赖
$ apt-get install libgtk2.0-dev libxpm-dev libjpeg-dev libgif-dev libtiff-dev libgnutls28-dev libncurses-dev
$ ./configure --prefix=/opt/emacs
$ make
$ make install
$ ln -s /opt/emacs/bin/emacs /usr/bin/emacs
```

##### 运行

```bash
$ emacs -nw
$ emacs
```

### windows

```
1. 安装完成后运行 C:\Program Files\Emacs\emacs-28.1\bin\addpm.exe 在开始菜单添加快捷方式

2. 配置文件路径 %AppData% 下 创建 .emacs 文件
```

### 字体

```
https://github.com/lxbrtsch/Menlo-for-Powerline
```

# 按键

> https://www.cnblogs.com/eat-and-die/p/10309681.html !!!!!!!

| M-x                            |                      |
| ------------------------------ | -------------------- |
| emacs-version                  | 查看版本             |
| package-list-packages          | 列出仓库中的所有插件 |
| package-install <RET> <插件名> | 安装插件             |
| package-delete <RET> <插件名>  | 删除插件             |

##### 按键说明

| Emacs 功能键 | 缩写 | 对应键盘按键(PC/Mac) |
| ------------ | ---- | -------------------- |
| Control      | C    | Ctrl / Control       |
| Meta         | M    | Alt / Option         |
| Shift        | S    | Shift / Shift        |
| Super        | s    | Win / Command        |
| Hyper        | H    | 无                   |
| DEL          |      | backspace            |

##### 快捷键

| 操作描述                             | 快捷键                 | 命令名                         |
| ------------------------------------ | ---------------------- | ------------------------------ |
| 输入命令                             | M-x                    | execute-extended-command       |
| 退出程序                             | C-x C-c                | save-buffers-kill-terminal     |
| 放弃当前输入                         | C-g                    | keyboard-quit                  |
| 光标向上一行（方向键上）             | C-p                    | previous-line                  |
| 光标向下一行（方向键下）             | C-n                    | next-line                      |
| 光标向左一个字符（方向键左）         | C-b                    | backward-char                  |
| 光标向右一个字符（方向键右）         | C-f                    | forward-char                   |
| 光标向左移动一个词                   | M-b                    | backward-word                  |
| 光标向右移动一个词                   | M-f                    | forward-word                   |
| 光标移至行首                         | C-a                    | move-beginning-of-line         |
| 光标移至行尾                         | C-e                    | move-end-of-line               |
| 光标移动到一行缩进的开头             | M-m                    | back-to-indentation            |
| 光标移至句首                         | M-a                    | backward-sentence              |
| 光标移至句尾                         | M-e                    | forward-sentence               |
| 光标移至文件开头                     | M-<                    | beginning-of-buffer            |
| 光标移至文件结尾                     | M->                    | end-of-buffer                  |
| 光标移动至窗口的中间、最上、最下     | M-r                    | move-to-window-line-top-bottom |
| 删除光标右侧字符                     | C-d                    | delete-char                    |
| 移除光标右侧词                       | M-d                    | kill-word                      |
| 移除光标左侧词                       | M-                     | backward-kill-word             |
| 移除右侧直到句子结尾                 | M-k                    | kill-sentence                  |
| 移除右侧直到行尾                     | C-k                    | kill-line                      |
| 设置标记以选择区域                   | C-SPC                  | set-mark-command               |
| 复制区域                             | M-w                    | kill-region-save               |
| 移除区域                             | C-w                    | kill-region                    |
| 插入已移除文本                       | C-y                    | yank                           |
| 插入历史移除文本                     | M-y                    | yank-pop                       |
| 撤回                                 | C-/ 或 C-_ 或 C-x u    | undo                           |
| 跳转到上一标记                       | C-x C-SPC 或 C-u C-SPC | pop-global-mark                |
| 跳转到行号                           | M-g M-g                | goto-line                      |
| 重复                                 | C-u                    | universal-argument             |
| 向下一页                             | C-v                    | scroll-up-command              |
| 向上一页                             | M-v                    | scroll-down-command            |
| 移动页面使得光标在中央/最上方/最下方 | C-l                    | recenter-top-bottom            |
| 向后搜索                             | C-s                    | isearch-forward                |
| 向前搜索                             | C-r                    | isearch-backward               |
| 交换前后字符                         | C-t                    | transpose-chars                |
| 交换前后词                           | M-t                    | transpose-words                |
| 交换前后两行                         | C-x C-t                | transpose-lines                |
| 在下方新建一行                       | C-o                    | open-line                      |
| 删除连续空行为一个空行               | C-x C-o                | delete-blank-lines             |
| 将后面的词变为小写                   | M-l                    | downcase-word                  |
| 将后面的词变为大写                   | M-u                    | upcase-word                    |
| 将后面的词变为首字母大写             | M-c                    | capitalize-word                |
| 简要描述快捷键功能                   | C-h c                  | describe-key-briefly           |
| 描述快捷键功能                       | C-h k                  | describe-key                   |
| 描述函数功能                         | C-h f                  | describe-function              |
| 描述变量                             | C-h v                  | describe-variable              |
| 列出含某一关键词的命令               | C-h a                  | apropos-command                |
| 列出含某一关键词的符号的文档         | C-h d                  | apropos-documentation          |
| 帮助的帮助                           | C-h ?                  | help-for-help                  |

##### 常用

```
C-x C-c		退出
C-x C-s		保存
C-x C-f		emacs 内打开文件
C-x C-r		emacs 内打开文件(只读)

C-x C-q		已打开文件切换到只读模式

C-S-<mouse-1> 表达“同时按下 Control 键和 Shift 键，然后鼠标左键点击“

M-x
	安装 M 和 x
	Esc 松开, 再按 x

C-a
C-x b
C-S-<mouse-1>  同时按下 Control 键和 Shift 键, 然后鼠标左键点击
```

##### 移动

```
C-p
C-n
C-b
C-f
M-b 	前一个词
M-f 	后一个词
M-a 	句首 
M-e 	句尾
C-a 	行首
C-e 	行尾
M-< 	文件开头
M->		文件末尾
M-r		移动光标到窗口中 / 上 / 下
C-l	 	光标所在行位于窗口中 / 上 / 下
C-v		下一页
M-v 	上一页

标记跳转
	1. 不选中文本, 按 2 次 C-SPC
    2. 移动到其他地方
    3. C-u C-SPC 回刚刚的位置
```

##### 帮助信息

```
C-h c	查看快捷键对应的命令
C-h k	查询快捷键
C-h f	查询函数
C-h v	查询变量
C-h a	查询关键字
C-h d	列出含某一关键词的符号的文档
```

##### 编辑

```
C-d		delete
M-<DEL>	删除上边词
M-d		删除下边词
M-k		删至句尾
C-k		删至行尾
M-w 	复制
C-w 	剪切
C-SPC   选择模式
C-/		撤销
C-_		撤销
C-x u	撤销
C-g C-/	重做一次

C-u 12 C-n		向下 12 行, 默认是 4 次

C-t		光标所在字符和前一个字符互换
M-t		光标所在词和下一个互换
C-x C-t	光标所在行和上一行互换
C-o		光标所在行插入空行
C-x C-o 删除连续空行

M-l		光标后单词小写
M-u		光标后单词大写
M-c		光标所在字符大写, 后面的字符全小写\


标记与跳转
    1. 按下两次 C-SPC
    2. 光标移动到别的位置
    3. C-x C-SPC 或 C-u C-SPC，即可立刻跳转回刚刚的位置


想要跳到特定的行
	M-g M-g 加行号
	回车即可
```

##### 搜索

```
向下搜索
    C-s
    输入搜索得内容, 此时会自动跳到第一个符合的位置
    按 C-s 光标跳到下一个
    按 C-r 光标跳到上一个
    按回车光标停留在当前位置, 并结束搜索


向上搜索
	C-r
```

##### 文件

```
C-x C-c		保存(保存选择 y, 不保存选择 n)
C-x C-s		保存buffer
C-x C-f		打开文件
C-x C-v		打开文件(默认显示当前文件目录)
C-x C-r		只读打开文件
C-x C-q		已打开文件切为只读

M-x 输入 kill-emacs不保存关闭
```

##### buffer

```
C-x b		buffer 切换
C-x k		关闭当前 buffer

C-x C-b		buffer list window
	说明
		* 开头结尾的是 Emacs 用于输出一些信息的 Buffer，不是打开文件产生
		% 开头的没保存
	操作
        ?	可以显示帮助
        q 	退出
        d 	标记一个 Buffer 打算关闭
        s 	标记一个 Buffer 打算保存
        u 	取消标记
        x 	执行刚刚标记过的删除和保存操作
```

##### window

```
C-x 2		上下分割 window
C-x 3		左右分割 window
C-x 0		关闭当前 window
C-x 1		关闭其它 window, Buffer 没有关闭
C-x o		切换到下一个 window

C-x 4 f		在另一个 window 打开新的文件，如果只有一个窗口就分割成两个
C-x 4 b 	在另一个 window 切换到另一 Buffer，如果只有一个窗口就分割成两个
C-x 4 d 	在另一个 window 打开目录，如果只有一个窗口就分割成两个

增加/减少宽度
C-x {
C-x }
```

##### tab

```
C-x t 2 ;; 新建Tab 
      1 ;; 关闭其它Tab 
      0 ;; 关闭当前Tab 
      b ;; 在新Tab中打开Buffer
```

##### Frame

```
C-x 5 2		打开新 Frame
C-x 5 f		打开新 Frame 并打开文件
```

# 配置

##### 环境变量

```
# 获取PATH变量
M-x getenv  --> PATH


# 设置变量
插件 exec-path-from-shell
```

##### 配置文件路径

```
优先级从高到低
    ~/.emacs
    ~/.emacs.el
    ~/.emacs.d/init.el
    ~/.config/emacs/init.el
    

default.el: 位于 Emacs 的任何标准的 package 搜索目录下，其中 Emacs 的 package 搜索目录由 load-path 变量定义
site-start.el: 位于 Emacs 的任何标准的 package 搜索目录下, 加载 package 中的配置是优先加载 site-start.el , 最后加载 default.el 
early-init.el: 在初始化 package 系统和 GUI 之前加载

–no-init-file		Emacs 启动时, 选项来阻止 Emacs 加载初始化文件
-q					Emacs 启动时, 选项来阻止 Emacs 加载初始化文件
–no-site-file		禁止 Emacs 加载 site-start.el 配置文件

初始化文件中将 inhibit-default-init 设置为 t ,那么 Emacs 不会加载 default.el
```

```lisp
;; Emacs 启动时自动调用 package-initialize 导入已经安装了的包
(package-initialize)
;; 禁用 package-initialize 调用
(setq package-enable-at-startup nil)
```

##### 全局快捷键

- 格式

  ```
  (global-set-key (kbd <KEY>) <FUNCTION>)
      <key>: 快捷键
      <FUNCTION>: 功能	
  ```

##### 源分类

| 类型         | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| gnu          | 一般是必备的，其它的 elpa 中的包会依赖 gnu 中的包            |
| melpa        | 滚动升级，收录了的包的数量最大<br />默认插件安装到 `~/.emacs.d/elpa/` |
| melpa-stable | 依据源码的 Tag （Git）升级，数量比 melpa 少，因为很多包作者根本不打 Tag |
| org          | 仅仅为了 org-plus-contrib 这一个包，org 重度用户使用         |
| marmalade    | 似乎已经不维护了，个人不推荐                                 |

##### ~/.emacs.d/early-init.el

> 最先执行的配置文件

```lisp
(push '(menu-bar-lines . 0) default-frame-alist) ; 隐藏菜单栏
(push '(tool-bar-lines . 0) default-frame-alist) ; 隐藏工具栏
(push '(vertical-scroll-bars) default-frame-alist) ; 隐藏滚动条
(setq inhibit-startup-screen t) ; 关闭启动界面
;(setq frame-inhibit-implied-resize t) ; 禁止改变 frame 大小
(setq display-line-numbers-type 'relative) ; 行号类型: relative(相对行号), visual, t
(setq make-backup-files nil)                 ; 关闭文件自动备份
(setq default-buffer-file-coding-system 'utf-8)
(setq gc-cons-threshold most-positive-fixnum) ; 设置垃圾回收阈值, 加速启动速度

(global-display-line-numbers-mode t) ; 显示行号
(electric-pair-mode t) ; 自动补全括号
(show-paren-mode t) ; 括号匹配高亮
(prefer-coding-system 'utf-8) ; 设置系统的编码
(set-default-coding-systems 'utf-8)
(set-terminal-coding-system 'utf-8)
(set-keyboard-coding-system 'utf-8)
(column-number-mode t)                       ; 在 Mode line 上显示列号
(global-auto-revert-mode t)                  ; 当另一程序修改了文件时，让 Emacs 及时刷新 Buffer
(delete-selection-mode t)                    ; 选中文本后输入文本会替换文本（更符合我们习惯了的其它编辑器的逻辑）
(savehist-mode 1)                            ; 打开 Buffer 历史记录保存

(add-hook 'prog-mode-hook #'show-paren-mode) ; 编程模式下，光标在括号上时高亮另一个括号
(add-hook 'prog-mode-hook #'hs-minor-mode)   ; 编程模式下，可以折叠代码块
```

##### ~/.emacs.d/init.el

> 配置文件入口

```lisp
(use-package ace-window ; window 跳转
  :bind (("C-x o" . 'ace-window))
)


(use-package undo-tree ; 撤销命令树
  :init (global-undo-tree-mode)
)

(use-package lsp-ui 
  :init
  :config
  (setq lsp-ui-sideline-delay 0.1) ; 在显示边线之前等待几秒钟
  :commands 
  lsp-ui-mode
)

(use-package lsp-ivy ; 补全系统、部分常用命令、搜索功能
  :init
  :commands 
  lsp-ivy-workspace-symbol
)

(use-package lsp-treemacs 
  :init
  :commands 
  lsp-treemacs-errors-list
)


; 全文补全框架
(use-package company
  :config
  (global-company-mode t)
  (setq company-idle-delay 0.3) ; 输入时, 代码补全延迟
  (setq company-backends
    '((company-files
       company-keywords
       company-capf
       company-yasnippet
       )
      (company-abbrev company-dabbrev)))

)


; (use-package lsp-pyright
;   :hook (python-mode . (lambda ()
;                         (require 'lsp-pyright)
;                         (lsp-deferred))))
; (use-package python-mode
;   :hook (python-mode . lsp-deferred)
;   :custom
;   (dap-python-debugger 'debugpy)
;   :config
;   (require 'dap-python))

; (use-package pyvenv
;   :after python-mode
;   :config
;   (pyvenv-mode 1))

; (use-package py-isort
;   :after python
;   :hook ((python-mode . pyvenv-mode)
;          (before-save . py-isort-before-save)))

; (use-package blacken
;   :delight
;   :hook (python-mode . blacken-mode)
;   :custom (blacken-line-length 79))




; (dap-register-debug-template "My flask"
;   (list :type "python"
;         :jinja t
;         :module "flask"
;         :request "launch"
;         :env '(
;                ("PYTHONPATH" . "/home/glfadd/.pyenv/versions/p-3.9.2-learn")
;                ("FLASK_APP" . "./aaaa.py")
;                ("FLASK_ENV" . "development")
;                )
;         :name "My flask")

; )
; (use-package dap-mode
; )

(dap-register-debug-template "frontend-graphql"
                             (list :type "python"
                                   :program "run" ;; this due to the insistence of dap-debug of populating this one with the current file, adding :flask t did nothing for this value.
                                   :module "flask"
;                                   :args "--no-debugger --no-reload"
                                   :cwd "~/Desktop/learn/python"
                                   :request "launch"
                                   :environment-variables '(
                                                            ("FLASK_APP" . "aaaa.py")
                                                            ("FLASK_ENV" . "development")
                                                            ("FLASK_DEBUG" . "0"))
                                   :name "Python :: flask-graphql"
                                   :hostName "localhost"
                                   :host "localhost"))
```

##### 安装包

```
M-x list-packages 查看所有(安装/未安装)包
M-x package-refresh-contents 更新缓存

C-s django-snippets 搜索
i - 选择要安装的包
d - 选择要删除的包
U - 升级已安装的包
x - 执行操作
d - 选择要删除的包
```

##### 配置快捷键

- 配置全局快捷键

  ```lisp
  (global-set-key (kbd <KEY>) <FUNCTION>)
  
  ; 例如
  (global-set-key (kbd "RET") 'newline-and-indent)
  ```

- 定义函数

  ```lisp
  (defun next-ten-lines()
    "Move cursor to next 10 lines."
    (interactive)
    (next-line 10))
  
  (global-set-key (kbd "M-n") 'next-ten-lines)            ; 光标向下移动 10 行
  ```

##### 设置变量方式

- 1. 配置文件中使用 (setq name value) 

- 2. customize 中设定

  ```
  1. 配置文件中使用 (setq name value) 
  3. 运行过程中临时修改 M-x set-variable 
  ```

- 3. 运行过程中临时修改 M-x set-variable 

  ```
  M-x set-variable 
  <变量名>
  <回车>
  <输入值>
  <回车>
  ```

##### 配置更新方式

- 方式 1: 重启

- 方式 2: 手动执行选中部分de 代码

  ```
  (1)选中配置的代码
  (2)M-x 输入 eval-region
  ```

- 方式 3: 重新执行 buffer 中所有代码

  ```
  M-x 输入 eval-buffer
  ```

# use-package

> [github](https://github.com/jwiegley/use-package)
>
> (require 'xxx) 可以理解为 “导入并执行”，类似于 Python 的 import

##### 安装

```lisp
;; 使用 use-package 管理扩展
(unless (package-installed-p 'use-package) 
    (package-refresh-contents) 
    (package-install 'use-package))


;; use-package 全局设置
(eval-and-compile 
    (setq use-package-always-ensure t) ;不用每个包都手动添加:ensure t关键字 
    (setq use-package-always-defer t) ;默认都是延迟加载，不用每个包都手动添加:defer t 
    (setq use-package-always-demand nil) 
    (setq use-package-expand-minimally t) 
    (setq use-package-verbose t))

(require 'use-package)
```

##### 参数示例

```lisp
(use-package smooth-scrolling 
    :ensure t ; 确认安装，如果没有安装过就自动安装
    :defer nil ;是否要延迟加载 
    :init ; 在加载插件前执行一些命令
    (setq smooth-scrolling-margin 2) ; 设置变量
    :config ; 在加载插件后执行一些命令
    (smooth-scrolling-mode t) 
    :bind ; 快捷键的绑定
    ("C-c V" . 'ivy-pop-view)          ; 移除 buffer 记录
    :hook ; hook模式的绑定
    (prog-mode . flycheck-mode)
)
```

# package

##### x benchmark-init (启动耗时)

>  [github](https://github.com/dholm/benchmark-init-el)
>
> 自带的  `M-x emacs-init-time` 显示信息少

- install

  ```
  (use-package benchmark-init 
    :init (benchmark-init/activate) 
    :hook (after-init . benchmark-init/deactivate))
  ```

- use

  ```
  树状统计图
  M-x benchmark-init/show-durations-tree
  
  列表统计图
  M-x benchmark-init/show-durations-tabulated
  ```

##### all-the-icons (图标字体)

> [github](https://github.com/domtronn/all-the-icons.el)

```
1. use-package 安装 all-the-icons
2. M-x all-the-icons-install-fonts 下载字体, 选择一个路径 .emacs.d/fonts
3. 如果下载速度慢, 下载 https://github.com/domtronn/all-the-icons.el.git, 将里面的 fonts 拷贝到这个目录下
4. 进入 fonts 目录, 安装字体
```

##### doom-modeline (底部状态栏)

> [github](https://github.com/seagle0128/doom-modeline)
>
> [docs](https://www.5axxw.com/wiki/content/ywi4vx#doom-modeline)

##### gruvbox-theme (主题)

> [github](https://github.com/greduan/emacs-theme-gruvbox)
>
> [docs](https://www.5axxw.com/wiki/content/fnsh6j)

- install

  ```lisp
  (use-package gruvbox-theme 
      :init (load-theme 'gruvbox-dark-soft t))
  ```

##### which-key (快捷键提示)

> [github](https://github.com/justbur/emacs-which-key)
>
> [docs](https://www.5axxw.com/wiki/content/ablyvl)

- install

  ```
  (use-package which-key
    :config (which-key-mode))
  ```

##### dashboard (启动页)

>  [github](https://github.com/emacs-dashboard/emacs-dashboard)

- install

  ```
  (use-package dashboard
    :config
    (setq dashboard-banner-logo-title "Welcome to Emacs!") ;; 个性签名，随读者喜好设置
    ;; (setq dashboard-projects-backend 'projectile) ;; 读者可以暂时注释掉这一行，等安装了 projectile 后再使用
    (setq dashboard-startup-banner 'official) ;; 也可以自定义图片
    (setq dashboard-items '((recents  . 5)   ;; 显示多少个最近文件
  			  (bookmarks . 5)  ;; 显示多少个最近书签
  			  (projects . 10))) ;; 显示多少个最近项目
  ```

##### 

```
speedbar 是 emacs 自带
M-x speedbar
sr-speedbar
```



##### neotree (文件树)

> [github](https://github.com/jaypei/emacs-neotree)

- keybind

  ```
  <f8>		打开neotree
  p			上移
  n			下移
  SPC/RET/TAB	这三个快捷键都可以打开文件或展开目录
  U			跳转到上一级目录
  g			刷新
  H			显示或隐藏 隐藏文件(dotfiles)
  O			打开 / 关闭 目录下的所有目录结构
  A			最大化 / 最小化neotree窗口
  C-c C-n		创建文件或目录(以"/"结尾)
  C-c C-d		删除文件或目录
  C-c C-r		重命名文件后目录
  C-c C-c		设置当前目录为展示的根目录
  C-c C-p		复制文件或目录
  
  
  (global-set-key [f5] 'neotree-toggle)
  (global-set-key [f8] 'neotree-refresh)
  (global-set-key [f8] 'neotree-dir)
  
  
  ```

#####  ace-window (window 切换)

> [github](https://github.com/abo-abo/ace-window)

- key

  ```
  x   删除
  m   交换
  M   移动
  c   复制
  j   选择缓冲区
  n   上一个窗口
  u   在另一个窗口中选择缓冲区
  c   垂直或水平分割窗口
  v   垂直分割
  b   水平分割
  o   最大化当前
  ?   显示命令绑定
  ```

##### undo-tree

> 撤销命令记录

- install

  ```
  (use-package undo-tree
    :ensure t
    :init (global-undo-tree-mode))
  ```

- use

  ```
  C-x u	打开树状页面
  ```

##### good-scroll(未使用)

> 显示滚动美化
>
> [github](https://github.com/io12/good-scroll.el)

- install

  ```
  (use-package good-scroll
    :ensure t
    :init (good-scroll-mode))
  ```


##### flycheck (语法检测)

> [github](https://github.com/flycheck/flycheck)
>
> [document](https://www.flycheck.org/en/latest/)
>
> [document languages](https://www.flycheck.org/en/latest/languages.html)
>
> https://git.0xee.eu/0xee/emacs-config/src/commit/3d96c238166b7ee652d8a90137b2fe3552fbad5b/lsp.el?lang=en-US

- install

  ```
  
  ```
  
- python

  > [语法检查器](https://github.com/msherry/flycheck-pycheckers)
  >
  > [document](https://www.flycheck.org/en/latest/user/syntax-checkers.html#flycheck-checker-config-files)

  ```bash
  $ pip install flake8
  ```

- java

  ```
  
  ```

- use

  ```
  C-c ! v
  C-c ! l
  ```

##### evil (vim)

> [github](https://github.com/emacs-evil/evil)

##### general.el

> [github](https://github.com/noctuid/general.el)

##### centaur-tabs 标签切换(弃用)

>  [github](https://github.com/ema2159/centaur-tabs)

##### tab-line-mode

```
https://jdhao.github.io/2021/09/30/emacs_custom_tabline/

https://andreyorst.gitlab.io/posts/2020-05-10-making-emacs-tabs-look-like-in-atom/

看看这个
https://amitp.blogspot.com/2020/06/emacs-prettier-tab-line.html
```

##### shell

##### buffer

```
Speedbar and imenu
speedbar/sr-speedbar 倒是又 buffer list，但它不能同时显示文件树。buffer 与树不可兼得，只能在两种状态下切换，跟 VSCode 这些编辑器还是有些不同：
ace-jump-buffer


(global-set-key (kbd "s-<left>") 'previous-buffer)
(global-set-key (kbd "s-<right>") 'next-buffer)
ibuffer

```

##### yasnippet 代码片段

> [github](https://github.com/joaotavora/yasnippet)

##### crux 一些快捷操作

##### format-all 代码格式化

##### 远程访问

```
tramp
```

##### swiper (搜索列表)

##### counsel (剪贴板历史)

### 弃用

##### elpy

##### company-lsp(停止维护弃用)

> [github](https://github.com/tigersoldier/company-lsp)

##### x smart-mode-line (底部状态栏)

> [github](https://github.com/Malabarba/smart-mode-line)
>
> 不好看

# ivy

```
helm，ivy


https://github.com/emacs-lsp/lsp-ivy
```



> 交互式补全工具, 用来补全系统、部分常用命令、搜索功能
>
> 包括三部分: ivy, counsel, swiper
>
> [github](https://github.com/abo-abo/swiper)
>
> [document](https://oremacs.com/swiper/#key-bindings)
>
> https://emacs-china.org/t/ivy/12091
>

```
使用模糊查询 ivy--regex-plus 需要系统安装 fzf
```

##### avy

> [github](https://github.com/abo-abo/avy)

```

```

##### ivy-avy

> 光标跳转
>
> [github](https://github.com/abo-abo/avy)

```
(global-set-key (kbd "C-s") 'swiper-isearch)
(global-set-key (kbd "M-x") 'counsel-M-x)
(global-set-key (kbd "C-x C-f") 'counsel-find-file)
(global-set-key (kbd "M-y") 'counsel-yank-pop)
(global-set-key (kbd "<f1> f") 'counsel-describe-function)
(global-set-key (kbd "<f1> v") 'counsel-describe-variable)
(global-set-key (kbd "<f1> l") 'counsel-find-library)
(global-set-key (kbd "<f2> i") 'counsel-info-lookup-symbol)
(global-set-key (kbd "<f2> u") 'counsel-unicode-char)
(global-set-key (kbd "<f2> j") 'counsel-set-variable)
(global-set-key (kbd "C-x b") 'ivy-switch-buffer)
(global-set-key (kbd "C-c v") 'ivy-push-view)
(global-set-key (kbd "C-c V") 'ivy-pop-view)

(global-set-key (kbd "C-c c") 'counsel-compile)
(global-set-key (kbd "C-c g") 'counsel-git)
(global-set-key (kbd "C-c j") 'counsel-git-grep)
(global-set-key (kbd "C-c L") 'counsel-git-log)
(global-set-key (kbd "C-c k") 'counsel-rg)
(global-set-key (kbd "C-c m") 'counsel-linux-app)
(global-set-key (kbd "C-c n") 'counsel-fzf)
(global-set-key (kbd "C-x l") 'counsel-locate)
(global-set-key (kbd "C-c J") 'counsel-file-jump)
(global-set-key (kbd "C-S-o") 'counsel-rhythmbox)
(global-set-key (kbd "C-c w") 'counsel-wmctrl)

(global-set-key (kbd "C-c C-r") 'ivy-resume)
(global-set-key (kbd "C-c b") 'counsel-bookmark)
(global-set-key (kbd "C-c d") 'counsel-descbinds)
(global-set-key (kbd "C-c g") 'counsel-git)
(global-set-key (kbd "C-c o") 'counsel-outline)
(global-set-key (kbd "C-c t") 'counsel-load-theme)
(global-set-key (kbd "C-c F") 'counsel-org-file)
```

# company-mode 

```
https://github.com/company-mode/company-mode



```

# lsp

[home page](https://emacs-lsp.github.io/lsp-mode/)

##### lsp-mode (Emacs LSP 协议库)

>  [github](https://github.com/emacs-lsp/lsp-mode)

##### lsp-ui

> [github](https://github.com/emacs-lsp/lsp-ui)
>
> [docs](https://github.com/emacs-lsp/lsp-ui/blob/master/lsp-ui-doc.el)

### python

##### elpy (弃用)

##### lsp-python-ms (弃用)

>  [github](https://github.com/emacs-lsp/lsp-python-ms)

```
https://github.com/Microsoft/python-language-server
```

##### 虚拟环境 (选做)

```bash
$ pip3 install virtualenv
$ mkdir -p ~/.emacs.d/.python-environments
$ virtualenv -p /usr/local/bin/python3 --prompt="<venv:jedi>" jedi
$ virtualenv -p python3 --prompt="<venv:jedi>" jedi
```

##### pyvenv (虚拟环境)

> [github](https://github.com/jorgenschaefer/pyvenv)

```
M-x pyvenv-workon		激活具体虚拟环境(~/.pyenv/versions 下的环境)
M-x pyvenv-activate 	其他的虚拟环境
M-x pyvenv-deactivate	退出当前的虚拟环境
```

##### server

> https://github.com/emacs-lsp/lsp-python-ms
> https://emacs-lsp.github.io/lsp-python-ms
> [python-lsp-server](https://github.com/python-lsp/python-lsp-server)

```bash
$ pip install 'python-language-server[all]'
$ pip install python-lsp-server
# 查看包信息
$ pip show python-language-server

$ pip install jedi flake8 importmagic autopep8 rope pylint ipython 
	jedi		自动补全
	pylint		语法检测
	importmagic 自动导入工具
	
$ yum install python-lsp-server


https://www.bilibili.com/read/cv12938972/



安装 lsp-treemacs 以获得项目范围的错误概述。
安装 helm-lsp 为 xref-apropos 提供类型完成功能。


pylsp


elpy					
flycheck				语法检测
company-jedi			python 补全
virtualenvwrapper		python 虚拟环境


https://www.cnblogs.com/ibgo/p/4529050.html
https://segmentfault.com/a/1190000039793511?utm_source=tag-newest

刷新 package 包
M-x package-refresh-contents <RET>








语法检测
elpy默认使用 flymake检查语法，替换为 flycheck
(use-package elpy
  :hook
  (elpy-mode . flycheck-mode) ;; 添加flycheck, 替换flymake
  :config
  (setq elpy-modules (delq 'elpy-module-flymake elpy-modules))
)




python虚拟环境
pip install virtualenvwrapper
```

##### 报错1

打开 py 文件时提示, 打开日志信息如下

```
Command "pyls" is not present on the path.
Command "pylsp" is not present on the path.
Command "pyls" is not present on the path.
Command "pylsp" is not present on the path.
```

原因

```
Emacs无法找到pyls的可执行文件，因为该文件的目录不在Emacs的环境变量中
```

解决办法

- 方式1

  ```
  配置文件添加:
      (setq lsp-pyls-server-command "~/.local/bin/pyls")
      (setq lsp-pylsp-server-command "~/.local/bin/pylsp")
  
  
  提示:
  1. lsp-clients-python-command 被 lsp-pyls-server-command 代替了
  2. 不能使用 /home/gong/.local/lib/python3.11/site-packages/pyls, 会提示报错
      Command "/home/gong/.local/lib/python3.11/site-packages/pyls" is not present on the path.
      Command "pylsp" is not present on the path.
      Command "/home/gong/.local/lib/python3.11/site-packages/pyls" is not present on the path.
      Command "pylsp" is not present on the path.
  ```

- 方式2 (临时的)

  ```
  M-x setenv RET PATH 然后设置环境变量
  ```
  



##### company-capf

> 文本补全框架
>
> [github](https://github.com/company-mode/company-mode/blob/master/company-capf.el)
>
> [文档](http://company-mode.github.io/)
>
> 参考 https://ithelp.ithome.com.tw/articles/10200533

### C

### go

# dap-mode

>调试工具
>
>[github](https://github.com/emacs-lsp/dap-mode)
>
>[homepage](https://emacs-lsp.github.io/dap-mode/page/features/)
>
>[configuration](https://emacs-lsp.github.io/dap-mode/page/configuration/)
>
>文档 https://www.joyk.com/dig/detail/1551816021702193
>
>https://emacs-lsp.github.io/dap-mode/page/adding-debug-server/
>
>教程 https://alpha2phi.medium.com/emacs-beginner-configuration-9578dbe71d03
>
>也许能直接用的配置文件 https://alpha2phi.medium.com/emacs-lsp-and-dap-7c1786282324
>
>flask 的问题 https://github.com/emacs-lsp/dap-mode/issues/234
>
>​	问题视频 https://www.youtube.com/watch?v=ffS7DHbSpVc&ab_channel=Jorge%28%40shackraonGab%29
>

##### 安装

##### 命令

```
dap-hydra 查看命令
dap-debug 开始调试

dap-next
dap-step-in
dap-breakpoint-add

dap-ui-breakpoints	
```

### python

```
pip install ptvsd pytest debugpy
```

### java

```
是否需要安装 node
```

# 游戏

##### 内置游戏

```
M-x 游戏名
q			退出
    doctor		机器人对话
    snake		贪吃蛇
    gomoku		五子棋
    bubbles		消消乐
```

##### 俄罗斯方块

```


```

