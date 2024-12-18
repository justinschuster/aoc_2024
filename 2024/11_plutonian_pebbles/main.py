'''
rules:
    0: 1,
    even -> two stones, left half of digits -> left stone, right half -> right stone
    else: new stone, old stone number * 2024

'''


def read_input(input='11_plutonian_pebbles/input.txt'):
    text = open(input, 'r').read().split()
    return list(int(x) for x in text)


def split_stone(stone):
    stone_str = str(stone)

    n = len(stone_str)
    mid = n // 2
    left, right = '', ''

    for i in range(mid):
        left += stone_str[i]

    for i in range(mid, n):
        right += stone_str[i]

    return int(left), int(right)


def blink(stones):
    out = []

    for stone in stones:
        n = len(str(stone))
        if stone == 0:
            out.append(1)
        elif n % 2 == 0:
            left, right = split_stone(stone)
            out.append(left)
            out.append(right)
        else:
            out.append(stone*2024)

    return out


def solve(stones, blinks):
    while 0 < blinks:
        stones = blink(stones)
        blinks -= 1

    return len(stones)


if __name__ == '__main__':
    puzzle = read_input()
    answer = solve(puzzle, 25)
    print(answer)