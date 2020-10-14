# python3
# this program checks whether there is a path between vertex a and b in a directed graph

import unittest


class Graph:
    def __init__(self, graph_list):
        self.graph_map = {}
        self.safe_graph(graph_list)

    def safe_graph(self, graph_list):
        for key in graph_list.keys():
            vertex = Node(key)
            for value in graph_list[key]:
                vertex.descendants.append(value)
            self.graph_map[key] = vertex

    def print_graph(self):
        for key in self.graph_map.keys():
            print(self.graph_map[key])
            print('vertex: ', key, '   ', 'descendants: ', self.graph_map[key].descendants)

    def path_exists(self, start_vertex, end_vertex):
        start_vertex.visited = True
        for value in start_vertex.descendants:
            vertex = self.graph_map[value]
            if not vertex.visited:
                if vertex.value == end_vertex.value or self.path_exists(vertex, end_vertex):
                    return True
        return False


class Node:
    def __init__(self, value):
        self.value = value
        self.descendants = []
        self.visited = False


class TestPathExists(unittest.TestCase):
    def setUp(self):
        graph_map = {'e': ['a'], 'a': ['c', 'd'], 'c': [], 'd': ['g', 'c'], 'f': ['d'], 'g': ['b'], 'b': []}
        self.graph = Graph(graph_map)
        self.vertex_a = self.graph.graph_map['a']

    def test_path_exists_1(self):
        self.vertex_a = self.graph.graph_map['a']
        vertex_b = self.graph.graph_map['c']
        self.assertTrue(self.graph.path_exists(self.vertex_a, vertex_b))

    def test_path_exists_2(self):
        self.vertex_a = self.graph.graph_map['a']
        vertex_b = self.graph.graph_map['d']
        self.assertTrue(self.graph.path_exists(self.vertex_a, vertex_b))

    def test_path_exists_3(self):
        self.vertex_a = self.graph.graph_map['a']
        vertex_b = self.graph.graph_map['g']
        self.assertTrue(self.graph.path_exists(self.vertex_a, vertex_b))

    def test_path_exists_4(self):
        self.vertex_a = self.graph.graph_map['a']
        vertex_b = self.graph.graph_map['b']
        self.assertTrue(self.graph.path_exists(self.vertex_a, vertex_b))

    def test_path_exists_5(self):
        self.vertex_a = self.graph.graph_map['a']
        vertex_b = self.graph.graph_map['f']
        self.assertFalse(self.graph.path_exists(self.vertex_a, vertex_b))

    def test_path_exists_6(self):
        self.vertex_a = self.graph.graph_map['a']
        vertex_b = self.graph.graph_map['e']
        self.assertFalse(self.graph.path_exists(self.vertex_a, vertex_b))


if __name__ == '__main__':
    unittest.main()
