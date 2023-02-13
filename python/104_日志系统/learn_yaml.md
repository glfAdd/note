##### 格式

- 大小写敏感
- 使用缩进表示层级关系
- 缩进时不允许使用Tab键，只允许使用空格。
- 缩进1个或多个空格，只要相同层级的元素左侧对齐即可

##### 字符串

- 字符串可以不用引号, 单引号或者双引号
- 必须使用引号情况
  - 当字符串是 true 或者 false, 否则的话，会被认为是一个布尔值
  - 当字符串是 null或者 ~, 否则的话，会被认为是一个null
  - 当字符串像一个数字，比如整数（2,4）、浮点数（2.6,12.3）、科学计数（12e7）等等可以被看作是数字的字符串
  - 当字符串看起来像一个日期格式 2014-12-31
  - 当字符串的首部或者尾部有空白字符，那么必须使用引号，否则在解析文件的时候会将首部和尾部的空白字符移除
  - 当字符串中包含下面的字符，必须要使用引号，如果你使用单引号的话可以避免转义，如果使用双引号那么在下面的字符前面必须使用转义字符“\”

```
: { } [ ] , & * # ? | - < > = ! % @ `
```

##### 单行字符串

```yaml
string in YAML
'A singled-quoted string in YAML'
"A double-quoted string in YAML"
```

##### 多行字符串

- 每行前面使用2个空格字符表明继续使用前一种定义语法，并且不会出现在最终的字符串中

```yaml
>
  string in YAML
  string in YAML
```

##### 数字

```yaml
# 整数
12
# 八进制
014
# 十六进制
0x0C
# 浮点数
13.4
# 科学计数法
1.2e+34
# 无穷大
.inf
```

##### 空

```yaml
null
~
```

##### 布尔值

```yaml
true 也可以用on、1 表示
false 也可以用off、0表示
```

##### 日期

```yaml
2001-12-14t21:59:43.10-05:00
2002-12-14
```

##### 列表

```yaml
# 相当于python的 ['PHP', 'Perl', 'Python']
- PHP
- Perl
- Python
```

##### 字典

```yaml
# 相当于python的 {'PHP':5.2, 'MySQL':5.1, 'Apache':'2.2.20'}
PHP: 5.2
MySQL: 5.1
Apache: 2.2.20
```

##### 混合使用

```yaml
'Chapter 2': [Introduction, Helpers]
'symfony 1.0': { PHP: 5.0, Propel: 1.2 }
```

 ##### 嵌套

- yaml 格式 1

```yaml
name: Tom
detail:
  - 1
  - 2
  - 3
  - a: 1
    b: 2
    c:
      - cat
      - dog
      - pig
age: 12
```

- json 格式 1

```json
{
  "name": "Tom",
  "detail": [
    1,
    2,
    3,
    {
      "a": 1,
      "b": 2,
      "c": [
        "cat",
        "dog",
        "pig"
      ]
    }
  ],
  "age": 12
}
```

##### 多行字符串 - 需要段落

- 原始字符串

```
I am a coder.My blog is didispace.com.
```

- 希望的结果

```
I am a coder.
My blog is didispace.com.
```

- 方式1

```yaml
# 通过\n在显示的时候换行
# 通过配置行末的\让这个字符串换行继续写, 否则第二行行首会多一个空格
# 这里必须使用双引号来定义字符串，不能用单引号。因为单引号是不支持\n换行的
string: "I am a coder.\n\
         My blog is didispace.com."
```

- 方式2
  - `|`：文中自动换行 + 文末新增一空行
  - `|+`：文中自动换行 + 文末新增两空行
  - `|-`：文中自动换行 + 文末不新增行

```yaml
string: |
  I am a coder.
  My blog is didispace.com.

string: |+
  I am a coder.
  My blog is didispace.com.

string: |-
  I am a coder.
  My blog is didispace.com.
```

##### 多行字符串 - 不需要段落

- 希望结果, 写的时候是换行的, 但在实际解析中不换行

```
I am a coder.My blog is didispace.com.
```

- 方式1
  - 双引号或单引号都可以

```
string: 'I am a coder.
         My blog is didispace.com.'
```

- 方式2
  - `>`：文中不自动换行 + 文末新增一空行
  - `>+`：文中不自动换行 + 文末新增两空行
  - `>-`：文中不自动换行 + 文末不新增行

```
string: >
  I am a coder.
  My blog is didispace.com.

string: >+
  I am a coder.
  My blog is didispace.com.

string: >-
  I am a coder.
  My blog is didispace.com.
```

##### 锚点和引用

- 锚点用符号“&”定义，并用符号“*”进行引用
- 使用"<<:", 将键值对一起引入

```yaml
# 引用
default-db: &default-db-config
  host: 127.0.0.1
  port: 3306

user-db:
  <<: *default-db-config
  

# 效果
default-db:
  host: 127.0.0.1
  port: 3306

user-db:
  host: 127.0.0.1
  port: 3306 
```

- 仅引入配置的值

```yaml
# 引用
site:
  url:
    user: &site.user www.user.net
    shop: &site.shop www.shop.net

site:
  slogan:
    *site.user: everyone is great!
    *site.shop: buy anything you want!
    

# 效果
site:
  url:
    user: www.user.net
    shop: www.shop.net

site:
  slogan:
    www.user.net: everyone is great!
    www.shop.net: buy anything you want!
```

##### 设置变量的值

- 这种方式不能动态替换变量的 kye 

```yaml
default-db:
  port: 3306

user-db:
  port: ${default-db.port}
```









