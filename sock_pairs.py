'''John works at a clothing store. He has a large pile of socks that he must pair by color for sale.
Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
For example, there are n = 7 socks with colors ar = [1, 2, 1, 2, 1, 3, 2]. There is one pair of color 1 and one of color 2.
There are three odd socks left, one of each color. The number of pairs is 2.'''


def sock_merchant(sock_list):
    pairs = 0
    sock_dict = {}
    for sock in sock_list:
        if sock in sock_dict:
            sock_dict[sock] += 1
        else:
            sock_dict[sock] = 1
        if sock_dict[sock] % 2 == 0:
            pairs += 1
    return pairs


if __name__ == '__main__':
    sock_list = list(map(int, input().split()))
    print(sock_merchant(sock_list))





