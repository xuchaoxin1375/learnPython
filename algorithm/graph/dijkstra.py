import logging as l
import math

inf = math.inf

l.basicConfig(level=l.INFO)


class Edge():
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


class Node():
    def __init__(self, sign):
        # self.number = number
        self.sign = sign
        # for initial nodes(vertex) of the graph
        self.distance = math.inf
        # set the node's precursor:
        self.precursor = None

    def initialize_source_node(self):
        self.distance = 0
        return self


class G():
    # the source node :
    s_node = None

    def __init__(self, edges, nodes):
        self.edges = edges
        self.nodes = nodes

    # def generate_nodes(self):
    #     # get the nodes number(you can custom the number regularity,there use the default simple number system)
    #     self.nodes = [Node(chr(sign)) for sign in range(ord('A'), ord('E')+1)]

    def print_nodes(self):
        for node in self.nodes:
            # l.debug(f'{node.sign,node.distance}')
            print(f'{node.sign, node.distance}')

    def print_nodes_ford(self):
        self.print_nodes()

    def print_nodes_dijkstra(self, nodes_ite):
        for node in nodes_ite:
            # l.debug(f'{node.sign,node.distance}')
            print(f'{node.sign, node.distance}')

    def get_weight(self, u, v):
        for edge in self.edges:
            if edge.start == u and edge.end == v:
                return edge.weight

        return math.inf

    def relax(self, edge):
        u = edge.start
        v = edge.end
        l.debug(f'self.weight(u, v):{self.get_weight(u, v)}')
        new_distance = u.distance + self.get_weight(u, v)
        # debug
        l.debug(f'{edge.start.sign, edge.end.sign}')
        l.debug(f'new_distance:{new_distance}')
        if v.distance > new_distance:
            v.distance = new_distance
            v.precursor = u

    # def initialize_single_source(G, source_node):
    #     # for node in G.nodes:
    #     #     node.distance=0
    #     #     node.precursor=None
    #     source_node.distance = 0

    def bellman_ford(self, s):
        G.s_node = s.initialize_source_node()
        # l.info(f'G.s_node:{G.s_node.sign}')
        for i in range(len(self.nodes) - 1):
            for edge in self.edges:
                self.relax(edge)
                l.debug(f'{edge.end.distance}')
        return self

    def dijkstra(self, source_node):
        G.s_node = source_node.initialize_source_node()
        S = []  # the S is the set which contain the solved points
        # Q={}
        Q = self.nodes[:]
        # for node in self.nodes:
        #     # Q[node.sign]=node.distance
        #     Q.append([node.sign,])
        while len(Q) > 0:
            node_u = min(Q, key=lambda item: item.distance)
            S.append(node_u)
            # print("len=",len(Q))
            Q.remove(node_u)
            for edge in self.edges:
                if edge.start.sign == node_u.sign:
                    self.relax(edge)
                    # print("there...")
        return S

    # def print_dijkstra(self):
    # print_nodes(self.dijkstra())

    def print_ford_result(self):
        # self.bellman_ford(s)
        if not self.is_exist_shortest():
            print("there is a negative circle.")
        else:
            for node in self.nodes:
                # print()'''  '''
                print(f'from source node to node:{node.sign},the minimal distance is:{node.distance}')

    def is_exist_shortest(self):
        for edge in self.edges:
            if edge.end.distance > edge.start.distance + edge.weight:
                return False
        return True

    def print_precursor(self, node):
        if node.sign == G.s_node.sign:
            print(G.s_node.sign, end=" ")
            # return
        else:
            if node.precursor == None:
                print(G.s_node.sign, "->", node.sign,
                      "(the node is not accessible)", end=" ")
            else:
                self.print_precursor(node.precursor)
                print(node.sign, end=" ")

    def print_path(self):
        for node in self.nodes:
            # print(node.sign)

            self.print_precursor(node)
            print()


def print_nodes(nodes_ite):
    for node in nodes_ite:
        # l.debug(f'{node.sign,node.distance}')
        print(f'{node.sign, node.distance}')


def get_node_instance(sign):
    for node in nodes:
        if node.sign == sign:
            return node

    # throw exception
    return None


# get the edges parameters to instantiate the edge nodes ,put the edges to the list edges;

def generate_directed_edges():
    # the node instances constructed by the strings
    while (True):
        line = input("input node:(,,)")
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
    nodes = [Node(chr(sign)) for sign in range(ord('1'), ord('6') + 1)]
    return nodes


'''debug the edges is right: '''


def print_edges():
    for edge in edges:
        # print(edge.start.sign,edge.end.sign,edge.weight)
        l.info((edge.start.sign, edge.end.sign, edge.weight))


nodes = []
nodes = generate_nodes()
edges = []
edges = generate_directed_edges()
G = G(edges, nodes)
# G.print_nodes()
source_node = input("input the source node you want:(from 'A'~'E')\n")
# source_node="A"

source_node = get_node_instance(source_node)
result = G.dijkstra(source_node)
print("solved by dijkstra:")
G.print_nodes_dijkstra(result)

print("solved by bellman_ford:")
G.bellman_ford(source_node)
G.print_nodes_ford()
G.print_ford_result()
G.print_path()
''' 
the dijkstra only solve the data without negative weights in edges of the Graph

A,B,10
A,C,3
B,C,1
C,B,4
B,D,2
C,D,9
C,E,2
D,E,7
E,D,9
0

A,B,1
A,C,4
B,C,3
D,C,5
D,B,1
B,D,2
B,E,2
E,D,3
0

'''
''' test data 2:

1,2,10
2,1,10
1,5,45
5,1,45
1,4,30
4,1,30
4,6,20
6,4,20
2,3,50
3,2,50
2,5,40
5,2,40
2,6,25
6,2,25
3,5,35
5,3,35
3,6,15
6,3,15
5,6,55
6,5,55
0


'''
