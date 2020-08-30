# calculate the minimum absolute difference of all integers in an array


def minimum_absolute_difference(arr):
    sorted_numbers = sorted(arr)
    min_diff = 0
    for index in range(len(arr)-1):
        current_number, next_number = sorted_numbers[index], sorted_numbers[index+1]
        current_diff = abs(current_number - next_number)
        if not min_diff or min_diff > current_diff:
            min_diff = current_diff
        if min_diff == 0:
            return min_diff
    return min_diff


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    print(minimum_absolute_difference(arr))
