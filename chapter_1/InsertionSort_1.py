# -*- coding:utf-8 -*-


class InsertionSort:
    def __init__(self):
        pass

    def sort(self, data):
        """
        插入排序
        :param data:排序列表
        :return:
        """
        print('input data:', data)
        # 排序列表的长度
        input_length = len(data)
        # 遍历数据，可以从1开始，也可以从0，因为只有一个数的状态已经排好序，为了方便输出，这里写0
        for i in range(0, input_length):
            # 设置标记，保存当前排序的数
            key = data[i]
            # 计算需要比较的最大次数（只须向前比较即可，因此为i-1）
            j = i - 1
            # 从后向前遍历列表，直至标记比当前数大为止
            while j >= 0 and data[j] > key:
                # 如果当前数没有标记大，则当前数向后移
                data[j + 1] = data[j]
                # 向前查找遍历
                j -= 1
            # 将查找失败（j为第一个没有标记大的数字，所以标记应该在j+1的位置）
            data[j + 1] = key
            # 输出排序中间步骤，i+1是因为[]区间为左闭右开。
            print('sorting:', data[:i + 1])


if __name__ == '__main__':
    InsertionSort().sort([2, 9, 7, 5, 6, 4, 1])
