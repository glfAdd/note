```
#!/bin/sh
#!/bin/bash
```

> \#! 是一个约定的标记，它告诉系统这个脚本需要什么解释器来执行，即使用哪一种 Shell
>
> echo 命令用于向窗口输出文本(相当于 print)

```shell
#!/bin/bash
echo "Hello World !"
```

##### 运行

- 方式1: 作为可执行程序. 一定要写成 ./test.sh，而不是 test.sh，运行其它二进制的程序也一样，直接写 test.sh，linux 系统会去 PATH 里寻找有没有叫 test.sh 的，而只有 /bin, /sbin, /usr/bin，/usr/sbin 等在 PATH 里

```shell
chmod +x ./test.sh
./test.sh
```

- 方式2: 作为解释器参数. 直接运行解释器，其参数就是 shell 脚本的文件名. 不需要在第一行指定解释器信息，写了也没用。

```
/bin/sh test.sh
/bin/php test.php
```

## 变量

##### 定义变量

- 变量名和等号之间不能有空格
- 命名只能使用英文字母，数字和下划线，首个字符不能以数字开头
- 中间不能有空格，可以使用下划线
- 不能使用标点符号
- 不能使用bash里的关键字（可用help命令查看保留关键字）

```shell
# 有效的 Shell 变量名示例如下：
RUNOOB
LD_LIBRARY_PATH
_var
var2

# 无效的变量命名:
?var=123
user*name=runoob

# 除了显式地直接赋值，还可以用语句给变量赋值
# 将 /etc 下目录的文件名循环出来
for file in `ls /etc`
或
for file in $(ls /etc)
```

##### 使用变量

- 使用一个定义过的变量，只要在变量名前面加美元符号即可 
- 变量名外面的花括号是可选的，加不加都行，加花括号是为了帮助解释器识别变量的边界. 推荐给所有变量加上花括号

```shell
your_name="qinjx"
echo $your_name
echo ${your_name}

for skill in Ada Coffe Action Java; do
    echo "I am good at ${skill}Script"
done
```

- 已定义的变量，可以被重新定义

```shell
# 第二次赋值的时候不能写$your_name="alibaba"，使用变量的时候才加美元符（$）
your_name="tom"
echo $your_name
your_name="alibaba"
echo $your_name
```

##### 只读变量

- 使用 readonly 命令可以将变量定义为只读变量，只读变量的值不能被改变, 修改会报错

```shell
#!/bin/bash
myUrl="https://www.google.com"
readonly myUrl
myUrl="https://www.runoob.com"
```

##### 删除变量

- 使用 unset 命令可以删除变量
- 变量被删除后不能再次使用。unset 命令不能删除只读变量

```shell
#!/bin/sh
myUrl="https://www.runoob.com"
unset myUrl
echo $myUrl

# 以上实例执行将没有任何输出
```

##### 变量类型

- 运行shell时，会同时存在三种变量
  - 1) 局部变量 局部变量在脚本或命令中定义，仅在当前shell实例中有效，其他shell启动的程序不能访问局部变量。
  - 2) 环境变量 所有的程序，包括shell启动的程序，都能访问环境变量，有些程序需要环境变量来保证其正常运行。必要的时候shell脚本也可以定义环境变量。
  - 3) shell变量 shell变量是由shell程序设置的特殊变量。shell变量中有一部分是环境变量，有一部分是局部变量，这些变量保证了shell的正常运行

## 字符串

字符串可以用单引号，也可以用双引号，也可以不用引号

##### 单引号

- 单引号里的任何字符都会原样输出，单引号字符串中的变量是无效的；
- 单引号字串中不能出现单独一个的单引号（对单引号使用转义符后也不行），但可成对出现，作为字符串拼接使用。

```shell
str='this is a string'
```

##### 双引号

- 双引号里可以有变量
- 双引号里可以出现转义字符

```shell
your_name='runoob'
str="Hello, I know you are \"$your_name\"! \n"
echo -e $str

# 输出结果为：
Hello, I know you are "runoob"! 
```

