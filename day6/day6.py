from concurrent.futures import ProcessPoolExecutor
from copy import deepcopy

DIRECTIONS = ('^', 'v', '<', '>')

TURN_90 = {
    '^': '>',
    'v': '<',
    '<': '^',
    '>': 'v'
}

TO_ADD = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

def get_input(input_file="input.txt"):
    lines = open(input_file, 'r').readlines()
    return [list(x.replace('\n', '')) for x in lines]

def add_tuple(A, B):
    if len(A) != len(B):
        raise ValueError("Tuples must be of equal length")
    return tuple([A[i] + B[i] for i in range(len(A))])

def get_guard_position(matrix):
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col in DIRECTIONS:
                return (i, j), matrix[i][j]
    return -1, -1

def get_obstacles(matrix):
    obstacles = []
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == '#':
                obstacles.append((i, j))
    return obstacles

def is_outside(pos, dir, rows, cols):
    x, y = pos
    return any([
        (dir == '^' and x == 0),
        (dir == 'v' and x == rows - 1),
        (dir == '<' and y == 0),
        (dir == '>' and y == cols - 1)
    ])

def add_pos(pos, dir):
    return add_tuple(pos, TO_ADD[dir])

def solve(matrix):
    rows, cols = len(matrix), len(matrix[0]) # find matrix size

    obstacles = get_obstacles(matrix) # find all obstacles in matrix
    visited_obstacles = [] # keep track of obstacles we've seen
    pos, dir = get_guard_position(matrix) # find starting position of guard

    positions = [pos] # keep track of positions we've visted
    is_loop = False # loop boolean for Part Two
    while not is_outside(pos, dir, rows, cols): # make sure were bounded
        next_pos = add_pos(pos, dir) # move 1 step
        x, y = pos
        matrix[x][y] = ' '
        if next_pos in obstacles:
            if (next_pos, dir) in visited_obstacles:
                is_loop = True
                break

            visited_obstacles.append((next_pos, dir))
            dir = TURN_90[dir]
            next_pos = pos
            continue

        pos = next_pos
        if pos not in positions:
            positions.append(pos)

    return len(positions), positions, is_loop

def process_path(args):
    matrix, coords = args
    i, j = coords
    new_matrix = deepcopy(matrix)
    if new_matrix[i][j] in DIRECTIONS:
        return 0

    new_matrix[i][j] = '#'
    _, _, is_loop = solve(new_matrix)
    return i if is_loop else 0

def solve2(matrix, available_path):
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(
            process_path, [(matrix, coords) for coords in available_path]))
    return sum(results)

if __name__ == "__main__":
    puzzle1 = get_input()
    puzzle2 = get_input()

    ans1, positions, _ = solve(puzzle1)
    ans2 = solve2(puzzle2, positions)
    ans = (ans1, ans2)
    print(ans)
