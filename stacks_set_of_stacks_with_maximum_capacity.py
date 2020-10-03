# python3
# this program implements a set of stacks with a maximum capacity. When a stack is full, the next stack will be filled.

import unittest


class SetOfStacks:
    def __init__(self, amount_of_stacks, maximum_capacity=100):
        self.set_of_stacks = [[] for _ in range(amount_of_stacks)]
        self.maximum_capacity = maximum_capacity
        self.index_current_stack = 0

    def add(self, element):
        if len(self.set_of_stacks[self.index_current_stack]) < self.maximum_capacity:
            self.set_of_stacks[self.index_current_stack].append(element)
        elif len(self.set_of_stacks) > self.index_current_stack + 1:
            self.index_current_stack += 1
            self.add(element)

    def pop(self):
        if self.index_current_stack == 0 and len(self.set_of_stacks[0]) == 0:
            return
        else:
            value = self.set_of_stacks[self.index_current_stack].pop()
            if len(self.set_of_stacks[self.index_current_stack]) == 0 and self.index_current_stack > 0:
                self.index_current_stack -= 1
            return value

    def peek(self):
        return self.set_of_stacks[self.index_current_stack][-1]


class TestStack(unittest.TestCase):

    def test_add(self):
        stack = SetOfStacks(3, 2)
        stack.add(1)
        stack.add(2)
        stack.add(3)
        stack.add(4)
        self.assertEqual(stack.set_of_stacks, [[1, 2], [3, 4], []])

    def test_pop(self):
        stack = SetOfStacks(3, 2)
        stack.set_of_stacks = [[1, 2], [3], []]
        stack.index_current_stack = 1
        stack.pop()
        self.assertEqual(stack.set_of_stacks, [[1, 2], [], []])

    def test_peek(self):
        stack = SetOfStacks(3, 1)
        stack.set_of_stacks = [[1], [2], [3]]
        stack.index_current_stack = 2
        self.assertEqual(stack.peek(), 3)

    def test_add_pop_peek(self):
        stack = SetOfStacks(2, 2)
        stack.add(1)
        stack.add(2)
        self.assertEqual(stack.set_of_stacks, [[1, 2], []])
        stack.pop()
        self.assertEqual(stack.set_of_stacks, [[1], []])
        stack.add(3)
        self.assertEqual(stack.set_of_stacks, [[1, 3], []])
        self.assertEqual(stack.peek(), 3)


if __name__ == '__main__':
    unittest.main()