##### 拼接字符串

```shell
your_name="runoob"
# 使用双引号拼接
greeting="hello, "$your_name" !"
greeting_1="hello, ${your_name} !"
echo $greeting  $greeting_1
# 使用单引号拼接
greeting_2='hello, '$your_name' !'
greeting_3='hello, ${your_name} !'
echo $greeting_2  $greeting_3

# 输出结果为：
hello, runoob ! hello, runoob !
hello, runoob ! hello, ${your_name} !
```

##### 获取字符串长度

```shell
string="abcd"
echo ${#string} 

#输出 4
```

##### 提取子字符串

```shell
# 从字符串第 2 个字符开始截取 4 个字符
# 第一个字符的索引值为 0
string="runoob is a great site"
echo ${string:1:4} 

# 输出 unoo
```

##### 查找子字符串

```shell
# 查找字符 i 或 o 的位置(哪个字母先出现就计算哪个)：
# 脚本中 ` 是反引号，而不是单引号 '

string="runoob is a great site"
echo `expr index "$string" io`  

# 输出 4
```

## 数组

##### 定义数组

- bash 只支持一维数组, 不支持多维数组, 并且没有限定数组的大小,下标由 0 开始
- 用括号来表示数组，数组元素用"空格"符号分割开
- 可以不使用连续的下标，而且下标的范围没有限制。 

```shell
array_name=(value0 value1 value2 value3)

# 或者
array_name=(
value0
value1
value2
value3
)

# 单独定义数组的各个分量
array_name[0]=value0
array_name[1]=value1
array_name[n]=valuen
```

##### 读取数组

```shell
# 读取数组元素值的一般格式是
${数组名[下标]}

# 例如：
valuen=${array_name[n]}

