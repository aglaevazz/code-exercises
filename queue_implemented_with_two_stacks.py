# python3
# This program implements a queue by using two stacks.

import unittest


class MyQueue:
    def __init__(self):
        self.stack_add_items = []
        self.stack_pop_items = []

    def add(self, element):
        self.stack_add_items.append(element)

    def pop(self):
        if self.stack_pop_items:
            return self.stack_pop_items.pop()
        elif self.stack_add_items:
            self.pass_items_from_add_to_pop_stack()
            return self.pop()

    def peek(self):
        if self.stack_pop_items:
            return self.stack_pop_items[-1]
        elif self.stack_add_items:
            self.pass_items_from_add_to_pop_stack()
            return self.peek()

    def pass_items_from_add_to_pop_stack(self):
        while self.stack_add_items:
            self.stack_pop_items.append(self.stack_add_items.pop())


class TestMyQueue(unittest.TestCase):
    def test_add(self):
        queue = MyQueue()
        queue.add(1)
        queue.add(2)
        queue.add(3)
        self.assertEqual(queue.stack_add_items, [1, 2, 3])
        self.assertEqual(queue.stack_pop_items, [])

    def test_pop(self):
        queue = MyQueue()
        queue.stack_add_items = [1, 2, 3, 4]
        self.assertEqual(queue.pop(), 1)
        self.assertEqual(queue.stack_add_items, [])
        self.assertEqual(queue.stack_pop_items, [4, 3, 2])

    def test_peek(self):
        queue = MyQueue()
        queue.stack_add_items = [1, 2, 3, 4]
        self.assertEqual(queue.peek(), 1)

    def test_add_pop_peek(self):
        queue = MyQueue()
        queue.add(1)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.pop(), 1)
        self.assertEqual(queue.stack_add_items, [])
        self.assertEqual(queue.stack_pop_items, [])
        queue.add(2)
        queue.add(3)
        queue.add(4)
        self.assertEqual(queue.stack_add_items, [2, 3, 4])
        self.assertEqual(queue.stack_pop_items, [])
        self.assertEqual(queue.pop(), 2)
        self.assertEqual(queue.stack_add_items, [])
        self.assertEqual(queue.stack_pop_items, [4, 3])


if __name__ == '__main__':
    unittest.main()