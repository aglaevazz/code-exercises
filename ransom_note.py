'''Check if magazine contains all words for the ransom note (case-sensitive)
input: m = number of words in magazine, n = number of words in ransom note, magazine-string, note-string
m, n <= 30000
sample input:
6 4
give me one grand today night
give one grand today
sample output:
yes
'''


def check_magazine(magazine, note):
    dict_ = {}
    for word in note:
        if word in dict_:
            dict_[word] += 1
        else:
            dict_[word] = 1
    for word in magazine:
        if word in dict_:
            dict_[word] -= 1
            if dict_[word] == 0:
                del dict_[word]
            if dict_ == {}:
                print('Yes')
                return
    print('No')


if __name__ == '__main__':
    m, n = map(int, input().split())
    magazine = input().split()
    note = input().split()
    check_magazine(magazine, note)
