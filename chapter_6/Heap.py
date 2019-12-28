# -*- coding:utf-8 -*-


class Heap():
    def __init__(self):
        pass

    def max_heapify(self, heap_list, i):
        """
        调整最大堆
        :param heap_list:需要被调整的队列
        :param i: 需要被调整的节点
        :return:
        """
        list_length = len(heap_list)
        # 分别计算左孩子和右孩子索引
        left_point_index = 2 * i
        right_point_index = left_point_index + 1
        # 判断左孩子是否比根节点大，如果大，说明左子树需要调整
        if left_point_index < list_length and heap_list[left_point_index] > heap_list[i]:
            largest = left_point_index
        # 如果左孩子比根节点小，说明左子树为最大堆
        else:
            largest = i
        # 判断右子树是否需要调整
        if right_point_index < list_length and heap_list[right_point_index] > heap_list[largest]:
            largest = right_point_index
        # 如果需要调整，交换两个索引中的数并继续向下调整子树
        if largest != i:
            temp = heap_list[largest]
            heap_list[largest] = heap_list[i]
            heap_list[i] = temp
            self.max_heapify(heap_list, largest)
        return heap_list

    def build_max_heap(self, init_list):
        """
        构建最大堆
        :param init_list: 列表
        :return:
        """
        max_heap = []
        # 这里可以遍历全部数组，也可以只遍历前半,因为满二叉树的性质决定了后一半为叶子节点，可以视为已经排好序
        for i in range(int(len(init_list) / 2), 0, -1):
            max_heap = self.max_heapify(init_list, i)
        return max_heap

    def heap_sort(self, init_list):
        """
        堆排序
        :param init_list: 列表
        :return:
        """
        sort_list = []
        # 进行第一次堆排序
        max_heap = self.build_max_heap(init_list)
        # 将第一次排序的首元素加到排序列表中（下标从1开始）
        # sort_list.append(max_heap[1])
        # 取出第一个数并继续进行堆排序
        for i in range(len(init_list)):
            max_heap = max_heap[1:]
            # 如果堆大小只剩1，输出最后一个元素
            if len(max_heap) == 1:
                sort_list.append(max_heap[0])
                return sort_list
            # 获取新堆，并将根节点添加到排序列表中
            sort_list.append(self.build_max_heap(max_heap)[0])


if __name__ == '__main__':
    test_list = [0, 4, 1, 3, 2, 16, 9, 10, 14, 16, 7]
    print('初始队列：', test_list)
    # print('最大堆：', Heap().build_max_heap(test_list))
    print('排序：', Heap().heap_sort(test_list))
    pass
