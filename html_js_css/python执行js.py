# -*- coding: utf-8 -*-

import execjs
import execjs.runtime_names

# 将字符串当方法运行
print execjs.eval("'red yellow blue'.split(' ')")

ctx = execjs.compile("""
    function add(x, y) {
        return x + y;
    }
""")
# 调用方法
print ctx.call("add", 2, 2)

# windows 默认的执行JS的环境
print execjs.get().name
print execjs.get().eval('1 + 6')

js = execjs.get(execjs.runtime_names.JScript)
print js.eval("10 + 2")

print execjs.eval('new Date()')

# ==判断值是否相同, ===判断值和类型是否相同
print execjs.eval('1 == "1"')
print execjs.eval('1 === "1"')

print execjs.eval('')




