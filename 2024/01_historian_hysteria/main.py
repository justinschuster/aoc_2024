def readInput():
    with open('input', 'r') as file:
        left = []
        right = []
        for line in file:
            split_line = line.split('   ') # 3 spaces
            left.append(int(split_line[0])) 
            right.append(int(split_line[1]))
    return left, right

def part_one():
    left, right = readInput()
    sorted_left = sorted(left)
    sorted_right = sorted(right)
    n = len(sorted_left)
    out = 0
    for i in range(n):
        min_num = min(sorted_left[i], sorted_right[i])
        max_num = max(sorted_left[i], sorted_right[i])
        diff = max_num - min_num
        out += diff
    return out

def part_two():
    left, right = readInput()
    out = 0
    for i in left:
        c = right.count(i) * i
        out += c
    return out

if __name__ == '__main__':
    p1_ans = part_one()
    print(f"Part One: {p1_ans}")

    p2_ans = part_two()
    print(f"Part Two: {p2_ans}")
