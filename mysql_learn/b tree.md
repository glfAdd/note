##### 树的存储

- 顺序存储：将数据结构存储在固定的数组中，然在遍历速度上有一定的优势，所占空间比较大。适合满二叉树
- 链式存储：用链表

##### 树的用途

- xml，html等，那么编写这些东西的解析器的时候，不可避免用到树
- 路由协议就是使用了树的算法
- mysql数据库索引
- 文件系统的目录结构
- 很多经典的AI算法其实都是树搜索，此外机器学习中的decision tree也是树结构 

##### B-tree

- 分支节点：除根节点和叶子节点外都是
- 特性
  - 除根结点和叶子结点外，每个节点最多拥有m个子树，至少有m/2个子树
  - 根节点至少有2个子树
  - 所有叶子节点都在同一层、每个节点最多有m-1个key,最少(m/2)-1个，并且以升序排列
  - 另外B树种一个节点中可以存放很多的key
  - 任何一个关键字出现且只出现在一个结点中
  - 搜索有可能在非叶子结点结束

##### 检索过程描述

- 首先从根节点进行二分查找
- 如果找到则返回对应节点的data
- 否则对相应区间的指针指向的节点递归进行查找
- 根据根节点的数据与需要查找的数据进行比较，确认走哪个分支
- 直到找到节点或找到null指针，前者查找成功，后者查找失败

##### 磁盘IO与预读

磁盘读取依靠的是机械运动，分为寻道时间、旋转延迟、传输时间三个部分，这三个部分耗时相加就是一次磁盘IO的时间，大概9ms左右。这个成本是访问内存的十万倍左右；正是由于磁盘IO是非常昂贵的操作，所以计算机操作系统对此做了优化：预读；每一次IO时，不仅仅把当前磁盘地址的数据加载到内存，同时也把相邻数据也加载到内存缓冲区中。因为局部预读原理说明：当访问一个地址数据的时候，与其相邻的数据很快也会被访问到。每次磁盘IO读取的数据我们称之为一页（page）。一页的大小与操作系统有关，一般为4k或者8k。这也就意味着读取一页内数据的时候，实际上发生了一次磁盘IO。

##### B-Tree与二叉查找树的对比

我们知道二叉查找树查询的时间复杂度是O（logN），查找速度最快和比较次数最少，既然性能已经如此优秀，但为什么实现索引是使用B-Tree而不是二叉查找树，关键因素是磁盘IO的次数。数据库索引是存储在磁盘上，当表中的数据量比较大时，索引的大小也跟着增长，达到几个G甚至更多。当我们利用索引进行查询的时候，不可能把索引全部加载到内存中，只能逐一加载每个磁盘页，这里的磁盘页就对应索引树的节点。

##### mysql为什么使用b-tree

- 可以显著减少定位记录时所经历的中间过程，从而加快存取速度。一般用于数据库的索引，查找效率比较高。
- 在一棵树中检查任意一个节点都需要一次磁盘访问，因此B树的设计避免了大量的磁盘访问。减少磁盘IO的次数就必须要压缩树的高度，让瘦高的树尽量变成矮胖的树
- MySQL 是基于磁盘的数据库系统,索引往往以索引文件的形式存储的磁盘上,索引查找过程中就要产生磁盘I/O消耗,相对于内存存取，I/O存取的消耗要高几个数量级,索引的结构组织要尽量减少查找过程中磁盘I/O的存取次数。

# 二叉树

添加元素的思路：广度优先可以用队列实现。用list实现队列，队列左边pop(0)，队列右边添加节点。

二叉树遍历
前序遍历：通俗的说就是从二叉树的根结点出发，当第一次到达结点时就输出结点数据，按照先向左在向右的方向访问
中序遍历：就是从二叉树的根结点出发，当第二次到达结点时就输出结点数据，按照先向左在向右的方向访问。
后序遍历：就是从二叉树的根结点出发，当第三次到达结点时就输出结点数据，按照先向左在向右的方向访问。
层次遍历：按照树的层次自上而下的遍历二叉树

```python
class Node(object):
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)

            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def search(self):
        """广度遍例：一层层遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print cur_node.item
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def search2(self, node):
        """
        先序遍历
        :param node: 跟节点
        :return:
        """
        if node is None:
            return
        print node.item
        self.search2(node.lchild)
        self.search2(node.rchild)

    def search3(self, node):
        """
        中序遍历
        :param node: 跟节点
        :return:
        """
        if node is None:
            return
        self.search3(node.lchild)
        print node.item
        self.search3(node.rchild)

    def search4(self, node):
        """
        后序遍历
        :param node: 跟节点
        :return:
        """
        if node is None:
            return
        self.search4(node.lchild)
        self.search4(node.rchild)
        print node.item


if __name__ == '__main__':
    t = Tree()
    t.add(0)
    t.add(1)
    t.add(2)
    t.add(3)
    t.add(4)
    t.add(5)
    t.add(6)
    t.add(7)
    t.add(8)
    t.add(9)
    t.search()
    t.search2(t.root)
```

##### 根据遍历的结果写出二叉树

- 必须有一个中序才可以。因为根会把左右分开。

