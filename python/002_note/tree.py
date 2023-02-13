# coding=utf-8
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
            print(cur_node.item)
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
        print(node.item)
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
        print(node.item)
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
        print(node.item)


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
