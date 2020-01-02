# -*- coding:utf-8 -*-

class BellmanFord():
    def __init__(self):
        pass

    def bellman_ford(self, graph):
        """
        bellman_ford算法
        :param graph:
        :return:
        """
        weight = [float('inf') for _ in range(len(graph))]
        weight[0] = 0
        # 向前寻找并修改松弛变量
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                if graph[i][j] != 0:
                    if weight[j] > weight[i] + graph[i][j]:
                        weight[j] = weight[i] + graph[i][j]
        # 再遍历一遍判断是否有负环路（有的话再来一遍代价必然会更低）
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                if graph[i][j] != 0:
                    if weight[j] > weight[i] + graph[i][j]:
                        return False
        return weight


if __name__ == '__main__':
    graph = [[0, 6, 0, 0, 7], [0, 0, 5, -4, 8], [0, -2, 0, 0, 0, -2], [2, 0, 7, 0, 0], [0, 0, -3, 9, 0]]
    bf = BellmanFord()
    print(bf.bellman_ford(graph))
    pass
