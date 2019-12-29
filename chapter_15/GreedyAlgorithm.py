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

    def greedy_choose(self, S, i, j):
        """
        贪心算法解决活动问题
        :param S:
        :param i:
        :param j:
        :return:
        """
        # 返回点集合
        return_list = []

        def choose_one(i):
            """
            选择一个i时间点之后开始，并且持续时间最短的活动
            :param i:
            :return:
            """
            min_end_time = float('inf')
            return_one = None
            for each in S:
                if each[1] >= i and each[2] < min_end_time:
                    min_end_time = each[2]
                    return_one = each
            return return_one

        x = i
        while x <= j:
            one = choose_one(x)
            if one is None:
                return return_list
            return_list.append(one)
            x = one[2]


if __name__ == '__main__':
    S = [[1, 1, 4], [2, 3, 5], [3, 0, 6], [4, 5, 7], [5, 3, 9], [6, 5, 9], [7, 6, 10], [8, 8, 11], [9, 8, 12],
         [10, 2, 14], [11, 12, 16]]
    g = GreedyAlgorithm()
    print(g.choose_best_activity_with_dp(S, 0, 16))
    print(g.greedy_choose(S, 0, 16))
