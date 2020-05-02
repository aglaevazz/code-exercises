'''count letter a in infinitive string_loop.
input: a string to repeat, n = how many letters to consider to count 'a' (1 <= n <= 10^12).
sample input:
aba
10
sample output:
7
'''


def repeated_string(s, n):
    a_in_substring = s.count('a')
    substring_in_n = n // len(s)
    rest = n % len(s)
    a_in_rest = s[:rest].count('a')
    return a_in_substring * substring_in_n + a_in_rest


if __name__ == '__main__':
    string = input()
    n = int(input())
    print(repeated_string(string, n))
