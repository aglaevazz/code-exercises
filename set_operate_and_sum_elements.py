# python 3
# this programme operates a given set and then sums the elements of the set

import unittest


def operate_set(set_, list_of_operations):
    for operation in list_of_operations:
        if operation == 'pop' and len(set_) > 0:
            set_.pop()
        else:
            operation, number = operation.split(' ')
            number = int(number)
            if operation == 'remove' and number in set_:
                set_.remove(number)
            elif operation == 'discard' and len(set_) > 0:
                set_.discard(number)
    return set_


def get_sum_set(s):
    sum_ = 0
    for value in s:
        sum_ += value
    return sum_


class TestSetFunctions(unittest.TestCase):

    def test_operate_set(self):
        set_ = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        list_of_operations = ['pop', 'remove 9', 'discard 9', 'discard 8', 'remove 7', 'pop', 'discard 6', 'remove 5',
                              'pop', 'discard 5']
        new_set = {4}
        self.assertEqual(operate_set(set_, list_of_operations), new_set)

    def test_get_sum_set(self):
        set_ = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.assertEqual(get_sum_set(set_), 45)


if __name__ == '__main__':
    inf = input()
    set_ = set(map(int, input().split()))
    list_of_operations = []
    for _ in range(int(input())):
        list_of_operations.append(input().strip())
    set_ = operate_set(set_, list_of_operations)
    print(get_sum_set(set_))
