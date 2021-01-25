# python3
# implementation of quick-sort

import unittest
import random


def quick_sort(array):
    if not array or len(array) == 1:
        return array
    pivot = random.choice(array)
    i_left = 0
    i_right = len(array) - 1
    while i_left < i_right:
        left_element = array[i_left]
        right_element = array[i_right]
        if left_element > pivot:
            if right_element <= pivot:
                array[i_left], array[i_right] = right_element, left_element
                i_left += 1
                i_right -= 1
            else:
                i_right -= 1
        elif right_element <= pivot:
            i_left += 1
        else:
            i_left += 1
            i_right -= 1
    if array[i_left] <= pivot:
        i_left += 1
    return quick_sort(array[:i_left]) + quick_sort(array[i_left:])


class TestQuickSort(unittest.TestCase):

    def test_quick_sort(self):
        unsorted_array = [3, 6, 1, 7, 4, 15]
        self.assertEqual(quick_sort(unsorted_array), sorted(unsorted_array))
        unsorted_array = [90, 2, 44, 23, 1, 4, 24, 14, 100]
        self.assertEqual(quick_sort(unsorted_array), sorted(unsorted_array))
        unsorted_array = []
        self.assertEqual(quick_sort(unsorted_array), unsorted_array)
        unsorted_array = [90]
        self.assertEqual(quick_sort(unsorted_array), unsorted_array)
        unsorted_array = [7, 2]
        self.assertEqual(quick_sort(unsorted_array), sorted(unsorted_array))


if __name__ == '__main__':
    unittest.main()
