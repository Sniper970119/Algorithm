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

    def shop_with_dp(self, value, bag_size):
        """
        0-1背包
        :param value:
        :param bag_size:
        :return:
        """
        result = [[0 for _ in range(bag_size + 1)] for _ in range(len(value[0]))]

        for i in range(0, len(value[0])):
            for j in range(0, bag_size + 1):
                if value[i][1] <= j:
                    if result[i][j] < result[i - 1][j - value[i][1]] + value[i][2]:
                        result[i][j] = result[i - 1][j - value[i][1]] + value[i][2]
                else:
                    result[i][j] = result[i - 1][j]
        return result[-1][-1]

    def shop_with_greedy_algorithm(self, value, bag_size):
        """
        分数背包问题
        :param value:
        :param bag_size:
        :return:
        """
        each_value = [0 for _ in range(len(value))]
        total_value = 0
        # 计算商品均价
        for i in range(len(each_value)):
            each_value[i] = value[i][2] / value[i][1]
        # 循环装满背包
        while bag_size > 0:
            most_valued_idx = each_value.index(max(each_value))
            if value[most_valued_idx][1] < bag_size:
                # 对应背包能装满商品的情况
                bag_size -= value[most_valued_idx][1]
                total_value += each_value[most_valued_idx] * value[most_valued_idx][1]
                each_value.remove(each_value[most_valued_idx])
                value.remove(value[most_valued_idx])
            else:
                # 对应背包不能装全部商品的情况
                total_value += bag_size * each_value[most_valued_idx]
                bag_size = 0
            pass
        return total_value

    def huffman_code(self, data):
        """
        生成哈夫曼编码
        :param data:
        :return:
        """
        huffman_tree = self.build_huffman_tree(data)
        pass

    def build_huffman_tree(self, data):
        """
        构造哈弗曼树
        :param data:
        :return:
        """
        huffman_str = []
        huffman_tree = []

        def find_min():
            """
            寻找最小的两个点
            :return:
            """
            if len(data) == 1:
                return data[0], None
            min_data = float('inf')
            # 最小点
            most_min = data[0]
            # 次小点
            secd_min = data[0]
            # 遍历寻找最小点
            for each in data:
                if each[1] < min_data:
                    most_min = each
                    min_data = each[1]
            data.remove(most_min)
            min_data = float('inf')
            # 遍历寻找最小点
            for each in data:
                if each[1] < min_data:
                    secd_min = each
                    min_data = each[1]
            data.remove(secd_min)
            # 将这两个点的根加回去
            data.append(['*', most_min[1] + secd_min[1]])

            return most_min, secd_min

        def connect_tree():
            """
            连接树
            :return:
            """
            # 最小点
            most_min = huffman_str[-1]
            # 次小点
            secd_min = huffman_str[-2]

            flag = most_min[1] + secd_min[1]
            root_idx = 0
            # 遍历寻找最小两个点的根
            for i in range(len(huffman_str) - 1, -1, -1):
                if huffman_str[i][1] == flag:
                    root_idx = i
                    break
                pass
            # 连接左右子树
            huffman_tree[root_idx].left = huffman_tree[-1]
            huffman_tree[root_idx].right = huffman_tree[-2]
            # 移除这两个点
            huffman_str.remove(most_min)
            huffman_str.remove(secd_min)
            huffman_tree.remove(huffman_tree[-1])
            huffman_tree.remove(huffman_tree[-1])
            pass

        # 构造哈夫曼字符串（因为没办法连成树，先计算哈夫曼树的列表表示）
        for i in range(len(data)):
            most_min, secd_min = find_min()
            if secd_min is None:
                huffman_str.insert(0, most_min)
                continue
            huffman_str.insert(0, most_min)
            huffman_str.insert(0, secd_min)
            pass
        # 利用已知的哈夫曼顺序构造哈弗曼树
        for each in huffman_str:
            huffman_tree.append(tree(each[1], None, None, None))
        for i in range(int(len(huffman_str) / 2)):
            connect_tree()


class tree():
    def __init__(self, value, left, right, root):
        self.value = value
        self.left = left
        self.right = right
        self.root = root


if __name__ == '__main__':
    S = [[1, 1, 4], [2, 3, 5], [3, 0, 6], [4, 5, 7], [5, 3, 9], [6, 5, 9], [7, 6, 10], [8, 8, 11], [9, 8, 12],
         [10, 2, 14], [11, 12, 16]]
    g = GreedyAlgorithm()
    # print(g.choose_best_activity_with_dp(S, 0, 16))
    # print(g.greedy_choose(S, 0, 16))
    value = [[1, 10, 60], [2, 20, 100], [3, 30, 120]]
    # print(g.shop_with_greedy_algorithm(value, 50))
    # print(g.shop_with_dp(value, 50))
    data = [['f', 5], ['e', 9], ['c', 12], ['b', 13], ['d', 16], ['a', 45]]
    g.huffman_code(data)