# 使用 @ 或 * 符号可以获取数组中的所有元素
echo ${array_name[@]}
echo ${array_name[*]}
```

##### 获取数组的长度

```shell
# 取得数组元素的个数
length=${#array_name[@]}
# 或者
length=${#array_name[*]}

# 取得数组单个元素的长度
lengthn=${#array_name[n]}
```

## 注释

##### 单行注释

```shell

```

##### 多行注释

```shell
:<<EOF
注释内容...
注释内容...
注释内容...
EOF

# EOF 也可以使用其他符号:
:<<'
注释内容...
注释内容...
注释内容...
'

:<<!
注释内容...
注释内容...
注释内容...
!
```

## 启动shell的参数

##### 格式

- 在执行 Shell 脚本时，向脚本传递参数，脚本内获取参数的格式为 $n
- n 代表一个数字，1 为执行脚本的第一个参数，2 为执行脚本的第二个参数，以此类推
- $0 为执行的文件名, 包含文件路径
- 如果参数包含空格，应该使用单引号或者双引号将该参数括起来，以便于脚本将这个参数作为整体来接收。

```shell
#!/bin/bash
echo "Shell 传递参数实例！";
echo "执行的文件名：$0";
echo "第一个参数为：$1";
echo "第二个参数为：$2";
```

##### 处理参数的符号

| 参数处理 | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| $#       | 传递到脚本的参数个数                                         |
| $*       | 用一个单字符串显示所有向脚本传递的参数, 空格分隔             |
| $$       | 脚本运行的当前进程ID号                                       |
| $!       | 后台运行的最后一个进程的ID号                                 |
| $@       | 用一个单字符串显示所有向脚本传递的参数, 空格分隔             |
| $-       | 显示Shell使用的当前选项，与[set命令](https://www.runoob.com/linux/linux-comm-set.html)功能相同。 |
| $?       | 显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。 |

- $* 与 $@ 区别
  - 相同点：都是引用所有参数
  - 不同点：只有在双引号中体现出来。假设在脚本运行时写了三个参数 1、2、3，，则 " * " 等价于 "1 2 3"（传递了一个参数），而 "@" 等价于 "1" "2" "3"（传递了三个参数）

```shell
#!/bin/bash
echo "-- \$* 演示 ---"
for i in "$*"; do
    echo $i
done

echo "-- \$@ 演示 ---"
for i in "$@"; do
    echo $i
done
```

##### TODO 对参数校验减少错误

```






```

## 运算符

##### 格式

- 原生bash不支持简单的数学运算，但是可以通过其他命令来实现，例如 awk 和 expr，expr 最常用
- expr 是一款表达式计算工具，使用它能完成表达式的求值操作
- 表达式和运算符之间要有空格
- 完整的表达式要被 `  包含

```
#!/bin/bash
val=`expr 2 + 2`
echo "两数之和为 : $val"
```

##### 算术运算符

> a 为 10，变量 b 为 20

| 运算符 | 说明   | 举例                          |
| ------ | ------ | ----------------------------- |
| +      | 加法   | `expr $a + $b` 结果为 30。    |
| -      | 减法   | `expr $a - $b` 结果为 -10。   |
| *      | 乘法   | `expr $a \* $b` 结果为  200。 |
| /      | 除法   | `expr $b / $a` 结果为 2。     |
| %      | 取余   | `expr $b % $a` 结果为 0。     |
| =      | 赋值   | a=$b 将把变量 b 的值赋给 a。  |
| ==     | 相等   | [ $a == $b ] 返回 false。     |
| !=     | 不相等 | [ $a != $b ] 返回 true。      |

##### 关系运算符

- 关系运算符只支持数字，不支持字符串，除非字符串的值是数字

> a 为 10，变量 b 为 20：

| 运算符 | 说明     | 举例                       |
| ------ | -------- | -------------------------- |
| -eq    | 等于     | [ $a -eq $b ] 返回 false。 |
| -ne    | 不相等   | [ $a -ne $b ] 返回 true。  |
| -gt    | 大于     | [ $a -gt $b ] 返回 false。 |
| -lt    | 小于     | [ $a -lt $b ] 返回 true。  |
| -ge    | 大于等于 | [ $a -ge $b ] 返回 false。 |
| -le    | 小于等于 | [ $a -le $b ] 返回 true。  |

##### 布尔运算符

| 运算符 | 说明                                                | 举例                                     |
| ------ | --------------------------------------------------- | ---------------------------------------- |
| !      | 非运算，表达式为 true 则返回 false，否则返回 true。 | [ ! false ] 返回 true。                  |
| -o     | 或运算，有一个表达式为 true 则返回 true。           | [ $a -lt 20 -o $b -gt 100 ] 返回 true。  |
| -a     | 与运算，两个表达式都为 true 才返回 true。           | [ $a -lt 20 -a $b -gt 100 ] 返回 false。 |

##### 逻辑运算符

> a 为 10，变量 b 为 20

| 运算符 | 说明 | 举例                                       |
| ------ | ---- | ------------------------------------------ |
| &&     | AND  | [[ $a -lt 100 && $b -gt 100 ]] 返回 false  |
| \|\|   | OR   | [[ $a -lt 100 \|\| $b -gt 100 ]] 返回 true |

##### 字符串运算符

>  a 为 "abc"，变量 b 为 "efg"

| 运算符 | 说明                                         | 举例                     |
| ------ | -------------------------------------------- | ------------------------ |
| =      | 检测两个字符串是否相等，相等返回 true。      | [ $a = $b ] 返回 false。 |
| !=     | 检测两个字符串是否不相等，不相等返回 true。  | [ $a != $b ] 返回 true。 |
| -z     | 检测字符串长度是否为0，为0返回 true。        | [ -z $a ] 返回 false。   |
| -n     | 检测字符串长度是否不为 0，不为 0 返回 true。 | [ -n "$a" ] 返回 true。  |
| $      | 检测字符串是否为空，不为空返回 true。        | [ $a ] 返回 true。       |

##### 文件测试运算符

- 文件测试运算符用于检测 Unix 文件的各种属性

| 操作符  | 说明                                                         | 举例                      |
| ------- | ------------------------------------------------------------ | ------------------------- |
| -b file | 检测文件是否是块设备文件，如果是，则返回 true。              | [ -b $file ] 返回 false。 |
| -c file | 检测文件是否是字符设备文件，如果是，则返回 true。            | [ -c $file ] 返回 false。 |
| -d file | 检测文件是否是目录，如果是，则返回 true。                    | [ -d $file ] 返回 false。 |
| -f file | 检测文件是否是普通文件（既不是目录，也不是设备文件），如果是，则返回 true。 | [ -f $file ] 返回 true。  |
| -g file | 检测文件是否设置了 SGID 位，如果是，则返回 true。            | [ -g $file ] 返回 false。 |
| -k file | 检测文件是否设置了粘着位(Sticky Bit)，如果是，则返回 true。  | [ -k $file ] 返回 false。 |
| -p file | 检测文件是否是有名管道，如果是，则返回 true。                | [ -p $file ] 返回 false。 |
| -u file | 检测文件是否设置了 SUID 位，如果是，则返回 true。            | [ -u $file ] 返回 false。 |
| -r file | 检测文件是否可读，如果是，则返回 true。                      | [ -r $file ] 返回 true。  |
| -w file | 检测文件是否可写，如果是，则返回 true。                      | [ -w $file ] 返回 true。  |
| -x file | 检测文件是否可执行，如果是，则返回 true。                    | [ -x $file ] 返回 true。  |
| -s file | 检测文件是否为空（文件大小是否大于0），不为空返回 true。     | [ -s $file ] 返回 true。  |
| -e file | 检测文件（包括目录）是否存在，如果是，则返回 true。          | [ -e $file ] 返回 true。  |
| -S file | 判断某文件是否 socket                                        |                           |
| -L file | 检测文件是否存在并且是一个符号链接                           |                           |

```shell
#!/bin/bash

file="/var/www/runoob/test.sh"
if [ -r $file ]
then
   echo "文件可读"
else
   echo "文件不可读"
```

## echo

- 用于字符串的输出

##### 普通输出

```shell
echo "It is a test"
# 双引号可以省略
echo It is a test
```

##### 转义字符

```shell
echo "\"It is a test\""
echo \"It is a test\"
```

##### 使用变量

```shell
your_name="qinjx"
echo ${your_name}
```

##### 换行

```shell
echo "OK! \n" 
echo "It is a test"
```

##### 不换行

```shell
echo "OK! \c"
echo "It is a test"
```

##### 输出到文件

```shell
echo "It is a test" > myfile
```

##### 写什么样输出什么样, 不是用变量和转译字符

```shell
# 用单引号
echo '$name\"'
```

##### 执行shell命令

```shell
# 反引号 `
echo `date`
```

## printf

- 用于输出
- 需要手动换行 \n

##### 格式

```
printf  format-string  [arguments...]
```

```shell
# format-string为双引号
printf "%d %s\n" 60 "abc"

# 单引号与双引号效果一样
printf '%d %s\n' 550 "abc"

# 没有引号也可以输出
printf %s abcdef
```

- 对齐输出

```shell
#!/bin/bash

printf "%-10s %-8s %-4s\n" 姓名 性别 体重kg  
printf "%-10s %-8s %-4.2f\n" 郭靖 男 66.1234
printf "%-10s %-8s %-4.2f\n" 杨过 男 48.6543
printf "%-10s %-8s %-4.2f\n" 郭芙 女 47.9876

# ％s 字符串
# ％d 整型
# ％c 一个字符
# ％f 小数
# %-10s 指一个宽度为 10 个字符（- 表示左对齐，没有则表示右对齐），任何字符都会被显示在 10 个字符宽的字符内，如果不足则自动以空格填充，超过也会将内容全部显示出来。
# %-4.2f 指格式化为小数，其中 .2 指保留2位小数
```

- 这样仍可以正常输出

```shell
# arguments 比转译字符多, format-string 被重用
printf %s abc def
printf "%s\n" abc def
printf "%s %s %s\n" a b c d e f g h i j
# 如果没有 arguments，那么 %s 用NULL代替，%d 用 0 代替
printf "%s and %d \n"
```

##### 转译字符

| 序列  | 说明                                                         |
| ----- | ------------------------------------------------------------ |
| \a    | 警告字符，通常为ASCII的BEL字符                               |
| \b    | 后退                                                         |
| \c    | 抑制（不显示）输出结果中任何结尾的换行字符（只在%b格式指示符控制下的参数字符串中有效），而且，任何留在参数里的字符、任何接下来的参数以及任何留在格式字符串中的字符，都被忽略 |
| \f    | 换页（formfeed）                                             |
| \n    | 换行                                                         |
| \r    | 回车（Carriage return）                                      |
| \t    | 水平制表符                                                   |
| \v    | 垂直制表符                                                   |
| \\    | 一个字面上的反斜杠字符                                       |
| \ddd  | 表示1到3位数八进制值的字符。仅在格式字符串中有效             |
| \0ddd | 表示1到3位的八进制值字符                                     |

## 流程控制

##### if

```shell
a=10
b=20
if [ $a == $b ]
then
   echo "a 等于 b"
elif [ $a -gt $b ]
then
   echo "a 大于 b"
elif [ $a -lt $b ]
then
   echo "a 小于 b"
else
   echo "没有符合的条件"
fi
```

- 在同一行中的写法

```bash
if [ $(ps -ef | grep -c "ssh") -gt 1 ]; then echo "true"; fi
```

##### for

```shell
#!/bin/bash
for loop in 1 2 3 4 5
do
    echo "The value is: $loop"
done

for str in hello word
do
    echo $str
done
```

##### while

```shell
#!/bin/bash
int=1
while(( $int<=5 ))
do
    echo $int
    let "int++"
done
```

- 输入信息被设置为变量FILM，按<Ctrl-D>结束循环

```shell
echo '按下 <CTRL-D> 退出'
echo -n '输入你最喜欢的网站名: '
while read FILM
do
    echo "是的！$FILM 是一个好网站"
done
```

##### until

- until 循环执行一系列命令直至条件为 true 时停止
- 一般 while 循环优于 until 循环 ??????????????

```shell
#!/bin/bash
a=0
until [ ! $a -lt 10 ]
do
   echo $a
   a=`expr $a + 1`
done
```

##### case

- 每个 case 分支用右圆括号开始
- 用两个分号 ;; 表示 break 跳出整个 case 语句
- esac（就是 case 反过来）作为结束标记
- 如果匹配成功，执行相匹配的命令

```shell
#!/bin/bash
echo '输入 1 到 4 之间的数字:'
echo '你输入的数字为:'
read aNum
case $aNum in
    1)  echo '你选择了 1'
    ;;
    2)  echo '你选择了 2'
    ;;
    3)  echo '你选择了 3'
    ;;
    4)  echo '你选择了 4'
    ;;
    *)  echo '你没有输入 1 到 4 之间的数字'
    ;;
