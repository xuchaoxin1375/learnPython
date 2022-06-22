
""" 输入连通图的顶点的编号(顶点数书可以计算,也可以直接给出)和边(边数可以统计,也可以直接给出): 
输出最小生成树所包含的各条边(用边上的两个顶点来表示)

输入连通网的边数：(可选)
6 10

输入连通网的顶点：(如果没有特殊要求,可以根据输入的点数直接默认是从1开始为顶点编号)
1
2
3
4
5
6
输入各边的起始点和终点及权重：(边上的顶点和之前的编号体系必须相对应,输入0结束边的录入)
1,2,6
1,3,1
1,4,5
2,3,5
2,5,3
3,4,5
3,5,6
3,6,4
4,6,2
5,6,6
0

"""
class Edge():
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


class Node():
    def __init__(self, number, sign):
        self.number = number
        self.sign = sign

    # def set_sign(self, new_sign):
    #     self.sign = new_sign

# get the nodes number(you can custom the number regularity,there use the default simple number system)
nodes = [Node(i, i) for i in range(1, 7)]
# get the edges parameters to instantiate the edge nodes ,put the edges to the list edges;
edges = []
while(True):
    line = input("input node:")
    if line == "0":
        break
    edge_param = line.split(",")
    start, end, weight = int(edge_param[0]), int(
        edge_param[1]), int(edge_param[2])
    edges.append(Edge(start, end, weight))

#test: print(edges,node_numbers)
# the number of the edges we need is the number_of_nodes-1:
number_of_nodes = len(nodes)
# sort the edges' weights
edges.sort(key=lambda edge: edge.weight)
#test: print([ edge.weight for edge in edges])
# count:count and judge whether we have complete the MST(Minimum Spanning Tree)
count = 0
# save the edges whice will be the edge of the MST
result_edges = []
# select number_of_edges-1 edges to consist of the optimal solution
for edge in edges:
    sign_start = nodes[edge.start-1].sign
    sign_end = nodes[edge.end-1].sign
    # the core code:judge the cricuit:
    # by overlay the start node sign with the end node sign
    # print(edge.end)
    if sign_start != sign_end:
        result_edges.append(edge)
        # traverse the all nodes:
        for node in nodes:
            # node there:
            if node.sign == sign_end:
                node.sign = sign_start
        count += 1
        if count == number_of_nodes-1:
            break
    else:
        pass
# print(result_edges)
print("the edges consist of the MST by Kruskal method:")
for edge in result_edges:
    edge_tuple = edge.start, edge.end
    print(edge_tuple, "weight:", edge.weight)
