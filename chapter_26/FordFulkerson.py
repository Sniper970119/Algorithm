# -*- coding:utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt


class FordFulkerson():
    def __init__(self):
        self.inf = float('inf')
        pass

    def ford_fulkerson_method(self, flowGraph, remainGraph, from_node, to_node):
        while nx.has_path(remainGraph, from_node, to_node):
            # 寻找路径p的最小权重
            path = nx.shortest_path(remainGraph, from_node, to_node)
            min_weight = float('inf')
            min_weight_idx = 0
            for i in range(1, len(path)):
                if min_weight > remainGraph[path[i - 1]][path[i]]['weight']:
                    min_weight = remainGraph[path[i - 1]][path[i]]['weight']
                    min_weight_idx = i

            def judge_in_graph(G, from_node, to_node):
                for n, nbrs in G.adjacency():
                    for nbr, eattr in nbrs.items():
                        data = eattr['weight']
                        if n is from_node and nbr is to_node:
                            return True
                return False

            # 所有残存网络路径减（加）去最小值，流网络加（减）上最小值
            for i in range(1, len(path)):
                if judge_in_graph(flowGraph, path[i - 1], path[i]):
                    if remainGraph[path[i - 1]][path[i]]['weight'] - min_weight == 0:
                        remainGraph.remove_edge(path[i - 1], path[i])
                    else:
                        remainGraph[path[i - 1]][path[i]]['weight'] -= min_weight
                    flowGraph[path[i - 1]][path[i]]['weight'] += min_weight
                else:
                    if judge_in_graph(remainGraph, path[i - 1], path[i]):
                        remainGraph[path[i - 1]][path[i]]['weight'] -= min_weight
                    else:
                        remainGraph.add_edge(path[i - 1], path[i], weight=min_weight)
                    flowGraph[path[i - 1]][path[i]]['weight'] -= min_weight

        return flowGraph, remainGraph


if __name__ == '__main__':
    # 流图
    flowGraph = nx.DiGraph()
    flowGraph.add_nodes_from(['s', 'a', 'b', 'c', 'd', 't'])
    flowGraph.add_edges_from(
        [('s', 'a', {'weight': 0}), ('s', 'd', {'weight': 0}), ('a', 'b', {'weight': 0}),
         ('b', 't', {'weight': 0}),
         ('d', 'c', {'weight': 0}), ('c', 'b', {'weight': 0}), ('b', 'd', {'weight': 0}),
         ('c', 't', {'weight': 0}),
         ('d', 'a', {'weight': 0})])

    # 残存网络
    remainGraph = nx.DiGraph()
    remainGraph.add_nodes_from(['s', 'a', 'b', 'c', 'd', 't'])
    # remainGraph.add_edges_from(
    #     [('s', 'a', {'weight': 16}), ('a', 's', {'weight': 0}), ('s', 'd', {'weight': 13}),
    #      ('d', 's', {'weight': 0}),
    #      ('a', 'b', {'weight': 12}), ('b', 'a', {'weight': 0}), ('b', 't', {'weight': 20}),
    #      ('t', 'b', {'weight': 0}),
    #      ('d', 'c', {'weight': 14}), ('c', 'd', {'weight': 0}), ('c', 'b', {'weight': 7}),
    #      ('b', 'c', {'weight': 0}),
    #      ('b', 'd', {'weight': 9}), ('d', 'b', {'weight': 0}), ('c', 't', {'weight': 4}),
    #      ('t', 'c', {'weight': 0}),
    #      ('d', 'a', {'weight': 4}), ('a', 'd', {'weight': 0})])

    remainGraph.add_edges_from(
        [('s', 'a', {'weight': 16}), ('s', 'd', {'weight': 13}),
         ('a', 'b', {'weight': 12}), ('b', 't', {'weight': 20}),
         ('d', 'c', {'weight': 14}), ('c', 'b', {'weight': 7}),
         ('b', 'd', {'weight': 9}), ('c', 't', {'weight': 4}),
         ('d', 'a', {'weight': 4})])

    aaa = nx.shortest_path(flowGraph, 's', 't')
    print(aaa[1])
    print(type(aaa[1]))
    # print(nx.shortest_path(flowGraph, 's', 't'))
    print(flowGraph['s'][aaa[1]]['weight'])
    # remainGraph.add_edge('s', 'e', weight=10)
    print(FordFulkerson().ford_fulkerson_method(flowGraph, remainGraph, 's', 't'))
    # nx.shortest_path()
    # nx.draw(remainGraph)
    # plt.show()
