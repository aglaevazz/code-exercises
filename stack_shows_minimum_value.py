# python3
# this program implements a stack which also returns its minimum value any time

import unittest


class Node:
    def __init__(self, value, minimum):
        self.value = value
        self.minimum = minimum


class Stack:
    def __init__(self):
        self.stack = []
        self.current_min = None

    def add(self, element):
        if not self.current_min:
            self.current_min = element
        if element < self.current_min:
            self.current_min = element
        node = Node(element, self.current_min)
        self.stack.append(node)

    def pop(self):
        if len(self.stack) == 1:
            self.current_min = None
        return self.stack.pop(-1)

    def peek(self):
        return self.stack[-1]

    def get_min(self):
        return self.current_min


class TestStack(unittest.TestCase):

    def test_get_min(self):
        stack = Stack()
        self.assertFalse(stack.get_min())
        stack.add(2)
        stack.add(1)
        stack.pop()
        stack.peek()
        stack.add(3)
        stack.add(5)
        self.assertEqual(stack.get_min(), 1)


if __name__ == '__main__':
    unittest.main()


