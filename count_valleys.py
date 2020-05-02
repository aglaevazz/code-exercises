'''Count the valleys a hiker goes through starting and endig at sea level.
n = number of steps: 2 <= n <= 10^6
s = string of steps D: down, U: up
sample input:
8
UDDDUDUU
sample output:
1'''


def counting_valleys(steps):
    valleys = 0
    height = 0
    for step in list(steps):
        if step == 'D':
            height -= 1
        else:
            height += 1
            if height == 0:
                valleys += 1
    return valleys


if __name__ == '__main__':
    number_of_steps = input()
    steps = input()
    print(counting_valleys(steps))
