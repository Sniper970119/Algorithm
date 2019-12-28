# -*- coding:utf-8 -*

class Stack():
    def __init__(self):
        self.stack = []
        self.top = -1
        pass

    def push(self, i):
        self.stack.append(i)
        self.top += 1

    def pop(self):
        assert self.top != -1, 'stack empty'
        num = self.stack.pop()
        self.top -= 1
        return num

    def is_empty(self):
        """
        判断是否为空
        :return:
        """
        if self.top == -1:
            return True
        else:
            return False
        pass

    def print(self):
        """
        打印栈
        :return:
        """
        print(self.stack)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.print()
    s.pop()
    s.print()


