# Python3
# This program computes the suffix array of a given text (list of starting indices of sorted suffixes)

import unittest


class SuffixArray:
    # alphabet length is here the length of the ascii-alphabet (128 characters)
    def __init__(self, text, alphabet_length=128):
        self.text = [ord(character) for character in text]
        self.length_text = len(text)
        self.length_alphabet = alphabet_length
        self.equivalence_classes = [None for _ in range(self.length_text)]
        self.ordered_suffixes = [None for _ in range(self.length_text)]
        self.current_length_cyclic_shift = 1
        self.build_suffix_array()

    def build_suffix_array(self):
        self.sort_characters()
        self.compute_character_classes()
        while self.current_length_cyclic_shift <= self.length_text:
            self.sort_doubled()
            self.update_classes()
            self.current_length_cyclic_shift = self.current_length_cyclic_shift * 2

    def print_ordered_suffixes(self):
        print(' '.join(str(i) for i in self.ordered_suffixes))

    def sort_characters(self):
        count = [0 for _ in range(self.length_alphabet)]
        for i in range(self.length_text):
            count[self.text[i]] += 1
        for j in range(1, self.length_alphabet):
            count[j] = count[j] + count[j - 1]
        for i in range(self.length_text-1, -1, -1):
            character = self.text[i]
            count[character] = count[character] - 1
            self.ordered_suffixes[count[character]] = i

    def sort_doubled(self):
        count = [0 for _ in range(self.length_text)]
        new_order = [None for _ in range(self.length_text)]
        for i in range(self.length_text):
            count[self.equivalence_classes[i]] = count[self.equivalence_classes[i]] + 1
        for j in range(1, self.length_text):
            count[j] = count[j] + count[j - 1]
        for i in range(self.length_text-1, -1, -1):
            start = (self.ordered_suffixes[i] - self.current_length_cyclic_shift + self.length_text) % self.length_text
            current_class = self.equivalence_classes[start]
            count[current_class] = count[current_class] - 1
            new_order[count[current_class]] = start
        self.ordered_suffixes = new_order

    def compute_character_classes(self):
        self.equivalence_classes[self.ordered_suffixes[0]] = 0
        for i in range(1, self.length_text):
            if self.text[self.ordered_suffixes[i]] != self.text[self.ordered_suffixes[i - 1]]:
                self.equivalence_classes[self.ordered_suffixes[i]] = self.equivalence_classes[self.ordered_suffixes[i - 1]] + 1
            else:
                self.equivalence_classes[self.ordered_suffixes[i]] = self.equivalence_classes[self.ordered_suffixes[i - 1]]

    def update_classes(self):
        n = len(self.ordered_suffixes)
        new_classes = [0 for _ in range(n)]
        new_classes[self.ordered_suffixes[0]] = 0
        for i in range(1, n):
            current = self.ordered_suffixes[i]
            previous = self.ordered_suffixes[i-1]
            middle = current + self.current_length_cyclic_shift
            middle_previous = (previous + self.current_length_cyclic_shift) % n
            if self.equivalence_classes[current] != self.equivalence_classes[previous] or self.equivalence_classes[middle] != self.equivalence_classes[middle_previous]:
                new_classes[current] = new_classes[previous] + 1
            else:
                new_classes[current] = new_classes[previous]
        self.equivalence_classes = new_classes


class TestSuffixArray(unittest.TestCase):

    def test_build_suffix_array(self):
        suffix_array = SuffixArray('AAA$')
        self.assertEqual(suffix_array.ordered_suffixes, [3, 2, 1, 0])
        suffix_array = SuffixArray('GAC$')
        self.assertEqual(suffix_array.ordered_suffixes, [3, 1, 2, 0])
        suffix_array = SuffixArray('GAGAGAGA$')
        self.assertEqual(suffix_array.ordered_suffixes, [8, 7, 5, 3, 1, 6, 4, 2, 0])
        suffix_array = SuffixArray('AACGATAGCGGTAGA$')
        self.assertEqual(suffix_array.ordered_suffixes, [15, 14, 0, 1, 12, 6, 4, 2, 8, 13, 3, 7, 9, 10, 11, 5])


if __name__ == '__main__':
    text = input()
    suffix_array = SuffixArray(text)
    suffix_array.print_ordered_suffixes()
