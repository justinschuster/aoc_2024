def read_input(input='input.txt'):
    text = open(input, 'r').read()
    text = '2333133121414131402'

    # text = '12345'
    return list(int(digit) for digit in text)


def generate_diskmap(input):
    disk_map = ''
    file_id = 0
    for i, digit in enumerate(input):
        if i == 0 or i % 2 == 0:
            to_map = str(file_id) * digit
            disk_map = disk_map + to_map
            file_id += 1
        else:
            to_map = '.' * digit
            disk_map = disk_map + to_map
    return disk_map


def sort_diskmap(diskmap):
    dots = 0
    for i, digit in enumerate(diskmap):
        if digits == '.':
            dots += 1
            for j in diskmap[::-1]:
                continue


def solve(input):
    diskmap = generate_diskmap(input)

    return diskmap

if __name__ == '__main__':
    input = read_input()
    answer = solve(input)
    print(answer)
