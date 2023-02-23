##### 参考

```
好
    https://www.zhihu.com/column/c_1273568922378719232
    https://www.zhihu.com/column/c_1272122576572284928

https://blog.csdn.net/zhzhl202/article/details/7547445
https://www.zhihu.com/question/30560008
https://www.cnblogs.com/fasionchan/p/python-memory-pool.html
```



# 堆栈

<img src=".\image\CPython内存堆栈.webp" alt="CPython内存堆栈" style="zoom:100%;" />

```
堆: 存储 CPython 运行时的所有对象实体
栈: 存储堆中对象实体的引用


例如
a = 'Hello Word'
'Hello Word' 是字符串对象 PyASCIIObject
CPython 会将对象实体存储到堆内存中, 
对象实体的内存地址压栈存储, 而不是将 'Hello Word' 这个字符串值压入栈, 地址赋值给变量 a


Python 任何对象都由 CPython 的 C 底层由一个叫 struct PyObject 结构体所封装. 这个结构体在 CPython 运行时存储在堆内中
```

##### 可变对象 / 不可变对象

```
可变对象: list, dict, 其内部元素可修改, 修改的是引用
不可变对象: 基本数据类型 int, float, str, byte 
```

##### list 引用

<img src=".\image\list 引用1.webp" alt="list 引用1" style="zoom:80%;" />

<img src=".\image\list 引用2.webp" alt="list 引用2" style="zoom:80%;" />

```
list 是 Python 对象, 对象实体就是在堆内存中
list 是容器对象, 存储的是元素实体的引用, 而非元素实体本身
修改某个元素本质是修改指向元素的引用, CPython 在堆内存中创建了一个新的对象分配新的内存空间, 元素保存的地址指向新的元素
list 类型对象的在其元素修改前后,变量 L 始终引用同一个lsit对象
```





# 内存池

- malloc: 计算机内存由操作系统管理, 应用程序通过"系统调用"向操作系统申请内存, C 库函数将"系统调用"封装成内存分配器, 提供可调用的 malloc 函数
- 内存池的内存到最后还是会回收到内存池, 不会调用 C 的 free 释放掉, 以便下次使用

## CPython 内存结构

<img src=".\image\CPython内存架构.webp" alt="CPython内存架构" style="zoom:100%;" />

<img src=".\image\CPython内存架构2.svg" alt="CPython内存架构2" style="zoom:50%;" />

![CPython内存架构3](.\image\CPython内存架构3.webp)

```
python 管理的是 0, 1, 2, 3 层

python 的内存分为大内存和小内存, 以256字节为界限
    小内存的对象, 使用内存池进行分配, 不调用 free 函数释放内存, 下次继续使用
    大内存的对象, 使用 malloc 函数分配内存, free 函数释放内存
```

- 第 3 层

```
对象缓冲池
python 内置基本类型（int, dict等）都有独立的私有内存池, 对象之间的内存池不共享, 即int释放的内存, 不会被分配给float使用
```

- 第 2 层

```
内存池
小内存使用内存池进行分配
当申请的内存小于256KB时, 内存分配主要由 Python 对象分配器实施
是 Python 对象分配器, Python 对象分配/释放内存(例如:PyObject_New / Del）都会调用它
```

- 第 1 层

```
大内存使用malloc进行分配
当申请的内存大于256KB时, 由 Python 原生的内存分配器进行分配, 本质上是调用 C 标准库中的 malloc/realloc 等函数
是 PyMem 内存分配函数, 它确保 CPython 运行时, 堆中有足够可用的堆内存，如果没有，它会向下一层请求更多的内存.
```

- 第 0 层

```
C 库中的 malloc, free 等函数直接和操作系统的虚拟内存管理器交互, 分配和释放内存
并且接受来自上一层 PyMem 内存分配函数的内存空间请求, 以及将系统分配的内存空间返回给上一层 PyMem
```

- 第 -1 层

```
虚拟内存管理原理
基于页表的虚拟内存管理器，以页 ( page )为单位管理内存，CPU 内存管理单元( MMU )在这个过程中发挥重要作用
```

- 第 -2 层

```
操作系统进行操作
底层存储设备, 直接管理物理内存以及磁盘等二级存储设备
```

## 内存管理架构

![L1内存管理](.\image\L1内存管理.webp)

