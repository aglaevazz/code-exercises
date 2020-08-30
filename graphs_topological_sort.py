# this program stores a directed graphs and then sorts it topologically


class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.visited = False
        self.preorder = None
        self.postorder = None


class Graph:
    def __init__(self, n_vertices, m_edges):
        self.n_vertices = n_vertices
        self.m_edges = m_edges
        self.graph_set = set()
        self.graph_dict = {}
        for i in range(1, n_vertices+1):
            self.graph_dict[i] = Node(i)
            self.graph_set.add(i)
        self.store_edges_and_vertices()
        self.clock = 1

    def store_edges_and_vertices(self):
        for i in range(self.m_edges):
            a, b = map(int, input().split())
            self.graph_dict[a].neighbors.append(b)

    def topological_sort(self):
        while self.graph_set:
            self.depth_first_search(self.graph_dict[self.graph_set.pop()])
        sorted_by_postorder = sorted(self.graph_dict.items(), key=lambda x: x[1].postorder, reverse=True)
        sorted_values = [i[1].value for i in sorted_by_postorder]
        return sorted_values

    def depth_first_search(self, vertex):
        if not vertex.visited:
            self.graph_set.discard(vertex.value)
            vertex.visited = True
            vertex.preorder = self.clock
            self.clock += 1
            for v in vertex.neighbors:
                node = self.graph_dict[v]
                self.depth_first_search(node)
            vertex.postorder = self.clock
            self.clock += 1


if __name__ == "__main__":
    n_vertices, m_edges = map(int, input().split())
    graph = Graph(n_vertices, m_edges)
    print(*graph.topological_sort())
