# -*- coding:utf-8 -*-

class DP():
    def __init__(self):
        self.value = None
        self.cut_loc = None
        pass

    def CUT_OD(self, length, cost):
        """
        钢管切割
        :param length:钢管长度
        :param cost:每个长度的价格（索引即长度）
        :return:
        """
        # 处理钢管长度为0的情况
        if length == 0:
            return 0
        # 初始化结果（最优解）
        q = -1
        for i in range(1, length + 1):
            # 求解最优解
            q = max(q, self.CUT_OD(length - i, cost) + cost[i])
        return q
        pass

    def memoized_CUT_ROD(self, length, cost):
        """
        钢管切割
        :param length:钢管长度
        :param cost:每个长度的价格（索引即长度）
        :return:
        """
        # 初始化切割价格数组，并直接定义长度0获益0（仅第一次初始化）
        if self.value is None:
            self.value = [-1 for _ in range(length + 1)]
            self.value[0] = 0
            self.cut_loc = [-1 for _ in range(length + 1)]
            self.cut_loc[0] = 0
        # 如果计算过当前长度的最优解，直接返回
        if self.value[length] >= 0:
            return self.value[length]
        for i in range(1, length + 1):
            if self.value[length] < self.memoized_CUT_ROD(length - i, cost) + cost[i]:
                self.value[length] = self.memoized_CUT_ROD(length - i, cost) + cost[i]
                self.cut_loc[length] = i
        return self.value[length]

    def bottom_up_CUT_ROD(self, length, cost):
        """
        自底向上
        :param length:
        :param cost:
        :return:
        """
        # 初始化切割价格数组，并直接定义长度0获益0（仅第一次初始化）
        if self.value is None:
            self.value = [-1 for _ in range(length + 1)]
            self.value[0] = 0
            self.cut_loc = [-1 for _ in range(length + 1)]
            self.cut_loc[0] = 0

        for i in range(1, length + 1):
            for j in range(1, i + 1):
                if self.value[length] < self.memoized_CUT_ROD(length - i, cost) + cost[i]:
                    self.value[length] = max(self.value[length], self.bottom_up_CUT_ROD(i - j, cost) + cost[j])
                    self.cut_loc[length] = j
        return self.value[length]

    def matrix_chain_order(self, p):
        """

        :param p:
        :return:
        """
        if self.value is None:
            self.value = [[float('inf') for _ in range(len(p))] for _ in range(len(p))]
            self.cut_loc = [[-1 for _ in range(len(p))] for _ in range(len(p))]

        p_length = len(p)
        # 初始化对角线元素
        for i in range(p_length):
            self.value[i][i] = 0
        # 长度为n的 （先计算两两的括号的、三三括号的。。。）
        for l in range(2, p_length + 1):
            # 寻找length-n+1 个长度为n的排序
            for i in range(0, p_length - l + 1):
                j = i + l - 1
                for k in range(i, j):
                    if self.value[i][j] > self.value[i][k] + self.value[k + 1][j] + p[i][0] * p[k][1] * p[j][1]:
                        self.value[i][j] = self.value[i][k] + self.value[k + 1][j] + p[i][0] * p[k][1] * p[j][1]
                        self.cut_loc[i][j] = k

    def print_optimal_parens(self, i, j):
        """
        打印括号分布
        :param i: from
        :param j: to
        :return:
        """
        if i == j:
            print('A_', i, ' ', end='')
        else:
            print('(', end='')
            self.print_optimal_parens(i, self.cut_loc[i][j])
            self.print_optimal_parens(self.cut_loc[i][j] + 1, j)
            print(')', end='')


if __name__ == '__main__':
    cost = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    dp = DP()
    # 25
    print('length:9   best value:', dp.CUT_OD(9, cost))
    dp.memoized_CUT_ROD(10, cost)
    result = [0, 1, 2, 3, 2, 2, 6, 1, 2, 3, 10]
    print('result:', result)
    print('best value:', dp.value)
    print('best cut_loc:', dp.cut_loc)
    # 重新初始化value
    dp = DP()
    dp.bottom_up_CUT_ROD(10, cost)
    print('best value:', dp.value)
    print('best cut_loc:', dp.cut_loc)

    p = [[30, 35], [35, 15], [15, 5], [5, 10], [10, 20], [20, 25]]
    dp = DP()
    dp.matrix_chain_order(p)
    print('best value:')
    for i in range(len(p)):
        print(dp.value[i])
    print('best cut_loc:')
    for i in range(len(p)):
        print(dp.cut_loc[i])
    dp.print_optimal_parens(0, 5)
    pass
