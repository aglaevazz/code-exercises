# python3

# this programme checks if a string is zero or one edit (insert, delete, replace) away from another string
# upper and lower case letters are considered different letters
# e.g. 'away' is one edit away from 'Away'

import unittest


def is_up_to_one_away(string1, string2):
    absolute_length_difference = abs(len(string1) - len(string2))
    if absolute_length_difference > 1:
        return False
    elif absolute_length_difference == 0:
        return difference_is_up_to_max_difference(string1, string2, 2)
    else:
        return difference_is_up_to_max_difference(string1, string2, 1)


def difference_is_up_to_max_difference(string1, string2, max_difference):
    string1_alphabet = [0 for character in range(129)]
    string2_alphabet = [0 for character in range(129)]
    for character in string1:
        string1_alphabet[ord(character)] += 1
    for character in string2:
        string2_alphabet[ord(character)] += 1
    difference = 0
    for i, j in zip(string1_alphabet, string2_alphabet):
        difference += abs(i-j)
        if difference > max_difference:
            return False
    return True


class TestOneAway(unittest.TestCase):

    def test_get_difference(self):
        string1 = 'maya'
        string2 = 'Maya'
        self.assertTrue(difference_is_up_to_max_difference(string1, string2, 2))
        string1 = 'maya'
        string2 = 'aya'
        self.assertTrue(difference_is_up_to_max_difference(string1, string2, 1))
        string1 = 'Maya'
        string2 = 'Maya'
        self.assertTrue(difference_is_up_to_max_difference(string1, string2, 0))

    def test_is_up_to_one_away(self):
        string1 = 'lee'
        string2 = 'Leena'
        self.assertFalse(is_up_to_one_away(string1, string2))
        string1 = 'Lee'
        string2 = 'Leen'
        self.assertTrue(is_up_to_one_away(string1, string2))
        string1 = 'Lee'
        string2 = 'Lea'
        self.assertTrue(is_up_to_one_away(string1, string2))
        string1 = 'Lee'
        string2 = 'Lee'
        self.assertTrue(is_up_to_one_away(string1, string2))


if __name__ == '__main__':
    unittest.main()




