def read_input(input='input.txt'):
    text = open(input, 'r').read().replace('\n', '')
    return list(int(digit) for digit in text)


def solve(input):
    files, space = input[::2], input[1::2]

    if len(space) < len(files):
        space.append(1)

    diskmap = []
    for i, file in enumerate(files):
        diskmap.extend([i]*file)
        diskmap.extend([None]*space[i])

    pointer = 0
    while pointer < len(diskmap):
        while diskmap[-1] == None:
            diskmap.pop(-1)
            pointer -= 1

        if diskmap[pointer] == None:
            diskmap[pointer] = diskmap.pop(-1)

        pointer += 1

    return sum([x * i for i, x in enumerate(diskmap)])


if __name__ == '__main__':
    input = read_input()
    answer = solve(input)
    print(answer)
