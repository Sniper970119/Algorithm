# -*- coding:utf-8 -*-

class FolydWarshall():
    def __init__(self):
        pass

    def floyd_warshall(self, graph):
        """
        floyd_warshall算法实现，其中graph就是weight
        :param graph:
        :return:
        """
        inf = float('inf')
        # 初始化path
        path = [[inf for _ in range(len(graph[0]))] for _ in range(len(graph))]
        for i in range(len(path)):
            for j in range(len(path[0])):
                if graph[i][j] != inf and i != j:
                    path[i][j] = i
        for k in range(len(graph)):
            for i in range(len(graph)):
                for j in range(len(graph[0])):
                    if graph[i][j] > graph[i][k] + graph[k][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]
                        path[i][j] = k
        return graph, path
        pass


if __name__ == '__main__':
    inf = float('inf')
    graph = [[0, 3, 8, inf, -4], [inf, 0, inf, 1, 7], [inf, 4, 0, inf, inf],
             [2, inf, -5, 0, inf], [inf, inf, inf, 6, 0]]
    fw = FolydWarshall()
    graph, path = fw.floyd_warshall(graph)
    print(graph)
    print(path)
    import numpy
    graph1 = numpy.array(graph)
    path12 = numpy.array(path)
    pass
