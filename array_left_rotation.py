# input: length array (<= 10^5), number of left rotation (< n), output: resulting array
# sample input:
# 5 4
# 1 2 3 4 5
# sample output:
# 5 1 2 3 4



def left_rotation(array, rotations):
    return array[rotations:] + array[:rotations]


if __name__ == '__main__':
    n_array, rotations = map(int, input().split())
    array = list(map(int, input().rstrip().split()))
    print(left_rotation(array, rotations))
