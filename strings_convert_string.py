# python3
# This programme determines whether string a can be converted to an original string by n deletions and/or attachments.
# All available operations have to be used. Excess operations can be performed on an empty string.

import unittest


def string_is_convertible_to_original(string, original_string, n_operations):
    if len(string) > len(original_string):
        n_operations -= len(string) - len(original_string)
        if n_operations < 0:
            return 'No'
        string = string[:len(original_string)]
    elif len(string) < len(original_string):
        n_operations -= len(original_string) - len(string)
        if n_operations < 0:
            return 'No'
        original_string = original_string[:len(string)]
    if string_a_is_convertible_to_string_b(string, original_string, n_operations):
        return 'Yes'
    return 'No'


def string_a_is_convertible_to_string_b(string_a, string_b, n_operations):
    i = 0
    for letter_string_a, letter_string_b in zip(string_a, string_b):
        if letter_string_a != letter_string_b:
            n_operations -= (len(string_b) - i) * 2
            if n_operations < 0:
                return False
        i += 1
    if n_operations % 2 == 0 or len(string_a) * 2 <= n_operations:
        return True
    return False


class TestFunctions(unittest.TestCase):

    def test_string_a_is_convertible_to_string_b(self):
        string_a = 'aba'
        string_b = 'abc'
        n_operations = 2
        self.assertTrue(string_a_is_convertible_to_string_b(string_a, string_b, n_operations))
        n_operations = 3
        self.assertFalse(string_a_is_convertible_to_string_b(string_a, string_b, n_operations))
        n_operations = 1
        self.assertFalse(string_a_is_convertible_to_string_b(string_a, string_b, n_operations))
        string_b = 'aba'
        n_operations = 8
        self.assertTrue(string_a_is_convertible_to_string_b(string_a, string_b, n_operations))
        n_operations = 7
        self.assertTrue(string_a_is_convertible_to_string_b(string_a, string_b, n_operations))
        n_operations = 5
        self.assertFalse(string_a_is_convertible_to_string_b(string_a, string_b, n_operations))

    def test_string_is_convertible_to_original(self):
        string = ''
        original_string = ''
        n_operations = 0
        self.assertEqual(string_is_convertible_to_original(string, original_string, n_operations), 'Yes')
        string = 'abbaa'
        original_string = 'abb'
        n_operations = 1
        self.assertEqual(string_is_convertible_to_original(string, original_string, n_operations), 'No')
        string = 'abb'
        original_string = 'abbaa'
        n_operations = 1
        self.assertEqual(string_is_convertible_to_original(string, original_string, n_operations), 'No')


if __name__ == '__main__':
    unittest.main()
