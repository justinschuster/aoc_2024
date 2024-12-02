def readInput():
    with open('input', 'r') as file:
        left = []
        right = []
        for line in file:
            split_line = line.split('   ') # 3 spaces
            left.append(int(split_line[0])) 
            right.append(int(split_line[1]))
    return left, right

def main():
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

if __name__ == '__main__':
    print(main())
