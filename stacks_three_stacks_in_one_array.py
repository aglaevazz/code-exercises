# python3
# this program implements three stacks in one array

import unittest


class Stacks:
    def __init__(self, number_of_stacks):
        self.array_of_stacks = [[] for _ in range(number_of_stacks)]

    def add(self, element, stack_index=-1):
        self.array_of_stacks[stack_index].append(element)

    def pop(self, stack_index=-1):
        del self.array_of_stacks[stack_index][-1]

    def peek(self, stack_index=-1):
        return self.array_of_stacks[stack_index][-1]


class TestStacks(unittest.TestCase):

    def test_add(self):
        stacks = Stacks(3)
        stacks.add(1, 0)
        stacks.add(2, 0)
        stacks.add(3, 1)
        stacks.add(4, 1)
        stacks.add(5, 2)
        stacks.add(6, 2)
        self.assertEqual(stacks.array_of_stacks, [[1, 2], [3, 4], [5, 6]])

    def test_pop(self):
        stacks = Stacks(2)
        stacks.array_of_stacks = [[7, 2, 8], [8]]
        stacks.pop(0)
        self.assertEqual(stacks.array_of_stacks, [[7, 2], [8]])
        stacks.pop()
        self.assertEqual(stacks.array_of_stacks, [[7, 2], []])

    def test_peek(self):
        stacks = Stacks(2)
        stacks.array_of_stacks = [[7, 2, 8], [8]]
        self.assertEqual(stacks.peek(0), 8)
        self.assertEqual(stacks.peek(), 8)


if __name__ == '__main__':
    unittest.main()
