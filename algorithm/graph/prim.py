import math
import logging as l
l.basicConfig(level=l.INFO)
inf = math.inf


class Edge():
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


class Node():
    def __init__(self, sign):
        self.sign = sign
        self.key = math.inf
        self.precursor = None


class G():
    root=None
    def __init__(self, edges, nodes):
        self.edges = edges
        self.nodes = nodes

    def prim(self, root):
        l.debug(f"{root}")
        l.debug(f"root.key：{root.key}")
        G.root=root
        G.root.key = 0
        A = []
        Q = self.nodes[:]
        while len(Q) > 0:
            u = min(Q, key=lambda node: node.key)
            Q.remove(u)
            A.append(u)
            for edge in self.edges:
                v = edge.start
                if edge.end.sign == u.sign:
                    if v in Q:
                        if edge.weight < v.key:
                            v.precursor = u
                            v.key = edge.weight
        return A

    def print_MST(self, A):
        sum_weight = 0
        for node in A:
            sum_weight += node.key
            if node.precursor==None:
                precursor=G.root.sign
            else:
                precursor=node.precursor.sign
            print(node.sign, "->",precursor )
        print("the smallest weight:", sum_weight)

    # def print_MST(Q):
    #     sum_weight=0
    #     for node in Q:
    #         sum_weight+=node.key
    #     print(sum)


def get_node_instance(sign):
    for node in nodes:
        if node.sign == sign:
            return node

    # throw exception
    return None

# get the edges parameters to instantiate the edge nodes ,put the edges to the list edges;


def generate_edges():
    while(True):
        line = input("input node:")
        if line == "0":
            break
        edge_param = line.split(",")
        start, end, weight = edge_param[0], edge_param[1], int(edge_param[2])
        start_node = get_node_instance(start)
        end_node = get_node_instance(end)
        # print(end_node.sign)
        edges.append(Edge(start_node, end_node, weight))
    return edges


def generate_nodes():
    # get the nodes number(you can custom the number regularity,there use the default simple number system)
    nodes = [Node(str(sign)) for sign in range(1, 8+1)]
    return nodes


'''debug the edges is right: '''


def print_edges():
    for edge in edges:
        # print(edge.start.sign,edge.end.sign,edge.weight)
        l.info((edge.start.sign, edge.end.sign, edge.weight))


nodes = []
nodes = generate_nodes()
edges = []
edges = generate_edges()
G = G(edges, nodes)
# G.print_nodes()
source_node = input("input the source node you want:(from 1~8)\n")
# source_node="A"

source_node = get_node_instance(source_node)
result = G.prim(source_node)
# print_MST(result)
G.print_MST(result)


''' 
1,2,6
2,1,6
1,3,5
3,1,5
2,3,12
3,2,12
3,4,9
4,3,9
3,6,7
6,3,7
6,5,15
5,6,15
6,7,10
7,6,10
1,7,8
7,1,8
1,8,14
8,1,14
7,8,3
8,7,3
0


3,8,5,6,7,9,15
'''
