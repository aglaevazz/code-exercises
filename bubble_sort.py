# bubble sort and count swaps


def bubble_sort(n, array):
    sorted_ = False
    swaps = 0
    n_unsorted = n
    while not sorted_:
        sorted_ = True
        for index in range(n_unsorted-1):
            current, next_ = array[index], array[index+1]
            if current > next_:
                array[index], array[index+1] = next_, current
                swaps += 1
                sorted_ = False
        n_unsorted -= 1
    print('Array is sorted in {} swaps.'.format(swaps))
    print('First Element: {}'.format(array[0]))
    print('Last Element: {}'.format(array[-1]))


if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    bubble_sort(n, array)
