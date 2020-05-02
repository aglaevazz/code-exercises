# determine minimum steps in a mobile game jumping clouds. Jump has to be 1 or 2 steps.
# Jump may only be on cloud '0', not '1'.
# sample input:
# 7
# 0 0 1 0 0 1 0
# sample output:
# 4


def jumping_on_clouds(cloud_list):
    current_position = 0
    jumps = 0
    while len(cloud_list) > current_position + 2:
        if cloud_list[current_position + 2] == 0:
            current_position += 2
        else:
            current_position += 1
        jumps += 1
    if len(cloud_list) > current_position + 1:
        jumps += 1
    return jumps


if __name__ == '__main__':
    n = int(input())

    cloud_list = list(map(int, input().rstrip().split()))

    print(jumping_on_clouds(cloud_list))
