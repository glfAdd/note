##### 内置序列类型

- 容器序列:能存放不同类型的数据。存放的是引用
  list、tuple和collections.deque
- 扁平序列:只能容纳一种类型.存放的是值.一段连续的内存空间,只能存放诸如字符、字节和数值这种基础类型.
  str、bytes、bytearray、memoryview、array.array
- 可变序列MutableSequence:
  list、bytearray、array.array、collections.deque、memoryview。
- 不可变序列Sequence
  tuple、str、bytes。

##### 列表推导listcomps和生成器表达式genexps
- 列表推导是构建列表（ list） 的快捷方式， 而生成器表达式则可以用来创建其他任何类型的序列


