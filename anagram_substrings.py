def sherlockAndAnagrams(s):
    map_ = {}
    for start in range(len(s)):
        for end in range(start+1, len(s)+1):
            substring = str(sorted(list(s[start:end])))
            print('sub: ', substring)
            if substring in map_:
                map_[substring] += 1
            else:
                map_[substring] = 0
    result = map_.values()
    print(result)
    anagram_substrings = 0
    for integer in result:
        anagram_substrings += integer
    return anagram_substrings

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(result)