# python3
# this program implements Kruskal's algorithm to connect any points on a plane with segments of minimum total length

import math
import unittest


def safe_graph(n, vertices_list):
    edges = []
    sets = [0 for _ in range(n+1)]
    vertices = [0 for _ in range(n+1)]
    index0 = 1
    for vertex in vertices_list:
        vertices[index0] = vertex
        subset = {index0}
        sets[index0] = subset
        index0 += 1
    index1 = 1
    while index1 < n+1:
        x1, y1 = vertices[index1]
        index2 = index1 + 1
        while index2 < n+1:
            x2, y2 = vertices[index2]
            distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            edges.append((index1, index2, distance))
            index2 += 1
        index1 += 1
    return sets, edges


def kruskal_minimum_spanning_tree(sets, edges):
    minimum_total_weight = 0
    edges.sort(key=lambda x: x[2])
    for edge in edges:
        a, b, weight = edge
        set_a, set_b = sets[a], sets[b]
        if set_a.isdisjoint(set_b):
            minimum_total_weight += weight
            new_set = set_a.union(set_b)
            for i in set_a:
                sets[i] = new_set
            for i in set_b:
                sets[i] = new_set
    return minimum_total_weight


class TestKruskalsMinimumSpanningTree(unittest.TestCase):
    def test_kruskals_minimum_spanning_tree(self):
        n = 4
        vertices = [(0, 0), (0, 1), (1, 0), (1, 1)]
        sets, edges = safe_graph(n, vertices)
        self.assertEqual(kruskal_minimum_spanning_tree(sets, edges), 3.0)

        n = 5
        vertices = [(0, 0), (0, 2), (1, 1), (3, 0), (3, 2)]
        sets, edges = safe_graph(n, vertices)
        self.assertEqual(kruskal_minimum_spanning_tree(sets, edges), 7.06449510224598)


if __name__ == '__main__':
    n = int(input())
    vertices = []
    for _ in range(n):
        vertex = tuple(map(int, input().split()))
        vertices.append(vertex)
    sets, edges = safe_graph(n, vertices)
    print(kruskal_minimum_spanning_tree(sets, edges))
