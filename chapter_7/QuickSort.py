# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-

import random


class QuickSort():
    def __init__(self):

        pass

    def quick_sort(self, init_list, i):
        """
        快速排序
        :param init_list: 排序列表
        :param i: 比较元素索引
        :return:
        """
        length = len(init_list)
        # 计算左右索引
        left_index = 0
        right_index = length - 1
        # 将比较元素放到最后，防止它是最大值时不进行交换
        temp = init_list[i]
        init_list[i] = init_list[right_index]
        init_list[right_index] = temp
        # 比较元素值
        flag = init_list[right_index]
        # 比较元素索引（因为交换元素位置会变）
        flag_index = right_index
        # 重复执行直至左右标记重叠
        while left_index != right_index:
            # 从左向右找比flag大的数交换
            for i in range(left_index, right_index):
                if flag < init_list[left_index]:
                    temp = flag
                    init_list[flag_index] = init_list[left_index]
                    flag_index = i
                    init_list[left_index] = temp
                    break
                else:
                    left_index += 1
            # 从右向左找比flag小的数交换
            for i in range(right_index, left_index, -1):
                if flag > init_list[right_index]:
                    temp = flag
                    init_list[flag_index] = init_list[right_index]
                    flag_index = i
                    init_list[right_index] = temp
                    break
                else:
                    right_index -= 1
        return init_list, left_index
        pass

    def quick_sort_for_random(self, init_list, i, left, right):
        """
        快速排序
        :param init_list: 排序列表
        :param i: 比较元素索引
        :return:
        """
        length = len(init_list)
        # 计算左右索引
        left_index = left
        right_index = right
        # 将比较元素放到最后，防止它是最大值时不进行交换
        temp = init_list[i]
        init_list[i] = init_list[right_index]
        init_list[right_index] = temp
        # 比较元素值
        flag = init_list[right_index]
        # 比较元素索引（因为交换元素位置会变）
        flag_index = right_index
        # 重复执行直至左右标记重叠
        while left_index != right_index:
            # 从左向右找比flag大的数交换
            for i in range(left_index, right_index):
                if flag < init_list[left_index]:
                    temp = flag
                    init_list[flag_index] = init_list[left_index]
                    flag_index = i
                    init_list[left_index] = temp
                    break
                else:
                    left_index += 1
            # 从右向左找比flag小的数交换
            for i in range(right_index, left_index, -1):
                if flag > init_list[right_index]:
                    temp = flag
                    init_list[flag_index] = init_list[right_index]
                    flag_index = i
                    init_list[right_index] = temp
                    break
                else:
                    right_index -= 1
        return init_list, left_index
        pass

    def random_quick_sort(self, init_list, left, right):

        """
        随机快速排序
        :param init_list:列表
        :return:
        """
        # 如果是单一元素排序，直接返回
        if right == left:
            return init_list
        # 随机初始化一个目标元素
        random_index = random.randint(left, right)
        # 进行排序，获取到排序后的列表以及目标元素现在的索引
        sort_list, sort_flag_index = self.quick_sort_for_random(init_list.copy(), random_index, left, right)
        # 如果当前目标不是最小值，则排序左子树
        if sort_flag_index != left:
            sort_list = self.random_quick_sort(sort_list, left, sort_flag_index - 1)
        # 如果当前目标不是最大值，排序右子树
        if sort_flag_index != right:
            sort_list = self.random_quick_sort(sort_list, sort_flag_index + 1, right)
        return sort_list


if __name__ == '__main__':
    test_list = [2, 8, 7, 1, 3, 5, 6, 4]
    print('init list:', test_list)
    print('sort result:', QuickSort().random_quick_sort(test_list, 0, len(test_list) - 1))

