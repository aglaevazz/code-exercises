# python3
# this program checks if a binary tree is a binary search tree


import unittest


def is_binary_search_tree(root):
    if not root:
        return True
    in_order_tree_list = get_in_order_tree_list(root)
    previous_node_value = in_order_tree_list[0]
    for current_node_value in in_order_tree_list[1:]:
        if current_node_value < previous_node_value:
            return False
        previous_node_value = current_node_value
    return True


def get_in_order_tree_list(root_binary_tree, in_order_tree_list=None):
    if not in_order_tree_list:
        in_order_tree_list = []
    if root_binary_tree:
        in_order_tree_list = get_in_order_tree_list(root_binary_tree.left, in_order_tree_list)
        in_order_tree_list.append(root_binary_tree.value)
        in_order_tree_list = get_in_order_tree_list(root_binary_tree.right, in_order_tree_list)
    return in_order_tree_list


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TestFunctions(unittest.TestCase):

    def test_get_in_order_tree_list(self):
        tree_root = Node(5)
        tree_root.left = Node(2)
        tree_root.left.left = Node(1)
        tree_root.left.right = Node(3)
        tree_root.right = Node(8)
        tree_root.right.left = Node(7)
        self.assertEqual(get_in_order_tree_list(tree_root), [1, 2, 3, 5, 7, 8])

        tree_root = None
        self.assertEqual(get_in_order_tree_list(tree_root), [])

    def test_is_binary_search_tree(self):
        tree_root = None
        self.assertTrue(is_binary_search_tree(tree_root))

        tree_root = Node(5)
        self.assertTrue(is_binary_search_tree(tree_root))

        tree_root = Node(5)
        tree_root.left = Node(2)
        tree_root.left.left = Node(1)
        tree_root.left.right = Node(3)
        tree_root.right = Node(8)
        tree_root.right.left = Node(7)
        self.assertTrue(is_binary_search_tree(tree_root))

        tree_root = Node(1)
        tree_root.left = Node(5)
        tree_root.left.left = Node(3)
        tree_root.left.right = Node(7)
        tree_root.right = Node(10)
        tree_root.right.left = Node(15)
        self.assertFalse(is_binary_search_tree(tree_root))

        tree_root = Node(5)
        tree_root.left = Node(6)
        tree_root.left.left = Node(1)
        tree_root.left.right = Node(3)
        tree_root.right = Node(8)
        tree_root.right.left = Node(7)
        self.assertFalse(is_binary_search_tree(tree_root))


if __name__ == '__main__':
    unittest.main()
