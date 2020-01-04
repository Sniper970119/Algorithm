# -*- coding:utf-8 -*-

class Dijsktra():
    def __init__(self):
        pass

    def Dijsktra(self, graph):
        """
        Dijsktra算法(默认从0开始
        :param graph:
        :return:
        """
        weight = []
        # 初始化距离向量（因为调用的时候吧0作为inf了，这里需要处理一下x）
        for i in range(len(graph[0])):
            if graph[0][i] != 0:
                weight.append(graph[0][i])
            else:
                weight.append(float('inf'))
        # 访问列表
        vis = [0 for _ in range(len(graph))]
        vis[0] = 1
        weight[0] = 0
        # 查找最短路
        while sum(vis) != len(graph[0]):
            min_value = float('inf')
            min_index = 0
            # 寻找未被访问过的最小点
            for j in range(len(graph[0])):
                if weight[j] < min_value and vis[j] == 0:
                    min_value = weight[j]
                    min_index = j
            vis[min_index] = 1
            # 更新距离
            for j in range(len(graph[0])):
                if weight[j] > weight[min_index] + graph[min_index][j]:
                    weight[j] = weight[min_index] + graph[min_index][j]
        return weight


if __name__ == '__main__':
    graph = [[0, 10, 0, 0, 5], [0, 0, 1, 0, 2], [0, 0, 0, 4, 0], [7, 0, 6, 0, 0], [0, 3, 9, 2, 0]]
    print(Dijsktra().Dijsktra(graph))
