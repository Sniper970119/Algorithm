# -*- coding:utf-8 -*-


class FIndMaxSubarray:
    def __init__(self, init_array):
        self.init_array = init_array
        pass

    def find(self, start, end):
        """
        递归寻找最大子数组
        :return:
        """
        # 递归结束标记
        if start == end:
            return [self.init_array[start]], self.init_array[start]
        mid = int((start + end) / 2)
        # 分别处理左、右、以及跨越重点的情况
        left_subarray, left_sum = self.find(start, mid)
        right_subarray, right_sum = self.find(mid + 1, end)
        cross_subarray, cross_sum = self.find_max_crossing_subarray(target_array=self.init_array[start:end+1])
        # 比较三种结果大小并返回
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_subarray, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_subarray, right_sum
        else:
            return cross_subarray, cross_sum

    def find_max_crossing_subarray(self, target_array):
        """
        寻找当前列表以中点为基准的最大子列表
        :param target_array:
        :return:
        """
        # 左最大子数组
        left_max_sub_array = []
        # 右最大子数组
        right_max_sub_array = []
        # 中间索引
        mid_index = int(len(target_array) / 2)
        # 最大子数组
        max_subarray = []
        # 中间值
        mid_number = target_array[mid_index]
        # 临时存储的最大值
        _sum = 0
        # 临时存储的索引值
        _index = 0
        # 用于存放临时和的变量
        temp_sum = 0
        # 对左侧数字查找最大子数组
        for i in range(mid_index, 0, -1):
            # 计算临时和
            temp_sum = temp_sum + target_array[i]
            # 判断该位取舍
            if temp_sum > _sum:
                _sum = temp_sum
                _index = i
        # 截取数组
        left_max_sub_array = target_array[_index:mid_index]
        # 数据初始化
        _sum = 0
        _index = 0
        temp_sum = 0
        # 对右侧数字查找最大子数组
        for i in range(mid_index, len(target_array)):
            temp_sum = temp_sum + target_array[i]
            if temp_sum > _sum:
                _sum = temp_sum
                _index = i
        # 截取数组
        right_max_sub_array = target_array[mid_index:_index + 1]
        # 合并数组
        max_subarray = left_max_sub_array + right_max_sub_array
        # 求和
        max_subarray_sum = sum(max_subarray)
        return max_subarray, max_subarray_sum


if __name__ == '__main__':
    init_array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    max_sum, max_array = FIndMaxSubarray(init_array).find(0, len(init_array) - 1)
    print(init_array)
    print(max_array, '\t', max_sum)
    pass
