# python 3
# this program safes numbers in an ascending-ordered list into a binary search tree with minimum height

import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def safe_tree_from_sorted_list(self, tree_list, start_index=None, end_index=None, current_root=None):
        if not tree_list:
            return
        if not start_index and start_index != 0:
            start_index, end_index = 0, len(tree_list) - 1
        if start_index == end_index:
            self.insert(Node(tree_list[start_index]), current_root)
        elif end_index - start_index == 1:
            self.insert(Node(tree_list[start_index]), current_root)
            self.insert(Node(tree_list[end_index]), current_root)
        else:
            index_insert_element = start_index + ((end_index - start_index) // 2)
            node = Node(tree_list[index_insert_element])
            self.insert(node, current_root)
            self.safe_tree_from_sorted_list(tree_list, start_index, index_insert_element - 1, node)
            self.safe_tree_from_sorted_list(tree_list, index_insert_element + 1, end_index, node)

    def insert(self, node, root=None):
        if not self.root:
            self.root = node
        else:
            if not root:
                root = self.root
            if node.value < root.value:
                if root.left_child:
                    self.insert(node, root.left_child)
                else:
                    root.left_child = node
            else:
                if root.right_child:
                    self.insert(node, root.right_child)
                else:
                    root.right_child = node

    def traverse_in_order(self, root=None, tree_list=None):
        if not tree_list:
            tree_list = []
        if not self.root:
            return tree_list
        if not root:
            root = self.root
        if root.left_child:
            tree_list = self.traverse_in_order(root.left_child, tree_list)
        tree_list.append(root.value)
        if root.right_child:
            tree_list = self.traverse_in_order(root.right_child, tree_list)
        return tree_list


class TestSafeTree(unittest.TestCase):
    def setUp(self):
        self.binary_search_tree = BinarySearchTree()

    def test_safe_tree_from_sorted_list_1(self):
        tree_list = []
        self.binary_search_tree.safe_tree_from_sorted_list(tree_list)
        self.assertEqual(tree_list, self.binary_search_tree.traverse_in_order())

    def test_safe_tree_from_sorted_list_2(self):
        tree_list = [1]
        self.binary_search_tree.safe_tree_from_sorted_list(tree_list)
        self.assertEqual(tree_list, self.binary_search_tree.traverse_in_order())

    def test_safe_tree_from_sorted_list_3(self):
        tree_list = [2, 4, 7, 8, 10, 16]
        self.binary_search_tree.safe_tree_from_sorted_list(tree_list)
        self.assertEqual(tree_list, self.binary_search_tree.traverse_in_order())

    def test_safe_tree_from_sorted_list_4(self):
        tree_list = [4, 8, 19, 20, 25, 100, 20000, 2121283, 1006735263]
        self.binary_search_tree.safe_tree_from_sorted_list(tree_list)
        self.assertEqual(tree_list, self.binary_search_tree.traverse_in_order())


if __name__ == '__main__':
    unittest.main()
