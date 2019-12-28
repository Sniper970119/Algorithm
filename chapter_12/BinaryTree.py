# -*- coding:utf-8 -*-

class BinaryTree():
    def __init__(self, root):
        self.root = root
        pass

    def tree_search(self, root, k):
        """
        二叉树搜索
        :param k:搜索是否有k
        :return:
        """
        if root is None:
            return None
        if root.value == k:
            return root.value
        if k < root.value:
            return self.tree_search(root.left, k)
        else:
            return self.tree_search(root.right, k)

    def tree_max(self):
        """
        搜索最大元素
        :return:
        """
        node = self.root
        while node.right is not None:
            node = node.right
        return node.value

    def tree_min(self):
        """
        搜索最小元素
        :return:
        """
        node = self.root
        while node.left is not None:
            node = node.left
        return node.value

    def tree_insert(self, node, k, pre=None, left=True):
        """
        插入树
        :param node: 根节点
        :param k: 插入值
        :param pre: 当前节点的父节点
        :param left: 是否为向左寻找（判断大小的依据）
        :return:
        """
        # 说明需要新增叶子节点
        if node is None:
            n = Node(k)
            if left:
                pre.left = n
            else:
                pre.right = n
            return
        # 向左比较
        if node.value > k and left:
            self.tree_insert(node.left, k, node, True)
        # 向右比较
        elif node.value < k and not left:
            self.tree_insert(node.right, k, node, False)
        # 插入结点
        else:
            n = Node(k)
            if left:
                pre.left = n
                n.left = node
            else:
                pre.right = n
                n.right = node

    def print_tree(self, node):
        """
        打印树的中序遍历
        :return:
        """
        if node is None:
            return
        self.print_tree(node.left)
        if node is not None:
            print(node.value, end='  ')
        else:
            return
        self.print_tree(node.right)
        pass


class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def getter_value(self):
        return self.value

    def getter_left(self):
        return self.left

    def getter_right(self):
        return self.right

    def setter_value(self, value):
        self.value = value

    def setter_left(self, left):
        self.left = left

    def setter_right(self, right):
        self.right = right


if __name__ == '__main__':
    n11 = Node(9)
    n10 = Node(13, n11)
    n9 = Node(4)
    n8 = Node(2)
    n7 = Node(20)
    n6 = Node(17)
    n5 = Node(7, None, n10)
    n4 = Node(3, n8, n9)
    n3 = Node(18, n6, n7)
    n2 = Node(6, n4, n5)
    root = Node(15, n2, n3)
    b = BinaryTree(root)
    print(b.tree_search(root, 15))
    print(b.print_tree(root))

    print('insert:', b.tree_insert(root, 1))
    print(b.print_tree(root))

    # print(b.tree_max())
    # print(b.tree_min())
    pass
