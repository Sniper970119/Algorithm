# -*- coding:utf-8 -*-

class GraphAlgorithm():
    def __init__(self):
        pass

    def bfs(self, graph, init_idx, flag=None):
        """
        广度优先遍历
        :param graph:
        :return:
        """
        result = []
        # 第一次运行的数据初始化
        if flag is None:
            flag = [0 for _ in range(len(graph))]
            flag[init_idx - 1] = 1
            result = [init_idx]
        temp_list = []
        for j in range(len(flag)):
            if graph[init_idx - 1][j] == 1 and flag[j] == 0:
                result.append(j + 1)
                temp_list.append(j)
                flag[j] = 1
        # 递归广搜
        for i in range(len(temp_list)):
            result.extend(self.bfs(graph, temp_list[i] + 1, flag))
        return result

    def dfs(self, graph, init_idx, flag=None):
        """
        深度优先遍历
        :param graph:
        :param init_idx:
        :param flag:
        :return:
        """
        result = [init_idx]
        if flag is None:
            flag = [0 for _ in range(len(graph))]
        for i in range(len(graph)):
            if graph[init_idx - 1][i] == 1 and flag[i] == 0:
                flag[i] = 1
                result.extend(self.dfs(graph, i + 1, flag))
        return result


if __name__ == '__main__':
    graph = [[0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 1]]
    g = GraphAlgorithm()
    # print(g.bfs(graph, 1))
    print(g.dfs(graph, 1))

# 1 2 5 4
