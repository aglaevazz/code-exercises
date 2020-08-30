# this program stores a undirected graph in an adjacency-list and checks if there is a path between two vertices


class Node:
    def __init__(self, index):
        self.index = index
        self.visited = False
        self.neighbors = []


def store_graph_in_adjacency_list():
    n_vertices, n_edges = map(int, input().split())
    graph = [i for i in range(n_vertices + 1)]
    for i in range(1, n_vertices + 1):
        vertex = Node(i)
        graph[i] = vertex
    for _ in range(n_edges):
        vertex_index_a, vertex_index_b = map(int, input().split())
        vertex_a = graph[vertex_index_a]
        vertex_b = graph[vertex_index_b]
        vertex_a.neighbors.append(vertex_b)
        vertex_b.neighbors.append(vertex_a)
    return graph


def path_exists(start_vertex, end_vertex, graph):
    if start_vertex == end_vertex:
        return 1
    else:
        start_vertex.visited = True
        for neighbor in start_vertex.neighbors:
            if not neighbor.visited:
                if path_exists(neighbor, end_vertex, graph) == 1:
                    return 1
        return 0


def print_graph(graph):
    for node in graph[1:]:
        print(node.index, [neighbor.index for neighbor in node.neighbors])


if __name__ == '__main__':
    graph = store_graph_in_adjacency_list()
    vertex_a, vertex_b = map(int, input().split())
    vertex_a, vertex_b = graph[vertex_a], graph[vertex_b]
    print(path_exists(vertex_a, vertex_b, graph))