esac
```

##### continue 和 break

- 同其他语言的用法

## 函数

##### 格式

- 可以带function fun() 定义，也可以直接fun() 定义,不带任何参数
- 如果不加返回值，将以最后一条命令运行结果，作为返回值
- 函数声明必须写在函数使用之前

```
[ function ] funname [()]
{
    action;
    [return int;]
}
```

##### 没有返回值函数

```shell
#!/bin/bash

demoFun(){
    echo "这是我的第一个 shell 函数!"
}
demoFun
```

##### 有返回只的函数

- 函数返回值在调用该函数后通过 $? 来获得
- 如果没有立刻保存返回值, 会被后面的语句覆盖

```shell
#!/bin/bash

funWithReturn(){
    echo "这个函数会对输入的两个数字进行相加运算..."
    echo "输入第一个数字: "
    read aNum
    echo "输入第二个数字: "
    read anotherNum
    echo "两个数字分别为 $aNum 和 $anotherNum !"
    return $(($aNum+$anotherNum))
}
funWithReturn
echo "输入的两个数字之和为 $? !"
```

##### 有参数函数

- 通过 $n 的形式来获取参数的值，例如，$1表示第一个参数，$2表示第二个参数
- 实际传入的参数少也可以正常调用
- $10 不能获取第十个参数，获取第十个参数需要${10}。当n>=10时，需要使用${n}来获取参数
- 可以使用 "处理参数的符号"

```shell
#!/bin/bash

