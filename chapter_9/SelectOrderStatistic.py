# -*- coding:utf-8 -*-
import random


class SelectOrderStatistic():
    def __init__(self):
        pass

    def quick_sort(self, init_list, i, left, right):
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

    def randomized_select(self, init_list, order_statistic_idx, left, right):
        """
        利用快速排序找出第n个顺序统计量
        :param init_list:
        :param order_statistic_idx:
        :return:
        """
        if len(init_list) == 1:
            return init_list
        random_index = random.randint(left, right)
        init_list, flag_idx = self.quick_sort(init_list, random_index, left, right)
        # 这里进行了剪枝，不需要想快排一样左右均排序，选择一侧的进行排序即可
        if flag_idx == order_statistic_idx:
            return init_list[flag_idx]
        elif flag_idx > order_statistic_idx:
            return self.randomized_select(init_list, order_statistic_idx, left, flag_idx - 1)
        else:
            return self.randomized_select(init_list, order_statistic_idx, flag_idx + 1, right)


if __name__ == '__main__':
    test_list = [2, 4, 1, 9, 8, 7, 6, 3, 5, 0]
    print('result:', SelectOrderStatistic().randomized_select(test_list, 1, 0, 9))
