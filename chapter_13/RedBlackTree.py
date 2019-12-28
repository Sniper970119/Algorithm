# -*- coding:utf-8 -*-

class RedBlackTree():
    def __init__(self, root):
        self.root = root
        pass

    def left_rotate(self, node, pre):
        """
        左旋(node的左节点旋转到node当前位置
        :param node:
        :param pre:
        :return:
        """
        print('left rote')
        next = node.right
        # 如果交换的点是父节点的左孩子
        if pre.left == node:
            pre.left = next
            if next.key is not None:
                next.pre = pre

            node.right = pre
            pre.pre = node
        # 如果交换的点是父节点的右孩子
        if pre.right == node:
            pre.right = next
            if next.key is not None:
                next.pre = pre

            node.left = pre
            pre.pre = node
        self.root = node
        return

    def right_rotate(self, node, pre):
        """
        右旋(node的右节点旋转到node当前位置
        :param node:
        :param pre:
        :return:
        """
        print('right rote')
        next = node.right
        # 如果交换的点是父节点的左孩子
        if pre.left == node:
            pre.left = next
            if next.key is not None:
                next.pre = pre

            node.right = pre
            pre.pre = node
            # next.right = node
        # 如果交换的点是父节点的右孩子
        if pre.right == node:
            pre.right = next
            if next.key is not None:
                next.pre = pre

            node.left = pre
            pre.pre = node
        self.root = node
        return

    def rb_insert(self, node, k, pre=None, left=True):
        """
        插入树
        :param node: 根节点
        :param k: 插入值
        :param pre: 当前节点的父节点
        :param left: 是否为向左寻找（判断大小的依据）
        :return:
        """
        # 说明需要新增叶子节点
        if node.left.key == None and node.right.key == None:
            print('add to leave', k)
            n = Node(k, 'red', self.root.pre, self.root.pre)
            if node.key > k:
                if node.pre.key is not None:
                    pre.right = n
                    n.pre = pre

                    n.right = node
                    node.left = node.right = self.root.pre
                else:
                    node.left = n
                    n.pre = node
            else:

                if node.pre.key is not None:
                    pre.left = n
                    n.pre = pre

                    n.left = node
                    node.left = node.right = self.root.pre
                else:
                    node.right = n
                    n.pre = node

            self.rb_fixup(n)
            return
        if node.left.key == None:
            if node.key > k:
                self.rb_insert(node.right, k, node)
            else:
                n = Node(k, 'red')
                n.right = pre.right

                n.pre = pre
                n.right.pre = n
            return
        if node.right.key == None:
            if node.key > k:
                self.rb_insert(node.left, k, node)
            else:
                n = Node(k, 'red', self.root.pre, self.root.pre)

                pre.left = n
                n.pre = pre

                n.left = node
                node.left = node.right = self.root.pre

            return

        # 向左比较
        if node.key > k and left:
            self.rb_insert(node.left, k, node)
        # 向右比较
        elif node.key < k:
            self.rb_insert(node.right, k, node)
        # 插入结点
        else:
            n = Node(k, 'red')
            if left:
                pre.left = n
                n.pre = pre

                n.left = node
                node.pre = n

                n.right = node.right
                node.right.pre = n

                node.right = self.root.pre
            else:
                pre.right = n
                n.pre = pre

                n.right = node
                node.pre = n

                n.left = node.left
                node.left.pre = n

                node.left = self.root.pre

            self.rb_fixup(n)

    def rb_fixup(self, node):
        """
        整理格式与重绘
        :return:
        """
        while node.pre.color == 'red':
            if node.pre == node.pre.pre.left:
                y = node.pre.pre.right
                if y.color == 'red':
                    node.pre.color = 'black'
                    y.color = 'black'
                    node.pre.pre.color = 'red'
                elif node == node.pre.right:
                    node = node.pre
                    self.left_rotate(node.pre, node.pre.pre)
                node.pre.color = 'black'
                node.pre.pre.color = 'red'
                self.right_rotate(node.pre, node.pre.pre)
            else:
                y = node.pre.pre.left
                if y.color == 'red':
                    node.pre.color = 'black'
                    y.color = 'black'
                    node.pre.pre.color = 'red'
                elif node == node.pre.left:
                    node = node.pre
                    self.right_rotate(node.pre, node.pre.pre)
                node.pre.color = 'black'
                node.pre.pre.color = 'red'
                self.left_rotate(node.pre, node.pre.pre)
        self.root.color = 'black'
        pass

    def print_inorder_tree(self, node):
        """
        打印树的中序遍历
        :return:
        """
        if node.key is None:
            return
        self.print_inorder_tree(node.left)
        if node is not None:
            if node.color is 'red':
                color = 'r'
            else:
                color = 'b'
            print(node.key, '<', color, '>', end='  ')
        else:
            return
        self.print_inorder_tree(node.right)

    def print_preorder_tree(self, node):
        """
        打印树的中序遍历
        :return:
        """
        if node.key is None:
            return
        if node is not None:
            if node.color is 'red':
                color = 'r'
            else:
                color = 'b'
            print(node.key, '<', color, '>', end='  ')
        else:
            return
        self.print_preorder_tree(node.left)
        self.print_preorder_tree(node.right)

        pass


