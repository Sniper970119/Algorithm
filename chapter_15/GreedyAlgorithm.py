# -*- coding:utf-8 -*-

class GreedyAlgorithm():
    def __init__(self):
        pass

    def choose_best_activity_with_dp(self, S, i, j):
        """
        使用动态规划计算最佳活动选择
        :param S: 活动列表
        :param i: 起始时间
        :param j: 终止时间
        :return:
        """
        # 用来保存需要在哪个点分割
        value = [0 for _ in range(j - i + 1)]
        # 用来保存从i到j最多有几个活动
        count = [[0 for _ in range(j - i + 1)] for _ in range(j - i + 1)]
        # 初始化，每个活动的起始终止时间置为1
        for each in S:
            count[each[1]][each[2]] = 1
        # dp
        for x in range(1, len(value)):
            for y in range(x):  # 这个相当于上面说的k
                if count[i][y] + count[y][x] > count[i][x]:
                    count[i][x] = count[i][y] + count[y][x]
                    value[x] = y
        return value


if __name__ == '__main__':
    S = [[1, 1, 4], [2, 3, 5], [3, 0, 6], [4, 5, 7], [5, 3, 9], [6, 5, 9], [7, 6, 10], [8, 8, 10], [9, 8, 12],
         [10, 2, 14], [11, 12, 16]]
    g = GreedyAlgorithm()
    print(g.choose_best_activity_with_dp(S, 0, 16))

