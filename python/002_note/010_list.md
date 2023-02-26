##### list 引用

<img src="./image/list 引用1.webp" alt="list 引用1" style="zoom:80%;" />

<img src=".\image\list 引用2.webp" alt="list 引用2" style="zoom:80%;" />

```
list 是 Python 对象, 对象实体就是在堆内存中
list 是容器对象, 存储的是元素实体的引用, 而非元素实体本身
修改某个元素本质是修改指向元素的引用, CPython 在堆内存中创建了一个新的对象分配新的内存空间, 元素保存的地址指向新的元素
list 类型对象的在其元素修改前后,变量 L 始终引用同一个lsit对象
```


