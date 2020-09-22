# python3
# Implementation of Bellman Ford Algorithm
# This program checks whether a directed, weighted graph contains a negative cycle.
# It outputs 1 if the graph contains a negative cycle and 0 if it doesn't.

import unittest


class Graph:
    def __init__(self, n_vertices, m_edges, graph_list):
        self.n_vertices = n_vertices
        self.m_edges = m_edges
        self.distances = [n_vertices*10000 for _ in range(n_vertices+1)]
        self.neighbors = [[] for _ in range(n_vertices+1)]
        for edge in graph_list:
            a, b, weight = edge
            self.neighbors[a].append((b, weight))

    def graph_contains_negative_cycle(self):
        self.distances[1] = 0
        count = 0
        negative_cycle = True
        while negative_cycle and count < self.n_vertices:
            count += 1
            negative_cycle = self.relax_edges(1)
        negative_cycle = self.relax_edges(1, last_iteration=True)
        return int(negative_cycle)

    def relax_edges(self, start_vertex, last_iteration=False):
        altered = False
        for vertex in range(1, self.n_vertices+1):
            for neighbor in self.neighbors[vertex]:
                neighbor_vertex, weight = neighbor
                if self.relax_edge(vertex, neighbor_vertex, weight):
                    if last_iteration:
                        return True
                    altered = True
        return altered

    def relax_edge(self, current_vertex, neighbor_vertex, weight):
        new_distance = self.distances[current_vertex] + weight
        current_distance = self.distances[neighbor_vertex]
        if new_distance < current_distance:
            self.distances[neighbor_vertex] = new_distance
            return True
        return False


class TestCheckForNegativeCycle(unittest.TestCase):
    def test_check_for_negative_cycle(self):
        n_vertices, m_edges = 4, 4
        graph_list = [(1, 2, -5), (4, 1, 2), (2, 3, 2), (3, 1, 1)]
        graph = Graph(n_vertices, m_edges, graph_list)
        self.assertEqual(graph.graph_contains_negative_cycle(), 1)

        n_vertices, m_edges = 5, 7
        graph_list = [(1, 2, 4), (1, 3, 3), (2, 3, -2), (2, 4, 4), (3, 4, -3), (3, 5, 1), (4, 5, 2)]
        graph = Graph(n_vertices, m_edges, graph_list)
        self.assertEqual(graph.graph_contains_negative_cycle(), 0)


if __name__ == '__main__':
    n_vertices, m_edges = map(int, input().split())
    graph_list = []
    for edge in range(m_edges):
        a, b, weight = map(int, input().split())
        graph_list.append((a, b, weight))
    graph = Graph(n_vertices, m_edges, graph_list)
    print(graph.graph_contains_negative_cycle())
