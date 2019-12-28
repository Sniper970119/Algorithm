# -*- coding:utf-8 -*-

class LinklistMine():
    def __init__(self):
        self.first = Point()
        self.first.prev = self.first
        self.first.next = self.first
        pass

    def list_search(self, k):
        """
        抄找链表中的k元素
        :param k:
        :return:
        """
        p = self.first.next
        while p.value != k:
            if p is not self.first:
                p = p.next
            else:
                return 'Null'
        return k

    def list_insert(self, value):
        """
        插入value
        :param value:
        :return:
        """
        # 设置新节点
        p = Point()
        p.set_value(value=value)
        # 连接到链表中
        point = self.first.prev
        p.prev = point
        point.next = p
        self.first.prev = p
        p.next = self.first
        pass

    def list_delete(self, k):
        """
        删除k
        :param k:
        :return:
        """
        p = self.first.next
        while p.value != k:
            if p is not self.first:
                p = p.next
        # 删除p
        p.prev.next = p.next
        p.next.prev = p.prev
        pass

    def print(self):
        """
        打印
        :return:
        """
        if self.first.next is self.first:
            print('linklist empty')
            return
        print('linklist:', end='')
        point = self.first.next
        while point is not self.first:
            print(point.value, ' ', end='')
            point = point.next
        print()


class Point():
    def __init__(self):
        self.prev = None
        self.value = None
        self.next = None

    def link_prev(self, point):
        """
        连接prev
        :param point:
        :return:
        """
        self.prev = point

    def link_next(self, point):
        """
        连接next
        :param point:
        :return:
        """
        self.next = point

    def set_value(self, value):
        """
        设置值
        :param value:
        :return:
        """
        self.value = value


if __name__ == '__main__':
    l = LinklistMine()
    l.print()
    l.list_insert(4)
    l.list_insert(5)
    l.list_insert(6)
    l.print()
    l.list_delete(5)
    l.print()
    pass
