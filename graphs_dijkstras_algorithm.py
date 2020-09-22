# python3
# Implementation of Dijkstra's Algorithm to calculate the weight of the shortest path in a weighted directed graph.
# It outputs -1 if there is no path.

import unittest


class Node:
    def __init__(self, value, n_vertices):
        self.value = value
        self.neighbors = []
        self.distance = 10000 * n_vertices
        self.previous = None
        self.index = None


class Graph:
    def __init__(self, n_vertices, m_edges, graph_list):
        self.n_vertices = n_vertices
        self.m_edges = m_edges
        self.graph_map = {}
        for i in range(1, n_vertices+1):
            self.graph_map[i] = Node(i, n_vertices)
        self.store_graph(graph_list)

    def store_graph(self, graph_list):
        for edge in graph_list:
            current_vertex_value, next_vertex_value, weight = edge
            self.graph_map[current_vertex_value].neighbors.append((next_vertex_value, weight))

    def print_graph(self):
        for vertex in self.graph_map.values():
            print('value', vertex.value)
            print('neighbors', vertex.neighbors)

    def get_cheapest_price(self, start_vertex_value, end_vertex_value):
        distances = self.dijkstra_algorithm(start_vertex_value)
        # print(distances)
        distance = distances[end_vertex_value-1]
        if distance == float('inf'):
            return -1
        return distance

    def dijkstra_algorithm(self, start_vertex_value):
        distances = [float('inf') for _ in range(1, self.n_vertices+1)]
        distances_repo = [(float('inf'), i) for i in range(1, self.n_vertices+1)]
        distances[start_vertex_value-1] = 0
        distances_repo[start_vertex_value-1] = (0, start_vertex_value)
        while distances_repo:
            distances_repo = sorted(distances_repo, key=lambda item: item[0], reverse=True)
            distance, current_vertex_value = distances_repo.pop(-1)
            current_vertex = self.graph_map[current_vertex_value]
            for neighbor in current_vertex.neighbors:
                next_vertex_value, weight_current_next = neighbor
                next_vertex = self.graph_map[next_vertex_value]
                new_distance = distances[current_vertex_value-1] + weight_current_next
                if distances[next_vertex_value-1] > new_distance:
                    distances[next_vertex_value-1] = new_distance
                    distances_repo = self.change_priority(distances_repo, next_vertex_value, new_distance)
                    next_vertex.preview = current_vertex
        return distances

    @staticmethod
    def change_priority(distances_repo, next_vertex_value, new_distance):
        for item in distances_repo:
            distance, value = item
            if value == next_vertex_value:
                i = distances_repo.index(item)
                distances_repo[i] = (new_distance, value)
                return distances_repo


class TestGetCheapestFlight(unittest.TestCase):
    def test_get_cheapest_flight(self):
        n_vertices, m_edges = 4, 4
        graph_list = [(1, 2, 1), (4, 1, 2), (2, 3, 2), (1, 3, 5)]
        graph = Graph(n_vertices, m_edges, graph_list)
        a, b = 1, 3
        self.assertEqual(graph.get_cheapest_price(a, b), 3)

        n_vertices, m_edges = 5, 9
        graph_list = [(1, 2, 4), (1, 3, 2), (2, 3, 2), (3, 2, 1), (2, 4, 2), (3, 5, 4), (5, 4, 1), (2, 5, 3), (3, 4, 4)]
        graph = Graph(n_vertices, m_edges, graph_list)
        a, b = 1, 5
        self.assertEqual(graph.get_cheapest_price(a, b), 6)

        n_vertices, m_edges = 3, 3
        graph_list = [(1, 2, 7), (1, 3, 5), (2, 3, 2)]
        graph = Graph(n_vertices, m_edges, graph_list)
        a, b = 3, 2
        self.assertEqual(graph.get_cheapest_price(a, b), -1)


if __name__ == "__main__":
    n_vertices, m_edges = map(int, input().split())
    graph_list = []
    for _ in range(m_edges):
        current_vertex_value, next_vertex_value, weight = map(int, input().split())
        graph_list.append((current_vertex_value, next_vertex_value, weight))
    graph = Graph(n_vertices, m_edges, graph_list)
    a, b = map(int, input().split())
    print(graph.get_cheapest_price(a, b))
