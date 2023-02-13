##### 注释

```lua
-- 单行注释

--[[
 多行注释
 多行注释
 --]]
```

##### require

```lua
把 lua 代码分成不同的模块, 使用 require 函数加载进来
路径分隔符用 . 或 / 

例如: 加载 other_modules/anothermodule.lua 文件
require 'other_modules.anothermodule'
require 'other_modules/anothermodule'
```

##### 

```
vim.g.{name}: 全局变量
vim.b.{name}: 缓冲区变量
vim.w.{name}: 窗口变量
vim.t.{name}: 选项卡变量
vim.v.{name}: 预定义变量
```