funWithParam(){
    echo "第一个参数为 $1 !"
    echo "第二个参数为 $2 !"
    echo "第十个参数为 $10 !"
    echo "第十个参数为 ${10} !"
    echo "第十一个参数为 ${100} !"
    echo "参数总数有 $# 个!"
    echo "作为一个字符串输出所有参数 $* !"
}
funWithParam 1 2 3 4 5 6 7 8 9 34 73
```

## Shell 输入/输出重定向

##### 格式

| 命令            | 说明                                               |
| --------------- | -------------------------------------------------- |
| command > file  | 将输出重定向到 file。                              |
| command < file  | 将输入重定向到 file。                              |
| command >> file | 将输出以追加的方式重定向到 file。                  |
| n > file        | 将文件描述符为 n 的文件重定向到 file。             |
| n >> file       | 将文件描述符为 n 的文件以追加的方式重定向到 file。 |
| n >& m          | 将输出文件 m 和 n 合并。                           |
| n <& m          | 将输入文件 m 和 n 合并。                           |
| << tag          | 将开始标记 tag 和结束标记 tag 之间的内容作为输入。 |

##### 输入重定向

- 本来需要从键盘获取输入的命令会转移到文件读取内容

```bash
# 查看文件的行数
# 第一个例子，会输出文件名
# 第二个不会，因为它仅仅知道从标准输入读取内容
wc -l a.txt
wc -l < a.txt

