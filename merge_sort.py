# python3
# implementation of merge sort

import unittest


def merge_sort(array):
    if len(array) == 0 or len(array) == 1:
        return array
    else:
        left_array, right_array = array[:len(array)//2], array[len(array)//2:]
        sorted_left_array = merge_sort(left_array)
        sorted_right_array = merge_sort(right_array)
        return merge_sorted_arrays(sorted_left_array, sorted_right_array)


def merge_sorted_arrays(left_array, right_array):
    sorted_array = []
    i_left, i_right = 0, 0
    while i_left < len(left_array) and i_right < len(right_array):
        current_left = left_array[i_left]
        current_right = right_array[i_right]
        if current_left < current_right:
            sorted_array.append(current_left)
            i_left += 1
        elif current_right < current_left:
            sorted_array.append(current_right)
            i_right += 1
        else:
            sorted_array.append(current_left)
            sorted_array.append(current_right)
            i_left += 1
            i_right += 1
    if i_left < len(left_array):
        sorted_array += left_array[i_left:]
    elif i_right < len(right_array):
        sorted_array += right_array[i_right:]
    return sorted_array


class TestMergeSort(unittest.TestCase):

    def test_merge(self):
        sorted_array_1 = [2, 4, 14]
        sorted_array_2 = [1, 5, 30]
        self.assertEqual(merge_sorted_arrays(sorted_array_1, sorted_array_2), sorted(sorted_array_1 + sorted_array_2))
        sorted_array_1 = []
        sorted_array_2 = [1]
        self.assertEqual(merge_sorted_arrays(sorted_array_1, sorted_array_2), sorted(sorted_array_1 + sorted_array_2))

    def test_merge_sort(self):
        unsorted_array = [3, 6, 1, 7, 4, 15]
        self.assertEqual(merge_sort(unsorted_array), sorted(unsorted_array))
        unsorted_array = []
        self.assertEqual(merge_sort(unsorted_array), unsorted_array)
        unsorted_array = [3]
        self.assertEqual(merge_sort(unsorted_array), unsorted_array)
        unsorted_array = [15, 13, 9, 5, 4, 1, 6]
        self.assertEqual(merge_sort(unsorted_array), sorted(unsorted_array))


if __name__ == '__main__':
    unittest.main()
