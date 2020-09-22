# python3
# this program computes the length of the shortest path between two vertices in a given undirected graph
from queue import Queue
import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.neighbors = []


class Graph:
    def __init__(self, n_vertices, n_edges, graph_list):
        self.n_vertices = n_vertices
        self.n_edges = n_edges
        self.graph_map = self.save_graph(graph_list)

    def save_graph(self, graph_list):
        graph = {}
        for i in range(1, self.n_vertices+1):
            vertex = Node(i)
            graph[i] = vertex
        for element in graph_list:
            a, b = element
            graph[a].neighbors.append(b)
            graph[b].neighbors.append(a)
        return graph

    def print_graph(self):
        for key in self.graph_map.keys():
            print(key, self.graph_map[key].neighbors)

    def get_shortest_path(self, starting_vertex, destination_vertex):
        distances, preview_list = self.breadth_first_search(starting_vertex)
        return self.reconstruct_shortest_path(starting_vertex, destination_vertex, preview_list)

    def breadth_first_search(self, starting_vertex_value):
        starting_vertex = self.graph_map[starting_vertex_value]
        distances = [self.n_vertices+1 for _ in range(self.n_vertices+1)]
        preview = [self.n_vertices+1 for _ in range(self.n_vertices+1)]
        distances[starting_vertex_value] = 0
        queue = Queue()
        queue.put(starting_vertex)
        while not queue.empty():
            current = queue.get()
            # current_value = current.value
            for vertex_value in current.neighbors:
                if distances[vertex_value] == self.n_vertices+1:
                    vertex = self.graph_map[vertex_value]
                    queue.put(vertex)
                    preview[vertex_value] = current.value
                    distances[vertex_value] = distances[current.value] + 1
        return distances, preview

    def reconstruct_shortest_path(self, starting_vertex_value, destination_vertex_value, preview_list):
        result = 0
        current = destination_vertex_value
        while current != starting_vertex_value:
            preview_vertex_value = preview_list[current]
            if preview_vertex_value == self.n_vertices + 1:
                return -1
            current = preview_list[current]
            result += 1
        return result


class TestShortestPath(unittest.TestCase):
    def test_shortest_path_algorithm(self):
        n_vertices, n_edges = 4, 4
        graph_list = [(1, 2), (4, 1), (2, 3), (3, 1)]
        graph = Graph(n_vertices, n_edges, graph_list)
        a, b = 2, 4
        self.assertEqual(graph.get_shortest_path(a, b), 2)

        n_vertices, n_edges = 5, 4
        graph_list = [(5, 2), (1, 3), (3, 4), (1, 4)]
        graph = Graph(n_vertices, n_edges, graph_list)
        a, b = 3, 5
        self.assertEqual(graph.get_shortest_path(a, b), -1)


if __name__ == "__main__":
    n_vertices, n_edges = map(int, input().split())
    graph_list = []
    for _ in range(n_edges):
        a, b = map(int, input().split())
        graph_list.append((a, b))
    graph = Graph(n_vertices, n_edges, graph_list)
    a, b = map(int, input().split())
    print(graph.get_shortest_path(a, b))
