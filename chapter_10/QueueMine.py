# -*- coding:utf-8 -*-

class Queue():
    def __init__(self):
        self.queue = [0 for _ in range(10)]
        self.head = 0
        self.tail = -1
        pass

    def enqueue(self, i):
        """
        入队
        :param i:
        :return:
        """
        self.tail += 1
        self.queue[self.tail] = i

    def dequeue(self):
        """
        出队
        :return:
        """
        self.head += 1
        return self.queue[self.head - 1]

    def is_empty(self):
        """
        判断空
        :return:
        """
        if self.head == self.tail + 1:
            return True
        else:
            return False

if __name__ == '__main__':
    pass