##### 如何使用特殊方法

```
特殊方法的存在是为了被Python解释器调用的，自己并不需要调用它们。没有my_object.__len__()这种写法，而应该使用len(my_object)。在执行len(my_object)的时候，如果my_object是一个自定义类的对象，那么Python会自己去调用其中由你实现的__len__方法。

Python内置的类型，比如list、str、bytearray等，那么CPython会抄个近路，__len__实际上会直接返回PyVarObject里的ob_size属性。PyVarObject是表示内存中长度可变的内置对象的C语言结构体。直接读取这个值比调用一个方法要快很多。
```