# 同时使用
wc -l < a.txt > b.txt
```

##### 重定向

- 一般情况下，每个 Unix/Linux 命令运行时都会打开三个文件：
  - 标准输入文件(stdin)：stdin的文件描述符为0，Unix程序默认从stdin读取数据。
  - 标准输出文件(stdout)：stdout 的文件描述符为1，Unix程序默认向stdout输出数据。
  - 标准错误文件(stderr)：stderr的文件描述符为2，Unix程序会向stderr流中写入错误信息。
- 默认情况下，command > file 将 stdout 重定向到 file，command < file 将stdin 重定向到 file。
- 如果希望 stderr 重定向到 file，可以这样写

```bash
$ command 2>file
```

- 如果希望 stderr 追加到 file 文件末尾，可以这样写

```
$ command 2>>file
```

- 如果希望将 stdout 和 stderr 合并后重定向到 file，可以这样写

```
$ command > file 2>&1
或者
$ command >> file 2>&1
```

- command 命令将 stdin 重定向到 file1，将 stdout 重定向到 file2。 

```
$ command < file1 >file2
```

##### Here Document

```




```

##### /dev/null

- /dev/null 是一个特殊的文件，写入到它的内容都会被丢弃
- 如果尝试从该文件读取内容，那么什么也读不到
- 将命令的输出重定向到它，会起到"禁止输出"的效果
- 如果希望屏蔽 stdout 和 stderr，可以这样写
  -  **2** 和 **>** 之间不可以有空格，**2>** 是一体的时候才表示错误输出

```
$ command > /dev/null 2>&1
```

## 文件引用

shell脚本可以互相引用, 方便封装

##### 格式

```shell
# 注意点号(.)和文件名中间有一空格
. filename   
# 或
source filename
```

- a.sh

```shell
#!/bin/bash

name="小明"
```

- b.sh

```shell
#!/bin/bash

#使用 . 号来引用a.sh 文件
. ./a.sh

# 或者使用以下包含文件代码
# source ./a.sh

echo ${name}
```