class Node():
    def __init__(self, key, color='black', left=None, right=None, pre=None):
        assert color in ['red', 'black'], 'error color'
        self.color = color
        self.left = left
        self.right = right
        self.key = key
        self.pre = pre

    def setter_color(self, color):
        assert color in ['red', 'black'], 'error color'
        self.color = color

    def getter_color(self):
        return self.color


if __name__ == '__main__':
    """
    # n15 = Node(None, 'black')
    # n14 = Node(20, 'black', n15, n15)
    # n13 = Node(22, 'black', n14, n15)
    # n12 = Node(17, 'black', n15, n15)
    # n11 = Node(12, 'black', n15, n15)
    # n9 = Node(14, 'black', n11, n12)
    # n10 = Node(19, 'black', n9, n13)
    # n8 = Node(2, 'black', n15, n15)
    # # n7 = Node(18, 'black', n9, n10)
    # n6 = Node(9, 'black', n15, n15)
    # n5 = Node(6, 'black', n15, n15)
    # n4 = Node(3, 'black', n8, n15)
    # n3 = Node(11, 'black', n6, n10)
    # n2 = Node(4, 'black', n4, n5)
    # n1 = Node(7, 'black', n2, n3)
    # n1.pre = n15
    # n2.pre = n1
    # n3.pre = n1
    # n4.pre = n2
    # n5.pre = n2
    # n6.pre = n3
    # # n7.pre = n3
    # n8.pre = n4
    # n9.pre = n10
    # # n9.pre = n7
    # n10.pre = n3
    # # n10.pre = n7
    # n11.pre = n9
    # n12.pre = n9
    # n13.pre = n10
    # n14.pre = n13
    # n15.pre = n1

    # rbt = RedBlackTree(n1)
    # rbt.print_preorder_tree(n1)
    # print()
    # rbt.print_inorder_tree(n1)
    # print()
    #
    # rbt.rb_insert(n1, 13)
    #
    # rbt.print_preorder_tree(n1)
    # print()
    # rbt.print_inorder_tree(n1)
    # print()
    """

    n15 = Node(None, 'black')
    n1 = Node(12, 'black', n15, n15, n15)
    n15.pre = n1
    rbt = RedBlackTree(n1)
    rbt.print_preorder_tree(n1)
    print()
    rbt.print_inorder_tree(n1)
    print()

    rbt.rb_insert(rbt.root, 1)
    rbt.rb_insert(rbt.root, 9)
    rbt.rb_insert(rbt.root, 2)
    rbt.rb_insert(rbt.root, 0)

    rbt.print_preorder_tree(rbt.root)
    print()
    rbt.print_inorder_tree(rbt.root)
    print()
    # n6 = Node(None)
    # n4 = Node(3, 'red', n6, n6)
    # n3 = Node(11, 'red', n6, n6)
    # n2 = Node(4, 'red', n4, n6)
    # n1 = Node(7, 'red', n2, n3, n6)
    # n6.pre = n1
    # rbt = RedBlackTree(n1)
    # rbt.print_preorder_tree(n6.pre)
    # print()
    # rbt.print_inorder_tree(n6.pre)
    # print()
    # print()
    #
    # rbt.right_rotate(n2, n1)
    # rbt.root = n2
    #
    # rbt.print_preorder_tree(rbt.root)
    # print()
    # rbt.print_inorder_tree(rbt.root)
    # print()

    pass
