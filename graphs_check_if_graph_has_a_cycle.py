# this program stores a directed graph and checks if the graph has a cycle by depth-first_search


class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.color = "white"


class Graph:
    def __init__(self, n_vertices, n_edges):
        self.n_vertices = n_vertices
        self.n_edges = n_edges
        self.graph_dict = {}
        self.graph_list = [i for i in range(1, self.n_vertices+1)]
        for i in range(1, self.n_vertices+1):
            self.graph_dict[i] = Node(i)

    def store_edges(self):
        for _ in range(self.n_edges):
            a, b = map(int, input().split())
            self.graph_dict[a].neighbors.append(b)

    def graph_is_cyclic(self):
        while self.graph_list:
            vertex = self.graph_dict[self.graph_list[-1]]
            if self.depth_fist_search(vertex) == 1:
                return 1
        return 0

    def depth_fist_search(self, vertex):
        if vertex.color == "grey":
            return 1
        elif vertex.color == "white":
            vertex.color = "grey"
            for v in vertex.neighbors:
                node = self.graph_dict[v]
                if node.color != "black":
                    if self.depth_fist_search(node) == 1:
                        return 1
            vertex.color = "black"
            self.graph_list.remove(vertex.value)
        return 0


if __name__ == '__main__':
    n_vertices, n_edges = map(int, input().split())
    graph = Graph(n_vertices, n_edges)
    graph.store_edges()
    print(graph.graph_is_cyclic())
