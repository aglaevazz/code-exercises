# python3
# this program creates a list of linked lists for the nodes at each level of a binary tree

import random
import unittest


class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, new_node, current_node=None):
        if not self.root:
            self.root = new_node
            return
        if not current_node:
            current_node = self.root
        if current_node.left and current_node.right:
            # randomly travel to left or right child
            left_right = [current_node.left, current_node.right]
            random_side = random.choice(left_right)
            self.add_node(new_node, random_side)
        elif current_node.left:
            current_node.right = new_node
        else:
            current_node.left = new_node

    def get_in_order_list_of_nodes(self, current_node, list_of_nodes=None):
        if not list_of_nodes:
            list_of_nodes = []
        if current_node:
            list_of_nodes = self.get_in_order_list_of_nodes(current_node.left, list_of_nodes)
            list_of_nodes.append(current_node.value)
            list_of_nodes = self.get_in_order_list_of_nodes(current_node.right, list_of_nodes)
        return list_of_nodes

    def get_list_of_linked_lists_of_nodes_at_each_level(self, current_node, level=0, list_of_linked_lists=None):
        if not list_of_linked_lists:
            tree_depth = self.get_tree_depth(self.root)
            list_of_linked_lists = [LinkedList() for _ in range(tree_depth)]
        if current_node:
            current_level_linked_list = list_of_linked_lists[level]
            current_level_linked_list.add_node(current_node)
            list_of_linked_lists = self.get_list_of_linked_lists_of_nodes_at_each_level(current_node.left, level + 1,
                                                                                        list_of_linked_lists)
            list_of_linked_lists = self.get_list_of_linked_lists_of_nodes_at_each_level(current_node.right, level + 1,
                                                                                        list_of_linked_lists)
        return list_of_linked_lists

    def get_tree_depth(self, current_node, current_depth=0):
        if not current_node:
            return current_depth
        current_depth += 1
        left_depth = self.get_tree_depth(current_node.left, current_depth)
        right_depth = self.get_tree_depth(current_node.right, current_depth)
        if left_depth > right_depth:
            return left_depth
        return right_depth


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def get_linked_list_as_list_of_values(self, list_of_values=None):
        if not list_of_values:
            list_of_values = []
        if not self.head:
            return list_of_values
        current = self.head
        while current:
            list_of_values.append(current.value)
            current = current.next
        return list_of_values


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None


class TestTreeLinkedListNode(unittest.TestCase):

    def setUp(self):
        self.tree = Tree()
        self.tree.root = Node(1)
        self.tree.root.left = Node(2)
        self.tree.root.right = Node(3)
        self.tree.root.left.left = Node(4)

    # test class Tree
    def test_get_in_order_list_of_nodes(self):
        self.assertEqual(self.tree.get_in_order_list_of_nodes(self.tree.root), [4, 2, 1, 3])

    def test_get_tree_depth(self):
        self.assertEqual(self.tree.get_tree_depth(self.tree.root), 3)

    def test_get_list_of_linked_lists_of_nodes_at_each_level(self):
        expected_list_of_values = [[1], [2, 3], [4]]
        actual_list_of_linked_lists = self.tree.get_list_of_linked_lists_of_nodes_at_each_level(self.tree.root)
        actual_list_of_values = [LinkedList.get_linked_list_as_list_of_values(linked_list) for linked_list in
                                 actual_list_of_linked_lists]
        self.assertEqual(actual_list_of_values, expected_list_of_values)

    # test class LinkedList
    def test_linked_list_get_linked_list_as_list_of_values(self):
        linked_list = LinkedList()
        linked_list.add_node(Node(1))
        linked_list.add_node(Node(2))
        linked_list.add_node(Node(3))
        linked_list.add_node(Node(4))
        self.assertEqual(linked_list.get_linked_list_as_list_of_values(), [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