```
PyMem_* 位于 CPython 内存模型第1层
_PyObject_* 函数族衔接第1层和第2层的
```

```c
typedef struct {
    // 用户上下文作为第一个参数
    void *ctx;
    // 分配一块内存
    void* (*malloc) (void *ctx, size_t size);
    // 分配以零初始化的内存块
    void* (*calloc) (void *ctx, size_t nelem, size_t elsize);
    // 分配或调整内存块大小
    void* (*realloc) (void *ctx, void *ptr, size_t new_size);
    // 释放内存块
    void (*free) (void *ctx, void *ptr);
} PyMemAllocatorEx;


static PyMemAllocatorEx _PyMem_Raw = {
    NULL,
    _PyMem_RawMalloc,
    _PyMem_RawCalloc,
    _PyMem_RawRealloc,
    _PyMem_RawFree
};
```

## L1 和 L2 交互

##### 大对象和小对象

![L1和L2交互](.\image\L1和L2交互.webp)

```
大对象:
1. 大于512字节的 Python 对象
2. Arenas 对象 256KB 就是 CPython 的大对象, 此时给 Arenas 大对象的内存分配, CPython 会调用第 0 层 C 库的 malloc 分配器为其分配内存(PyMem_RawMalloc 或 PyMem_RawRealloc)
因此 C 底层的 malloc 分配器是仅供给 arenas 对象使用的


小对象:
1. 小于等于 512 字节的 Python 对象
2. 小型对象的内存请求按该对象的类型尺寸分组, 这些分组按 8 个字节对齐, 由于返回的地址必须有效对齐。这些类型尺寸的对象的内存请求由4KB的内存池提供内存分配，当然前提是该内存池有闲置的块。
```



## 内存池

##### 作用

```
1. 避免频繁地申请、释放内存空间(malloc 与 free)导致性能降低;
2. 避免频繁分配与释放小块的内存会产生内存碎片导致降低内存利用效率	
```

##### 堆内存模型

![堆内存模型](.\image\堆内存模型.webp)

```
arenas 对象:
1. 每个 Arenas 固定大小为256KB
2. 每个 Arenas 对象包装包含64个内存池
3. 对象头部用两个 struct area_object 类型的指针在堆中构成 Arenas 对象的双重链表


pool (内存池):
1. 每个 pool 固定大小为 4KB (内存分页的大小)
2. 每个 pool 包含尺寸相同的 block
3. pool 头部用两个 struct pool_heade r类型的指针构成 pool 对象的双重链表


block (块)
1. block 是最小的内存单元, 基本单位是 8bytes
2. 用 8 字节对齐的方式确定块的尺寸, 大小为 8 的整数倍
	如果想申请 27B 的内存, 会分配一个 32B 的 block
	尺寸 25~32 字节这个区间的任意 Python 对象, block 都是 32 字节
```

##### block (块)

<font color='red'>CPython 3.6 是基于 8 字节的内存对齐</font>
<font color='red'>CPython 3.7 后基于 16 字节对齐</font>

```
 * Request in bytes     Size of allocated block      Size class idx
 * ----------------------------------------------------------------
 *        1-8                     8                       0
 *        9-16                   16                       1
 *       17-24                   24                       2
 *       25-32                   32                       3
 *       33-40                   40                       4
 *       41-48                   48                       5
 *       49-56                   56                       6
 *       57-64                   64                       7
 *       65-72                   72                       8
 *        ...                   ...                     ...
 *      497-504                 504                      62
 *      505-512                 512                      63
```

##### pool (池)

```c
struct pool_header {
    union { block *_padding;
            uint count; } ref;          // 已分配内存块的数量
    block *freeblock;                   // 标识下一次分配block的起始位置
    struct pool_header *nextpool;       // 指向下一个内存池
    struct pool_header *prevpool;       // 指向上一个内存池
    uint arenaindex;                    // 当前 pool 所属的 arena 的索引
    uint szidx;                         /* block size class index        */
    uint nextoffset;                    // freeblock 的下一次偏移的位置
    uint maxnextoffset;                 // 当前 pool 最后一个 block 的偏移, 当 nextoffset 大于 maxnextoffset 时就没有可分配的 block 了
};

typedef struct pool_header *poolp;
```





### 小对象内存管理

```
Python的内存池又分为4个层次：Block、Pool、Arean、usedpool
```



### 对象缓冲池



内存碎片



### 