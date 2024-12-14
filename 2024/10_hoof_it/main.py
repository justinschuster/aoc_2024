def read_input(input='input.txt'):
    out = []
    lines = open(input, 'r').readlines()
    for line in lines:
        line = line.replace('\n', '')
        line = list(int(char) for char in line)
        out.append(line)
    return out


def find_trailheads(input):
    trailheads = set()
    for x, line in enumerate(input):
        for y, char in enumerate(line):
            if char == 0:
                trailheads.add((x,y))
    return trailheads


def find_score(trailhead, input, visited=[]):
    x, y = trailhead

    if input[x][y] == 9 and trailhead not in visited:
        visited.append(trailhead)
        return 1

    num_rows, num_cols = len(input), len(input[0])

    moves = [
        (x-1, y),
        (x+1, y),
        (x, y-1),
        (x, y+1)
    ]

    score = 0
    for move in moves:
        x2, y2 = move
        if not (0 <= x2 < num_rows and 0 <= y2 < num_cols):
            continue

        if input[x2][y2] == input[x][y] + 1:
            score += find_score(move, input, visited)

    return score


def solve(input):
    trailheads = find_trailheads(input)

    score = 0
    for trailhead in trailheads:
        score += find_score(trailhead, input)

    return score


if __name__ == '__main__':
    input = read_input('2024/10_hoof_it/test_input.txt')
    answer = solve(input)
    print(answer)
