def get_input():
    matrix = []
    with open('input.txt', 'r') as file:
        matrix = [list(line.strip()) for line in file]
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))

def find_guard(matrix):
    guard_symbols = ['<', '>', '^', 'v']
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col in guard_symbols:
                return (i, j)
    return (-1, -1)

def rotate_matrix(matrix):
    return [list(row) for row in zip(*matrix)][::-1]

def part_one(matrix):
    visited = [row[:] for row in matrix]
    while True:
        guard_pos = find_guard(matrix)
        i, j = guard_pos[0], guard_pos[1]
        visited[i][j] = 'X'
        if i-1 < 0:
            break
        elif matrix[i-1][j] == '#':
            matrix = rotate_matrix(matrix)
            visited = rotate_matrix(visited)
        else:
            temp = matrix[i-1][j]
            matrix[i-1][j] = matrix[i][j]
            matrix[i][j] = temp

    count = 0
    for row in visited:
        for col in row:
            if col == 'X': count += 1
    return count

def main():
    matrix = get_input()

    # part one
    steps = part_one(matrix)
    print(f"Part One: {steps}")

if __name__ == "__main__":
    main()
