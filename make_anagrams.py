# return minimum deletions needed to make an anagram from two words


def make_anagram(str_a, str_b):
    deletions = 0
    dict_a, dict_b = {}, {}
    letters = set(str_a + str_b)
    for letter in letters:
        dict_a[letter], dict_b[letter] = 0, 0
    for letter in str_a:
        dict_a[letter] += 1
    for letter in str_b:
        dict_b[letter] += 1
    for letter in letters:
        deletions += abs(dict_a[letter] - dict_b[letter])
    return deletions


if __name__ == '__main__':
    a = input()
    b = input()
    print(make_anagram(a, b))
