import re

def read_input():
    matrix = []
    with open('input.txt', 'r') as file:
        for line in file:
            matrix.append(line.strip())
    return matrix

def count_pattern(matrix, pattern):
    count = 0
    for row in matrix:
        row_str = ''.join(row)
        count += len(re.findall(pattern, row_str))
        count += len(re.findall(pattern, row_str[::-1]))
    return count

def get_vertical(matrix):
    rows, cols = len(matrix), len(matrix[0])
    rotated = [[0 for _ in range(rows)] for _ in range(cols)] 
    for r in range(rows):
        for c in range(cols):
            rotated[c][rows-1-r] = matrix[r][c]
    return rotated

def get_diagonal(matrix):
    diagonals = []
    rows, cols = len(matrix), len(matrix[0])

    # check down to the left
    for d in range(-(rows-1), 0):
        diag = [matrix[i][i-d] for i in range(max(0, d), min(rows, cols+d))]
        diagonals.append(diag)

    # check down to the right
    for d in range(rows+cols-1):
        diag = [matrix[i][d-i] for i in range(max(0, d-cols+1), min(rows, d+1))]
        diagonals.append(diag)

    return diagonals

def part_one(matrix):
    pattern = r'XMAS'
    count = 0
    count += count_pattern(matrix, pattern)
    count += count_pattern(get_vertical(matrix), pattern)
    count += count_pattern(get_diagonal(matrix), pattern)
    return count

def main():
    matrix = read_input() 

    # part one
    print(part_one(matrix))
 
if __name__ == '__main__':
    main()
